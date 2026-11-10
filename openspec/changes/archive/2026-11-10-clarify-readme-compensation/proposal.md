# Proposal

## Why

The current-status paragraph in both root READMEs lists compensation as an
implemented capability without distinguishing retained historical records from
current execution. That can conflict with the earlier no-automatic-compensation
guidance and with the current implementation.

## What Changes

- Replace that unqualified capability claim in English and Simplified Chinese.
- Describe stopping failed or uncertain actions for human review and preserving
  historical Saga/compensation records without automatically issuing inverse actions.
- Keep existing acceptance limitations and historical evidence unchanged.

## Capabilities

### New Capabilities

None. This is a wording correction; no new specification or runtime behavior is introduced.

### Modified Capabilities

None. Existing execution and approval requirements are unchanged (`skip_specs: true`).

## Impact

Only the two root READMEs, their change record and its navigation entry are in scope.
No application, tests, dependency, schema, workflow, inventory or historical receipt
changes are required. Documentation and offline checks do not establish real-service,
full RAG, C10, UAT or production acceptance.
