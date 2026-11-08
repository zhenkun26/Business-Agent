# Migrate independent Business-Agent repository

## Why

Create an independent repository from BusinessAgent while preserving project history, MIT licensing and collaborator attribution. The maintainer additionally requested removing two previously deleted personal photos from the new repository history only.

## What Changes

- Preserve all branches and commits, removing only IMG_5043.jpg and IMG_5044.jpg from historical trees. Retain tags locally and in mappings without pushing pending separate review.
- Update both READMEs for the independent destination and credit kingoftaro.
- Retain auditable commit/ref mappings and precisely remap existing secret-scan false-positive fingerprints.
- Run new checks without migrating Issues, PRs, CI history, secrets or protection settings.

## Capabilities

### New Capabilities
- `repository-migration`: verifiable source-to-destination continuity and bounded history cleanup.

### Modified Capabilities
None. Runtime behavior and license terms remain unchanged.

## Impact

The old repository is unchanged. The destination remains private pending separate approval. No image publication, deployment, release, paid service, credential migration or branch-protection migration. Historic signatures on rewritten commits cannot authenticate new hashes.
