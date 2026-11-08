"""Read-only production input and installed-inventory verifier; no application imports."""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import platform
from pathlib import Path
import re
import subprocess
import sys
from typing import Any, Iterable

NOTICE_DIRECTORY = 'deploy/third-party-notices'
NOTICE_COMPONENT_FILES = {
    'langchain-core': {'LangChain-Core-1.5.3-MIT.txt'},
    'langchain-text-splitters': {'LangChain-Text-Splitters-1.1.2-MIT.txt'},
    'langsmith': {'LangSmith-0.10.15-MIT.txt'},
    'loguru': {'Loguru-0.7.3-MIT.txt'},
    'lxml': {'ExtractSchFromRNG-77dcd36.xsl.txt', 'ExtractSchFromXSD-77dcd36.xsl.txt'},
}
NOTICE_FILES = {'source-map.json', 'README.md'} | set().union(*NOTICE_COMPONENT_FILES.values())
FINAL_NOTICE_ROOT = Path('/app/deploy/third-party-notices')
INPUT_FILES = {
    'Dockerfile.prod', 'deploy/requirements-prod.txt', 'deploy/requirements-prod.lock',
    'deploy/requirements-ml.txt', 'deploy/debian.sources', 'scripts/verify_build.py',
} | {NOTICE_DIRECTORY + '/' + name for name in NOTICE_FILES}
PIN = re.compile(r'([A-Za-z0-9_.-]+)(?:\[([a-z,]+)\])?==([A-Za-z0-9_.+!-]+)')
SHA = re.compile(r'[a-f0-9]{64}')


class InvalidBuild(ValueError):
    """Fixed code only; do not expose environment paths or arbitrary package metadata."""


def normalized(name: str) -> str:
    return re.sub(r'[-_.]+', '-', name).lower()


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def pins(text: str, *, hashes: bool = False) -> dict[str, dict[str, Any]]:
    result = {}
    for line in text.replace('\\\n', ' ').splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        pieces = line.split()
        match = PIN.fullmatch(pieces[0])
        if not match:
            raise InvalidBuild('BUILD_PIN_INVALID')
        name, extras, version = match.groups()
        name = normalized(name)
        if name in result or (extras and (name != 'pyjwt' or extras != 'crypto')):
            raise InvalidBuild('BUILD_PIN_DUPLICATE_OR_EXTRA')
        values = []
        for piece in pieces[1:]:
            prefix = '--hash=sha256:'
            if not hashes or not piece.startswith(prefix) or not SHA.fullmatch(piece[len(prefix):]):
                raise InvalidBuild('BUILD_HASH_INVALID')
            values.append(piece[len(prefix):])
        if hashes and (not values or len(values) != len(set(values))):
            raise InvalidBuild('BUILD_HASH_MISSING_OR_DUPLICATE')
        result[name] = {'version': version, 'extras': extras or '', 'hashes': sorted(values)}
    if not result:
        raise InvalidBuild('BUILD_PINS_EMPTY')
    return result


def checked_file(root: Path, relative: str) -> Path:
    parts = Path(relative)
    if parts.is_absolute() or '..' in parts.parts or not parts.parts:
        raise InvalidBuild('BUILD_PATH_INVALID')
    path = root.absolute() / parts
    if any(p.is_symlink() for p in (path, *path.parents)) or not path.is_file():
        raise InvalidBuild('BUILD_FILE_INVALID')
    return path


