# Phase 1 Developer Workflow Design

Forge modpack “The End Game”. This spec covers **Phase 1 only**: git, packwiz, Prism, GitHub Actions, agent skills, and docs. Zero mods. Implementation starts only after this spec is approved.

Verified against current packwiz docs (`packwiz init` flags, installer, export), Forge files (latest 1.20.1 build as of 2026-07-21 used only as the **init seed**), the panel CurseForge Generic egg (`PROJECT_ID`, `VERSION_ID`, `API_KEY`), and `Kira-NT/mc-publish@v3`.

## Goal

An empty packwiz pack in git, a local Prism loop driven by packwiz-installer, and a tag workflow that exports CurseForge + Modrinth files and always creates a GitHub Release. Store uploads run only when secrets exist. No jars in git.

**Phase 1 is done when** tag `v0.0.1` produces a GitHub Release with both empty-pack artifacts. CurseForge/Modrinth skip-with-log is success until project IDs and tokens exist. the panel is documented, not a Phase 1 gate.

## Locked decisions

- Packwiz root: `pack/` (not repo root). Docs, CI, and `.agents/` stay outside the export.
- Branching: GitHub Flow. Default branch `main`. Feature branches, PRs, then `v*` tags on `main`.
- One pack + packwiz `side` (`client` / `server` / `both`). server overlay/JVM overlay in `server/`, never indexed.
- Local Prism: `packwiz serve` → `http://localhost:8080/pack.toml`. the panel does **not** use GitHub raw or packwiz-installer.
- the panel: CurseForge Generic egg. Tracks the last **published CurseForge file**, not live git.
- CI: one tag workflow. GitHub Release always. CurseForge/Modrinth gated on secrets.
- **Versions live only in `pack/pack.toml`.** Docs, skills, CI, and CONTRIBUTING read Minecraft, loader, and loader version from that file. They must not hardcode those numbers. Bump by editing `pack.toml` (and verifying current Forge/MC docs), never by editing prose.
- Existing remote: `https://github.com/TinorNoah/The-End-Game.git` (currently empty). Do not create a second repo.

## Single source of truth (`pack.toml`)

`pack/pack.toml` is the only durable record of:

- pack `version` (must match git tag `vX.Y.Z` without the `v`)
- Minecraft version
- mod loader name and version (Forge for Phase 1 seed)

**Allowed to mention version numbers:** this spec’s one-time `packwiz init` command (seeds `pack.toml`), and `pack.toml` itself after init.

**Forbidden to mention version numbers:** `AGENTS.md` conventions, `CONTRIBUTING.md`, `README.md`, `server/README.md`, all three skills, and GitHub Actions YAML/`with:` inputs. Those files say “read `pack/pack.toml`” (or parse it in CI) and describe *how* to compare a mod or instance against those fields.

When implementing, rewrite any continual-learning bullets that currently pin Forge/MC numbers so they point at `pack.toml` instead.

Phase 1 init seed (written once into `pack.toml`, then forgotten by other files). Re-check the current recommended Forge build for the chosen Minecraft version immediately before running init:

```text
packwiz init --name "The End Game" --author TinorNoah --version 0.0.1 --mc-version 1.20.1 --modloader forge --forge-version 47.4.22 -y
```

## Architecture

Source of truth is git + packwiz TOML. Jars are never committed.

```
The-End-Game/
  pack/                         # packwiz root — only this tree is indexed/exported
    pack.toml
    index.toml
    .packwizignore
    mods/                       # may be empty; do not add .gitkeep (would export)
    config/                     # same — empty dirs are optional in git
  server/                       # server overlay — never in packwiz index
    README.md
  .github/workflows/release.yml
  .agents/skills/add-mod/SKILL.md
  .agents/skills/test-server/SKILL.md
  .agents/skills/publish-release/SKILL.md
  .gitignore
  .gitattributes                # * -text
  AGENTS.md
  CLAUDE.md                     # exactly: @AGENTS.md
  CONTRIBUTING.md
  README.md
  docs/superpowers/specs/       # this spec
```

Init runs inside `pack/` using the seed command in **Single source of truth**. After that, every consumer reads `pack.toml`. Version rule: git tag `vX.Y.Z` must equal `pack.toml` `version` `X.Y.Z`. First tag is `v0.0.1`.

## Components

### pack/

Created by `packwiz init` as above. Phase 1 adds no mods. `.packwizignore` excludes `*.zip` and `*.mrpack` so exports never re-enter the index. Do not add `.gitkeep` under `mods/` or `config/` — those files would be packed. Git simply will not track empty directories.

### .gitattributes

