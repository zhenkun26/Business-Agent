# Tasks

## 1. Bilingual clarification

- [x] 1.1 Correct both current-status paragraphs and verify the wording against the source references in design.md.
- [x] 1.2 Add the change to contents.md and verify all newly added local links resolve.
- [x] 1.3 Run focused offline Saga tests, strict scoped OpenSpec validation and whitespace checks; report any unavailable check without claiming it passed.

## 2. Review and publication

- [x] 2.1 Review the complete diff and verify application, workflow, schema, dependency and historical evidence files are unchanged.
- [x] 2.2 Open a draft PR, verify its head and changed-file scope, and record the corresponding CI state without reusing older evidence.

## Workflow follow-up

- Archive this documentation-only change after review requirements are satisfied; no main-spec sync is needed because no requirement changed.
- Reverify the final revision and applicable CI after any later archive or merge.

## Local verification

- Offline Python 3.12 unittest checks: Saga recovery 38, approval execution 34,
  human-hold integration 8; all 80 passed using synthetic doubles.
- OpenSpec 1.16.1 scoped strict validation, the two new README anchors, change
  navigation and `git diff --check` passed.
- Separate read-only review found no correctness or bilingual-parity issue.
- The full offline pytest entry reported `BLOCKED: DEPENDENCIES_UNAVAILABLE`;
  it did not run the full suite. Safe preflight execution passed, with UAT and
  release gates still BLOCKED. No application or real provider was started.

## PR verification

[Draft PR #7](https://github.com/zhenkun26/Business-Agent/pull/7) was opened with
implementation head `84234dfd688783f8acc94c1fb5527bd3ae619152` and seven documentation
files. Its tree exactly matched the locally reviewed tree
`10e9351d7a8096cb363ed4211909e93e2abd0748`. CI run `42760956826` was in progress when
this record was written, not passed. This record creates a later documentation
revision; check that revision's own CI before any merge. No acceptance gate is closed.

## Pre-archive verification

[CI run 42761059636](https://github.com/zhenkun26/Business-Agent/actions/runs/42761059636),
attempt 1, passed all five jobs for head `d57dfd95b3aba54c31bc04fa7c8afd5537a38fc5`.
It tested GitHub's PR merge revision `6a26e8ded903fdb2c8de479553033147a23bf1f6`.
Python 3.11 and 3.13 each passed 2170 tests plus 640 subtests and eight offline checks.
The existing isolated C10 persistence slice, synthetic demo and image/security checks
also passed. Image publication was not enabled. These checks do not establish full
C10, full RAG, real-enterprise UAT or production acceptance.

All five implementation/review tasks are complete. This documentation-only change
has no delta specifications to sync. Its archive move and navigation update create
a later revision, which must pass its own checks and CI before merge; a merge must
also be verified separately. The older pending-CI record above remains historical.

Scoped strict validation and archived-task validation passed for this change.
The repository-wide archived-task check still reports one incomplete task in the
unchanged `2026-08-04-documentation-baseline` archive; this correction does not
alter or claim to resolve that historical finding.
