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
- From repo root: `python scripts/release.py` — tag `vX.Y.Z`, wait for GitHub Release, deploy the panel

Never commit `.jar` files, launcher instance folders, `.env`, or tokens.

## Layout

- `pack/` — packwiz root (only this tree is exported)
- `server/` — server overlay; never indexed
- `.agents/skills/` — shared agent skills (not `.cursor/skills/`)
- `.github/workflows/release.yml` — tag pipeline
- `scripts/release.py` — tag + GitHub Release wait + the panel

Use packwiz `side` (`client` / `server` / `both`) on mods and configs. One pack, not two roots.

## Local test (Prism)

1. Set the Prism instance Minecraft and loader to the values in `pack/pack.toml`.
2. From `pack/`, run `packwiz serve`.
3. Put `packwiz-installer-bootstrap.jar` in the instance `.minecraft`.
4. Pre-launch: `$INST_JAVA -jar packwiz-installer-bootstrap.jar http://localhost:8080/pack.toml` (do not quote `$INST_JAVA` in instance.cfg; see CONTRIBUTING.md)

See CONTRIBUTING.md for the full loop.

## CI

Push tag `vX.Y.Z` on `main` after `pack.toml` `version` is `X.Y.Z`. One command: `python scripts/release.py` (tag + GitHub Release wait + the panel). Workflow: refresh, export zip + mrpack, GitHub Release always. CurseForge/Modrinth upload only if secrets exist:

- `CURSEFORGE_TOKEN`, `CURSEFORGE_PROJECT_ID`
- `MODRINTH_TOKEN`, `MODRINTH_PROJECT_ID`

Never hardcode those values. Missing secrets must skip with an explicit log, not fail the Release.

## Dedicated server

CurseForge Generic egg tracks the last published CurseForge file, not git. Until that listing is public, `python scripts/deploy_server.py` (default `--from-local`) installs the Forge Minecraft egg and uploads the current pack’s server-side mods via Wings. `--share-only` writes ATLauncher zip/mrpack under `dist/`. See `server/README.md`. Application API `papp_` key in gitignored `.env`; default panel `https://example.invalid`, node `node` / `example.invalid`. `test-server` skill: local deploy until CF is public; then `--curseforge --reinstall`.

## Skills

- `minecraft-modding` — research, compatibility, approval, manifest (read before any install)
- `add-mod` — packwiz install after `minecraft-modding` approval; then refresh
- `test-server` — the panel via `scripts/deploy_server.py` (`--from-local` until CurseForge is public); console still from the panel until a client API key exists
- `publish-release` — only on explicit `/publish-release`; runs `python scripts/release.py`

## Learned User Preferences

- Verify current versions, docs, and API behavior on the web before implementing; do not assume file structures, tool defaults, or mod compatibility.
- Favor maintainability over speed-of-first-commit on this long-lived pack.
- Ask clarifying questions before structural decisions (repo layout, branching, client/server split) rather than picking silently.
- Never hardcode API tokens or platform project IDs; store them as GitHub Actions secrets.
- Keep agent skills under `.agents/skills/` (not `.cursor/skills/`) so any agent tool reads the same files.
- Run the `publish-release` skill only on an explicit `/publish-release` invocation (`disable-model-invocation: true`).
- Research each candidate mod in detail (compatibility first, including planned content mods), ask why it belongs, and compare alternatives before installing. Prefer client and server changes that make the pack smoother without reliability issues.
- Record mod decisions in `docs/mods/` (considered, chosen, held, or dropped; rationale; packwiz `side`); document only configs that need pack notes.

## Learned Workspace Facts

- Pack display name is **Lead and Leylines** (`pack/pack.toml` `name`). GitHub remote is `https://github.com/TinorNoah/Lead-and-Leylines.git`. Modrinth slug is `lead-and-leylines` (`https://modrinth.com/modpack/lead-and-leylines`). Pack files are MIT (`LICENSE`); third-party mods keep their own licenses. Modrinth listing: description from README pitch, license MIT, version environment client and server.
- This is a long-term Minecraft Forge modpack managed with packwiz; never commit jars.
- Packwiz root is `pack/`; docs (including `docs/mods/` decision logs), CI, and `.agents/` stay at the repo root and are not exported. Shaders are a pack feature (Oculus + Embeddium); Colorwheel is the Create + Oculus path. Do not add a separate dynamic-lights mod while Oculus is in.
- Branching is GitHub Flow (`main`, feature branches, PRs); `v*` tags trigger release; `pack.toml` version matches the tag without the `v`.
- Minecraft, loader, and loader version live only in `pack/pack.toml`; bump that file and keep the README Pack details table in sync in the same change. Do not hardcode versions in skills or workflows.
- One pack uses packwiz `side` (`client` / `server` / `both`); server overlay/JVM overlay lives in `server/` and is never exported. Server-logic optimizers we ship use `both` so Prism singleplayer matches the dedicated server.
- Local Prism testing uses `packwiz serve` plus packwiz-installer-bootstrap against `http://localhost:8080/pack.toml`.
- panel is `https://example.invalid`; Wings node display name `node`, FQDN `example.invalid`. Deploy with `python scripts/deploy_server.py` (local pack tree via Forge egg + Wings until CurseForge is public; Generic egg tracks the last published CurseForge file after that).
- On `v*` tags, CI exports a CurseForge zip and Modrinth mrpack, always attaches both to a GitHub Release, and gates store uploads on secrets.
- Use `.gitattributes` `* -text` so Windows line endings do not break packwiz hashes.
- `CLAUDE.md` is a one-line `@AGENTS.md` pointer.
- Planned content to stay compatible with: TACZ, Superb Warfare, Apotheosis, Create, AE2, Ars Nouveau, Modern Industrialization, Building Gadgets, Mining Gadgets, Mekanism, Mob Grinding Utils, plus later biome / magic / tech / utility mods. Do not add distant-tick freezers, a second Lithium port, a second claim mod, or a second map UI. Create + Oculus uses Colorwheel (not Iris/Oculus Flywheel Compat).
