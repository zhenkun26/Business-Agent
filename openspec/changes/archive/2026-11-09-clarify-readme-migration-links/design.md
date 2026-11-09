# Design

## Context

See proposal.md for motivation. The baseline contains 43 old-repository URLs; only two are repository-root links in source paragraphs. Four current/frozen source manifests contain neither exact root README paths nor their current hashes.

## Goals / Non-Goals

**Goals:** Clearly distinguish migration documentation from the original repository.

**Non-Goals:** Rewriting history, changing contributor credit, claiming new runtime or rights acceptance, or replacing the remaining historical evidence links.

## Decisions

Use relative links labeled “migration explanation” / “迁移说明”. Retain the BusinessAgent name as unlinked source history. Do not relabel a new target as the old repository. Keep the existing migration explanation unchanged and add it to the process index. No spec requirements change; use the official CLI's explicit documentation-only skip_specs mechanism while retaining propose/apply/strict validation/archive stages.

## Risks / Trade-offs

[Historical links may remain unavailable] → Preserve their evidentiary identity rather than imply replacement evidence.

[Existing acceptance limits could be misunderstood] → No manifest or receipt refresh, and no new runtime/full-RAG/UAT/rights claim.

## Migration Plan

Validate scoped changes, commit normally with verified privacy-safe identity, and run fresh candidate-bound checks. Independent review and CI precede any public merge. Revert this documentation commit if rollback is needed.
