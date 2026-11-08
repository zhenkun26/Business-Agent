## ADDED Requirements

### Requirement: Independent migration preserves bounded history
The migrated repository SHALL preserve every source commit and branch, with all historical tags retained locally and mapped but not pushed pending separate review, except that the two explicitly removed photo paths SHALL be absent from all reachable and stored objects; mappings SHALL record resulting SHA changes.

#### Scenario: A migrated commit is inspected
- **WHEN** source and destination commits are compared through the recorded mapping
- **THEN** their trees differ only by the authorized photo removal
- **AND** author, committer, timestamps, messages and parent order remain intact

### Requirement: Attribution and verification remain accurate
The repository SHALL retain MIT licensing, kingoftaro collaborator credit and existing third-party notices, and SHALL distinguish new verification from historical source evidence.

#### Scenario: Migration checks execute
- **WHEN** the destination is imported and checked
- **THEN** no Issues, PRs, CI history, secrets or protection settings are copied
- **AND** no image publication or deployment is performed
