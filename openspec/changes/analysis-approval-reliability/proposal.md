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
