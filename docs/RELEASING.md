# Releasing Lead and Leylines

How versions, channels, and `CHANGELOG.md` work. Skills (`publish-release`, `update-changelog`) are short checklists; this file is the policy.

The Pelican test server address is shared with testers out of band (Discord/DM/etc.). Never put it in the repo, GitHub Release text, CurseForge notes, or Modrinth notes.

## Channels

`python scripts/release.py vX.Y.Z --channel <channel>` (default `alpha`).

| Channel | GitHub | CurseForge | Modrinth | Live instance | Local Prism |
|---|---|---|---|---|---|
| `alpha` | Prerelease | Alpha (client zip + server zip) | Alpha (mrpack + server zip) | Updated first | Synced last |
| `beta` | Prerelease | Beta (client zip + server zip) | Beta (mrpack + server zip) | Updated first | Synced last |
| `release` | Official Latest | Release (client zip + server zip) | Release (mrpack + server zip) | Updated first | Synced last |

Default is `alpha`: GitHub prerelease, then Wings updates the live instance, then CurseForge/Modrinth **alpha**. `--channel release` is GitHub Latest, then Wings, then CurseForge/Modrinth **release**. Use `--channel release` only for a public stable.

Order on the operator machine:

1. Tag and GitHub Release (client zip, mrpack, server-mods zip)
2. Wings pull / live instance update (unless `--skip-server`)
3. GitHub Actions publishes CurseForge and Modrinth (unless `--skip-stores`)
4. Local Prism sync (unless `--skip-prism`)

Missing `GH_TOKEN` skips GitHub tagging and store dispatch, but still updates the live instance and Prism.

GitHub Actions (`.github/workflows/publish-stores.yml`) is **dispatched after** the live instance update. It does not run on tag push. It uploads the GitHub Release client zip as the CurseForge primary file and the server-mods zip as an additional file of that primary. Modrinth gets the mrpack as primary and the same server-mods zip as an extra file. `workflow_dispatch` can retry an existing tag. Store tokens and project ids live as GitHub Actions secrets (`CURSEFORGE_TOKEN`, `CURSEFORGE_PROJECT_ID`, `MODRINTH_TOKEN`, `MODRINTH_PROJECT_ID`). Do not hardcode those values. `MODRINTH_PROJECT_ID` is the 8-character dashboard id, not the slug.

`--upload-stores` also uploads from the operator machine when `.env` has those values (same client + server files, after Wings). `--skip-curseforge` / `--skip-modrinth` still skip a store.

### No promoting a prerelease tag

Do not later re-upload the same `X.Y.Z` as a store `release`. A GitHub prerelease stays alpha/beta on the stores. Cut a **new** version tag and run `release.py --channel release` for an official GitHub Latest plus store release.

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

Then `python scripts/release.py vX.Y.Z --channel …` extracts the `## [X.Y.Z]` section (from that heading through the next `## [` heading) as the GitHub Release body and the CurseForge/Modrinth notes. `--changelog FILE` and `--notes TEXT` override that extract. If the section is missing or has no real bullets, the script hard-fails **before** tagging or calling any API.

### Merge conflicts

Every branch that logs player-facing work edits the same `[Unreleased]` lines, so conflicts are expected and normal. Resolve by keeping **both** branches’ bullets under the right subheader.

If that becomes painful, a fragment-file / towncrier-style `changelog.d/` compiled at release is a reasonable upgrade. Do not build that until the single file actually hurts.

## Public text

Never mention panel URL, join IP, or the dedicated server in `CHANGELOG.md`, GitHub Release bodies, CurseForge/Modrinth notes, or the README. Share the test-server address out of band.