def verify_notice_directory(directory: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    """Verify one actual directory; source and installed callers stay separate."""
    if {path.name for path in directory.iterdir()} != NOTICE_FILES:
        raise InvalidBuild('BUILD_NOTICE_SET_DRIFT')
    hashes = {}
    for name in sorted(NOTICE_FILES):
        path = checked_file(directory, name)
        actual = digest(path.read_bytes())
        if actual != manifest['files'][NOTICE_DIRECTORY + '/' + name]:
            raise InvalidBuild('BUILD_NOTICE_DRIFT')
        hashes[name] = actual
    mapping = json.loads(checked_file(directory, 'source-map.json').read_text())
    if (mapping.get('schema') != 1 or mapping.get('distribution_acceptance') != 'BLOCKED'
            or set(mapping.get('components', {})) != set(NOTICE_COMPONENT_FILES)):
        raise InvalidBuild('BUILD_NOTICE_MAP_INVALID')
    for package, names in NOTICE_COMPONENT_FILES.items():
        entry = mapping['components'][package]
        locked = manifest['packages'][package]
        if (entry.get('version') != locked['version'] or entry.get('notice_license') != 'MIT'
                or entry.get('wheel_sha256') != sorted(w['sha256'] for w in locked['wheels'])
                or set(entry.get('files', {})) != names):
            raise InvalidBuild('BUILD_NOTICE_BINDING_DRIFT')
        for name in names:
            notice = entry['files'][name]
            data = checked_file(directory, name).read_bytes()
            if (notice.get('sha256') != hashes[name] or notice.get('bytes') != len(data)
                    or not isinstance(notice.get('source'), str)
                    or not notice['source'].startswith('https://')):
                raise InvalidBuild('BUILD_NOTICE_BINDING_DRIFT')
    return {'status': 'SCOPED_NOTICE_BYTES_VERIFIED', 'files': hashes,
            'distribution_acceptance': 'BLOCKED', 'complete_license_audit': 'NOT_ESTABLISHED'}


def verify_inputs(root: Path) -> dict[str, Any]:
    manifest_path = checked_file(root, 'deploy/build-inputs.json')
    manifest = json.loads(manifest_path.read_text())
    if manifest.get('schema') != 1 or set(manifest.get('files', {})) != INPUT_FILES:
        raise InvalidBuild('BUILD_MANIFEST_INVALID')
    for name, expected in manifest['files'].items():
        path = checked_file(root, name)
        if digest(path.read_bytes()) != expected:
            raise InvalidBuild('BUILD_INPUT_DRIFT')
    if manifest.get('platform') != 'linux/amd64':
        raise InvalidBuild('BUILD_PLATFORM_INVALID')
    recipe = (root / 'Dockerfile.prod').read_text()
    for key in ('base', 'frontend'):
        ref = manifest[key]['reference']
        if not re.fullmatch(r'[a-z0-9./:-]+@sha256:[a-f0-9]{64}', ref) or ref not in recipe:
            raise InvalidBuild('BUILD_IMAGE_REFERENCE_INVALID')
    if recipe.count('FROM ' + manifest['base']['reference']) != 2:
        raise InvalidBuild('BUILD_BASE_DRIFT')
    required = ('--require-hashes', '--no-deps', '--only-binary=:all:',
                'Dir::Etc::sourceparts=-', 'Dir::Etc::sourcelist=/build-info/deploy/debian.sources')
    if not all(value in recipe for value in required) or 'install --upgrade' in recipe:
        raise InvalidBuild('BUILD_INSTALL_POLICY_INVALID')
    sources = (root / 'deploy/debian.sources').read_text()
    if ('trusted=yes' in sources.lower() or 'allow-insecure' in sources.lower()
            or sources.count('Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg') != 2
            or sources.count(manifest['snapshot']) != 2):
        raise InvalidBuild('BUILD_OS_SOURCE_INVALID')
    expected = pins((root / 'deploy/requirements-prod.txt').read_text())
    locked = pins((root / 'deploy/requirements-prod.lock').read_text(), hashes=True)
    packages = manifest['packages']
    if set(expected) != set(locked) or set(expected) != set(packages):
        raise InvalidBuild('BUILD_PACKAGE_SET_DRIFT')
    for name, pin in expected.items():
        record = packages[name]
        if (pin['version'] != locked[name]['version'] or pin['extras'] != locked[name]['extras']
                or pin['version'] != record['version']
                or locked[name]['hashes'] != sorted(w['sha256'] for w in record['wheels'])):
            raise InvalidBuild('BUILD_PACKAGE_LOCK_DRIFT')
        if record['source'] != f'https://pypi.org/pypi/{name}/{pin["version"]}/json':
            raise InvalidBuild('BUILD_PACKAGE_SOURCE_INVALID')
        for wheel in record['wheels']:
            if not wheel['filename'].endswith('.whl') or not SHA.fullmatch(wheel['sha256']):
                raise InvalidBuild('BUILD_WHEEL_INVALID')
    verify_notice_directory(root / NOTICE_DIRECTORY, manifest)
    return manifest


def compare_packages(expected: dict[str, Any], installed: Iterable[tuple[str, str]],
                     *, profile: str) -> dict[str, str]:
    if profile not in {'production', 'experimental-ml'}:
        raise InvalidBuild('BUILD_PROFILE_INVALID')
    actual = {}
    for name, version in installed:
        name = normalized(name)
        if name in actual:
            raise InvalidBuild('BUILD_INSTALLED_DUPLICATE')
        actual[name] = version
    if any(actual.get(name) != record['version'] for name, record in expected.items()):
        raise InvalidBuild('BUILD_INSTALLED_VERSION_DRIFT')
    if profile == 'production' and set(actual) != set(expected):
        raise InvalidBuild('BUILD_INSTALLED_EXTRA')
    return dict(sorted(actual.items()))


def inventory(root: Path, manifest: dict[str, Any], installed: Iterable[tuple[str, str]],
              *, profile: str, python: str, system: str, machine: str,
              os_packages: str, notice_root: Path) -> dict[str, Any]:
    if python != manifest['python'] or system != 'Linux' or machine != 'x86_64':
        raise InvalidBuild('BUILD_RUNTIME_PLATFORM_DRIFT')
    packages = compare_packages(manifest['packages'], installed, profile=profile)
    debs = {}
    for line in os_packages.splitlines():
        columns = line.split('\t')
        if len(columns) != 3 or columns[0] in debs:
            raise InvalidBuild('BUILD_OS_INVENTORY_INVALID')
        name, version, architecture = columns
        if not re.fullmatch(r'[a-z0-9][a-z0-9+.:~-]*', name) or not version or not architecture:
            raise InvalidBuild('BUILD_OS_INVENTORY_INVALID')
        debs[name] = {'version': version, 'architecture': architecture}
    if not {'ca-certificates', 'tzdata', 'libpq5:amd64'}.issubset(debs):
        raise InvalidBuild('BUILD_OS_INVENTORY_MISSING')
    notices = verify_notice_directory(notice_root, manifest)
    return {
        'schema': 1, 'profile': profile,
        'status': 'INSTALLED_SET_VERIFIED' if profile == 'production' else 'EXPERIMENTAL_NOT_ACCEPTED',
        'python': python, 'platform': manifest['platform'], 'base': manifest['base']['reference'],
        'frontend': manifest['frontend']['reference'], 'snapshot': manifest['snapshot'],
        'build_inputs_sha256': digest((root / 'deploy/build-inputs.json').read_bytes()),
        'input_sha256': manifest['files'], 'python_packages': packages,
        'os_packages': dict(sorted(debs.items())),
        'retained_notices': {**notices, 'checked_location': 'FINAL_IMAGE',
                             'directory': str(notice_root)},
        'runtime_acceptance': 'BLOCKED', 'full_rag': 'BLOCKED', 'c10': 'OPEN',
        'bit_identical_rebuild': 'NOT_ESTABLISHED',
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--installed', action='store_true')
    parser.add_argument('--profile', choices=('production', 'experimental-ml'), default='production')
    args = parser.parse_args()
    try:
        manifest = verify_inputs(args.root)
        if args.installed:
            # Explicit installed mode only: fixed read-only command, bounded, no shell.
            os_packages = subprocess.run(
                ['dpkg-query', '-W', '-f=${binary:Package}\t${Version}\t${Architecture}\n'],
                capture_output=True, text=True, check=True, timeout=15).stdout
            result = inventory(args.root, manifest,
                               ((d.metadata['Name'], d.version)
                                for d in importlib.metadata.distributions()),
                               profile=args.profile, python=platform.python_version(),
                               system=platform.system(), machine=platform.machine(),
                               os_packages=os_packages, notice_root=FINAL_NOTICE_ROOT)
        else:
            result = {'status': 'INPUTS_VERIFIED', 'packages': len(manifest['packages']),
                      'notice_source_inputs': 'VERIFIED', 'installed_notices': 'NOT_CHECKED',
                      'installed_image': 'BLOCKED', 'runtime': 'BLOCKED', 'c10': 'OPEN'}
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    except InvalidBuild as exc:
        print(json.dumps({'status': 'FAIL', 'code': str(exc)}))
    except Exception:
        print(json.dumps({'status': 'FAIL', 'code': 'BUILD_VERIFICATION_FAILED'}))
    return 1


if __name__ == '__main__':
    sys.exit(main())
