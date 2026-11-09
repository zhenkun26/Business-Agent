# Tasks

## 1. Bilingual navigation

- [x] 1.1 Replace the two source-paragraph root hyperlinks with labeled migration links; verify exact paragraph changes, preserved credits and old-URL count 43 to 41.
- [x] 1.2 Add a minimal changelog entry and process-index link; verify local targets and unchanged migration explanation.

## 2. Integration checks

- [x] 2.1 Run strict scoped CLI validation and whitespace checks; verify manifests, historical receipts and archived changes remain unchanged.
- [x] 2.2 Obtain independent review and run fresh candidate-bound verification; report exact revision and limitations without claiming runtime/full RAG/UAT/rights acceptance.

## Workflow follow-up

- Archive the scoped change only after review requirements are satisfied; no main-spec sync is needed because no requirements change.
- Verify the archived result and final candidate before publication.

## Verification evidence

Independent content and strict-CLI review found no blocker. OpenSpec 1.16.1 strict scoped validation passed; no spec-level behavior changed.

Source candidate `9616fab1f31fb89c0d48b333740475b3189a163a` has tree `a41a9e195cf6b2b5681485995f103fc3cd32cdc7`. Fresh local Python 3.13 verification bound to that clean candidate passed seven checks; the full Python suite remained BLOCKED with DEPENDENCIES_UNAVAILABLE. No local full-suite success is claimed.

[PR 2 CI run 42578785296](https://github.com/zhenkun26/Business-Agent/actions/runs/42578785296) passed all five jobs. The actual tested merge was `02578b85e655bc29c3c6347112d277748d515c5c`, with parents `15cd84f942ccc0ce49afcfc1513efe4c2f07f441` and source candidate `9616fab1f31fb89c0d48b333740475b3189a163a`, and the same tree above. Python 3.11 and 3.13 each passed 2170 tests plus 640 subtests; coverage was 81.8543%. Node checks passed 80 and 14 cases. These results describe that initial merge, not the subsequent archival commit; final-head CI is still required before merge.

Runtime/full RAG/UAT and outstanding rights acceptance remain unchanged. Historical receipts and manifests were not refreshed.
