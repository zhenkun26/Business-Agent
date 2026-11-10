# Design

## Context

See [proposal.md](proposal.md) for the wording issue. The review uses base commit
`caaf4b87e78625e9896dc84d7e5b7a8f059cd56b`:

- `enterprise-agent/app/api/approval.py::_execute_approval_tools` dispatches the
  committed plan through the current execution path.
- `enterprise-agent/app/tools/saga.py::SagaCoordinator.execute` stops a failed
  sequence through `recover_owned` and exposes `automatic_compensation: False`.
- `enterprise-agent/app/core/saga_retry.py::recover_owned` retains a manual hold;
  `retry_saga_compensations` is a compatibility job name, not inverse dispatch.
- `compensate_step` in that module validates retained historical inverse receipts
  without claiming or sending an inverse, and does not release the manual hold.
- `enterprise-agent/tests/test_saga_recovery.py` contains synthetic checks for
  failure, uncertain results, late receipts and the absence of inverse writes.

## Goals / Non-Goals

State the existing boundary in the status summary without removing historical
Saga records or suggesting that historical compensation never existed. Do not
change execution semantics or infer runtime acceptance from source inspection.

## Decisions

Replace the unqualified word “compensation” with a short explicit description in
both languages. Link to the already published approval guidance. Removing the
word alone would avoid one false impression but leave the historical records
unexplained; claiming automatic rollback would contradict the current source.

## Risks / Trade-offs

- Historical names can imply executable compensation. Explain that the records
  are retained for review and do not authorize automatic inverse actions.
- A documentation-only check can be mistaken for runtime validation. Keep all
  current acceptance limitations and report check scope separately.

No deployment or migration is needed. Reverting these documentation edits does
not change application behavior.