Repo root, from the official packwiz example pack:

```text
* -text
```

Prevents Git on Windows from rewriting line endings and breaking packwiz hashes.

### .gitignore

Repo root. Start from the example pack (`*.zip`, `*.mrpack`) and extend:

- `*.jar`
- `.minecraft/`, `minecraft/`, `instances/`
- Prism/MultiMC instance directories if they appear in-tree
- packwiz cache directories
- `.env`, credentials, API key files
- OS junk (`.DS_Store`, `Thumbs.db`)

Never commit jars or a live Minecraft instance.

### server/

Not indexed by packwiz. Phase 1 is a README only:

- Egg: the panel [CurseForge Generic]()
- Docker image: pick the egg Java image required by the Minecraft version currently in `pack.toml` (look up Mojang/Forge Java requirements when that version changes; do not hardcode a Java version in the README or skills)
- `PROJECT_ID`: CurseForge modpack project ID (set in the panel, not git)
- `VERSION_ID`: `latest` on the test server (follows newest CF file)
- `API_KEY`: CurseForge console key in the panel, never in git
- Overlay files (`user_jvm_args.txt`, `ops.json`, host scripts) are named in the README in Phase 1 but not created yet. When they exist, re-copy after every egg reinstall because the install script writes `/mnt/server`.
- Until the first CurseForge file exists, the egg cannot install this pack. No git-URL fallback.

### .github/workflows/release.yml

Trigger: push of tags matching `v*`. Working directory for packwiz: `pack/`.

1. Checkout. Install Go. `go install github.com/packwiz/packwiz@latest`. Log `packwiz --version`.
2. `packwiz refresh`.
3. Parse `pack.toml` for pack `version`, Minecraft version, loader name, and loader version. Assert pack `version` equals the tag without the leading `v`. Fail if not.
4. `packwiz curseforge export` and `packwiz modrinth export`.
5. **Always:** create a GitHub Release for that tag with `softprops/action-gh-release` (or equivalent current action); attach the `.zip` and `.mrpack`. `permissions: contents: write`. Use `GITHUB_TOKEN`.
6. **If** `secrets.CURSEFORGE_TOKEN != ''` and `secrets.CURSEFORGE_PROJECT_ID != ''`: upload the `.zip` with `Kira-NT/mc-publish@v3`, passing `loaders` and `game-versions` from the parsed `pack.toml` fields (not literals in the YAML). Else skip with an explicit log line.
7. **If** `secrets.MODRINTH_TOKEN != ''` and `secrets.MODRINTH_PROJECT_ID != ''`: upload the `.mrpack` the same way. Else skip with an explicit log line.

Secret **names** (values never in the repo):

- `CURSEFORGE_TOKEN`
- `CURSEFORGE_PROJECT_ID`
- `MODRINTH_TOKEN`
- `MODRINTH_PROJECT_ID`

If packwiz export refuses a pack with zero mods, stop and report. Do not add a dummy mod.

### Agent skills (`.agents/skills/`, not `.cursor/skills/`)

| Skill | Invocation | Behavior |
|---|---|---|
| `add-mod` | Auto when adding a mod | Read Minecraft + loader from `pack/pack.toml`. Search CurseForge/Modrinth, confirm the candidate supports those versions, `packwiz curseforge install` or `packwiz modrinth install` (aliases `cf add` / `mr add` are fine), `packwiz refresh`, never commit jars. Skill text must not hardcode MC/loader versions |
| `test-server` | Auto when testing the panel | Reinstall/restart, wait for boot, pull console, flag crash/error patterns and the egg’s “not a server pack” warning. Skill text includes the panel API call **placeholders** until an MCP connection exists (intentional, not a missing spec). If no CF file exists, report blocked-on-publish |
| `publish-release` | Only `/publish-release` (`disable-model-invocation: true`) | Align `pack.toml` version with the tag, push tag `vX.Y.Z` from `main`, point at the workflow. Does not bypass CI |

### Docs

- `AGENTS.md`: project conventions (packwiz commands, never commit jars, CI, Prism, panel egg, skills, **read versions from `pack.toml`**) under ~200 lines. **Keep** the existing `## Learned User Preferences` and `## Learned Workspace Facts` sections; put conventions above them; retarget any learned bullets that pin MC/Forge numbers to `pack.toml`.
- `CLAUDE.md`: exactly `@AGENTS.md`
- `CONTRIBUTING.md`: human loop — add-mod → Prism (`packwiz serve` + installer bootstrap) → tag. Include exact Prism steps and egg variable names. Tell the reader to set the Prism instance Minecraft/loader to whatever `pack.toml` currently says.
- `README.md`: pack identity and pointers to CONTRIBUTING and AGENTS. No version numbers.

