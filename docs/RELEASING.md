# Releasing Lead and Leylines

How versions, channels, and `CHANGELOG.md` work. Skills (`publish-release`, `update-changelog`) are short checklists; this file is the policy.

The Pelican test server address is shared with testers out of band (Discord/DM/etc.). Never put it in the repo, GitHub Release text, or CurseForge notes.

Modrinth publishing was discontinued. CurseForge is the sole public store target. The `.mrpack` file is still built for ATLauncher testers; it is not uploaded to a Modrinth listing.

## Channels

`python scripts/release.py vX.Y.Z --channel <channel>` (default `alpha`).

| Channel | GitHub | CurseForge | Pelican | Local Prism |
|---|---|---|---|---|
| `alpha` | Prerelease | Off unless requested | Updated | Synced last |
| `beta` | Prerelease | Off unless requested | Updated | Synced last |
| `release` | Official Latest | Off unless requested | Updated | Synced last |

Default is `alpha`: GitHub prerelease, then the Pelican server update, then local Prism. CurseForge is not part of that path. Pass `--curseforge` to publish the store from GitHub Actions after Pelican, or `--upload-stores` to upload from this machine. `--channel release` is GitHub Latest. Use it for a public stable, and add `--curseforge` only when a store release was asked for.

Order on the operator machine:

1. Tag and GitHub Release (client zip, mrpack, server-mods zip)
2. Pelican pulls that server-mods zip from the GitHub Release (`deploy_server.py --from-local`, unless `--skip-server`). That deploy reuses the zip just attached and does not build the pack again.

Pack builds (the release export, the smoke-test server zip, and a deploy that has to attach a missing zip) reuse a jar when the packwiz cache or `.cache/mod-files` already has that file's hash. Only missing files are downloaded. `packwiz modrinth export` uses the packwiz cache the same way. Do not delete those caches or fetch every jar before a release, smoke test, or deploy.
3. CurseForge only with `--curseforge` or `--upload-stores`
4. Local Prism sync (unless `--skip-prism`)

Missing `GH_TOKEN` skips the GitHub Release. Pelican cannot update without that zip, so the server step fails until the token is set. Prism still runs only after a successful server step.

GitHub Actions (`.github/workflows/publish-stores.yml`) runs only when `release.py` is given `--curseforge`, or from a manual `workflow_dispatch`. It does not run on tag push. It uploads the GitHub Release client zip as the CurseForge primary file and the server-mods zip as an additional file of that primary. Store tokens and project ids live as GitHub Actions secrets (`CURSEFORGE_TOKEN`, `CURSEFORGE_PROJECT_ID`). Do not hardcode those values.

`--upload-stores` uploads from the operator machine when `.env` has those values (same client + server files, after Pelican). `--skip-curseforge` and `--skip-stores` still skip CurseForge even if a publish flag is set.

### No promoting a prerelease tag

Do not later re-upload the same `X.Y.Z` as a store `release`. A GitHub prerelease stays alpha/beta on the stores. Cut a **new** version tag and run `release.py --channel release --curseforge` for an official GitHub Latest plus store release.

## Changelog

`CHANGELOG.md` at the repo root follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/).

- Update it **continuously** when something is player-noticeable (mod add/remove/update, config, bug fix), not only at release. Use the `update-changelog` skill.
- `[Unreleased]` must have at least one real bullet before a version can ship. Category headers with no bullets do not count. Do not invent entries.
- Phrasing is user-facing impact, not commit subjects. Stay consistent with `docs/mods/manifest.md` without copying its full rationale.
- Never mention the test server, panel URL, join address, or other hosting details.

Git tags are `vX.Y.Z`. Changelog headers are `## [X.Y.Z]` with **no** `v`, plus a date when released: `## [X.Y.Z] - YYYY-MM-DD`.

### Source of truth at publish time

`scripts/release.py` is **read-only** on `CHANGELOG.md`. It does not promote, rewrite, or append that file.

Editorial promotion happens in the `publish-release` skill **before** running the script, in the same commit as the `pack.toml` / README version bump:

1. If `[Unreleased]` has no real bullets, stop.
2. Rename `[Unreleased]` to `## [X.Y.Z] - YYYY-MM-DD` (today’s date).
3. Re-scaffold an empty `[Unreleased]` with `### Added`, `### Changed`, `### Fixed`, `### Removed`.

Then `python scripts/release.py vX.Y.Z --channel …` extracts the `## [X.Y.Z]` section (from that heading through the next `## [` heading) as the GitHub Release body and the CurseForge notes. `--changelog FILE` and `--notes TEXT` override that extract. If the section is missing or has no real bullets, the script hard-fails **before** tagging or calling any API.

### Merge conflicts

Every branch that logs player-facing work edits the same `[Unreleased]` lines, so conflicts are expected and normal. Resolve by keeping **both** branches’ bullets under the right subheader.

If that becomes painful, a fragment-file / towncrier-style `changelog.d/` compiled at release is a reasonable upgrade. Do not build that until the single file actually hurts.

## Public text

Never mention panel URL, join IP, or the dedicated server in `CHANGELOG.md`, GitHub Release bodies, CurseForge notes, or the README. Share the test-server address out of band.
