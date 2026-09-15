# Releasing Lead and Leylines

How versions, channels, and `CHANGELOG.md` work. Skills (`publish-release`, `update-changelog`) are short checklists; this file is the policy.

The Pelican test server address is shared with testers out of band (Discord/DM/etc.). Never put it in the repo, GitHub Release text, CurseForge notes, or Modrinth notes.

## Channels

`python scripts/release.py vX.Y.Z --channel <channel>` (default `alpha`).

| Channel | GitHub | CurseForge | Modrinth | Test server |
|---|---|---|---|---|
| `alpha` | Prerelease | Not uploaded | Not uploaded | Updated |
| `beta` | Prerelease | Not uploaded | Not uploaded | Updated |
| `release` | Stable release (not a prerelease) | Uploaded | Uploaded | Updated |

Only `--channel release` uploads to CurseForge or Modrinth. `alpha` and `beta` create a GitHub prerelease and update the test server; they do not touch the stores.

`--skip-curseforge` / `--skip-modrinth` still skip a store even on `release`. Missing `CURSEFORGE_*` / `MODRINTH_*` in `.env` also skip that store with a log line. Missing `GH_TOKEN` fails. `MODRINTH_PROJECT_ID` is the 8-character dashboard id, not the slug.

There is no tag GitHub Actions publish job. The operator machine runs `scripts/release.py`.

### No promoting a prerelease tag

An `alpha` or `beta` tag is never “promoted” later to a store build. If a build should go to CurseForge/Modrinth, cut a **new** version tag and run `release.py` with `--channel release`.

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
