# Design

## Context and decisions

Start from public main `4c8441a9a95e383160bb27587024c559cbb7f260` in an isolated local branch. Maintain only the eight hyperlinks in the phase-one assessment, plus a dated correspondence note and the required changelog and index entries. Preserve every other byte of the assessment after reversing these edits.

Three mapped commits preserve the initial-snapshot, R100-move and MIT-declaration semantics. The five file targets have byte-identical content. Use pinned objects, not floating main links. Correspondence does not preserve original commit identities or verified signatures and does not establish independent authorship or additional legal rights.

The note links to the existing rewritten-history explanation and explicitly preserves the historical candidate ID, file hashes, attribution and rights conclusions. No private paths, private audit reports, personal information or learning material enter these artifacts.

## Non-goals

No historical PR/CI substitution; no old archive rewrites; no changes to code, license terms, frozen evidence or manifest hashes. The provenance document is not a registered input of the current offline/source-license manifests. Do not regenerate those files.

## Verification

Check the exact eight substitutions and restore them plus the note to reproduce the baseline document byte-for-byte. Resolve all eight pinned targets and verify commit semantics and file SHA-256 values. Verify the relative note link, preserved literal candidate binding, attribution, whitespace, unchanged manifests and 43 remaining old repository URLs. Run provenance integrity, unchanged eight-check offline workflow and scanner regressions against the final local commit, retaining fresh receipts privately. Record any failed or unavailable check honestly; no receipt reuse.

## Lifecycle and rollback

Use the isolated OpenSpec 1.16.1 CLI with telemetry and update checks disabled. Its real instructions admit this spec-driven change; no project tooling or dependencies are changed. Follow the successful specs instruction snapshot before writing the main specification. Archive only this change after verification and review. Revert the documentation commit normally if needed; no history rewrite or force operation. No public action is part of this local preparation.
