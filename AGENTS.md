# The End Game

Long-lived Minecraft Forge modpack. Source of truth is git + packwiz TOML under `pack/`.

## Versions

Read Minecraft version, loader name, and loader version from `pack/pack.toml` (`version`, `[versions]`). Do not copy those numbers into docs, skills, or workflow inputs. Bump by editing `pack.toml` after checking current loader docs.

Pack `version` must match git tag `vX.Y.Z` without the `v`.

## Commands

Run packwiz from `pack/`:

- `packwiz refresh` after any manual file change
- `packwiz curseforge install <mod>` / `packwiz modrinth install <mod>` (aliases `cf add` / `mr add`)
- `packwiz update --all`
- `packwiz curseforge export` / `packwiz modrinth export`
- `packwiz serve` → `http://localhost:8080/pack.toml`

Never commit `.jar` files, launcher instance folders, `.env`, or tokens.

## Layout

- `pack/` — packwiz root (only this tree is exported)
- `server/` — Pelican overlay; never indexed
- `.agents/skills/` — shared agent skills (not `.cursor/skills/`)
- `.github/workflows/release.yml` — tag pipeline

Use packwiz `side` (`client` / `server` / `both`) on mods and configs. One pack, not two roots.

## Local test (Prism)

1. Set the Prism instance Minecraft and loader to the values in `pack/pack.toml`.
2. From `pack/`, run `packwiz serve`.
3. Put `packwiz-installer-bootstrap.jar` in the instance `.minecraft`.
4. Pre-launch: `"$INST_JAVA" -jar packwiz-installer-bootstrap.jar http://localhost:8080/pack.toml`

See CONTRIBUTING.md for the full loop.

## CI

Push tag `vX.Y.Z` on `main` after `pack.toml` `version` is `X.Y.Z`. Workflow: refresh, export zip + mrpack, GitHub Release always. CurseForge/Modrinth upload only if secrets exist:

- `CURSEFORGE_TOKEN`, `CURSEFORGE_PROJECT_ID`
- `MODRINTH_TOKEN`, `MODRINTH_PROJECT_ID`

Never hardcode those values. Missing secrets must skip with an explicit log, not fail the Release.

## Pelican

CurseForge Generic egg. Tracks the last published CurseForge file, not git. See `server/README.md`. `test-server` skill: if no CF file yet, report blocked-on-publish.

## Skills

- `add-mod` — search, verify against `pack.toml`, install, refresh
- `test-server` — Pelican reinstall/console; API calls are placeholders until MCP exists
- `publish-release` — only on explicit `/publish-release`

## Learned User Preferences

- Verify current versions, docs, and API behavior on the web before implementing; do not assume file structures, tool defaults, or mod compatibility.
- Favor maintainability over speed-of-first-commit on this long-lived pack.
- Ask clarifying questions before structural decisions (repo layout, branching, client/server split) rather than picking silently.
- Never hardcode API tokens or platform project IDs; store them as GitHub Actions secrets.
- Keep agent skills under `.agents/skills/` (not `.cursor/skills/`) so any agent tool reads the same files.
- Run the `publish-release` skill only on an explicit `/publish-release` invocation (`disable-model-invocation: true`).

## Learned Workspace Facts

- This is a long-term Minecraft Forge modpack managed with packwiz; never commit jars.
- GitHub remote is `https://github.com/TinorNoah/The-End-Game.git`.
- Packwiz root is `pack/`; docs, CI, and `.agents/` stay at the repo root and are not exported.
- Branching is GitHub Flow (`main`, feature branches, PRs); `v*` tags trigger release; `pack.toml` version matches the tag without the `v`.
- Minecraft, loader, and loader version live only in `pack/pack.toml`; bump that file, never prose.
- One pack uses packwiz `side` (`client` / `server` / `both`); Pelican/ops/JVM overlay lives in `server/` and is never exported.
- Local Prism testing uses `packwiz serve` plus packwiz-installer-bootstrap against `http://localhost:8080/pack.toml`.
- The Pelican test server uses the CurseForge Generic egg and tracks the last published CurseForge file, not live git.
- On `v*` tags, CI exports a CurseForge zip and Modrinth mrpack, always attaches both to a GitHub Release, and gates store uploads on secrets.
- Use `.gitattributes` `* -text` so Windows line endings do not break packwiz hashes.
- `CLAUDE.md` is a one-line `@AGENTS.md` pointer.