## Data flow

### 1. Add or change (local)

`packwiz curseforge install` / `packwiz modrinth install` (or drop a config into `pack/config/` with the correct `side`). Then `packwiz refresh`. Commit TOML and configs only. Feature branch → PR → `main`.

### 2. Client test (Prism)

From `pack/`, `packwiz serve` hosts `http://localhost:8080/pack.toml` and refreshes the index on each request. Prism instance Minecraft and loader must match `pack.toml` (read those fields; do not copy numbers into CONTRIBUTING). Place `packwiz-installer-bootstrap.jar` in the instance `.minecraft`. Pre-launch:

```text
"$INST_JAVA" -jar packwiz-installer-bootstrap.jar http://localhost:8080/pack.toml
```

Serve must be running. This path tests **unreleased** `main`. The instance itself is not in git.

Bootstrap jar: download `packwiz-installer-bootstrap.jar` from the latest GitHub release of `packwiz/packwiz-installer-bootstrap` when writing CONTRIBUTING (re-check the releases page then; do not pin a guessed tag in this spec).

### 3. Server test (the panel, CurseForge Generic egg)

Not git tracking. After a tag publishes the CurseForge zip: set egg vars, reinstall. Egg prefers a CurseForge server pack if `serverPackFileId` exists; otherwise it warns and uses the client zip (expected until a distinct server pack is uploaded). Overlay in `server/` is re-applied after reinstall.

Phase 1 does not require a live the panel install.

### 4. Release

Set `pack.toml` version to `X.Y.Z`. Merge to `main`. Push tag `vX.Y.Z`. Actions export → GitHub Release → optional store uploads. `/publish-release` only wraps this; it does not upload outside CI.

## Error handling

- Refresh or export fails → job fails. No Release, no store upload.
- Tag / `pack.toml` version mismatch → fail before export.
- GitHub Release fails → job fails.
- Store secrets missing → skip that step with an explicit log. Other steps continue.
- Store upload fails (401, bad ID, platform rejects empty pack) → that step fails. Do not guess IDs. Do not delete an already-created GitHub Release; document “Release exists, store did not.”
- Hash churn with no content change → fix line endings (`.gitattributes`); do not refresh until noise disappears.
- Jars / instance folders / `.env` staged → do not commit.
- `packwiz serve` down, bootstrap jar missing, or Prism Minecraft/loader ≠ `pack.toml` → setup error, not a pack bug.
- the panel: no CF file yet → blocked-on-publish, no git-URL fallback. Bad `API_KEY` / `PROJECT_ID` → egg ERROR in console. Key never in git. Egg “not a server pack” warning is flagged by `test-server`. Boot `Exception` / `Error` → pack not marked good.
- add-mod: candidate that does not support the Minecraft version and loader in `pack.toml` → refuse. Forgotten refresh after manual edits → always refresh before commit.

Secrets and the dedicated server `API_KEY` never appear in logs, AGENTS.md, or the spec beyond **names**.

## Testing

### Local, before any tag

1. `packwiz --version` works.
2. In `pack/`: `packwiz refresh` succeeds; `index.toml` lists only intended pack files (no exports, no repo docs).
3. Both exports succeed; artifacts gitignored.
4. Open exports: Minecraft and loader versions match `pack.toml`; **no mods**.
5. Prism: serve + launch; installer fetches localhost; empty Forge pack reaches the title screen.
6. `git status`: no jars, instance folders, or secrets staged.

### CI — Phase 1 gate

1. Scaffold merged to `main`.
2. Push `v0.0.1`.
3. Both exports succeed; GitHub Release `v0.0.1` has zip and mrpack.
4. CurseForge/Modrinth steps skip with the missing-secret log.
5. Job must not succeed if export or GitHub Release failed.

### Dedicated server

Not a Phase 1 gate. After the first CurseForge upload: reinstall egg, confirm boot.

### Out of scope (Phase 2)

Mods, kubejs, config tuning, loaded multiplayer world, CurseForge/Modrinth project creation.

## Implementation constraints

- Search current docs again immediately before running packwiz, installer, or Actions commands. Do not assume flags from memory.
- Ask for tokens and project IDs when store upload is unblocked; never invent them.
- Do not add mods in Phase 1.
- Preserve continual-learning sections in `AGENTS.md` when adding conventions.
- Initialize git locally if needed, default branch `main`, remote `origin` = existing GitHub URL.
- Push `main` and tag `v0.0.1` only with explicit user approval. The Phase 1 CI proof is that tag; do not push it unprompted.
