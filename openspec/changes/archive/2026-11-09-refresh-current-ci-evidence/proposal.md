# Refresh current CI evidence

## Why

Six live evidence references still direct readers to superseded executions. The fresh
2026-11-09 verification provides current technical evidence for public main, but only
its actually executed checks and inspected artifacts may replace those claims.

## What Changes

- Refresh the six live references in README.md, THIRD_PARTY_NOTICES.md, the UAT plan,
  open-source quickstart and release checklist; align the English README summary.
- Bind current claims to workflow_dispatch run 42591561481, attempt 1, exact head
  15cd84f942ccc0ce49afcfc1513efe4c2f07f441, with publish=false and skipped GHCR login/push.
- Separate fresh Python/offline/scanner/native-HTTP/isolated-persistence/image evidence
  from historical Mac/browser checks and from still-unestablished acceptance.
- Record only the new audited artifact identity and scoped notice-byte result; document
  retention/access limits without promising anonymous or permanent access.
- Add a bounded changelog entry and index this lifecycle. Preserve all remaining
  historical references, frozen files, rights conclusions and formal acceptance gates.

## Capabilities

### New Capabilities
None. This is evidence maintenance, not a new product or documentation behavior.

### Modified Capabilities
None. Existing documentation and acceptance requirements remain unchanged. This
pure documentation change uses the supported skip_specs declaration; no main-spec
sync is needed, and no artificial requirement is introduced to satisfy validation.

## Impact

Documentation only. No application/workflow/dependency/manifest, license or attribution
changes. No publication, deployment, PR, merge or history rewriting. Review and applicable
checks precede any completion judgment; a later documentation revision is not the head
executed by the cited run. The separate historical-navigation phase is out of scope.
