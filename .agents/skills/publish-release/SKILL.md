---
name: publish-release
description: Publish a pack version from a git tag and changelog (GitHub Release, CurseForge, dedicated test server, then local Prism). Use only when the user explicitly types /publish-release.
disable-model-invocation: true
---

# Publish a release

The operator machine tags GitHub, updates the Pelican server, then syncs local Prism. CurseForge stays off unless the user explicitly asks for a store publish. Default channel is a GitHub prerelease. `--channel release` is GitHub Latest. Add `--curseforge` only when a store publish was asked for.

Policy (channels, changelog, public text): [docs/RELEASING.md](../../../docs/RELEASING.md).

Never pass `--channel release` unless the user explicitly asks for a public, stable release — default to `alpha`.

Do not mention the test server, panel, join address, or the dedicated server in GitHub Release text, CurseForge notes, CHANGELOG.md, or other GitHub-facing copy.

## Steps

1. Confirm `main` is the intended commit (clean working tree, PR merged).
2. Run `python3 scripts/installed_catalog.py --check`. If it fails, fix `docs/installed/catalog.toml`, regenerate, and merge that before releasing. Policy: [docs/installed/MAINTENANCE.md](../../../docs/installed/MAINTENANCE.md).
3. Read `pack_version` from `pack/pack.toml` via `python scripts/read_pack_versions.py`. The README Pack details table must match.
4. If the user asked for a new version: edit `pack.toml` `version` to `X.Y.Z` (no `v`), sync the README table, promote `CHANGELOG.md` `[Unreleased]` to `## [X.Y.Z] - YYYY-MM-DD` (today’s date), re-scaffold empty `[Unreleased]` with Added/Changed/Fixed/Removed, `packwiz refresh`, commit on a branch/PR as usual, merge to `main`. Git tags are `vX.Y.Z`; changelog headers are `## [X.Y.Z]` with no `v`. If `[Unreleased]` has no real bullets, STOP — do not invent entries. `release.py` does not edit CHANGELOG.md.
5. Default notes are the `## [X.Y.Z]` section in `CHANGELOG.md`. `--changelog FILE` / `--notes TEXT` override. Do not invent server/hosting notes.
6. From the repo root run `python scripts/release.py vX.Y.Z --channel alpha` (`release` only if the user asked for a public stable). Order: GitHub Release (client zip, mrpack, server-mods zip) → Pelican via `deploy_server.py --from-local` unless `--skip-server` → local Prism unless `--skip-prism`. The export reuses cached jars and downloads only missing files. The Pelican step reuses the zip just attached and does not build the pack again. Do not pass `--curseforge` or `--upload-stores` unless the user asked for a CurseForge publish. `--dry-run` prints the plan. Push only when the user asked to release or push. `release.py` re-runs the installed-catalog `--check` as a preflight.
7. Point the user at the GitHub Release URL. If CurseForge was requested, also point at the Publish stores workflow run. Store tokens live as GitHub Actions secrets. `GH_TOKEN` is required on the operator machine.

Never write tokens or project IDs into files.
