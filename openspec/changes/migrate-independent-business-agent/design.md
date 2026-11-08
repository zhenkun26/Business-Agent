# Design

Clone all source branches and tags into an isolated bare repository. Use git-filter-repo 2.47.0 with exact path removal, no empty-commit pruning and preservation of commit-message bytes and encoding. Compare every mapped tree, parent, author, committer, timestamp and tag payload. Remove only the two photos; retain all other source bytes and license notices.

Keep SHA-256 source-manifest contents and historical evidence unchanged. Update only the 16 existing Gitleaks ignore fingerprints through the verified commit map, with identical path/rule/line scope. Do not broaden secret-scan exclusions.

Update operational repository links in both READMEs, distinguish source CI evidence from new checks, and retain kingoftaro attribution plus MIT commercial-use terms and third-party notice boundaries. Retain the original source link and mappings for traceability.

During import, push only the eleven branches. Every branch has only ci.yml with push restricted to main; current main requires explicit workflow_dispatch publish=true for image publication. Hold back all five historical tags because their older workflows could publish on tag push. Do not change Actions settings or copy repository settings, credentials or non-Git histories. Keep the destination private; public exposure requires separate confirmation.

Validate the final exact commit with the existing offline suite, publication/secret-scan policy tests, current tree/history scan and full new-repository CI. Report failures, unavailable checks and remaining enterprise/runtime acceptance boundaries separately. Do not archive or claim completion until migration checks finish.
