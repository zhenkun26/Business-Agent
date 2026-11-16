# Tasks

- [x] Verify PR #8, local baseline, and dotenv declaration mismatch.
- [x] Align dotenv declarations and test the minimum-version contract.
- [x] Reject unsupported analysis semantics and test supported selections.
- [x] Add approval API/UI pagination and regression coverage.
- [x] Review diff, run guarded checks, and update delivery status.
- [x] Commit locally; leave remote PRs unchanged.

Implementation is locally complete; runtime acceptance and remote review remain deferred.
The change stays available for review and is not synchronized into historical main specs.

## Authorized OpenTelemetry follow-up — 2026-11-16

- [x] Retrieve official release metadata and verify all seven wheel hashes/dependencies.
- [x] Upgrade the existing compatible group and synchronize declarations, locks, and inventories.
- [x] Add trace-context boundary and SDK/FastAPI compatibility regressions.
- [x] Pass the eight guarded offline checks in a separate retained environment.
- [x] Update delivery evidence and commit the authorized security increment.
- [x] Push to current draft PR #9 and record hosted CI results on the PR; do not merge.

Run 43866292423 at `33ca97a` passed four jobs; the image job failed on the separately
authorized Debian/libpq5 follow-up below. OpenTelemetry pip-audit checks passed.


## Authorized Debian/libpq5 follow-up — 2026-11-16

- [x] Verify official frozen Release/Packages metadata and five OS security archive hashes.
- [x] Refresh the Debian snapshot and pin/assert the existing libpq5 fixed version.
- [x] Enforce final OS security versions/architecture and add negative regressions.
- [x] Synchronize inventories, pass guarded offline checks, and update delivery evidence.
- [ ] Review and commit the security increment, then verify the clean candidate.
- [ ] Push to current draft PR #9 and rerun hosted CI with publish=false; record results on the PR.

No merge, image publication, deployment, or paid model invocation.
