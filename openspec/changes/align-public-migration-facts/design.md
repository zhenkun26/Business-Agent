# Design

## Context

The maintainer requests English-default bilingual GitHub documentation. Existing READMEs already contain supported overview, examples, architecture, setup, tests, documentation and license sections. The migration explanation and source-bound notice evidence remain authoritative.

## Goals / Non-Goals

Improve entry-point language and navigation without inventing features or acceptance. No code, runtime, rights, history-rewrite or workflow change.

## Decisions

Move the full existing English body to README.md and the Chinese body to README-zh.md, keeping both in the same directory so relative links retain their targets. Keep README-en.md as a compatibility index with old section anchors. Preserve Chinese root section anchors in the English default for existing links. README-zh.md is the requested language companion, not an unrelated root document; README.md remains canonical.

Lead with overview, examples, capabilities and setup. Move detailed historical verification/source boundaries alongside verification and limitations; retain approval safety boundaries before Quick start, without removing their qualification. Keep a short early non-production scope warning in both languages. Update both language switches and directory descriptions.

Retain public attribution, licenses and the reviewed migration corrections. Historical run 42591561481 is evidence only for 15cd84f942ccc0ce49afcfc1513efe4c2f07f441, never for this later candidate.

## Risks / Trade-offs

Changing the default language can break incoming fragments; preserve compatibility anchors. Preserve all existing section bodies and command blocks except explicit navigation changes and equivalent bilingual scope wording. Dependency-limited local checks cannot establish full pytest, runtime, distribution or UAT acceptance.

## Open Questions

None.
