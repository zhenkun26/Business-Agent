# C24 offline final-candidate verification

Date: 2026-10-19. Scope: E0/E1 only. **C24 remains open; overall acceptance is BLOCKED.**
The [ISSUES acceptance criteria](../40-process/ISSUES.md#c24) remain authoritative.
C23 `6de94c6` was pushed to `origin/codex/delivery-ci-gates` and verified before this increment.

## Current F2-10 prerequisite — 2026-10-20

Use the [current offline entry and CI coverage contract](offline-verification.md) for the
current candidate. It covers all Python tests plus both Node entries, assets, build inputs,
pending-source inventory, synthetic RAG controls and safe preflight. Its own reviewed source
manifest and no-skip accounting supersede this historical fixed inventory as the current
entry. The original C24 runner/manifest below remain unchanged and intentionally reject
drift; do not refresh their hashes to imply retrospective acceptance. C24 remains OPEN,
real runtime/full RAG BLOCKED, F2-05 privacy/F2-09 rights pending and C10 OPEN.

## Reproducible entry and evidence identity

Run from the repository root, using Python 3.11+ and an existing Node interpreter:

```bash
# Inventory only; no child execution, Git calls or fixture creation.
python3 -I -B enterprise-agent/scripts/final_candidate.py

# Explicit execution; choose a never-used receipt ID.
python3 -I -B enterprise-agent/scripts/final_candidate.py --execute --record c24-candidate-001

# Receipt/parser regressions, without pytest or plugins.
python3 -I -B enterprise-agent/tests/test_final_candidate.py
```

The [orchestrator](../../enterprise-agent/scripts/final_candidate.py) fixes 31 entries:
29 test suites, the seven-file frontend integrity check and the original five-function
readiness entry. The [source manifest](../../enterprise-agent/scripts/final_candidate_sources.json)
freezes 291 source/config/fixture files. This is an identity inventory, **not permission to
execute every listed file**. Only the fixed entry points execute. The manifest deliberately
excludes the orchestrator itself (the trusted entry, hashed in the receipt), Markdown and
itself; the tracked candidate digest binds all tracked files, including those exclusions.
There is no automatic trust-refresh command. Review changed source/import/side-effect
boundaries before deliberately revising its digest and rerunning affected checks.

Receipts bind HEAD, tracked content digest, dirty state, untracked-file count, historical
mode differences, reviewed source digest, runner hash, Python/Node versions, UTC time,
entry status and test/skip counts. Check source and candidate identity before/after the
sweep. `candidate_binding=PASS` means the content is clean, stable and bound to the commit;
it is **not** application acceptance. A dirty or untracked worktree remains unbound.
Mode-only differences are recorded and preserved, not silently staged or normalized.

Results use exclusive creation under ignored `enterprise-agent/eval/results/final-candidate/`.
No overwrite, append-to-existing, rotation or deletion is performed. Symlink paths and
collisions are refused. A crash or interrupted run without a completed receipt proves
nothing; retain fixtures/partial files, choose a new ID and rerun. Candidate-bound evidence
is generated again after the local commit; its commit hash lives in the ignored receipt
and delivery response, avoiding a self-referential documentation commit.

Exit 0 is inventory-only. Executed checks return 1 if an entry fails, otherwise 2 because
acceptance stays BLOCKED. Missing prerequisites/source drift/record failure also return 2
with a fixed reason. Inspect the JSON, not just the exit code. Empty/wrong/duplicate test
counts, malformed summaries, unexpected skips and failed children cannot be PASS. No raw
stdout/stderr, exception text, environment values, credentials or application payloads are
persisted. Timeouts fail the entry; there is no business retry.

## Current offline coverage and remaining acceptance

The following counts are test methods/cases, not subtests, coverage percentages, independent
requirements or runtime measurements. Multiple suites exercise shared helpers. The seven
asset files and five readiness functions are counted separately from tests.

| Item | Current offline check / passing cases | Uncovered acceptance; entire item remains open |
| --- | --- | --- |
| C01 | Deployment 10 PASS + 1 PyYAML skip; Dockerfile 4 PASS | Actual Compose resolution, same image digest, build/Nginx/login/SSE |
| C02 | Profile 15 + remote adapters 12 PASS | Real embedding/reranker/LLM, quota/cost, installed dependency imports |
| C03 | Bootstrap/migration orchestration 22 PASS | Real PG SQL, concurrent upgrade/rollback and initialization |
| C04 | Session ownership 20 PASS | Real HTTP/PG ownership and races |
| C05 | Runtime authorization 29 PASS | Real JWT crypto, revocation, API/SSE |
| C06 | Credential safety 20 PASS; browser lifecycle included below | Real browser/SSO and historical credential review/remediation |
| C07 | Retrieval authorization 21 PASS | Actual Milvus/SQL filtering and citations |
| C08 | Request context/history/dependencies 23 PASS | Real LangGraph concurrent dispatch/history |
| C09 | Cross-process state 28 PASS | Actual two processes, Redis Lua/TTL/restart |
| C10 | Lifecycle 27 + stale-writer isolation/publication 28 PASS | Real saver/PG locking, two-process expiry races and API/SSE remain BLOCKED; C10 stays open |
| C11 | Approval lifecycle 34 PASS | PG atomic claims/expiry/crash and browser flows |
| C12 | Tool operation safety 41 PASS | PG/HTTP duplicate dispatch and uncertain response |
| C13 | Saga recovery/HTTP compensation 34 PASS | Durable PG/process failure and external inverse effects |
| C14 | Queue/worker 50 PASS | Real locking, worker restart and external dispatch |
| C15 | Knowledge publication 36 PASS | PG/Milvus indexing consistency and full RAG |
| C16 | Analysis adapter 33 PASS | Real CRM snapshots, identity and API/SSE agreement |
| C17 | Quality/metric contracts 29 PASS | Frozen 122-case real-model RAG run, six role controls, semantic review |
| C18 | Reference integration 45 PASS | R01–R20 independent persistent HTTP/application chain |
| C19 | Controlled SSO 37 PASS | S01–S16 real RS256/IdP/browser/Redis/PG |
| C20 | Delivery 45 + credential VM 14 PASS; 7 asset files PASS | B01–B16 actual browser DOM/UI/API role journeys |
| C21 | Observability 45 PASS | O01–O16 disk retention/replay, real faults, traces, firing/resolved alerts |
| C22 | Recovery 46 PASS | D01–D16 actual cold capture/fresh-volume restore, RTO/RPO |
| C23 | Capacity 42 PASS | L01–L16 actual frozen 30-minute workload, queue/resource/cost evidence |
| C24 | Safety 12 + receipt 16 PASS; five functions execute successfully | Complete application regression, E2/E3 and final runtime evidence |
| C25 | Offline reconciliation delivered separately | Git/PR/CI/support/version/document reconciliation and delivery conclusion |

Current C10 follow-up sweep: **818 tests PASS, 1 skipped/BLOCKED**, seven frontend asset/license files
PASS. Five readiness functions execute: three result PASS, two BLOCKED (UAT readiness and
release gate). They do not increase the 818 test count. Synthetic G0 is not application E2E.

## Side effects and trust boundary

- Python children use `-I -B`; no full pytest, conftest/plugin discovery or bytecode/cache writes.
  Node executes only the two reviewed VM entries; `NODE_OPTIONS`/`NODE_V8_COVERAGE` are removed.
  The existing host environment is otherwise inherited so its Git wrapper works; tests use
  synthetic configuration/injected clients, do not read `.env`, and never serialize the environment.
- C01/C02/C03 entries were reviewed for read-only source loading and injected dependencies.
  C04–C23 entry/fixture/import boundaries follow the [side-effect inventory](safe-validation.md).
  HTTP, PG, Redis, Milvus, JWT, LangGraph, Docker and model behaviors are replaced or extracted
  where stated. No service/listener/browser, dependency install, image build or paid API runs.
- C22 creates retained synthetic archive/files under `eval/results/c22-tests-<uuid>/` with
  Docker/chown injected. Safety tests retain `eval/results/safe-validation-tests/<uuid>/`;
  the synthetic symlink there is intentional and never removed. C24 receipt tests retain
  `eval/results/c24-tests-<uuid>/`. These tests may edit their newly created synthetic fixtures;
  they never delete them or modify application/user data. The orchestrator itself creates only
  the optional exclusive receipt and invokes fixed children/Git metadata commands.
- This is trusted local code orchestration, not an OS sandbox. Existing child audit hooks
  provide additional guards but cannot prove all native-code behavior is confined. The host,
  interpreters, Git wrapper, standard libraries and concurrent filesystem editors are trusted.
  Before/after hashes detect drift; they do not prevent transient concurrent edits. Do not edit
  the checkout during a sweep. Do not use this entry to run unreviewed or malicious code.

## Failures found and disposition

The first comprehensive run found an outdated C02 worker-startup test double: C21 added
imports/lifecycle behavior that the isolated extracted function did not have. Add injected
audit/tool initialization, asyncio and DB closure, and expect the current sanitized
`WORKER_FAILED` error for the worker. Still assert the model probe is attempted once,
DB/audit/tools initialization never happens after failure, and worker cleanup occurs.
No application behavior was changed. The repaired 15-case suite and full sweep pass.

An initial ad-hoc launcher stripped the host environment and broke the configured Git
wrapper (exit 126), causing three safety-test errors. The normal environment rerun passes
all 12. The durable runner preserves the host environment and only removes the documented
Node preload/coverage options. Initial failures are retained here; they are not relabelled
as successful runs. The PyYAML skip remains distinct; Ruby parsing is separate E0 evidence,
not execution of that Python test or a Compose engine.

The first Ruby YAML sweep also rejected unquoted colon-bearing flow scalars in the
reference and SSO Compose recipes. Quote only those nine strings and verify the parsed
security options and mount values. All nine reviewed YAML files then parse; this is parser
compatibility/E0 evidence, not Compose interpolation, merge or deployment.

Additional static checks: 214 Python sources compile in memory, three JavaScript sources
pass `node --check`, and two shell wrappers pass `bash -n`. No bytecode or build output
is created. Changed document links and delta structure are checked separately.

## Gates that this increment cannot close

L01–L16, D01–D16, O01–O16, B01–B16, S01–S16, R01–R20, real runtime/full RAG and historical
credentials remain BLOCKED. No enterprise evidence, formal UAT, grey release, production
approval, maximum capacity, monthly SLA or current image security claim is made.

Whole pytest/plugin/temporary-fixture behavior and actual dependency-based imports have not
been reviewed/run under the non-deletion rule. The fixed sweep covers the closeout suites,
not the entire repository test population. The current host lacks Docker/OpenSpec/ruff;
image builds, scanners/current CI, real Linux and `openspec validate --strict` are BLOCKED.
Manual delta structure/link checks are only E0, never a substitute for OpenSpec strict.

Resume runtime acceptance only after separate authorization, isolated Linux resources,
resolved C10 fencing and the prerequisite matrices/observations. Freeze candidate image,
model profile, fixtures and environment again; changed bytes invalidate affected results.
C24 stays open. C25, spec synchronization/archive, push/merge/deployment/release do not
follow automatically from this offline increment.


### C10 follow-up evidence (2026-10-19)

The 28-case fencing entry was reviewed for SQL/clock/saver substitution and side effects
before addition to the fixed inventory. No new skips or collection exclusions were added.
Local full pytest independently passes 900 tests + 232 subtests, zero skips; its retained
receipt and platform limits are in the C10 delivery record. The fixed inventory's existing
`FULL_PYTEST_DEPENDENCIES` gate is a scope limitation of that entry, not a failure of this
separately executed local suite. Remote CI/image results at earlier commits are historical
and do not validate the C10 source changes. Current C10, real runtime/full RAG, all live
matrices, OpenSpec strict and release remain BLOCKED/open.


## Stage-one technical candidate progress — 2026-11-07

This separate dated section does not rewrite historical C24 evidence above. The current
milestone is open-source usability; enterprise pilot evaluation, real-environment pilot
and production use remain later stages. Stage one is not yet accepted or merged.

- Mac arm64 Python 3.13.15 used a previously approved binary-driver adapter. Run-05
  passed 15 actual HTTP checks and 14 focused demo tests after a misleading startup-log
  correction. Two owned containers and two processes exited; data/evidence were retained.
- Run-04 actual browser checks passed login, 你好/您好, explicit unsupported pre-execution
  rejection, current-session history, refresh/login isolation, relogin and logout with
  password/authenticated-content clearing. Run-05 changed logging only, not UI bytes.
- History limitation: backend persistence and session-specific querying are established;
  current-session history can show a snapshot with unknown status, not business success.
  Refresh returns to login; relogin opens a new empty session with no visible recovery
  entry for the previous session. No complete history-management claim is made.
- Linux CI now explicitly requires system libpq5, pure psycopg, and no binary/C package,
  then fresh startup, tracked acceptance and owned stop. Actual Linux results are pending.
- Image publication is disabled by default: explicit manual publish=true on main only,
  behind existing security and C10/native checks. Three publication-policy tests covering
  27 event/ref/input combinations passed. No publication or deployment occurred.
- First full-suite attempt: 2134 collected, 2133 passed plus 640 subtests, one failure in
  an old hard-coded CI needs assertion. Its exact three-dependency assertion was repaired;
  a later full rerun passed as recorded below. This first failure is retained rather than relabeled PASS.
- Source inventory: 457 historical records plus eight new engineering fixtures = 465.
  Registration does not clear prior unknown rights. Maintainer testimony covers only
  three C17 documents (two departmental documents and after-sales policy) and eight CRM
  examples as fictional from creation; it is not evidence for other works or external grants.
- The separately authorized CRM increment now labels eight fictional customers and uses
  NOT-A-PHONE phone placeholders and example.invalid customer email addresses in current
  examples and product material. The internal-mail seed deliberately uses
  fictional-demo-manager@company.internal with a synthetic-data comment, preserving
  the existing private-domain policy. The three tests also checked the real classifier
  AST: the internal recipient is admitted, while external customer/CC cases are rejected
  or classified at their existing boundary; no mail rule was broadened. Three
  focused tests passed; orders/non-contact fields were unchanged by AST comparison. One
  new test source is included in the eight additions above. Expected final pytest count
  is 2137 (2120 + 14 demo + 3 CRM), confirmed by the precommit rerun below. Run-05 predates
  these CRM edits and is not live evidence of all final bytes; the narrow demo denies CRM
  calls. Linux CI must test the final commit. Old C17 documents and unapproved UAT phone
  changes remain outside this replacement scope.

Source uncertainty, full C10/runtime/RAG and enterprise acceptance limitations remain.
The current merge condition is stage-one readiness, not completion of later enterprise
stages, but material distribution-rights blockers cannot be hidden or silently waived.

Retained historical screenshots were not replaced and may still display historical contact details or additional unconfirmed recipients. The text/fixture update is not a claim that all visual examples or their source rights have been cleared.


### Final precommit offline rerun — 2026-11-07T13:05:20Z

The r2 aggregate receipt reports all eight checks PASS: 2137 Python tests plus 640
subtests, Node 80/14, seven assets, 81.8543% coverage and stable sources. Candidate
binding remains BLOCKED because this was a dirty precommit candidate, not a clean
committed or remote-CI result. This does not establish stage-one completion.

The second full-suite attempt had 24 failures caused by the edited demo-seed checksum.
The repair changed only schema_manifest.demo_seed SHA; an old marker is still rejected
without state mutation. All 26 focused bootstrap checks passed. That failed attempt
is retained separately from the successful r2 result, with no skipped checks or lowered
admission gate claimed.

The 39 actual-Gitleaks regression tests passed. Local documentation-link review checked
60 targets with zero missing. Linux native-driver and C10 CI execution remain pending,
as do unknown-source and historical-screenshot decisions. Final committed binding and
remote results must be checked before any conditional merge.

### Staged whitespace inspection

A staged check included newly added files that the earlier unstaged diff check did not
cover. It found extra EOF blank lines in the project-authored fictional-CRM specification;
only those redundant terminal blank lines were removed.

The verified upstream license bytes are preserved: the Fraunces, Manrope and NotoSansSC
license line-21 trailing spaces and the OpenSpec MIT license's extra EOF blank line are
intentional upstream-byte preservation, not silently stripped formatting. Consequently,
a blanket claim that the complete staged diff has no whitespace findings would be
incorrect. Earlier diff-check results describe only their actual inspected scope.


### Verified code candidate CI — documentation follow-up

[Run 42376168479](https://github.com/zhenkun26/BusinessAgent/actions/runs/42376168479)
passed all five jobs for code head 42644960a499cefe71c8ad21110bdd0b9cec39ce;
actual merge checkout was 96fb4ed665f20e13d461829320bba913f6041b22.
This section follows that verified code in documentation only. The later documentation
commit and its own CI are recorded in the PR, not represented by a self-referential hash.

- Python 3.11 and 3.13 each passed 2137 tests plus 640 subtests.
- Native synthetic-demo artifact 13576140776 records 15/15 checks, driver implementation
  python and libpq 180006. Ubuntu CI explicitly installed libpq5
  18.6-1.pgdg24.04+2 and preflight established no binary/C wrapper. Owned stop succeeded
  in public logs. This proves the specified CI runner environment, including preinstalled
  tools/configured repositories, not all bare machines or operating systems.
- C10 artifact 13576330125 records 17 + 17 + 24 + 5 checks PASS, clean before/after,
  source binding PASS and containers_stopped=true. Its full_c10=false and full RAG
  BLOCKED declarations remain authoritative; scoped checks do not close full acceptance.
- Production image and security checks passed, with Trivy limited to the existing
  HIGH/CRITICAL, ignore-unfixed=true gate. GHCR login and push were skipped.
- Historical failed attempts remain above. Unknown-source decisions, retained historical
  screenshots, missing cross-refresh UI history recovery and full enterprise/RAG
  acceptance limitations remain unresolved. No merge, publication or deployment follows
  from this documentation update.


### First reversible asset cleanup — 2026-11-07

Only the current high-resolution `01-login.png` encoding is changed. It remains
3200 x 1730, 8-bit RGBA at 192 DPI. Its 22,145,730 uncompressed scanline bytes
and decoded pixel hash are unchanged. The current PNG shrinks from 6,329,166
to 1,601,370 bytes (4,727,796 bytes, 74.69856%); this is source-file size only,
not a production-image or measured page-transfer reduction. The page uses WebP.

The initial compression experiment incorrectly retained the private fpng fdEC
marker with a new zlib stream. Independent review rejected that experiment:
the [official fdEC format](https://github.com/richgel999/fpng/wiki/fdEC-PNG-chunk-definition)
requires restrictions the rewritten stream does not meet. The accepted standard
PNG removes only that 17-byte encoding marker and recompresses IDAT; original
IHDR, pHYs and IEND bytes, alpha and scanlines are preserved. No author, license
or source-permission metadata is removed. Specialized fpng fast decoding is not
preserved or claimed; no repository dependency on it was found.

Independent CRC/strict EOF/scanline and separately implemented RGBA checks passed.
Native ImageIO properties and pixels match, and Edge InPrivate directly decoded
both files at 3200 x 1730 with normal visible content. A separate retained
presentation fixture, omitting only PNG during copying, passed page-15 lazy
loading, carousel navigation, return navigation and refresh. Both variants
requested WebP successfully, with no PNG requests or screenshot errors. These
checks are not a same-viewport screenshot diff or every-browser certification.

Original SHA256: `899fed0a7b83cca5338171657eed151166bf38238f039fd12335123264c2a78c`.
Current SHA256: `c0c94c7a92934a818bf698490aac0225779c6aa4ea2be5553824fc93772985ff`.
Pixel SHA256: `a905c29b1ca94dfc67165bdb6517e3e36b9d3c8dc9994489eba9971af269e634`.
The exact original remains recoverable from commit 42644960a499cefe71c8ad21110bdd0b9cec39ce
and a retained independently verified copy. Historical 457-item CSV, previous
diagnostic files and Git history are unchanged. Current inventory remains 465
pending items: compression does not establish source rights. No other screenshot
content is changed. Aggregate verification and exact committed CI must be recorded
separately; this change does not close stage one or authorize publication.

The isolated PNG precommit aggregate (2026-11-07T14:02:21Z) passed all eight
checks: 2137 Python tests plus 640 subtests, Node 80/14, seven frontend assets
and 81.8543% coverage. Sources remained stable. Its dirty candidate binding is
BLOCKED by design; exact clean-commit verification and remote CI are separate
required evidence, not inferred from this precommit result.


## Presentation copy refresh — 2026-11-07

Applied the independently reviewed r4 presentation copy after the separate PNG
commit `62cc7573fc476e95077fa90d9301df19ecd26b10`. The page now separates the
model-free synthetic demo from the unaccepted full external-model candidate,
labels July prototype diagrams and screenshots as historical, states current
approval/manual-hold semantics, and identifies all three later delivery stages
as unfinished. Source decisions still block stage one. This is a copy update,
not model, RAG, UAT, production or source-rights acceptance.

Page SHA256: `fa4a70d3942a347e9676c0d0a34507f984d4f2c58256b10d911365fc7bb08875`.
Original page SHA256: `1b3152c5b4b228a9fd2e5ac8e636f44e4cd6b9bac227f3d336f3fb82a90f921f`.
The original and all intermediate candidates remain retained. Current inventory
hash binding changes only for this page; all 465 pending items and the historical
457-item CSV retain their review status and content respectively.

Independent static review and actual desktop-browser review covered r3 key pages
and the r4 page-25 roadmap, plus refreshed opening and closing pages. The retained
r4 fixture matched the page hash above and returned HTTP 200 on both recorded
GETs. Browser receipt: `eval/results/presentation-copy-review-711f61a47d63/browser-r4-receipt-0516e8807102.json`,
SHA256 `bfcb38a216cc074aa29fd00fe2c52bf926e158851f8e5c08584dfb1d07f5c088`.
These are desktop checks, not mobile or all-viewport certification. The existing
FAQ-modal keyboard/background-page-navigation issue remains a separate known
item; this copy update neither introduces a fix nor conceals it.

Local static checks preserve all 27 section identifiers, CSS and navigation/
animation scripts; HTML parsing and inline JavaScript syntax checks passed.
The preceding PNG commit's eight clean aggregate checks and five passing CI jobs
belong to that PNG commit only. The page precommit aggregate at 2026-11-07T14:24:00Z passed all eight checks:
2137 Python tests plus 640 subtests, Node 80/14, seven assets and 81.8543%
coverage. Source stability passed; dirty candidate binding remains BLOCKED as
designed. Receipt: `enterprise-agent/eval/results/offline/presentation-r4-precommit-20261107.json`.
Exact clean-commit binding and remote CI remain separate required evidence.


## Second reversible asset cleanup — 2026-11-07

Only `interview/产品介绍网页/screenshots/06-zhangsan-tracked.png` is re-encoded:
613,356 to 360,187 bytes, saving 253,169 bytes (41.276%). The standard PNG
preserves 3200 x 1730, 8-bit RGBA, 192 DPI, the original IHDR/pHYs/IEND chunks
and all 22,145,730 scanline bytes. The identified fpng fdEC payload
`522493e300` is removed with its 17-byte chunk because the rewritten IDAT is
not the restricted fpng encoding. Specialized fpng fast decoding is not claimed.
No author, license or source-permission metadata is removed.

Original SHA256: `eac227d45eafee917196e3c2875fafd5d5d4a3729d312fec89b7e10243ccefac`.
Current SHA256: `ad2152a2a25292910572d3b8b95618dea63b1a77811ad2b960e53195125cb899`.
Scanline SHA256: `7c10e4cead1b71e2b6bfbbe666c3bc61334f0abd1355803331dcdacd5918936e`.
Decoded pixel SHA256: `02db7171f95e0b5c6761afac7e52f04591d4b02ae08eac27eb36eabfaf57e80d`.
Strict CRC/EOF and scanline checks passed. Independent filter-0/2 RGBA review
and native ImageIO decoding agreed on pixels; ImageIO properties also matched.
The original is recoverable byte-for-byte from commit
`62cc7573fc476e95077fa90d9301df19ecd26b10` and retained original/Git-restored
copies under `eval/results/tracked-png-diagnostic-ee1c243b930e/`.

Actual Edge InPrivate direct decoding displayed both images at 3200 x 1730
with complete, normal, visually consistent approval-list content. Both image
GETs returned 200, with fixture hashes matching the originals and candidate.
Receipt: `eval/results/tracked-png-browser-8a0273c63aa7/browser-receipt-f54f3779ae14.json`.
This is not an automated screenshot pixel diff or cross-browser certification.
The page still uses the unchanged WebP; no page-transfer or production-image
size improvement is claimed. Only the current PNG inventory hash and dependent
inventory binding are refreshed. All 465 source items remain pending; the
historical 457-item CSV and all previous evidence remain unchanged. Compression
is not source-rights acceptance. This local candidate does not close stage one
or authorize publication. The precommit aggregate at 2026-11-07T14:32:00Z passed all eight checks:
2137 Python tests plus 640 subtests, Node 80/14, seven assets and 81.8543%
coverage. Sources stayed stable; dirty binding remained BLOCKED as designed.
Receipt: `enterprise-agent/eval/results/offline/cleanup-tracked-png-precommit-20261107.json`.
Exact clean-commit verification and remote CI remain separate required evidence.


## Third reversible asset cleanup — 2026-11-07

Only `interview/产品介绍网页/screenshots/07-zhangsan-ask-progress.png` is
re-encoded: 561,505 to 383,218 bytes, saving 178,287 bytes (31.75163%).
The standard PNG preserves 3200 x 1730, 8-bit RGBA, 192 DPI, all original
IHDR/pHYs/IEND bytes and 22,145,730 scanline bytes. The only removed chunk is
the identified 17-byte fpng fdEC marker (payload 522493e300); the new zlib
stream does not claim specialized fpng fast decoding. No author/license or
source-permission metadata is removed.

Original SHA256: `b4540248fa8763384e96e61da3809f1a3575d1c8b604467521f67af70d53550f`.
Current SHA256: `7536c712af90cc4cc6a299156a04928145fc54cd9951ee217d849aaa7c7da9a7`.
Decoded pixel SHA256: `3654a5fa0c5f464569004a57fc88e8fe0cad616c6e409f2c4a9c2ba7505dca12`.
Strict CRC/EOF and identical scanlines passed; independent filter-0/2 RGBA
reconstruction agrees with native ImageIO pixels and properties. All pixels
remain opaque. Exact originals remain recoverable from commit
`8848eecb5d39e7ca639f8040c3dfddec130624dd` and retained byte-identical copies
under `eval/results/progress-png-diagnostic-3abde10d0f54/`.

Actual Edge InPrivate directly displayed both files at 3200 x 1730, with
normal, visually consistent historical approval-progress content. Both GETs
returned 200 and actual fixture hashes matched. Browser receipt:
`eval/results/progress-png-browser-197c3be78c7e/browser-receipt-20b0541eac29.json`.
This is not automatic screenshot pixel-diff or cross-browser certification.
The page still uses the unchanged WebP: no page-transfer or production-image
saving is claimed. Only this PNG current inventory hash and its dependent
source-map binding change; all 465 items remain pending. Historical 457-item
CSV and prior evidence remain unchanged. Compression does not clear rights.

The first write attempt lost its execution connection. On recovery, HEAD
remained 8848eec with a clean tree, all four original hashes and no third
cleanup section; the candidate was applied only after confirming no partial
write. The precommit aggregate at 2026-11-07T23:29:21Z passed all eight checks:
2137 Python tests plus 640 subtests, Node 80/14, seven assets, 81.8543%
coverage and stable sources. Dirty candidate binding remains BLOCKED by design.
Receipt: `enterprise-agent/eval/results/offline/cleanup-progress-png-precommit-20261107.json`.
Exact clean-commit verification and remote CI remain separate required evidence.


## Fourth reversible asset cleanup — 2026-11-07 UTC

Only `interview/产品介绍网页/screenshots/04-zhaoliu-pending.png` is
re-encoded: 457,946 to 287,798 bytes, saving 170,148 bytes (37.1546%).
The standard PNG preserves 3200 x 1730, 8-bit RGBA, 192 DPI, all original
IHDR/pHYs/IEND bytes and all 22,145,730 scanline bytes. Only the identified
17-byte fpng fdEC marker (payload 522493e300) is removed; ordinary zlib level 9
compression does not claim compatibility with the specialized fpng fast decoder.
No author/license or source-permission metadata is removed.

Original SHA256: `37f47171c1133f298500b7888e0f5d542722aee0f8323455306c8874d104f7cd`.
Current SHA256: `740fd3b1d9e2160ed7175f66e0c2c487b874644ab26cf0694993e2068487b082`.
Decoded pixel SHA256: `4cf13a6b479ac442eb8694fcb38aebfd89692c7032ec4c304b699a9bd30922d6`.
Strict CRC/EOF, identical scanlines and native ImageIO pixel/property checks
passed for this image; independent review passed before application. Originals
are recoverable byte-for-byte from `24b40a1d6a0b8d79e7767011a647399ca2f279ce`
and retained original/Git-restored copies in
`eval/results/pending-png-diagnostic-24b40a1d/`.

Actual Edge InPrivate opened baseline and candidate sequentially; AX dimensions
were 3200 x 1730 and screenshots displayed complete, normal, visually consistent
pending and historical approval lists. Both image GETs returned 200; fixture
hashes were verified.
Receipt: `eval/results/pending-png-browser-24b40a1d/browser-receipt.json`.
This is not an automated screenshot pixel diff or cross-browser certification.
The page uses unchanged WebP: no page-transfer or production-image saving is
claimed. Only this PNG current inventory SHA and the dependent inventory binding
are refreshed. All 465 source items remain pending; the historical 457-item CSV
and all prior evidence remain unchanged. Compression does not clear source rights.
The precommit aggregate at 2026-11-07T23:40:04Z passed all eight checks:
2137 Python tests plus 640 subtests, Node 80/14, seven assets, 81.8543%
coverage and stable sources. Dirty binding remains BLOCKED by design.
Receipt: `enterprise-agent/eval/results/offline/cleanup-pending-png-precommit-20261107.json`.
Exact clean-commit verification and remote CI remain separate required evidence.


## Fifth reversible asset cleanup — 2026-11-07 UTC

Only `interview/产品介绍网页/screenshots/09-zhaoliu-saga-result.png` is
re-encoded: 445,522 to 297,334 bytes, saving 148,188 bytes (33.2617%).
The standard PNG preserves 3200 x 1730, 8-bit RGBA, 192 DPI, original
IHDR/pHYs/IEND bytes and all 22,145,730 scanline bytes. Only the identified
17-byte fpng fdEC marker (payload 522493e300) is removed; standard zlib level 9
does not claim compatibility with the specialized fpng fast decoder.
No author/license or source-permission metadata is removed.

Original SHA256: `51e2569a46772bbd3f5fdd19086b23d63f81b7b98ca76ba48f4be43b8d3b055e`.
Current SHA256: `139cbde16d9152607db3c23f925fbfb2330892c830fb802e97af47925f0e4d9d`.
Decoded pixel SHA256: `cfb92c720fa99537de31bd38cece412bdcceb79f5c1dfd1591da9dae39e3f843`.
Strict chunk CRC/zlib EOF, identical scanlines, native ImageIO pixel/property
checks and independent byte/pixel/recovery review passed before application.
Originals are recoverable byte-for-byte from `3998172455f3fb54699e01a568be00c1852baee1`
and retained original/Git-restored copies under
`eval/results/saga-result-png-diagnostic-3998172455/`.

Actual Edge InPrivate opened baseline and candidate sequentially; AX dimensions
were 3200 x 1730 and screenshots displayed complete, normal, visually consistent
historical Saga result content. Both actual browser image GETs returned 200
at 23:45:17Z and 23:46:16Z on 2026-11-07, separately from the earlier HTTP probe.
Fixture hashes were verified. Browser receipt:
`eval/results/saga-result-png-browser-3998172455/browser-receipt.json`.
This is not an automated screenshot pixel diff or cross-browser certification.
The page uses unchanged WebP: no page-transfer or production-image saving is
claimed. Only this PNG current inventory SHA and the dependent inventory binding
are refreshed. All 465 source items remain pending; the historical 457-item CSV
and prior evidence remain unchanged. Compression does not clear source rights.
The precommit aggregate at 2026-11-07T23:49:17Z passed all eight checks:
2137 Python tests plus 640 subtests, Node 80/14, seven assets, 81.8543%
coverage and stable sources. Dirty binding remains BLOCKED by design.
Receipt: `enterprise-agent/eval/results/offline/cleanup-saga-result-png-precommit-20261107.json`.
Exact clean-commit verification and remote CI remain separate required evidence.


## Sixth reversible asset cleanup — 2026-11-08 UTC

Only `interview/产品介绍网页/screenshots/02-zhangsan-welcome.png` is re-encoded:
355,241 to 223,511 bytes, saving 131,730 bytes (37.0819%). Standard zlib level 9
preserves IHDR/pHYs/IEND and all 22,145,730 scanline bytes; only the identified
17-byte fdEC marker (522493e300) is removed. Specialized fpng decoder compatibility
is not claimed. No author/license metadata is removed.

Original SHA256: `21ca016aca8251db085999d00a19fad7cc62a1fb80259f2ac13226baa0f1d1e4`.
Current SHA256: `288c70120096789963c7671f5bdae61c610e0518629e108fdc30a9143e0b9e8b`.
ImageIO pixel SHA256: `26db214ecd58637606ee407b021027d66987cd8f2aa623a24e187b4230e39c61`.
Strict CRC/EOF, scanline equality, native pixels/properties and independent review
passed. Originals are recoverable from `d2ee6253d220510f68191bfd7afc24bb46cbcd13`
and retained under `eval/results/zhangsan-welcome-png-diagnostic-20261107/`.

Actual Edge InPrivate AX/screenshot inspection found both 3200 x 1730 images clear,
normal and visually consistent. Direct image GETs returned 200 at 03:18:57Z and
03:19:15Z on 2026-11-08. Screenshot evidence is in the task conversation tool
history, not claimed as saved files. Browser receipt and fixture hashes:
`eval/results/zhangsan-welcome-png-browser-20261107/browser-receipt.json`.
This is not automated screenshot pixel diff or cross-browser certification.
Only this current inventory SHA and its offline binding change. All 465 source
items remain pending; historical 457-item CSV and earlier evidence are unchanged.
Unchanged WebP page usage means no page-transfer or production-image savings
are claimed. Compression does not clear source rights.

ImageIO also confirms unchanged 3200 x 1730, 8-bit RGBA and 192 DPI.
The initial Python 3.12 invocation lacked dependencies (seven checks passed,
Python BLOCKED); its receipt is retained as
`enterprise-agent/eval/results/offline/cleanup-welcome-png-precommit-20261108.json`.
No dependency was installed. Re-running with the existing isolated Python 3.13
environment passed all eight checks at 2026-11-08T03:24:02Z: 2137 tests plus
640 subtests, Node 80/14, seven assets, 81.8543% coverage and stable sources.
Receipt: `enterprise-agent/eval/results/offline/cleanup-welcome-png-precommit-20261108-env.json`.
Dirty candidate binding remains BLOCKED by design; clean-commit verification
and remote CI are separate evidence.


## Seventh reversible asset cleanup — 2026-11-08 UTC

Only `interview/产品介绍网页/screenshots/03-zhangsan-submitted.png` is re-encoded:
305,411 to 179,710 bytes, saving 125,701 bytes (41.1580%). Standard zlib level 9
preserves IHDR/pHYs/IEND and all 22,145,730 scanline bytes; only the identified
17-byte fdEC marker (522493e300) is removed. Specialized fpng fast-decoder
compatibility is not claimed. No author/license metadata is removed.

Original SHA256: `a0732246a54690d76adae99564f76bf9442ccbc1d0eeeed7f7b99490526dbd5d`.
Current SHA256: `78c6c288ac051c9ec0139e1b19f2194a3a7d95631a308de849e1925594bd8e1e`.
ImageIO pixel SHA256: `ecb90419829ad49441bd1d967ef755ce09cda838b3090ed2510f1280acdebfe3`.
Strict CRC/EOF, identical scanlines, native ImageIO pixels/properties and independent
RGBA reconstruction passed. Dimensions remain 3200 x 1730, 8-bit RGBA, 192 DPI.
Originals are recoverable byte-for-byte from `f96ae123ec57a976a3148282d0cd467f200808d0`
and retained under `eval/results/zhangsan-submitted-png-diagnostic-20261108/`.

Actual Edge InPrivate index AX showed Baseline/Candidate. Direct baseline/candidate
AX dimensions were 3200 x 1730 and screenshots were clear, normal and visually
consistent; historical content is unchanged. Actual direct GETs returned 200 at
03:31:24Z and 03:31:38Z on 2026-11-08, distinct from the 03:30:58Z HTTP probe.
Screenshot evidence is in the task conversation tool history, not saved files.
Browser receipt with verified fixture hashes:
`eval/results/zhangsan-submitted-png-browser-20261108/browser-receipt.json`.
This is not automatic screenshot pixel diff or cross-browser certification.
Only this current inventory SHA and its dependent offline binding change.
All 465 source items remain pending; historical 457-item CSV and prior evidence
remain unchanged. Unchanged WebP page usage means no page-transfer or production-image
saving is claimed. Compression does not clear source rights.

The precommit aggregate at 2026-11-08T03:33:27Z passed all eight checks using the
existing isolated Python environment: 2137 tests plus 640 subtests, Node 80/14,
seven assets, 81.8543% coverage and stable sources. No dependency was installed.
Receipt: `enterprise-agent/eval/results/offline/cleanup-submitted-png-precommit-20261108.json`.
Dirty candidate binding remains BLOCKED by design; exact clean-commit verification
and remote CI remain separate required evidence.


## Eighth reversible asset cleanup — 2026-11-08 UTC

Only `interview/产品介绍网页/screenshots/08-zhaoliu-saga-input.png` is re-encoded:
247,878 to 131,831 bytes, saving 116,047 bytes (46.8162%). Standard zlib level 9
preserves IHDR/pHYs/IEND and all 22,145,730 scanline bytes; only the identified
17-byte fdEC marker (522493e300) is removed. Specialized fpng fast-decoder
compatibility is not claimed. No author/license metadata is removed.

Original SHA256: `25b3124eca0601a90aa3e1a46e5f1490ee6c192c54c1c8ca09898e675e2d650f`.
Current SHA256: `96fbeca06898d69b4a2a8b97fd761aa56ccaacc529b1a3713c2e651714e1a181`.
ImageIO pixel SHA256: `b1511434e345cae37e3f3020a438bb7c0a154ada11b653d8d5bc7a6ad4bb805d`.
Strict CRC/EOF, identical scanlines, native ImageIO pixels/properties and independent
RGBA reconstruction passed. Dimensions remain 3200 x 1730, 8-bit RGBA, 192 DPI.
Originals are recoverable byte-for-byte from `1cd8c148aa043eb8cb4bd90a1a1f8edadf08631f`
and retained under `eval/results/zhaoliu-saga-input-png-diagnostic-20261108/`.

Actual Edge InPrivate index AX showed Baseline/Candidate. Direct baseline/candidate
AX dimensions were 3200 x 1730 and screenshots were clear, normal and visually
consistent; historical content is unchanged. Actual direct GETs returned 200 at
03:40:41Z and 03:40:55Z on 2026-11-08, distinct from the 03:39:13Z HTTP probe.
Screenshot evidence is in the task conversation tool history, not saved files.
Browser receipt with verified fixture hashes:
`eval/results/zhaoliu-saga-input-png-browser-20261108/browser-receipt.json`.
This is not automatic screenshot pixel diff or cross-browser certification.
Only this current inventory SHA and its dependent offline binding change.
All 465 source items remain pending; historical 457-item CSV and prior evidence
remain unchanged. Unchanged WebP page usage means no page-transfer or production-image
saving is claimed. Compression does not clear source rights.

The precommit aggregate at 2026-11-08T03:42:49.704703+00:00 passed all eight checks using the
existing isolated Python environment: 2137 tests plus 640 subtests, Node 80/14,
seven assets, 81.8543% coverage and stable sources. No dependency was installed.
Receipt: `enterprise-agent/eval/results/offline/cleanup-saga-input-png-precommit-20261108.json`.
Dirty candidate binding remains BLOCKED by design; exact clean-commit verification
and remote CI remain separate required evidence.


## Final handover documentation correction — 2026-11-08 UTC

This documentation-only follow-up to `088d8c84daba0b3449d4196fc167b58c38136455`
labels the original integration and intermediate CI-repair status as historical,
preserves their complete body and records the latest verified head/CI merge-ref
separately. It also replaces the bootstrap runbook's ambiguous review/reissue
wording with the existing human-hold contract: legacy NULL approvals stay
non-executable; replacements cannot bypass uncertain effects or a human hold.
No release or retry endpoint is added; any future operational procedure requires
separate review. The approval boundary documentation and actual provenance/owner
guards were checked. No application, schema, workflow or historical evidence changes.

The unchanged eight-check precommit run at 2026-11-08T04:02:17.329650+00:00
passed: 2137 tests + 640 subtests, Node 80/14, seven assets and 81.8543%
coverage, with stable source inputs. Receipt:
`enterprise-agent/eval/results/offline/handover-doc-review-precommit-20261108.json`.
Execution PASS is distinct from dirty candidate binding BLOCKED (exit 2).
These three documentation files are not bound by the current offline manifest;
no manifest refresh is required. All 465 source records remain pending and
release/UAT/privacy/full-runtime gates are not cleared. Exact clean-commit
verification and a fresh secret scan follow the separate local commit; no new
remote CI result is claimed for that documentation commit. No push, merge,
deployment, installation or deletion is performed in this correction.

Final review also makes explicit that the remote run belongs to the prior code/assets
candidate, not this documentation commit, and that the retained secret scan uses
the existing repository policy with broad path allowlists. A clean policy result
is not proof of absence across excluded docs/assets/tests; no result from a
separate default-rules-only scan is claimed here.


## Scoped source evidence and retained dependency notices (2026-11-08 UTC)

This increment supplements, rather than rewrites, the retained provenance history.
A fixed official Manrope 4.504 OFL is retained alongside the earlier notices; six
font mappings gain historical evidence without changing font bytes or rights states.
The C17 follow-up records the recovered, byte-exact six-control generation process
and the limited fictional-data confirmation. It does not clear the original corpus,
borrowed wording, screenshots or research materials, and does not rewrite historical
unknown replies or the historical 457-item matrix.

Four exact-version Python MIT notices and two complete upstream Schematron resources
with their file-level MIT grants are retained as eight supplemental notice/index files.
The latter match the lxml transform bodies under the explicitly recorded newline-only
comparison, not entire original files. Original lxml resources and LICENSES remain
unchanged. DOMPurify gains its lock-matched Babel helpers full MIT notice; its JavaScript,
Apache and MPL files remain unchanged. No dependency version changes or installation.

Build inputs bind the eight production notice files; the final Docker image explicitly
copies them. The existing installed-inventory check now reads the fixed final image
location and rejects missing, extra, changed or symlinked notices and version/hash-map
drift. Source-mode and synthetic checks do not claim final-image notice retention.
The actual Linux image check and new remote CI remain required after this commit.
No workflow or GHCR publication behavior changes. These checks are not a complete
native/vendor/OS license or corresponding-source audit, nor distribution acceptance.

The precommit aggregate at 2026-11-08T04:59:10.980485+00:00 passed all eight checks:
2170 Python tests plus 640 subtests, Node 80/14, eight frontend distribution/license
files and 81.8543% coverage. All 388 controlled offline inputs remained stable.
Receipt: `enterprise-agent/eval/results/offline/source-notices-precommit-20261108-r1.json`.
Dirty candidate binding remains BLOCKED by design (exit 2); exact clean-commit checks,
secret review and remote CI are separate subsequent evidence. The independent focused
suite passed 163 cases; no warning, skip or guard denial was reported. The historical
Manrope OFL preserves one upstream trailing space to retain exact official bytes.
The two verbatim Schematron source-notice files also retain upstream whitespace
flagged by the staged whitespace checker (11 locations); no source bytes are trimmed.
Authored-file whitespace checks exclude only those two exact upstream files.
All 465 source records stay pending, with F2-09/C10 and applicable runtime/privacy/UAT
limits preserved. No merge, registry publication, deployment or source removal is granted
by these evidence and notice changes.


## Bounded Gitleaks archive download retry (2026-11-08 UTC)

### Plan recorded before implementation

Baseline: `0707b0d1e0b45559cd44a8dde3129b6d821fa17d`, PR #8.
[CI 107](https://github.com/zhenkun26/BusinessAgent/actions/runs/42469818111)
attempts 1 and 2 failed while downloading the fixed official Gitleaks 8.24.3
Linux archive with HTTP 504. This is an upstream download failure, not a secret
finding or a failed Python assertion; later security/image checks did not run.

Add curl's finite transient-error retries with connection/per-attempt timeouts,
a retry-start budget and a hard step timeout. Preserve the exact official URL,
version, SHA-256, HTTPS/TLS flags, file output and checksum-before-extraction order.
No mirror, scanner bypass, broad error suppression, dependency installation or
application behavior change. Extend the existing workflow regression test with
bounded retry/pinning and fail-closed installation checks. Refresh only the two
changed existing workflow/test bindings in the current offline source manifest;
leave all historical manifests and evidence unchanged. Record focused outcomes
below; final full-suite, exact-commit and new remote CI evidence remain separate.

### Focused implementation evidence

The download now uses `--retry 4 --retry-delay 5 --retry-max-time 120` with
`--connect-timeout 10 --max-time 30`, plus a three-minute runner step timeout.
This allows at most five attempts. The 120-second retry budget limits retry
starts, not the duration of a final in-flight attempt; it is not described as
a hard wall-clock cap. The installed curl 8.7.1 official manual confirms that
default retry handling includes HTTP 504 and timeouts. No `--retry-all-errors`,
insecure flag, alternate URL, checksum waiver or continue-on-error is added.

Eight workflow regression cases PASS (five new and three existing). The actual
workflow bash block runs with offline shell-command doubles: download exit codes
22/28/6/60 stop before validation/extraction; checksum failure stops before tar;
tar failure stops before PATH publication; success validates the exact fixed
checksum input before extraction and PATH publication. Exact curl options and
step timeout are locked. These tests verify shell control flow and configured
bounds, not curl internals, real HTTPS transport or upstream availability. No
network transfer, temporary fixture deletion or new dependency is used.

Workflow YAML parsing, installation bash syntax, authored whitespace and all
388 current source bindings PASS. Only the existing workflow and regression-test
SHA-256 fields are refreshed; source membership and historical manifests remain
unchanged. The unchanged full offline suite, clean-commit binding and new remote
CI are separate subsequent checks. Existing runtime/privacy/UAT/source-rights
limits remain; this repair does not clear skipped security or image gates.

### First full precommit result and binding correction plan

The initial full run, `gitleaks-retry-precommit-20261108-r1`, remains FAIL
(exit 1): Python and provenance failed while the other six checks passed.
Python reported 2169 passed, 640 subtests passed, one failed and zero guard
denials. Its sole failure was `test_license_inventory.py::test_repository_inventory`,
raising `dependency declaration drift`. The current offline source bindings
were stable, but the separate license inventory still held the earlier workflow
SHA-256 in `declarations[".github/workflows/ci.yml"]`. The declaration items and
all source-file hashes matched; this was a missed secondary binding, not a
dependency, rights-state or application change.

Before correcting it: refresh only that existing declaration SHA-256 and then
the current offline manifest binding for `deploy/license-inventory.json`. Preserve
all items, counts, rights states, gates, historical manifests and the failed r1
receipt. Recheck the exact failed test, provenance verification, workflow cases
and 388 current bindings; a new full r2 run remains separate evidence.

After the scoped binding correction, provenance integrity, the exact previously
failed repository-inventory test, all eight workflow regression cases, 388 current
source bindings and whitespace checks PASS. The declaration count remains 32,
source rights remain pending for all 465 records, and production/browser package
counts remain 98/3. The failed r1 aggregate and child evidence remain unchanged.
These focused results do not replace the required new full run.

Full precommit rerun `gitleaks-retry-precommit-20261108-r2` passed all eight checks:
2170 Python tests plus 640 subtests, Node 80/14, eight frontend assets and
81.8543% coverage, with stable sources. Dirty candidate binding remains BLOCKED
(exit 2); the retained r1 failure is not overwritten. Exact clean-commit checks
and new remote CI are still required before merge.
