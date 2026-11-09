# Tasks

## 1. Plan and admission

- [x] 1.1 Revalidate all 32 original lines and eight blobs against integrated main, inspect all added target content, and confirm the reviewed patch applies without mismatch.
- [x] 1.2 Record proposal/design before edits, use supported documentation-only skip_specs, and preserve main specs and other changes.
- [x] 1.3 Obtain apply-ready instructions and strict validation for the complete planning artifacts before implementation.

## 2. Historical navigation

- [x] 2.1 Apply the exact eight-document reviewed patch; verify its standalone fingerprint, all 32 replacements, historical claims and three frozen blobs.
- [x] 2.2 Add the single lifecycle index line; verify no other auxiliary or README changes.
- [x] 2.3 Validate added relative targets/anchors, privacy patterns and unchanged document-consumer/release-gate tests without changing their contracts.

## 3. Candidate integration

- [x] 3.1 Run final scoped OpenSpec strict, whitespace, full unchanged-file and inventory checks; distinguish passed, failed and unavailable checks.
- [x] 3.2 Obtain independent candidate review before commit or publication, with exact base, patch fingerprint and verification limits.
- [x] 3.3 Require exact candidate CI and its evidence review after separately authorized publication; do not reuse an earlier run as this candidate result.

## Workflow follow-up

- Keep this change active until independent review and exact candidate CI have completed.
- Archive only this lifecycle after its prerequisites and authorization; skip_specs means no main-spec sync.

## Local candidate verification — 2026-11-09

- All 32 original lines and eight original blobs matched integrated main before edits. Independent in-memory replay of the reviewed patch reproduces all eight candidate documents byte-for-byte.
- Current-tree old PR/CI/artifact URL occurrences decreased from 35 to 3. All three frozen blobs are unchanged; original source names/event IDs remain. This is not a history-wide removal claim.
- Nine new relative links/fragments resolve to the actual current quickstart/notice evidence; the original 2026-11-08 notice anchor remains available. All 1,018 unaffected base files are byte-identical. Only nine existing files and four lifecycle files form this candidate.
- OpenSpec 1.16.1 scoped strict validation passed before application and afterward, with supported skip_specs and no main-spec changes. Archived-task validation is not globally passing: 23 items, 22 pass, and the existing documentation-baseline task remains incomplete at 31/32. No archive was performed.
- Python 3.13.15 focused verification passed 77 unchanged tests plus 11 subtests, including all nine UAT/release/grey-plan tests. The final run had no skips or audit-guard denials. The overall release result remains BLOCKED with release_allowed=false. A disabled unrelated asynchronous plugin produced an asyncio_mode configuration warning; no asynchronous tests were selected.
- The first private harness attempt was stopped before test execution by the write guard when pytest tried temporary-file output capture. Using the existing runner's sys capture and retained temporary fixture settings resolved that harness issue; repository tests and guards were not changed.
- All nine publication-policy tests passed. License inventory passed with 98 production packages, three browser packages, 465 retained pending-label records and 32 declaration files. Build/notice source inputs and all eight frontend distribution/license files passed. These are source/input checks, not a new installed-image inspection or distribution clearance.
- The unchanged full-suite entry returned BLOCKED / DEPENDENCIES_UNAVAILABLE. No full-suite, eight-check aggregate, scanner/image/runtime/browser or exact candidate remote CI success is claimed here. No dependencies were installed.
- Whitespace, exact file scope, new-content private-path patterns and frozen-byte checks passed. Independent review and exact candidate CI remain pending. The candidate is uncommitted and unpublished.

## Implementation-candidate review and CI — 2026-11-09

The preceding local-preparation record describes the state when it was written;
its pending/uncommitted statements are historical, not the later publication state.
Independent review passed before [PR #4](https://github.com/zhenkun26/Business-Agent/pull/4)
published implementation head `9826ee4588b6d27dbda4a6566a5d410459319ce6` from base
`8ec795ea57b07502caadd14d2f48682052814f9d`.

[Candidate CI 42609738902](https://github.com/zhenkun26/Business-Agent/actions/runs/42609738902),
pull_request attempt 1, passed all five jobs. The actual executed merge was
`43be1faaa23cabf01f17abffb6ea699fbca533de`, tree
`f9cf4d8596b75c08b45c3934f85a424f3e7e6d3e`, identical to the implementation head's tree.
Python 3.11 and 3.13 each passed 2170 tests + 640 subtests, all eight offline checks,
nine publication-policy tests, 39 scanner regressions and pip-audit. This PR's event
scan covered two commits and its exact tree contained 1,031 files. The isolated C10
persistence slice and 15 synthetic HTTP checks passed. Image build/load, actual
inventory and Trivy passed; GHCR login and publication were skipped.

Independent review covered all five job logs, nine artifacts, 24 new Git objects,
Docker/OCI and source bytes, with 21 binding checks passing. Additional private
privacy validation passed 18 raw/base64/percent positive controls through the actual
scan pipeline, including short base64 forms. This is the current review's coverage;
earlier direct-decoding/regex checks are not retroactively described as the same
end-to-end validation. No raw private evidence is published here.

These results do not establish full C10/RAG, enterprise UAT, source rights, browser
acceptance, complete distribution clearance or two clean reproducible builds. The
older separately cited run 42591561481 remains bound only to its original head.

## Scoped lifecycle closeout

After implementation-candidate review and CI, only this lifecycle is moved to the
2026-11-09 archive and its existing contents index entry is relocated. The original
eight-document navigation patch, three frozen records, code, gates, main specs and
other changes remain untouched. Supported skip_specs requires no main-spec sync.
The official archive skill's directory-move procedure retains all four artifacts.

This later archive-only revision was not tested by run 42609738902. It requires its
own complete candidate CI and independent review before further publication decisions.
At the time this closeout was prepared, PR #4 remained a draft awaiting confirmation;
no merge, release or image publication is authorized by this record.
