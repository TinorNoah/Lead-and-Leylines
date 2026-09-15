---
name: publish-release
description: Publish a pack version from a git tag and changelog (GitHub Release, CurseForge, Modrinth, then the dedicated test server). Use only when the user explicitly types /publish-release.
disable-model-invocation: true
---

# Publish a release

The operator machine runs the publisher. There is no tag GitHub Actions job.

Policy (channels, changelog, public text): [docs/RELEASING.md](../../../docs/RELEASING.md).

Never pass `--channel release` unless the user explicitly asks for a public, stable release — default to `alpha`.

Do not mention the test server, panel, join address, or the dedicated server in GitHub Release text, CurseForge/Modrinth notes, CHANGELOG.md, or other GitHub-facing copy.

## Steps

1. Confirm `main` is the intended commit (clean working tree, PR merged).
2. Read `pack_version` from `pack/pack.toml` via `python scripts/read_pack_versions.py`. The README Pack details table must match.
3. If the user asked for a new version: edit `pack.toml` `version` to `X.Y.Z` (no `v`), sync the README table, promote `CHANGELOG.md` `[Unreleased]` to `## [X.Y.Z] - YYYY-MM-DD` (today’s date), drop empty category headers from that versioned section, re-scaffold empty `[Unreleased]` with Added/Changed/Fixed/Removed, `packwiz refresh`, commit on a branch/PR as usual, merge to `main`. Git tags are `vX.Y.Z`; changelog headers are `## [X.Y.Z]` with no `v`. If `[Unreleased]` has no real bullets, STOP — do not invent entries. `release.py` does not edit CHANGELOG.md.
4. Default notes are the `## [X.Y.Z]` section in `CHANGELOG.md`. `--changelog FILE` / `--notes TEXT` override. Do not invent server/hosting notes.
5. From the repo root run `python scripts/release.py vX.Y.Z --channel alpha` (`release` only if the user asked for a public stable). That tags, creates the GitHub Release, uploads CurseForge/Modrinth only on `--channel release` when `.env` has those values, then `python scripts/deploy_server.py --from-local`. `--dry-run`, `--skip-server`, `--skip-curseforge`, and `--skip-modrinth` exist when the user asks. Push only when the user asked to release or push.
6. Point the user at the GitHub Release URL. Store uploads skip with a log if the channel is not `release`, or if `CURSEFORGE_*` / `MODRINTH_*` are unset. `MODRINTH_PROJECT_ID` must be the 8-character dashboard id, not the slug. `GH_TOKEN` is required.

Never write tokens or project IDs into files.
