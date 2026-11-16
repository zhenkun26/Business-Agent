# Design decisions

Reuse PR #8 as an explicit parent, leaving main and the published PR branch intact.
Raise the existing dotenv lower bound to 1.2.0; retain production pin 1.2.2.

Analysis remains deterministic. Consume supported vocabulary, ISO ranges, unambiguous
customer IDs, and status selections; reject residual scope rather than invoking a model
or approximating ranking/averages. Preserve authorization and per-currency integer sums.
Opaque IDs require a selector; matching case collisions fail closed.

Use bounded offset pagination because the UI requires previous/next pages, the existing
lists are live queues, and no durable snapshot infrastructure exists. Count and page share
one SQL statement; timestamp plus unique approval ID orders ties. This does not guarantee
stable membership between requests when another actor updates the queue. Refresh restarts
at zero. Preserve the API's existing row fields and role/requester predicates.

UI rows and page metadata share request sequence and authentication epoch guards.
Malformed metadata fails closed. Keep previous/next controls native and preserve existing
decision/reauthentication/human-review safeguards. No new packages, schemas, or migrations.
