---
name: publish-release
description: Align pack.toml version with a vX.Y.Z tag, push the tag, wait for GitHub Actions, and deploy the panel. Use only when the user explicitly types /publish-release.
disable-model-invocation: true
---

# Publish a release

Do not upload zip/mrpack files from the agent machine. CI does export and store publish.

## Steps

1. Confirm `main` is the intended commit (clean working tree, PR merged).
2. Read `pack_version` from `pack/pack.toml` via `python scripts/read_pack_versions.py`. The README Pack details table must match.
3. If the user asked for a new version, edit `pack.toml` `version` to `X.Y.Z` (no `v`), sync the README table, `packwiz refresh`, commit on a branch/PR as usual, merge to `main`.
4. From the repo root run `python scripts/release.py`. That tags `vX.Y.Z`, pushes `main` and the tag, waits for the GitHub Release, then `python scripts/deploy_server.py --from-local`. Use `--dry-run`, `--no-panel`, or `--no-wait` when the user asks. Push only when the user asked to release or push.
5. Point the user at the Actions run and the GitHub Release. Store uploads happen only if `CURSEFORGE_*` / `MODRINTH_*` secrets are set; otherwise those steps skip.

Never write tokens or project IDs into files.
