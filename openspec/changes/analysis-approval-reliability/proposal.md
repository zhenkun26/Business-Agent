# Analysis and approval reliability

## Why

The deterministic analyzer silently interprets unsupported English metrics, negation,
and unrecognized customer selectors as ordinary totals. Approval lists truncate at 50
records and report the page length as the total. The dotenv startup guard also requires
a newer minimum version than the development declarations require.

## Scope and design

Start from PR #8 head `1645e012170b30f9ff3022082602f9cd56b10212`, whose existing CI
passed. Keep that PR unchanged. Align the existing dotenv dependency minimum without
adding packages. Consume a bounded bilingual query vocabulary and explicit IDs; reject
unconsumed semantics instead of approximating them. Preserve exact minor-unit arithmetic,
currency grouping, identity checks, and original-query forwarding.

Add bounded offset pagination to all three approval lists with deterministic timestamp/ID
ordering. Count and page use one SQL statement so they observe the same statement snapshot,
including empty/out-of-range pages. Preserve role/requester predicates and review fields.
Provide previous/next controls with identity/request-generation guards. Lists remain live:
concurrent changes between requests require refreshing, not a frozen cross-page snapshot.

## Verification and delivery

Add regression tests for bilingual metric/filter rejection, customer casing, date conflicts,
51+ approvals, equal timestamps, empty pages, authorization boundaries, and late UI replies.
Run existing guarded offline checks without paid models, services, or new dependencies.
Record scope/results in the existing engineering delivery tracker and keep local commits
only. No push, merge, release, historical evidence rewrite, or filesystem deletion.

## Authorized security follow-up — 2026-11-16

PR #9 hosted verification found CVE-2026-126360 in opentelemetry-api 1.45.1.
The user authorized upgrading the compatible dependency group, updating locks/provenance,
verifying locally, pushing to the same PR, and rerunning CI without merge or paid models.
Official release metadata confirms API/SDK 1.45.2 and semantic-conventions,
instrumentation, instrumentation-asgi, instrumentation-fastapi, and util-http 0.66b2.
These are updates to seven existing packages; no new dependency or optional exporter
is required. Preserve production hash-only binary installation and all scan gates.
Verify release wheel hashes, Python 3.11/3.13 dependency closure, oversized traceparent
rejection before regex work, normal propagation, and SDK/FastAPI compatibility.
Retain offline and hosted results with their exact candidate identities.
