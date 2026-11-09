# Tasks

## 1. Factual alignment

- [x] 1.1 Align bilingual migration summaries and preserve attribution/license text.
- [x] 1.2 Bind the notice conclusion to the exact existing run/source and preserve license-review limits.

## 2. English-default bilingual entry

- [x] 2.1 Move full language bodies to English README.md and Chinese README-zh.md; verify language switches, section-body and command preservation.
- [x] 2.2 Retain compatibility navigation and Chinese root anchors; verify old fragments and local links.
- [x] 2.3 Synchronize contents.md and confirm no unrelated files or frozen blobs changed.

## 3. Revised candidate verification

- [x] 3.1 Run available offline controls, strict OpenSpec and whitespace checks; bind results to the revised file manifest with explicit unavailable checks.
- [x] 3.2 Obtain independent revised-candidate review before commit or publication.

## Workflow follow-up

- Archive after review requirements and candidate-specific CI audit are satisfied; verify the archived result.
- Merging requires specific confirmation. Historical CI is not validation of this candidate.

## Verified implementation evidence

Independent review approved implementation head
`02ca5253b3ed520ca8e373b0ad29efc9c1f6b926` on base
`e81e412a99a70278a3541aa0c839b861aff37c02`.
[CI run 42622331120](https://github.com/zhenkun26/Business-Agent/actions/runs/42622331120),
pull_request attempt 1, passed all five jobs. Its executed merge was
`6c064e252408178662d92fb26c868b28403f0b38`, tree
`9680306b532c9f1de4f8d5369ff9088ce417c8b8`, identical to the implementation tree.
The audited source contained 1,036 files with content SHA-256
`dd6102a7673460394a3ecd32439d9153815978cdb5f888c30835dddcd507730a`.

Python 3.11 and 3.13 each passed 2170 tests + 640 subtests, eight offline checks,
nine publication-policy tests and 39 scanner regressions. The isolated C10
persistence slice, 15 synthetic HTTP checks, image build/load, installed inventory
and Trivy passed. The image inventory covered 98 Python and 106 OS packages.
GHCR login and publication were skipped; release gates remain BLOCKED.

Independent bounded review checked all nine artifact hashes against GitHub and
passed 21 binding checks, including 14 build inputs and eight retained notices.
Deep review included eight ZIPs, one TAR, 180 trace JSON records, one protobuf frame,
six bundled OCI blobs and eleven descriptor references. Eighteen controls passed
through the actual privacy scan pipeline, including base64 forms down to 12 encoded
characters. No personal paths, private learning material, tokens or event payloads
were detected within that reviewed scope; this is not a complete-erasure guarantee.
External image layers/config were not separately downloaded and extracted.

The Docker build had 39 steps with 29 cached; this is not two clean reproducible
builds. These checks do not establish full C10/RAG, browser acceptance, enterprise
UAT, rights clearance, distribution clearance or formal release acceptance.
Historical run 42591561481 remains bound only to its original source revision.

## Scoped lifecycle closeout

Only this completed lifecycle is moved to the 2026-11-09 archive and its existing
contents index entry relocated. README/notice content, frozen historical records,
code, workflows, main specs and other change records remain unchanged. skip_specs
requires no main-spec sync. The official archive skill's directory-move procedure
retains all four artifacts.

This later archive-only candidate was not executed by run 42622331120. It requires
its own subsequent CI and independent review before further publication decisions.
No merge, release or image publication is authorized by this record.
