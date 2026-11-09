# Design

## Context

See proposal.md for motivation. Start from exact public main
15cd84f942ccc0ce49afcfc1513efe4c2f07f441. The reference inventory selects six live
occurrences in five documents; README-en gains the matching current summary. The
remaining historical occurrences and the prior eight-link lifecycle are untouched.

## Goals / Non-Goals

**Goals:** replace stale current-evidence claims with a compact, run-bound technical
summary and retain a readable route to historical observations. State that a later
documentation-only candidate has not itself been executed by the cited run.

**Non-Goals:** no retroactive PASS labels, full C10/RAG/UAT/release acceptance, new
browser proof, rights clearance, broad link migration, tool installation, source
inventory refresh, code/security-gate changes or public actions.

## Decisions

1. Prefer an existing quickstart evidence section over a new duplicate report. Record
   workflow_dispatch, attempt 1, the exact head and UTC run window. Name each actual
   scope separately: two Python versions, eight offline checks, publication-policy and
   scanner regressions, event-history/final-tree scans, pip-audit, isolated persistence,
   native-driver synthetic HTTP and image/installed-inventory/Trivy checks.
2. Keep Mac Run-04/Run-05 and old exact libpq package observations historical, linked
   to the dated retained record. A fresh native HTTP check is not fresh browser UI
   acceptance or proof of every OS/bare-machine setup.
3. Replace the notice evidence as one coherent record, using only newly inspected
   artifact 13661334195, its ZIP digest, image identity and eight-file scoped receipt.
   Link to the verified run with the artifact name/ID, rather than guess a direct
   download URL. Record the published retention deadline and untested anonymous access.
4. Keep UAT v1.3.0 baseline language separate from the fresh technical SHA. Retain
   execution-version revalidation and all existing release decision requirements.
5. Preserve license/attribution paragraphs and all non-target historical documents.
   Only scoped changelog/index/lifecycle additions accompany the six replacements.

## Risks / Trade-offs

- Stale evidence mistaken for current acceptance → date and label the Mac/browser
  observations, and preserve explicit full-C10/RAG/UAT/release limitations.
- Passing scans mistaken for exhaustive security proof → retain unchanged policy
  limits, including Trivy HIGH/CRITICAL with ignore-unfixed=true and bounded Git scope.
- Artifact loss or access differences → provide the run and ID, expiry and access caveat.
- New docs mistaken for a tested source revision → distinguish the verified head from
  this subsequent documentation-only diff; do not invent a self-referential hash.
- Local dependency drift → run documentation/integrity/focused checks only; never
  present an unavailable local full-suite result as a pass.

## Verification and lifecycle

Before edits, obtain actual OpenSpec status/instructions and strict validation with
telemetry/update checks disabled. After edits, verify exact changed paths, six removed
live old-link occurrences, unchanged historical references and all three frozen blobs.
Check relative links/fragments, whitespace, private-data patterns, source-license
inventory, build/frontend integrity and supported focused regressions. Record actual
results in tasks.md; distinguish remote execution evidence from local candidate checks.

Independent content review remains required. Keep the change active until review and
all selected checks complete; then archive only this lifecycle with no main-spec sync
(skip_specs). Any normal commit must use the approved noreply identity. No push, PR,
merge, release, image publication or history rewriting is part of this preparation.
