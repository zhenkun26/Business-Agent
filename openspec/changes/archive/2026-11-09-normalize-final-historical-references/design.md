# Design

## Context
Base main is 507ae4c53e4bdf95b944b0745b70d1afbc21a56d. The original receipt is at public commit 54a3954fd8eda56099f3efa33af370b1eb0bf4cd, blob a503645e17e117b31ec2773fb2ba7a59e3f1697e, SHA-256 2812b7b2cbeb3961744785e777d404ca62314ef60646a2e270b02f08c426c5f9.

## Goals / Non-Goals
Preserve all historical conclusions and identify original evidence. No history rewriting, historical task rerun, private artifact mirroring, runtime acceptance or release.

## Decisions
Edit exactly one JSON evidence string, preserving other bytes. Replace the two archive URLs with repository-qualified unlinked historical run identifiers plus dated unavailable-public-evidence errata. Do not redirect old run IDs to the new repository. Preserve earlier lifecycle records as historical facts.

## Risks / Trade-offs
Historical-tree hash/report equality establishes public-tree consistency only, not independent proof of original execution or private CI logs. Two original inputs have since changed; current inputs cannot validate the original report. New local checks and future CI concern this candidate only. Distribution release remains false; enterprise acceptance remains unestablished.

## Migration Plan
Prepare locally, independently review, and await publication authorization and successful audit of PR5 postmerge run 42630614045. Keep active; no archive, commit, push or PR in this preparation. Reverting this documentation patch restores navigation without deleting history.

## Implementation evidence (2026-11-09)

Independent review and the bounded audit passed for implementation head `1cfa9aaaed1254e388219a6ee1c212509d69b9c5`, base `507ae4c53e4bdf95b944b0745b70d1afbc21a56d`, executed merge `49cc9a41f8aa0dd3af8663223c6a38f81483f356`, tree `c2db500f145af7945f326e80bdba7d99b79f928c`. Content SHA-256: `77ef017c25b40655b3ec829dd69437908a2b11eb4b20d7e3fea795fe15d6a933`; nine-file patch SHA-256: `b8068bb4d7e5bf5865d891205b78519326feb6b0856ca7edfb82414e4e6822e0`. Of 1040 files, 1031 were unchanged from base.

[Implementation CI](https://github.com/zhenkun26/Business-Agent/actions/runs/42634382590), pull_request attempt 1: all five jobs succeeded. Each Python job passed 2170 tests plus 640 subtests, eight offline checks, nine publication-policy tests and 39 scanner regressions. Node checks passed 80 page and 14 credential cases; frontend checked eight files. C10 isolated assertions were 17/17/24/5, with 15 synthetic HTTP checks. Docker completed 39 steps, 29 cached; inventories contained 98 Python and 106 OS packages. Trivy passed existing policy; GHCR login and publication were skipped.

Nine downloaded artifact hashes and 21 source/run/artifact bindings passed, including 14 build inputs and eight retained notices. The bounded audit covered five logs, nine archives, metadata, 21 new Git objects, 180 trace JSON objects and protobuf records. All 18 actual-pipeline controls passed at base64 minimum length 12. Matches were limited to approved noreply identities, GitHub URL text and BuildKit local metadata.

Local implementation checks passed 180 focused pytest tests and nine publication-policy tests, plus source, notice, inventory, frontend, release-gate, strict OpenSpec and whitespace checks. This is not a local full-suite claim.

Zero old PR/CI/artifact navigation links is scoped to the current tree; ten old API URLs remain in untouched protection snapshots and Git history remains. Historical public-tree/report consistency does not independently establish original execution or private CI. External image layers/config were not independently extracted; cached builds do not prove two clean builds. Full C10/RAG/browser/UAT/rights/distribution/formal-release acceptance remains unestablished and release flags remain false.

This evidence belongs to the implementation revision only. The later lifecycle archive revision requires its own independent review, CI and audit; no implementation result is attributed to it. No PR-body update, merge or auto-merge is implied.
