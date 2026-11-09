# Tasks

## 1. Plan and admission

- [x] 1.1 Inspect exact-main source, instructions, affected claims and existing capabilities; verify the six selected references and isolated branch baseline.
- [x] 1.2 Write proposal and design before document edits; confirm the supported documentation-only skip_specs status and no new behavior requirement.
- [x] 1.3 Obtain actual apply-ready instructions and strict validation for the complete planning artifacts.

## 2. Scoped documentation maintenance

- [x] 2.1 Update README/quickstart current evidence and English parity; verify run/date/attempt/head and separate historical Mac/browser observations.
- [x] 2.2 Replace the notice record with freshly audited artifact/image/digest/notice fields; verify exact values and retention/access caveats without changing license/attribution text.
- [x] 2.3 Refresh UAT/release regression references and verify formal execution-version checks, unchanged acceptance baseline and BLOCKED release verdict.
- [x] 2.4 Add only the scoped changelog and lifecycle index entries; verify unchanged version, remaining historical links, manifest bytes and frozen blobs.

## 3. Candidate verification and review

- [x] 3.1 Run strict OpenSpec, whitespace, local-link/fragment, privacy-pattern and exact scope checks; report actual results without a fresh local full-suite claim.
- [x] 3.2 Run applicable unchanged inventory/build/frontend and focused regression checks; distinguish failures or unavailable checks from passes.
- [ ] 3.3 Complete independent diff/evidence review and resolve any blocking findings before marking the candidate ready.

## Verification record — 2026-11-09

- OpenSpec 1.16.1 strict validation passed before implementation and on the candidate;
  skip_specs is explicitly accepted. No main specification was changed.
- Whitespace, exact eight-existing-file scope, ten added relative links/fragments and
  inserted private-data pattern checks passed. All 1,011 other tracked files are byte-
  identical to the baseline; all three frozen Git blobs match their required identities.
- Exactly the six selected live old-repository URL occurrences were removed. Every
  remaining old reference and non-target historical document is unchanged. The notice
  attribution/license suffix and README source-rights suffix are byte-identical.
- Python 3.13.15 read-only checks passed: license inventory (98 production packages,
  three browser packages, 465 retained pending-label records, 32 declaration files),
  build/notice source inputs, and eight browser distribution/license files. These
  checks do not inspect an installed local image or grant distribution acceptance.
- All nine publication-policy tests passed. Local full pytest/eight-check execution
  was not rerun because 14 production pins differ; Gitleaks 8.24.3 is unavailable, so
  local scanner regressions were not run. Their fresh remote results remain bound
  only to run 42591561481 and its exact head.
- Independent content/evidence review is pending. No commit, archive or public action.

## 4. Follow-up after PR #3 failure — 2026-11-09

The proposal, design and preceding verification block retain the initial private
preparation record, not the present publication state. The later authorized draft
[PR #3](https://github.com/zhenkun26/Business-Agent/pull/3) published candidate
477bcf45c270f12570dd018bd7a85d21c5449e35 after independent review with no blocking
findings. That review did not establish candidate CI success.

[Candidate CI 42596676359](https://github.com/zhenkun26/Business-Agent/actions/runs/42596676359),
pull_request attempt 1, failed for both Python 3.11 and 3.13 at the current-offline
step. Its tested merge was 11f9b015070af0ff394ba869d6329f4432d92bdb, with the same
tree 41f96b4e4dca814b5d568a69207f53ada962977a as the source candidate. Both reports
showed python CHILD_FAILED and the other seven checks PASS; candidate binding and
source stability passed. C10, native-demo and Docker jobs were skipped. No successful
candidate suite, scanner, image or publication result is inferred from that run.

Read-only local reproduction found that GATE-01 wording “技术回归通过” was no longer
recognized by the unchanged release validator's “已通过” marker. The existing
release-gate assertion failed; the three other directly exercised UAT/grey-plan
assertions passed. The remote child report did not identify every failed Python
assertion, so this is a confirmed local regression, not proof of the only remote cause.

The subsequent approved base update is main
afcb2062cb696eb5d7fd229964eb584ccedfb404 after PR #2. A normal local merge preserves
both histories; its only conflict is resolved by retaining both reviewed CHANGELOG
entries verbatim. The initial all-old-URL inventory was 43 to 37, including two
source-root links. PR #2 removed those separately, so against the new base this
change is 41 to 35: exactly six live references removed, with 32 non-frozen historical
and three frozen references retained. Original planning dates and evidence are not
retroactively changed. Run 42591561481 still validates only exact 15cd84f, not this
new base or the post-merge candidate.

- [x] 4.1 Merge the verified new main normally and verify every resulting file is the exact union of the two reviewed batches; retain both CHANGELOG entries and no unrelated changes.
- [x] 4.2 Add only “已” to the GATE-01 technical-regression label; run all nine existing UAT/release/grey-plan tests unchanged and retain the overall BLOCKED verdict.
- [x] 4.3 Record the failed candidate CI, exact old/new bases and counting conventions while preserving the original initial-preparation record.
- [ ] 4.4 Verify the complete new-base diff, isolated one-character correction, merge resolution and strict validation; obtain independent review of the corrected candidate.
- [ ] 4.5 After separately authorized publication, require fresh final-candidate CI and artifact/privacy review; do not reuse the prior successful run as this candidate's result.

Post-merge local checks passed on the working repair candidate: all nine unchanged
UAT/release/grey-plan tests, with zero skips or audit-guard denials; nine publication-
policy tests; license inventory; build/notice source inputs; eight frontend files;
strict OpenSpec 1.16.1; whitespace and exact scope/frozen-byte checks. All 1,015
unaffected files from the new base are byte-identical. The release document differs
from the normal merge by exactly the added character “已”, and release_allowed stays
false. These focused checks do not establish a full local suite or final-candidate CI.
Independent review of this repaired candidate is still required.

The lifecycle stays active. Full local pytest remains unavailable because 14
production pins differ; pinned Gitleaks 8.24.3 remains unavailable. This follow-up
does not change tests, code, gates, dependencies, manifests, licenses or attribution.
No further push, PR-state change, archive, main merge or image publication is included
in the local repair preparation.

## Workflow follow-up

- After review and verification, archive only this lifecycle; skip_specs means no main-spec changes.
- Verify the archived artifact paths and update the scoped contents.md entry.
- Commit only a complete reviewed candidate if requested, using the approved owner noreply identity; record its own verification separately from the cited run.
- No push, PR, merge, image publication, deployment or history rewriting is part of this private preparation.
