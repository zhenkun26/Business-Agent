"""Offline CI publication and Gitleaks installation regression controls."""
from pathlib import Path
import itertools
import os
import shlex
import subprocess
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[2]
CONDITION = "github.event_name == 'workflow_dispatch' && github.ref == 'refs/heads/main' && inputs.publish == true"


class PublicationPolicyTests(unittest.TestCase):
    def setUp(self):
        self.workflow = yaml.safe_load((ROOT / ".github/workflows/ci.yml").read_text())

    def test_explicit_boolean_defaults_off(self):
        # PyYAML YAML 1.1 may resolve the GitHub 'on' key as True.
        events = self.workflow.get("on", self.workflow.get(True))
        value = events["workflow_dispatch"]["inputs"]["publish"]
        self.assertEqual(value["type"], "boolean")
        self.assertIs(value["default"], False)
        self.assertIs(value["required"], False)

    def test_login_and_push_reject_nonexplicit_events(self):
        steps = self.workflow["jobs"]["docker"]["steps"]
        login = [s for s in steps if s.get("uses", "").startswith("docker/login-action@")]
        push = [s for s in steps if "docker push " in s.get("run", "")]
        self.assertEqual(len(login), 1)
        self.assertEqual(len(push), 1)
        for step in login + push:
            self.assertEqual(step["if"], CONDITION)
        for event, ref, publish in itertools.product(
            ("pull_request", "push", "workflow_dispatch"),
            ("refs/heads/main", "refs/heads/feature", "refs/tags/v1"),
            (None, False, True),
        ):
            with self.subTest(event=event, ref=ref, publish=publish):
                # Evaluate the exact parsed condition's three fixed clauses, not
                # a second workflow policy that could drift independently.
                values = {"github.event_name": event, "github.ref": ref, "inputs.publish": publish}
                accepted = True
                for clause in CONDITION.split(" && "):
                    key, expected = clause.split(" == ")
                    target = True if expected == "true" else expected.strip("'")
                    accepted &= type(values[key]) is type(target) and values[key] == target
                self.assertEqual(accepted, (event, ref, publish) == ("workflow_dispatch", "refs/heads/main", True))

    def test_all_verification_precedes_scanned_image_publication(self):
        jobs = self.workflow["jobs"]
        docker = jobs["docker"]
        self.assertEqual(set(docker["needs"]), {"test", "c10-persistence", "synthetic-demo"})
        for job in ("c10-persistence", "synthetic-demo"):
            self.assertEqual(jobs[job]["needs"], "test")
            self.assertEqual(jobs[job]["permissions"], {"contents": "read"})
            provisioning = [s for s in jobs[job]["steps"] if "sudo apt-get install" in s.get("run", "")]
            self.assertEqual(len(provisioning), 1)
            self.assertIn("sudo apt-get install -y --no-install-recommends libpq5", provisioning[0]["run"])
            self.assertIn("dpkg-query -W", provisioning[0]["run"])
        steps = docker["steps"]
        build = next(i for i, s in enumerate(steps) if s.get("uses", "").startswith("docker/build-push-action@"))
        scan = next(i for i, s in enumerate(steps) if s.get("uses", "").startswith("aquasecurity/trivy-action@"))
        login = next(i for i, s in enumerate(steps) if s.get("uses", "").startswith("docker/login-action@"))
        push = next(i for i, s in enumerate(steps) if "docker push " in s.get("run", ""))
        self.assertLess(build, scan)
        self.assertLess(scan, login)
        self.assertLess(login, push)
        self.assertIs(steps[build]["with"]["push"], False)
        self.assertEqual(steps[scan]["with"]["exit-code"], "1")
        self.assertEqual(steps[scan]["with"]["severity"], "HIGH,CRITICAL")
        self.assertNotIn("continue-on-error", docker)
        for step in (steps[build], steps[scan], steps[login], steps[push]):
            self.assertNotIn("continue-on-error", step)
        self.assertNotIn("docker build", steps[push]["run"])


