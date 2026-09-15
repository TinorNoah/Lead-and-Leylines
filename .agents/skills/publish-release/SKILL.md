---
name: publish-release
description: Publish a pack version from a git tag and changelog (GitHub Release, CurseForge, Modrinth, then the dedicated test server). Use only when the user explicitly types /publish-release.
disable-model-invocation: true
---

# Publish a release

The operator machine runs the publisher. There is no tag GitHub Actions job.

The changelog is the public GitHub Release body and the CurseForge/Modrinth notes. Do not mention the test server, panel, join address, or the dedicated server anywhere in that text or in GitHub-facing docs.

## Steps

1. Confirm `main` is the intended commit (clean working tree, PR merged).
2. Read `pack_version` from `pack/pack.toml` via `python scripts/read_pack_versions.py`. The README Pack details table must match.
3. If the user asked for a new version, edit `pack.toml` `version` to `X.Y.Z` (no `v`), sync the README table, `packwiz refresh`, commit on a branch/PR as usual, merge to `main`.
4. Get a changelog from the user (`--changelog FILE` or `--notes TEXT`). Do not invent server/hosting notes.
5. From the repo root run `python scripts/release.py vX.Y.Z --changelog <file>`. That tags, creates the GitHub Release, uploads CurseForge/Modrinth when `.env` has those values, then `python scripts/deploy_server.py --from-local`. `--dry-run`, `--skip-server`, `--skip-curseforge`, and `--skip-modrinth` exist when the user asks. Push only when the user asked to release or push.
6. Point the user at the GitHub Release URL. Store uploads skip with a log if `CURSEFORGE_*` / `MODRINTH_*` are unset. `MODRINTH_PROJECT_ID` must be the 8-character dashboard id, not the slug. `GH_TOKEN` is required.

Never write tokens or project IDs into files.
