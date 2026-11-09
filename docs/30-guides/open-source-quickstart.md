# Open-source quickstart / 开源快速开始

## Phase-one source scope / 第一阶段来源范围

The [candidate-bound source assessment](../50-engineering/license-provenance.md#phase-one-source-assessment--2026-11-08) covers 465 records: 229 supported by
upstream evidence, 232 common-project contributions with maintainer-reported MIT
consent, and four repository-declared MIT associated research documents. Historical
PENDING inventory labels remain intact and are not 465 unresolved current blockers.
This is source-only scope, not independent proof of authorship or blanket third-party
clearance. Actual binary releases and the three later enterprise stages require separate
review; privacy/full RAG/full C10 acceptance is not closed. Final documentation review
and candidate checks remain required before merge.

## Current milestone / 当前阶段

Stage one targets reproducible isolated startup with synthetic examples and honest capability and source-rights boundaries. It is not a claim of real enterprise deployment, formal UAT, or production readiness.

第一阶段目标是隔离启动、合成示例与清楚的能力和来源边界，不代表真实企业部署、正式 UAT 或生产就绪。

## Starter verification / 启动入口核验

[Fresh CI run 42591561481](https://github.com/zhenkun26/Business-Agent/actions/runs/42591561481)
was workflow_dispatch attempt 1 at exact head
`15cd84f942ccc0ce49afcfc1513efe4c2f07f441`, created 2026-11-09 09:12:08 UTC
and completed 09:19:42 UTC. All five jobs succeeded. With publish=false, GHCR login
and image push were both skipped.

- Python 3.11 and 3.13 each passed 2170 tests + 640 subtests and all eight current
  offline checks, plus nine publication-policy tests and 39 scanner regressions.
- Actual event-history and exact final-tree secret scans and pip-audit passed under
  the unchanged policy. The dispatch scan selected 113 commits and reported 111
  scanned; the final tree contained 1,019 files, with zero unclassified findings.
  This is the selected event scope, not proof that every repository branch was scanned.
- The isolated C10 persistence slice passed. This does not establish full C10 or RAG
  acceptance.
- Native-libpq startup and all 15 synthetic HTTP checks passed on the Ubuntu runner,
  with pure Python psycopg and no binary/C wrapper. Owned demo resources were stopped.
  This run did not perform browser UI automation.
- Docker build, actual installed inventory and Trivy passed. Trivy retained the
  HIGH/CRITICAL, ignore-unfixed=true policy. The [current notice evidence](../../THIRD_PARTY_NOTICES.md#candidate-bound-linux-notice-evidence--2026-11-09)
  binds the newly inspected artifact and image; it is not blanket distribution clearance.

This is technical verification of the named head, not a fresh test of this subsequent
documentation diff or acceptance of real enterprise use, formal UAT, production release,
privacy, complete C10/RAG or source rights.

**Historical Mac/browser observations, 2026-11-07:** macOS arm64 Python 3.13.15 used
an approved binary-driver test adapter. Run-05 passed 15 actual HTTP checks and 14
focused demo tests after a startup-log correction; owned services stopped with data
retained. Run-04 browser checks passed login, both greeting shortcuts, unsupported-
operation rejection, current-session history, refresh/login isolation, relogin and
logout. Run-05 changed logging only, not UI bytes. These observations were not rerun
by the new CI, and the Mac adapter is not native-libpq proof. The unchanged
[dated record](../50-engineering/final-candidate-verification.md#stage-one-technical-candidate-progress--2026-11-07)
and [older Linux CI record](../50-engineering/final-candidate-verification.md#verified-code-candidate-ci--documentation-follow-up)
retain their original candidate IDs, counts and limitations. Neither establishes source
rights; see the current phase-one assessment above.

The verified Linux path assumes an Ubuntu CI-style environment with Python 3.13 already installed, a running accessible Docker daemon, and configured Ubuntu/PGDG APT sources. It is not a verified native-libpq setup for macOS or every bare Linux host. Complete the isolated setup and import preflight below before startup.

From the repository root, with prerequisites satisfied in an isolated Python environment:

    python -I -B enterprise-agent/scripts/run_synthetic_demo.py plan

The plan performs no startup. Choose a new nonexistent, non-symlink run directory:

    python -I -B enterprise-agent/scripts/run_synthetic_demo.py start --execute --run-dir enterprise-agent/eval/results/my-synthetic-demo-01

Startup prints a loopback URL and random test credentials. Keep this output private.
Open the printed URL locally, sign in and send “你好” or “您好”. Replies are fixed synthetic
greetings, not model answers. Only login, greetings and own history are supported; RAG,
approvals and business operations are rejected. A demo marker distinguishes this profile.

Optional tracked acceptance (creates synthetic users/sessions and a redacted report):

    python -I -B enterprise-agent/scripts/check_synthetic_demo.py --execute --require-python-driver --run-dir enterprise-agent/eval/results/my-synthetic-demo-01

The pure-driver option deliberately rejects binary/C implementations, including the
historical Mac test adapter. The fresh run named above passed this native-driver check; the historical Mac adapter remains a separate result.

Stop after use, or after partial startup with a retained receipt:

    python -I -B enterprise-agent/scripts/run_synthetic_demo.py stop --execute --run-dir enterprise-agent/eval/results/my-synthetic-demo-01

Stop targets owned services and retains containers, volumes and evidence; no deletion.
Use another fresh directory for another start. Keep private-state.json, logs and credentials
out of commits/public uploads. Share only inspected redacted acceptance reports.
Loopback bindings and Python guards are not OS/container-wide network isolation.

## Verified Linux prerequisites / 已验证Linux前置

The planned starter uses Python 3.11 or later, the existing production Python dependencies,
Docker for isolated PostgreSQL/Redis, and native **libpq** on the host. The project's pure
psycopg package needs libpq available to the operating system's dynamic loader; pip
installation alone is insufficient. No new psycopg binary dependency is added for the
demo. For Debian/Ubuntu, the system runtime package is libpq5. In an isolated environment with package-install permission, install it before the Python requirements. The fresh Ubuntu CI named above explicitly provisioned libpq5 and verified pure Python driver implementation with binary/C wrappers absent. The exact package version 18.6-1.pgdg24.04+2 and libpq 180006 belong to the older Linux CI record linked above, not a newly asserted package-version result. The verified path depends on the runner's existing base tools and configured APT sources, not a universal bare-machine proof.

计划入口需要 Python 3.11+、现有生产依赖、运行隔离 PostgreSQL/Redis 的 Docker，以及
宿主机原生 libpq。仅安装 Python requirements 不代表环境已经完整可用；本演示不会另加
psycopg 二进制依赖。Debian/Ubuntu 对应系统包为 libpq5；已通过的 Ubuntu CI 明确安装此前置并核验原生驱动；其预装工具和 APT 源仍属于环境条件，不代表任意裸机或所有系统都已验证。

The approved narrow profile uses the real application core but synthetic greeting responses.
It is not a generic replacement API and does not demonstrate real RAG or business actions.
Production mode must refuse the profile. A minimal Debian/Ubuntu setup sequence (requires system package-install permission; validated CI uses an Ubuntu runner with Python/Docker and its configured APT sources, not every bare Debian/Ubuntu host) is:

    sudo apt-get update
    sudo apt-get install -y --no-install-recommends libpq5
    python3.13 -m venv .venv_demo
    . .venv_demo/bin/activate
    python -m pip install -r enterprise-agent/deploy/requirements-prod.txt
    python -I -B -c "import importlib.util as u; import psycopg; assert u.find_spec('psycopg_binary') is None; assert u.find_spec('psycopg_c') is None; assert psycopg.pq.__impl__ == 'python'; print(psycopg.pq.version())"

Use a new environment directory; Docker must already be running and accessible. This adds no new Python dependency. Do not install a binary extra merely to bypass the native-driver acceptance check.

## Capability boundaries / 能力边界

| Area | What is established | What is not established |
| --- | --- | --- |
| Approval controls | Decision and requester execution confirmation are separate; failed/unknown actions retain human holds | Real enterprise approval acceptance or automatic hold release |
| Offline checks | Candidate-bound unit, integrity and synthetic contract evidence | Real model answers, complete RAG, business-user acceptance |
| History | Backend persistence and session-specific queries; current-session UI history checked | Refresh returns to login; relogin starts a new empty session, with no visible old-session recovery entry or complete history manager |
| Synthetic examples | Disposable test identities and business fixtures | Real employee or customer outcomes |
| Demo providers | Must be labeled individually by the starter's actual implementation | Real CRM/mail/ticket effects from a substitute API |
| Licenses and assets | Root project license and separate provenance inventory exist | Blanket clearance of unknown third-party material |

A full page refresh returns to login. After relogin there is no visible entry to recover the old session. Current-session history may show a persisted snapshot with unknown status; that is not a successful business execution receipt. Do not claim automatic cross-refresh recovery.

Historical synthetic-example evidence (not superseding the current source-only assessment):

The source inventory now contains 465 records: the historical 457 baseline plus eight new engineering fixtures. Registration does not clear unknown rights. The maintainer stated that three C17 documents (two departmental documents and after-sales policy) and eight CRM examples were fictional from creation; this is scoped author testimony, not external permission or clearance of other C17 material. The completed separate CRM increment labels eight fictional customers and uses NOT-A-PHONE telephone placeholders and example.invalid customer email addresses. The internal-mail seed deliberately retains fictional-demo-manager@company.internal with a synthetic-data comment: this private demo domain is required by the unchanged internal-mail safety classifier. It is not a customer address or a relaxed mail policy. Three focused tests passed; order and non-contact fields were unchanged. The historical expected full Python count was 2137 (2120 baseline + 14 demo + 3 CRM). Both supported Python jobs in the older Linux CI record passed 2137 tests plus 640 subtests and verified candidate binding and the native starter. Those counts belong to that earlier code candidate, not the fresh run above.

This document is a documentation-only follow-up to the fresh verified head named above. Any later documentation commit needs its own candidate checks; the cited run must not be presented as executing that later diff. Existing successful CI evidence does not by itself prove a different starter works. See [source provenance](../50-engineering/license-provenance.md) and [third-party notices](../../THIRD_PARTY_NOTICES.md); unknown rights are not permission to redistribute.

## Later stages / 后续三个阶段

1. **Enterprise pilot evaluation / 企业试点评估**: choose one concrete team problem, assess data permission and integration feasibility, and agree on measurable success criteria. Start with read-only knowledge questions and access isolation; do not require a full organization before evaluating value.
2. **Real-environment pilot / 真实环境试点**: use an agreed independent environment and approved business sandboxes. A small number of real users and a business contact judge actual results. Expand from read-only questions to a limited integration only after evidence supports it. Synthetic role tests remain technical preparation, not formal business acceptance.
3. **Production use / 生产使用**: separately establish security/privacy review, operational ownership, backups and recovery, monitoring, incident handling, upgrade rollback and staged rollout. A merge does not authorize deployment.

## Merge boundary / 合并边界

Stage-one merge requires verified reproducibility, accurate limitations, resolved material distribution-rights blockers and current candidate checks. Later enterprise milestones remain openly unfinished. Do not replace missing evidence with a PASS label.

Retained historical screenshots were not replaced and may still display historical contact details or additional unconfirmed recipients. The current source assessment records maintainer-reported consent for common-project screenshots; it does not independently verify every depicted identity, recipient or privacy condition.
