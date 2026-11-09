# Third-party notices and unresolved provenance

This is a source-distribution index, not a replacement license or a redistribution
clearance. The project's [MIT license](LICENSE) does not relicense third-party
components, fonts, media or datasets. The [F2-09 inventory and review procedure](docs/50-engineering/license-provenance.md)
records exact inputs, evidence limits and unresolved rights.

## Candidate-bound Linux notice evidence — 2026-11-09

[CI run 42591561481](https://github.com/zhenkun26/Business-Agent/actions/runs/42591561481),
workflow_dispatch attempt 1, verified exact head
`15cd84f942ccc0ce49afcfc1513efe4c2f07f441` on 2026-11-09
(created 09:12:08 UTC; completed 09:19:42 UTC). All five jobs succeeded.
Docker build, actual installed inventory and Trivy passed under the existing
HIGH/CRITICAL, ignore-unfixed=true policy. With publish=false, GHCR login and push
were skipped. This was verification, not publication or deployment.

The [run's production-build-inventory artifact](https://github.com/zhenkun26/Business-Agent/actions/runs/42591561481)
has ID `13661334195` and ZIP SHA-256
`74dbfde9f052b3ae3ad8c759a1ad3c25943f969edbe9bae5c98d70400ec1cc17`.
Its independently inspected receipt reports `SCOPED_NOTICE_BYTES_VERIFIED` for exactly
eight notice files and binds their SHA-256 values at `/app/deploy/third-party-notices`
in image `sha256:e5fabe6178718b0db5bea2111ec26f0d6a53a21fa93dacda98cec6d36d6c1d39`,
checked with network disabled and a read-only filesystem. This is actual scoped
final-image retention evidence, not a complete image license or redistribution audit.
The artifact's recorded expiry is 2027-02-07 09:12:09 UTC; authenticated download was
verified, but anonymous download was not tested and permanent access is not promised.
This subsequent documentation diff is not the source revision executed by that run.

The [phase-one source assessment](docs/50-engineering/license-provenance.md#phase-one-source-assessment--2026-11-08) distinguishes 229 upstream-supported records, 232 common-project contributions with maintainer-reported MIT consent, and four repository-declared MIT associated research documents. Historical PENDING labels remain unchanged, not 465 unresolved present-day blockers. BusinessAgent derives from the [hello-xiao-a](https://github.com/kingoftaro/hello-xiao-a/tree/8a9544594d129de0dc3b4738b988d36372091d5b) jointly developed with kingoftaro; this attribution does not transfer copyright or relicense third-party material.

## Browser components already retained in source

| Component | Declared version/license | Preserved upstream text |
| --- | --- | --- |
| Vue | 3.5.44 / MIT | [LICENSE](enterprise-agent/app/static/vendor/vue-3.5.44/LICENSE) |
| Marked | 18.1.1 / MIT | [LICENSE](enterprise-agent/app/static/vendor/marked-18.1.1/LICENSE) |
| DOMPurify | 3.4.17 / Apache-2.0 OR MPL-2.0 | [Apache text](enterprise-agent/app/static/vendor/dompurify-3.4.17/LICENSE), [MPL text](enterprise-agent/app/static/vendor/dompurify-3.4.17/LICENSE-MPL), [Babel helpers MIT text](enterprise-agent/app/static/vendor/dompurify-3.4.17/LICENSE-BABEL-HELPERS) |

Preserve these files and copyright/license headers with the corresponding distributions.
The exact upstream tarball URLs, integrity values and local file hashes are recorded in
the [vendor manifest](enterprise-agent/app/static/vendor/manifest.json). DOMPurify's
vendored bundle additionally contains a regenerator-runtime MIT attribution to Facebook.
That header is unchanged, and the complete @babel/helpers 7.29.10 MIT notice is now
retained alongside it, bound to DOMPurify 3.4.17's official lock and the helper archive.
The JavaScript and existing Apache/MPL texts are unchanged. No dual-license election
or complete bundled-component notice audit is asserted here.

## Python, OS, optional profiles and externally supplied services

The [machine-readable inventory](enterprise-agent/deploy/license-inventory.json) records
all 98 pinned production Python distributions, including publisher-declared license
expressions/classifiers and exact-release metadata sources. These declarations are not
a verified Linux wheel or native-library bill of materials. Preserve installed upstream
license/NOTICE files and review the actual final distribution before redistribution.
In particular, review LGPL declarations for psycopg/psycopg-pool, MPL declarations
including certifi/orjson/tqdm, dual licenses, and native components bundled in wheels.
This index does not determine compliance obligations or license compatibility.

Development/evaluation/ML/IdP requirements, Docker/service images and CI tools are
recorded separately as declarations. Unresolved closures, OS copyright files, bundled
libraries, model weights and provider terms do not inherit the production inventory's
coverage. The remote model profile does not distribute model weights.

## Scoped production notice retention — 2026-11-08

The [supplemental production notices](enterprise-agent/deploy/third-party-notices/README.md)
retain four full official MIT texts for langchain-core 1.5.3,
langchain-text-splitters 1.1.2, langsmith 0.10.15 and loguru 0.7.3. Verified local
cache-origin/RECORD evidence found no full MIT notice in those package trees; this is
not a fresh recomputation of their original wheel archives or final-image inspection.
The [source map](enterprise-agent/deploy/third-party-notices/source-map.json) binds
exact release-tag URLs, notice bytes and locked production wheel hashes.

For lxml 6.1.1, a separate file-level supplement retains both full official Schematron
converter files at commit 77dcd36c53d12ed786c144ece3b2af7694abdc56, including original
author/history comments and the complete MIT permission notice. The two transform
bodies match RNG2Schtrn.xsl and XSD2Schtrn.xsl in both locked Linux wheels under the
source map's exact, limited normalization. Their headers and full-file bytes differ.
This is specific upstream permission evidence, not an inference from lxml's BSD label.
The original package resources and LICENSES.txt, including its older unlicensed wording,
remain unchanged. No other lxml, native-library or OS obligation is cleared.

Dockerfile.prod explicitly retains this directory in the final image. The sealed
source-input check and `--installed` final-directory check are separate: the latter
verifies exact file membership and hashes and exports a scoped receipt with the
existing installed inventory. Source checks and synthetic regression tests do not
establish actual image retention. Run 42591561481 supplies the separately bound actual
scoped retention evidence above for source `15cd84f942ccc0ce49afcfc1513efe4c2f07f441`;
full image-license review remains separate.

The retained inventory schema still marks 465 controlled source records
PENDING_SOURCE_REVIEW; their newer source-only assessment is linked above. All 98 top-level
package wheel-review statuses remain PENDING. Outstanding work includes native/nested
components, OpenTelemetry Apache-text mapping, OS copyright/common-license files,
LGPL notices/companion GPL text/source and replaceability obligations, and MPL source
requirements. These notice additions do not grant distribution, runtime or release
acceptance and do not replace the project-wide provenance review.

## Verified upstream notice additions — 2026-11-07

This is a scoped evidence and notice update, not a blanket rights decision. The controlled
457 source statuses and their verifier are unchanged.

- **Twelve generated tooling files:** their instruction bodies match the official
  OpenSpec 1.7.0 package under its actual Codex/Kimi renderer rules. The npm archive's
  published integrity was verified without executing package code. Retain
  [the complete upstream MIT text](third_party/licenses/openspec/OpenSpec-1.7.0-MIT.txt)
  and its Copyright 2024 OpenSpec Contributors attribution.
  [Exact local/package/template mappings](third_party/licenses/openspec/provenance.json)
  distinguish this source match from project-wide authorship or distribution acceptance.
- **89 presentation font files:** six JetBrains Mono and 83 Noto Serif SC files match
  byte-for-byte the official Google Fonts distribution URLs recorded in the
  [verified source map](third_party/licenses/fonts/verified-source-map.json).
  Their [original copyright notices](third_party/licenses/fonts/NOTICE.md) and full
  [JetBrains OFL](third_party/licenses/fonts/JetBrainsMono-OFL.txt) /
  [Noto Serif OFL](third_party/licenses/fonts/NotoSerifSC-OFL.txt) are retained.
  Copy those notices with the font files in any separate website/export; repository
  retention alone does not prove an export contains them.
- **128 other fonts:** [conditional OFL applicability, version and comparison evidence](third_party/licenses/fonts/unresolved-source-map.json)
  remains separate. Full OFL texts and original notices are now retained for these groups.
  OFL permits modifications/subsetting under its conditions; byte differences are not
  a redistribution prohibition. Historical acquisition chains remain incompletely
  reconstructed, particularly Manrope 4.504. No exact Manrope release verification or
  blanket clearance is claimed. No source is replaced or relicensed.

The OFL conditions include notice retention, restrictions on selling fonts alone and
reserved names for modified fonts, and continued OFL licensing of font derivatives.
The upstream full texts control. These font licenses do not relicense application code
or documents created using the fonts.

## Historical unresolved-source assessment — before phase-one follow-up

The remaining font lineage questions, screenshots, documentation illustrations/research
material, seed SQL, evaluation corpus and embedded fixtures still need scoped author or
upstream provenance evidence. The additions above do not clear those records. Keep their
pending records visible. Do not infer a
license from a font family, filename, synthetic label, screenshot appearance or Git author.
The inventory does not authorize public distribution of unresolved assets.