class GitleaksInstallationTests(unittest.TestCase):
    """Execute the real workflow shell with offline command doubles.

    curl's documented retry engine owns HTTP retries. These tests lock its finite
    settings and test shell failure propagation, not GitHub availability or TLS.
    All doubles are shell builtins; no archive, executable or fixture is written.
    """

    def setUp(self):
        workflow = yaml.safe_load((ROOT / ".github/workflows/ci.yml").read_text())
        self.job = workflow["jobs"]["test"]
        installs = [step for step in self.job["steps"]
                    if "curl --fail" in step.get("run", "")]
        self.assertEqual(len(installs), 1)
        self.step = installs[0]
        self.script = self.step["run"]

    def run_install(self, *, download=0, checksum=0, extraction=0):
        # Keep the exact production script. The function boundary substitutes only
        # external commands, preserving set -euo pipefail, piping and redirection.
        doubles = "\n".join([
            'mkdir() { printf "mkdir\\n" >&2; }',
            f'curl() {{ printf "download\\n" >&2; return {download}; }}',
            'sha256sum() { while IFS= read -r line; do '
            'printf "checksum-input:%s\\n" "$line" >&2; done; '
            f'printf "checksum\\n" >&2; return {checksum}; }}',
            f'tar() {{ printf "extract\\n" >&2; return {extraction}; }}',
            'echo() { printf "publish-path\\n" >&2; }',
        ])
        result = subprocess.run(
            ["bash", "--noprofile", "--norc", "-c", doubles + "\n" + self.script],
            env={"PATH": os.defpath, "RUNNER_TEMP": "/synthetic-runner-temp",
                 "GITHUB_PATH": os.devnull},
            capture_output=True, text=True, timeout=5,
        )
        self.assertEqual(result.stdout, "")
        return result.returncode, result.stderr.splitlines()

    def test_fixed_archive_and_bounded_retry_policy(self):
        joined = self.script.replace("\\\n", " ")
        command = next(line.strip() for line in joined.splitlines()
                       if line.strip().startswith("curl "))
        self.assertEqual(shlex.split(command), [
            "curl", "--fail", "--silent", "--show-error", "--location",
            "--proto", "=https", "--tlsv1.2",
            "--retry", "4", "--retry-delay", "5", "--retry-max-time", "120",
            "--connect-timeout", "10", "--max-time", "30",
            "https://github.com/gitleaks/gitleaks/releases/download/v8.24.3/"
            "gitleaks_8.24.3_linux_x64.tar.gz",
            "--output", "$tool_dir/archive.tar.gz",
        ])
        self.assertEqual(self.step["timeout-minutes"], 3)
        self.assertEqual(self.step["shell"], "bash")
        self.assertIn("set -euo pipefail", self.script)
        self.assertIn('tool_dir="$RUNNER_TEMP/gitleaks-8.24.3"', self.script)
        self.assertIn('sha256sum --check -', self.script)
        self.assertIn('tar -xzf "$tool_dir/archive.tar.gz" -C "$tool_dir" gitleaks',
                      self.script)
        for scope in (self.job, self.step):
            self.assertNotIn("continue-on-error", scope)
        self.assertNotIn("if", self.step)

    def test_checksum_precedes_extraction_and_path_publication(self):
        code, trace = self.run_install()
        self.assertEqual(code, 0)
        self.assertEqual(trace, [
            "mkdir", "download",
            "checksum-input:9991e0b2903da4c8f6122b5c3186448b927a5da4deef1fe45271c3793f4ee29c"
            "  /synthetic-runner-temp/gitleaks-8.24.3/archive.tar.gz",
            "checksum", "extract", "publish-path",
        ])

    def test_download_failure_cannot_validate_extract_or_publish(self):
        # curl returns 22 after an HTTP error, 28 after timeout, 6 after DNS failure
        # and 60 after certificate validation failure. No shell fallback is allowed.
        for failure in (22, 28, 6, 60):
            with self.subTest(exit_code=failure):
                code, trace = self.run_install(download=failure)
                self.assertEqual(code, failure)
                self.assertEqual(trace, ["mkdir", "download"])

    def test_checksum_failure_cannot_extract_or_publish(self):
        code, trace = self.run_install(checksum=1)
        self.assertEqual(code, 1)
        self.assertEqual(trace[-1], "checksum")
        self.assertNotIn("extract", trace)
        self.assertNotIn("publish-path", trace)

    def test_extraction_failure_cannot_publish(self):
        code, trace = self.run_install(extraction=2)
        self.assertEqual(code, 2)
        self.assertEqual(trace[-1], "extract")
        self.assertNotIn("publish-path", trace)


if __name__ == "__main__":
    unittest.main()
