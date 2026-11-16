## ADDED Requirements

### Requirement: Deterministic analysis must preserve requested scope

The analyzer SHALL reject unsupported or unconsumed query semantics without publishing
substitute totals, and SHALL resolve case-insensitive customer selections only when unique.

#### Scenario: Unsupported statistic or negation
- **WHEN** a request asks for ranking, averages, or orders not completed
- **THEN** the analyzer returns a fixed unsupported error without a data result

#### Scenario: Lowercase or incomplete customer selector
- **WHEN** a request selects customer c001
- **THEN** only the uniquely matching source customer is included
- **WHEN** a selector has no ID, an unknown ID, or an ambiguous case match
- **THEN** the request fails without broadening to all customers

#### Scenario: Conflicting periods
- **WHEN** a relative period accompanies two explicit dates
- **THEN** the range is rejected before reading the source

### Requirement: Approval lists must expose bounded pages and accurate totals

Each approval list SHALL return a bounded page and the authorized total from one statement,
with a unique ID tie-breaker, while preserving existing identity and review safeguards.

#### Scenario: More than fifty records share a timestamp
- **WHEN** an actor has 53 matching approvals
- **THEN** the first page has 50 items, the next has three, and both report total 53

#### Scenario: Empty page or different actor
- **WHEN** the offset is beyond the authorized result set
- **THEN** items are empty and the authorized total remains available
- **WHEN** a different actor requests a page
- **THEN** that actor's role or ID predicate is applied again

#### Scenario: Stale browser response
- **WHEN** a response arrives after another page or identity is selected
- **THEN** neither its rows nor its pagination metadata replace the current view
