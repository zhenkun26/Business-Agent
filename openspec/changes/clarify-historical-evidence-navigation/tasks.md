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
- [ ] 3.2 Obtain independent candidate review before commit or publication, with exact base, patch fingerprint and verification limits.
- [ ] 3.3 Require exact candidate CI and its evidence review after separately authorized publication; do not reuse an earlier run as this candidate result.

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
