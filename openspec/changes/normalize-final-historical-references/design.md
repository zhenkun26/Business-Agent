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
