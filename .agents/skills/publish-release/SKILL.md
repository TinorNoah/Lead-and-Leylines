---
name: publish-release
description: Align pack.toml version with a vX.Y.Z tag, push the tag, and let GitHub Actions export and publish. Use only when the user explicitly types /publish-release.
disable-model-invocation: true
---

# Publish a release

Do not upload zip/mrpack files from the agent machine. CI does export and publish.

## Steps

1. Confirm `main` is the intended commit (clean working tree, PR merged).
2. Read `pack_version` from `pack/pack.toml` via `python scripts/read_pack_versions.py`.
3. If the user asked for a new version, edit `pack.toml` `version` to `X.Y.Z` (no `v`), `packwiz refresh`, commit on a branch/PR as usual, merge to `main`.
4. Tag `vX.Y.Z` where `X.Y.Z` equals `pack.toml` `version`. Push the tag only after the user confirms the push.
5. Point the user at the Actions run and the GitHub Release. Store uploads happen only if `CURSEFORGE_*` / `MODRINTH_*` secrets are set; otherwise those steps skip.

Never write tokens or project IDs into files.
