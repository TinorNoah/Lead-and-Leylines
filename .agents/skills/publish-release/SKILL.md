---
name: publish-release
description: Publish a pack version from a git tag and changelog (GitHub Release, CurseForge, dedicated test server, then local Prism). Use only when the user explicitly types /publish-release.
disable-model-invocation: true
---

# Publish a release

The operator machine tags GitHub, updates the live instance (Wings), then dispatches GitHub Actions for CurseForge. Local Prism syncs last. Default channel is GitHub prerelease + store alpha. `--channel release` is official on GitHub and CurseForge.

Policy (channels, changelog, public text): [docs/RELEASING.md](../../../docs/RELEASING.md).

Never pass `--channel release` unless the user explicitly asks for a public, stable release — default to `alpha`.

Do not mention the test server, panel, join address, or the dedicated server in GitHub Release text, CurseForge notes, CHANGELOG.md, or other GitHub-facing copy.

## Steps

1. Confirm `main` is the intended commit (clean working tree, PR merged).
2. Read `pack_version` from `pack/pack.toml` via `python scripts/read_pack_versions.py`. The README Pack details table must match.
3. If the user asked for a new version: edit `pack.toml` `version` to `X.Y.Z` (no `v`), sync the README table, promote `CHANGELOG.md` `[Unreleased]` to `## [X.Y.Z] - YYYY-MM-DD` (today’s date), re-scaffold empty `[Unreleased]` with Added/Changed/Fixed/Removed, `packwiz refresh`, commit on a branch/PR as usual, merge to `main`. Git tags are `vX.Y.Z`; changelog headers are `## [X.Y.Z]` with no `v`. If `[Unreleased]` has no real bullets, STOP — do not invent entries. `release.py` does not edit CHANGELOG.md.
4. Default notes are the `## [X.Y.Z]` section in `CHANGELOG.md`. `--changelog FILE` / `--notes TEXT` override. Do not invent server/hosting notes.
5. From the repo root run `python scripts/release.py vX.Y.Z --channel alpha` (`release` only if the user asked for a public stable). Order: GitHub Release (client zip, mrpack, server-mods zip) → `python scripts/deploy_server.py --from-local` unless `--skip-server` → dispatch `.github/workflows/publish-stores.yml` unless `--skip-stores` → `python scripts/update_prism.py` unless `--skip-prism`. CurseForge gets both the client pack and the server-mods zip. `--dry-run` and `--upload-stores` exist when the user asks. Push only when the user asked to release or push.
6. Point the user at the GitHub Release URL and the Publish stores workflow run. Store tokens live as GitHub Actions secrets. `GH_TOKEN` is required on the operator machine.

Never write tokens or project IDs into files.
