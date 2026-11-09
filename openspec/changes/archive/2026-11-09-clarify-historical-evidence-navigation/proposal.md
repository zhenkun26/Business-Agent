# Proposal

## Why

Historical PR, CI and artifact links no longer provide publicly accessible navigation after the repository migration. Integrated main now contains the separately verified technical evidence needed to distinguish current checks from preserved historical events.

## What Changes

- Replace exactly 32 historical URL occurrences in eight existing documents with unlinked original-repository-qualified event identifiers.
- Add separate dated current-verification links and scope caveats; preserve historical dates, counts, hashes, outcomes, skipped/failed checks and administrative/publication events.
- Preserve the three frozen references byte-for-byte and retain actual source attribution and license statements.
- Record this documentation-only lifecycle and its index entry, without changing application behavior or acceptance rules.

## Capabilities

### New Capabilities

None. This is documentation navigation maintenance; `skip_specs: true` applies.

### Modified Capabilities

None. Existing documentation-layout and progress-issue-records requirements remain unchanged.

## Impact

Eight historical Markdown documents, this lifecycle and its contents index entry only. No code, tests, workflows, manifests, policies, release-gate tables, main specifications or other changes are modified.

## Non-goals

No history rewrite, old-event transfer, private raw evidence publication, source-rights clearance, new browser verification, full C10/RAG, formal UAT or release acceptance. Obsolete bilingual README migration quantities are outside this change. No push, PR, merge, image publication or archive during candidate preparation.
