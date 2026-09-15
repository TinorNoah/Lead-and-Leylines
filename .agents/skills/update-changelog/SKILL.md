---
name: update-changelog
description: Use when a player-noticeable pack change lands (mod add/remove/update, config, or bug fix) and CHANGELOG.md [Unreleased] needs a bullet. Not only at release time.
---

# Update the changelog

Player-facing impact only. Policy: [docs/RELEASING.md](../../../docs/RELEASING.md). Do not mention the test server, panel, or join address.

## Steps

1. Open `CHANGELOG.md`.
2. Under `## [Unreleased]`, add one player-phrased bullet in `### Added`, `### Changed`, `### Fixed`, or `### Removed`.
3. If that subheader is missing, create it.
4. If this is a mod add/remove/update, stay consistent with `docs/mods/manifest.md` without copying its full rationale.
