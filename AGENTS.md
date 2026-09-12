# Lead and Leylines

Long-lived Minecraft Forge modpack. Source of truth is git + packwiz TOML under `pack/`.

## Versions

Read Minecraft version, loader name, and loader version from `pack/pack.toml` (`version`, `[versions]`). Do not copy those numbers into docs, skills, or workflow inputs. Bump by editing `pack.toml` after checking current loader docs.

Pack `version` must match git tag `vX.Y.Z` without the `v`.

## Commands

Run packwiz from `pack/`:

- `packwiz refresh` after any manual file change
- `packwiz curseforge install <mod>` / `packwiz modrinth install <mod>` (aliases `cf add` / `mr add`)
- Pin a Modrinth file with `packwiz modrinth install --project-id <id> --version-id <id> -y` (do not pass a slug together with `--version-id`)
- `packwiz update --all`
- `packwiz curseforge export` / `packwiz modrinth export`
- `packwiz serve` → `http://localhost:8080/pack.toml`

Never commit `.jar` files, launcher instance folders, `.env`, or tokens.

## Layout

- `pack/` — packwiz root (only this tree is exported)
- `server/` — server overlay; never indexed
- `.agents/skills/` — shared agent skills (not `.cursor/skills/`)
- `.github/workflows/release.yml` — tag pipeline

Use packwiz `side` (`client` / `server` / `both`) on mods and configs. One pack, not two roots.

## Local test (Prism)

1. Set the Prism instance Minecraft and loader to the values in `pack/pack.toml`.
2. From `pack/`, run `packwiz serve`.
3. Put `packwiz-installer-bootstrap.jar` in the instance `.minecraft`.
4. Pre-launch: `$INST_JAVA -jar packwiz-installer-bootstrap.jar http://localhost:8080/pack.toml` (do not quote `$INST_JAVA` in instance.cfg; see CONTRIBUTING.md)

See CONTRIBUTING.md for the full loop.

## CI

Push tag `vX.Y.Z` on `main` after `pack.toml` `version` is `X.Y.Z`. Workflow: refresh, export zip + mrpack, GitHub Release always. CurseForge/Modrinth upload only if secrets exist:

- `CURSEFORGE_TOKEN`, `CURSEFORGE_PROJECT_ID`
- `MODRINTH_TOKEN`, `MODRINTH_PROJECT_ID`

Never hardcode those values. Missing secrets must skip with an explicit log, not fail the Release.

## Dedicated server

CurseForge Generic egg. Tracks the last published CurseForge file, not git. See `server/README.md`. `test-server` skill: if no CF file yet, report blocked-on-publish.

## Skills

- `minecraft-modding` — research, compatibility, approval, manifest (read before any install)
- `add-mod` — packwiz install after `minecraft-modding` approval; then refresh
- `test-server` — the panel reinstall/console; API calls are placeholders until MCP exists
- `publish-release` — only on explicit `/publish-release`

## Learned User Preferences

- Verify current versions, docs, and API behavior on the web before implementing; do not assume file structures, tool defaults, or mod compatibility.
- Favor maintainability over speed-of-first-commit on this long-lived pack.
- Ask clarifying questions before structural decisions (repo layout, branching, client/server split) rather than picking silently.
- Never hardcode API tokens or platform project IDs; store them as GitHub Actions secrets.
- Keep agent skills under `.agents/skills/` (not `.cursor/skills/`) so any agent tool reads the same files.
- Run the `publish-release` skill only on an explicit `/publish-release` invocation (`disable-model-invocation: true`).
- Research each candidate mod in detail (compatibility first), ask why it belongs, and compare alternatives before installing.
- Record mod decisions in `docs/mods/` (considered, chosen, held, or dropped; rationale; packwiz `side`); document only configs that need pack notes.

## Learned Workspace Facts

- Pack display name is **Lead and Leylines** (`pack/pack.toml` `name`). GitHub remote remains `https://github.com/TinorNoah/The-End-Game.git` until the store/repo slugs are changed on purpose.
- This is a long-term Minecraft Forge modpack managed with packwiz; never commit jars.
- Modrinth pack slug is still `the-end-game2` (`https://modrinth.com/modpack/the-end-game2`) until renamed on Modrinth.
- Packwiz root is `pack/`; docs (including `docs/mods/` decision logs), CI, and `.agents/` stay at the repo root and are not exported. Shaders are a pack feature (Oculus + Embeddium); do not add a separate dynamic-lights mod while Oculus is in.
- Branching is GitHub Flow (`main`, feature branches, PRs); `v*` tags trigger release; `pack.toml` version matches the tag without the `v`.
- Minecraft, loader, and loader version live only in `pack/pack.toml`; bump that file and keep the README Pack details table in sync in the same change. Do not hardcode versions in skills or workflows.
- One pack uses packwiz `side` (`client` / `server` / `both`); server overlay/JVM overlay lives in `server/` and is never exported.
- Local Prism testing uses `packwiz serve` plus packwiz-installer-bootstrap against `http://localhost:8080/pack.toml`.
- The test server uses the CurseForge Generic egg and tracks the last published CurseForge file, not live git.
- On `v*` tags, CI exports a CurseForge zip and Modrinth mrpack, always attaches both to a GitHub Release, and gates store uploads on secrets.
- Use `.gitattributes` `* -text` so Windows line endings do not break packwiz hashes.
- `CLAUDE.md` is a one-line `@AGENTS.md` pointer.
