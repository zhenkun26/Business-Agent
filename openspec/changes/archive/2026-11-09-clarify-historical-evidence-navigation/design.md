# Design

## Context

See proposal.md for motivation. The base is integrated main `8ec795ea57b07502caadd14d2f48682052814f9d`, tree `9d4a1fba97adf5e4cb345b11a0008de42de1c2b3`. All 32 reviewed source lines and eight source blobs match this base. The current quickstart and notice targets now contain the separately audited verification and limitations, satisfying the prerequisite integration dependency.

## Goals / Non-Goals

**Goals:** preserve historical meaning while replacing inaccessible clickable navigation. Keep original event identities explicit and separate current evidence from old outcomes.

**Non-Goals:** no content expansion beyond the reviewed eight-document patch, required lifecycle and one index line; no changes to tests, parsers, release gates, policies, frozen files, main specs or other lifecycles.

## Decisions

1. Apply the reviewed 32-occurrence patch unchanged rather than remap old events to new same-number PRs. Original dates, outcomes, failed/skipped checks, counts, hashes, PR/admin and publication events remain historical.
2. Cite run 42591561481 only for exact `15cd84f942ccc0ce49afcfc1513efe4c2f07f441`, workflow_dispatch attempt 1 on 2026-11-09. The later navigation candidate is not its tested revision. No cached image build becomes two-clean-build proof, no HTTP test becomes browser proof, and skipped GHCR publication remains skipped.
3. Preserve generated historical anchors with an explicit anchor where needed. Validate new relative links against actual integrated target content, not just syntactic fragment existence.
4. Keep document-consumer status words, identifiers, table shapes and acceptance boundaries unchanged. In particular, retain the existing release-gate parser and its recognized status words; failed assertions require a reported truthful wording correction, never a weakened test.
5. Use supported documentation-only skip_specs. The plan is recorded before applying the navigation patch; no plan commit is necessary for this scoped documentation lifecycle. Keep candidate uncommitted pending independent review.

## Risks / Trade-offs

- Historical failure mistaken for current success → separate dated evidence blocks and unlinked original-repository-qualified IDs.
- Private evidence disclosure → publish no raw artifacts, local work paths or sensitive original metadata; inaccessible does not mean nonexistent or deleted.
- Artifact availability overstated → retain current notice expiry and authenticated-versus-anonymous access limits.
- Machine-consumed prose broken → run unchanged document-consumer/release-gate tests and require exact candidate CI later.
- Current-tree count mistaken for historical erasure → report 35 to 3 only for this candidate tree, retaining real Git history and source attribution.

## Verification and lifecycle

Verify all source lines/blobs before applying the exact approved patch, then inventory 32 removals and three unchanged frozen URLs. Verify new anchors, all unaffected tracked bytes, privacy patterns and whitespace. Run scoped OpenSpec strict and applicable existing focused tests without dependency installation. Full archive validation may retain the pre-existing incomplete documentation-baseline task; do not claim a global pass. Independent review and later exact candidate CI remain required. Do not archive, commit or publish during this preparation.
