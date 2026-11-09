## Purpose

Keep the eight phase-one provenance object links usable without changing the historical evidence or its limits.

## ADDED Requirements

### Requirement: Phase-one object links preserve historical meaning
The documentation SHALL use verified corresponding pinned objects for the three commit links and five file links in the phase-one assessment, while preserving its literal candidate ID, content SHA-256 values, attribution and rights conclusions.

#### Scenario: A reader follows a mapped evidence link
- **WHEN** the reader opens one of the eight maintained hyperlinks
- **THEN** the commit preserves the cited snapshot, move or declaration semantics, or the file has identical bytes
- **AND** a dated note distinguishes rewritten-history correspondence from unchanged historical identifiers and findings
- **AND** no preserved original commit identity, verified signature or additional legal right is claimed

### Requirement: Link maintenance stays narrowly bounded
The change SHALL leave historical PR and CI evidence, frozen artifacts, source inventories and acceptance gates unchanged.

#### Scenario: The local candidate is reviewed
- **WHEN** the diff and fresh checks are inspected
- **THEN** only the eight targets, correspondence note, documentation changelog/index entries and this change lifecycle artifacts differ
- **AND** new checks are bound to their actual candidate without implying production, UAT, full RAG or rights acceptance
