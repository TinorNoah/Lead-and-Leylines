# Phase 1 Developer Workflow Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Empty packwiz pack in git, Prism loop via packwiz-installer, tag workflow that exports CurseForge + Modrinth files and always creates a GitHub Release; store uploads gated on secrets; zero mods.

**Architecture:** `pack/` is the packwiz root. Repo-root docs, CI, and `.agents/` are never exported. `pack/pack.toml` is the only durable Minecraft/loader/version record. the panel uses the CurseForge Generic egg (documented, not a Phase 1 gate). Prism uses `packwiz serve` + installer bootstrap.

**Tech Stack:** git, packwiz, GitHub Actions, packwiz-installer-bootstrap, Kira-NT/mc-publish@v3, softprops/action-gh-release, Python 3.11+ `tomllib` for CI parsing.

**Spec:** `docs/superpowers/specs/2026-08-23-phase-1-dev-workflow-design.md`

## Global Constraints

- Minecraft, loader name, and loader version live only in `pack/pack.toml`. Do not hardcode those numbers in docs, skills, or workflow `with:` inputs.
- Never commit `.jar` files, Minecraft instance folders, `.env`, or API tokens/project IDs.
- Do not add mods in Phase 1. If empty-pack export fails, stop and report; do not add a dummy mod.
- Re-search current packwiz/Forge/Actions docs immediately before running install or CLI commands.
- Existing remote: `https://github.com/TinorNoah/Lead-and-Leylines.git`. Do not create a second repo.
- Push `main` and tag `v0.0.1` only with explicit user approval (Task 9).
- Preserve `AGENTS.md` learned sections; retarget any bullets that pin MC/Forge numbers to `pack.toml`.
- Skills live under `.agents/skills/`, not `.cursor/skills/`.
- `publish-release` must set `disable-model-invocation: true`.

## File map

| Path | Responsibility |
|---|---|
| `.gitignore` | Exclude jars, instances, exports, caches, secrets |
| `.gitattributes` | `* -text` so Windows line endings do not break hashes |
| `pack/pack.toml` | Pack identity + Minecraft/loader versions |
| `pack/index.toml` | Packwiz file index |
| `pack/.packwizignore` | Keep exports out of the index |
| `scripts/read_pack_versions.py` | Parse `pack.toml` for CI and local checks |
| `.github/workflows/release.yml` | Tag → export → GitHub Release → gated store upload |
| `server/README.md` | the panel CurseForge Generic egg vars; no version literals |
| `AGENTS.md` | Conventions + learned sections, &lt;200 lines |
| `CLAUDE.md` | Exactly `@AGENTS.md` |
| `CONTRIBUTING.md` | Human local loop |
| `README.md` | Pack identity + pointers |
| `.agents/skills/add-mod/SKILL.md` | Add a mod via packwiz |
| `.agents/skills/test-server/SKILL.md` | dedicated-server test with API placeholders |
| `.agents/skills/publish-release/SKILL.md` | Explicit `/publish-release` only |

---

### Task 1: Git repo and ignore files

**Files:**
- Create: `.gitignore`
- Create: `.gitattributes`

**Interfaces:**
- Consumes: existing empty GitHub remote URL
- Produces: `main` branch, ignore rules used by every later task

- [ ] **Step 1: Confirm git state**

Run from `C:\Users\tinor\Desktop\Lead and Leylines`:

```powershell
git rev-parse --is-inside-work-tree 2>$null
git remote -v
```

Expected: either not a repo yet, or a repo with no commits. If `origin` exists, it must be `https://github.com/TinorNoah/Lead-and-Leylines.git` (or the `git@github.com:TinorNoah/Lead-and-Leylines.git` equivalent). Do not change remotes. If not a repo:

```powershell
git init -b main
git remote add origin https://github.com/TinorNoah/Lead-and-Leylines.git
```

Skip `remote add` if origin already points at that URL.

- [ ] **Step 2: Write `.gitattributes`**

```gitattributes
# Disable Git line ending conversion, to prevent packwiz index hashes changing when committing from Windows
* -text
```

- [ ] **Step 3: Write `.gitignore`**

```gitignore
# Exported packs
*.zip
*.mrpack

# Never commit jars
*.jar

# Local Minecraft / launcher instances
.minecraft/
minecraft/
instances/
prismlauncher/
*.prism

# packwiz cache
.packwiz/
packwiz-cache/

# Secrets
.env
.env.*
!.env.example
*credentials*
*secret*
*.pem

# OS
.DS_Store
Thumbs.db
Desktop.ini
```

- [ ] **Step 4: Verify ignores**

```powershell
git check-ignore -v fake.jar fake.zip fake.mrpack .minecraft/options.txt .env
```

Expected: each path is ignored.

- [ ] **Step 5: Commit**

```powershell
git add .gitignore .gitattributes
git commit -m "chore: add packwiz-safe gitignore and disable line-ending conversion"
```

---

### Task 2: Initialize the empty packwiz pack

**Files:**
- Create: `pack/pack.toml` (via CLI, not hand-written)
- Create: `pack/index.toml` (via CLI)
- Create: `pack/.packwizignore`

**Interfaces:**
- Consumes: Task 1 repo
- Produces: `pack.toml` fields `name`, `author`, `version`, `[versions].minecraft`, `[versions].<loader>`

- [ ] **Step 1: Confirm packwiz is installed**

Re-read https://packwiz.infra.link/tutorials/creating/getting-started/ and https://packwiz.infra.link/reference/commands/packwiz/init/ then:

```powershell
packwiz --version
```

If missing, install with current docs (`go install github.com/packwiz/packwiz@latest` requires Go 1.24+, or the nightly binary). Do not proceed without a working `packwiz`.

- [ ] **Step 2: Re-check current Forge for the seed Minecraft version**

Open https://files.minecraftforge.net/net/minecraftforge/forge/index_1.20.1.html and note the top version. If it is still `47.4.22`, use the seed below. If it has moved, use the new top recommended build in `--forge-version` only (this is the one-time seed into `pack.toml`).

- [ ] **Step 3: Init inside `pack/`**

```powershell
New-Item -ItemType Directory -Force -Path pack | Out-Null
Set-Location pack
packwiz init --name "Lead and Leylines" --author TinorNoah --version 0.0.1 --mc-version 1.20.1 --modloader forge --forge-version 47.4.22 -y
Set-Location ..
```

If Step 2 found a newer Forge, substitute that `--forge-version`. Do not add mods. Do not create `mods/.gitkeep` or `config/.gitkeep`.

- [ ] **Step 4: Write `pack/.packwizignore`**

```gitignore
# Keep export artifacts out of the pack index
*.zip
*.mrpack
```

- [ ] **Step 5: Refresh and inspect**

```powershell
Set-Location pack
packwiz refresh
Get-Content pack.toml
Get-Content index.toml
Set-Location ..
```

Expected: `pack.toml` has `version = "0.0.1"`, a `[versions]` table with `minecraft` and `forge`, and `index.toml` does not list repo-root docs. Fail if `index.toml` includes `AGENTS.md` or `.github/`.

- [ ] **Step 6: Commit**

```powershell
git add pack/pack.toml pack/index.toml pack/.packwizignore
git commit -m "chore: initialize empty packwiz pack"
```

---

### Task 3: Pack version reader (CI + local)

**Files:**
- Create: `scripts/read_pack_versions.py`

**Interfaces:**
- Consumes: `pack/pack.toml`
- Produces: stdout JSON with keys `pack_version`, `minecraft`, `loader`, `loader_version`

- [ ] **Step 1: Write `scripts/read_pack_versions.py`**

```python
#!/usr/bin/env python3
"""Read pack identity from pack/pack.toml. No hardcoded game versions."""

from __future__ import annotations

import argparse
import json
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK_TOML = ROOT / "pack" / "pack.toml"


def read_pack(path: Path) -> dict[str, str]:
    with path.open("rb") as handle:
        data = tomllib.load(handle)
    pack_version = data.get("version")
    versions = data.get("versions")
    if not pack_version or not isinstance(versions, dict):
        raise SystemExit(f"pack.toml missing version or [versions]: {path}")
    minecraft = versions.get("minecraft")
    if not minecraft:
        raise SystemExit(f"pack.toml [versions] missing minecraft: {path}")
    loader_keys = [key for key in versions if key != "minecraft"]
    if len(loader_keys) != 1:
        raise SystemExit(
            f"expected exactly one loader key in [versions], found {loader_keys}"
        )
    loader = loader_keys[0]
    return {
        "pack_version": str(pack_version),
        "minecraft": str(minecraft),
        "loader": str(loader),
        "loader_version": str(versions[loader]),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--github-output",
        action="store_true",
        help="append KEY=value lines to $GITHUB_OUTPUT",
    )
    args = parser.parse_args()
    if not PACK_TOML.is_file():
        raise SystemExit(f"missing {PACK_TOML}")
    result = read_pack(PACK_TOML)
    if args.github_output:
        github_output = Path(sys.environ.get("GITHUB_OUTPUT", ""))
        if not github_output:
            raise SystemExit("GITHUB_OUTPUT is not set")
        with github_output.open("a", encoding="utf-8") as handle:
            for key, value in result.items():
                handle.write(f"{key}={value}\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run it against the real pack.toml**

```powershell
python scripts/read_pack_versions.py
```

Expected: JSON with `pack_version` `0.0.1`, plus `minecraft`, `loader` (`forge`), and `loader_version` matching `pack/pack.toml` — whatever init wrote, not a guessed number.

- [ ] **Step 3: Commit**

```powershell
git add scripts/read_pack_versions.py
git commit -m "chore: parse pack.toml versions for CI and local checks"
```

---

### Task 4: Tag release workflow

**Files:**
- Create: `.github/workflows/release.yml`

**Interfaces:**
- Consumes: `scripts/read_pack_versions.py`, `pack/`
- Produces: on `v*` tags — zip, mrpack, GitHub Release; optional CurseForge/Modrinth upload

- [ ] **Step 1: Confirm current action tags**

Check https://github.com/softprops/action-gh-release/releases and https://github.com/Kira-NT/mc-publish/releases. If majors are still `v2` and `v3`, use the YAML below. If they have moved, use the current major and note it in the commit message.

- [ ] **Step 2: Write `.github/workflows/release.yml`**

Do not put Minecraft or loader version literals in `with:`.

```yaml
name: Release

on:
  push:
    tags:
      - "v*"

permissions:
  contents: write

jobs:
  export-and-publish:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Read pack.toml
        id: pack
        run: python scripts/read_pack_versions.py --github-output

      - name: Assert tag matches pack version
        env:
          PACK_VERSION: ${{ steps.pack.outputs.pack_version }}
        run: |
          TAG="${GITHUB_REF_NAME}"
          EXPECTED="v${PACK_VERSION}"
          if [ "$TAG" != "$EXPECTED" ]; then
            echo "Tag $TAG does not match pack.toml version $PACK_VERSION (expected $EXPECTED)"
            exit 1
          fi

      - name: Set up Go
        uses: actions/setup-go@v5
        with:
          go-version: "1.24"

      - name: Install packwiz
        run: |
          go install github.com/packwiz/packwiz@latest
          echo "$HOME/go/bin" >> "$GITHUB_PATH"
          packwiz --version

      - name: Refresh and export
        working-directory: pack
        run: |
          packwiz refresh
          packwiz curseforge export
          packwiz modrinth export
          ls -la *.zip *.mrpack

      - name: GitHub Release
        uses: softprops/action-gh-release@v2
        with:
          files: |
            pack/*.zip
            pack/*.mrpack
          generate_release_notes: true
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: Skip CurseForge if secrets missing
        if: ${{ secrets.CURSEFORGE_TOKEN == '' || secrets.CURSEFORGE_PROJECT_ID == '' }}
        run: echo "CurseForge upload skipped: CURSEFORGE_TOKEN or CURSEFORGE_PROJECT_ID not set"

      - name: Upload to CurseForge
        if: ${{ secrets.CURSEFORGE_TOKEN != '' && secrets.CURSEFORGE_PROJECT_ID != '' }}
        uses: Kira-NT/mc-publish@v3
        with:
          curseforge-id: ${{ secrets.CURSEFORGE_PROJECT_ID }}
          curseforge-token: ${{ secrets.CURSEFORGE_TOKEN }}
          curseforge-files: pack/*.zip
          loaders: ${{ steps.pack.outputs.loader }}
          game-versions: ${{ steps.pack.outputs.minecraft }}
          version: ${{ steps.pack.outputs.pack_version }}
          version-type: alpha

      - name: Skip Modrinth if secrets missing
        if: ${{ secrets.MODRINTH_TOKEN == '' || secrets.MODRINTH_PROJECT_ID == '' }}
        run: echo "Modrinth upload skipped: MODRINTH_TOKEN or MODRINTH_PROJECT_ID not set"

      - name: Upload to Modrinth
        if: ${{ secrets.MODRINTH_TOKEN != '' && secrets.MODRINTH_PROJECT_ID != '' }}
        uses: Kira-NT/mc-publish@v3
        with:
          modrinth-id: ${{ secrets.MODRINTH_PROJECT_ID }}
          modrinth-token: ${{ secrets.MODRINTH_TOKEN }}
          modrinth-files: pack/*.mrpack
          loaders: ${{ steps.pack.outputs.loader }}
          game-versions: ${{ steps.pack.outputs.minecraft }}
          version: ${{ steps.pack.outputs.pack_version }}
          version-type: alpha
```

- [ ] **Step 3: Grep the workflow for version literals**

```powershell
Select-String -Path .github/workflows/release.yml -Pattern "1\.20|47\.4"
```

Expected: no matches.

- [ ] **Step 4: Commit**

```powershell
git add .github/workflows/release.yml
git commit -m "ci: export pack on version tags and gate store uploads"
```

---

### Task 5: server overlay docs

**Files:**
- Create: `server/README.md`

**Interfaces:**
- Consumes: spec egg variable names
- Produces: human/agent instructions; no Minecraft version literals

- [ ] **Step 1: Write `server/README.md`**

```markdown
# Server overlay

This directory is **not** part of the packwiz index. Do not put these files under `pack/`.

## panel egg

Use the [CurseForge Generic]() egg.

| panel env | Value |
|---|---|
| `PROJECT_ID` | CurseForge modpack project ID (set in the panel, never in git) |
| `VERSION_ID` | `latest` on the test server |
| `API_KEY` | CurseForge console key (panel only, never in git) |

Pick the egg Java docker image required by the Minecraft version in `pack/pack.toml`. Look up current Mojang/Forge Java requirements when that version changes.

The egg installs from the last published CurseForge file. It does not track git. Until the first CurseForge upload exists, this pack cannot be installed on the dedicated server. Do not fall back to a GitHub raw `pack.toml` URL.

If the egg warns that the file is not a server pack, it will use the client zip. That is expected until a distinct CurseForge server pack is uploaded.

## Overlay files (not created in Phase 1)

After they exist, re-copy these onto the server **after every egg reinstall** (the install script writes `/mnt/server`):

- `user_jvm_args.txt`
- `ops.json`
- host-specific scripts
```

- [ ] **Step 2: Confirm no version literals**

```powershell
Select-String -Path server/README.md -Pattern "1\.20|47\.4|Java 17"
```

Expected: no matches.

- [ ] **Step 3: Commit**

```powershell
git add server/README.md
git commit -m "docs: describe the panel CurseForge Generic egg overlay"
```

---

### Task 6: Root docs (AGENTS, CLAUDE, CONTRIBUTING, README)

**Files:**
- Modify: `AGENTS.md` (add conventions above learned sections; retarget version bullets)
- Create: `CLAUDE.md`
- Create: `CONTRIBUTING.md`
- Create: `README.md`

**Interfaces:**
- Consumes: `pack.toml` as the version source (by reference, not copied numbers)
- Produces: agent + human workflow docs

- [ ] **Step 1: Replace `AGENTS.md` with conventions plus retargeted learned sections**

Keep the file under ~200 lines. Do not put Minecraft or Forge version numbers anywhere.

```markdown
# Lead and Leylines

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
- `server/` — server overlay; never indexed
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

## Dedicated server

CurseForge Generic egg. Tracks the last published CurseForge file, not git. See `server/README.md`. `test-server` skill: if no CF file yet, report blocked-on-publish.

## Skills

- `add-mod` — search, verify against `pack.toml`, install, refresh
- `test-server` — the panel reinstall/console; API calls are placeholders until MCP exists
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
- GitHub remote is `https://github.com/TinorNoah/Lead-and-Leylines.git`.
- Packwiz root is `pack/`; docs, CI, and `.agents/` stay at the repo root and are not exported.
- Branching is GitHub Flow (`main`, feature branches, PRs); `v*` tags trigger release; `pack.toml` version matches the tag without the `v`.
- Minecraft, loader, and loader version live only in `pack/pack.toml`; bump that file, never prose.
- One pack uses packwiz `side` (`client` / `server` / `both`); server overlay/JVM overlay lives in `server/` and is never exported.
- Local Prism testing uses `packwiz serve` plus packwiz-installer-bootstrap against `http://localhost:8080/pack.toml`.
- The test server uses the CurseForge Generic egg and tracks the last published CurseForge file, not live git.
- On `v*` tags, CI exports a CurseForge zip and Modrinth mrpack, always attaches both to a GitHub Release, and gates store uploads on secrets.
- Use `.gitattributes` `* -text` so Windows line endings do not break packwiz hashes.
- `CLAUDE.md` is a one-line `@AGENTS.md` pointer.
```

- [ ] **Step 2: Write `CLAUDE.md`**

File contains exactly:

```text
@AGENTS.md
```

No extra newline-only variations beyond a single trailing newline.

- [ ] **Step 3: Write `README.md`**

```markdown
# Lead and Leylines

A git-managed Minecraft Forge modpack using [packwiz](https://packwiz.infra.link/). Mods are TOML metadata, never committed jars.

- Minecraft and loader versions: `pack/pack.toml`
- Contributor loop: [CONTRIBUTING.md](CONTRIBUTING.md)
- Agent conventions: [AGENTS.md](AGENTS.md)
```

- [ ] **Step 4: Write `CONTRIBUTING.md`**

Before writing the bootstrap download sentence, open https://github.com/packwiz/packwiz-installer-bootstrap/releases and use the latest `.jar` asset URL in the steps (do not invent a tag). Do not put Minecraft/Forge version numbers in this file.

```markdown
# Contributing

## Install packwiz

Follow current docs: https://packwiz.infra.link/tutorials/creating/getting-started/

Confirm with `packwiz --version`. Work inside `pack/` for packwiz commands.

## Add a mod

Prefer the `add-mod` skill, or by hand:

1. Read Minecraft version and loader from `pack/pack.toml`.
2. Confirm the mod supports that Minecraft version and loader on CurseForge or Modrinth.
3. `packwiz curseforge install <slug-or-url>` or `packwiz modrinth install <slug-or-url>`.
4. `packwiz refresh`.
5. Commit the new `*.pw.toml` and `index.toml` / `pack.toml` changes. Never commit jars.

## Test on Prism

1. Create a Prism instance whose Minecraft version and loader match `pack/pack.toml`.
2. Download `packwiz-installer-bootstrap.jar` from the latest release of https://github.com/packwiz/packwiz-installer-bootstrap/releases into the instance `.minecraft` folder (same folder as `options.txt`).
3. From `pack/` run `packwiz serve` and leave it running (`http://localhost:8080/pack.toml`).
4. Instance settings → Custom commands → enable Custom Commands. Pre-launch:

   `"$INST_JAVA" -jar packwiz-installer-bootstrap.jar http://localhost:8080/pack.toml`

5. Launch. The installer syncs the instance to the current pack. If serve is down, pre-launch fails.

The Prism instance is local only. Do not commit it.

## Release

1. Set `pack.toml` `version` to `X.Y.Z` (no `v`).
2. Merge to `main`.
3. Tag and push `vX.Y.Z` (or use `/publish-release`).
4. GitHub Actions exports zip + mrpack and creates a GitHub Release. CurseForge/Modrinth upload if those secrets are set.

Secrets (repo Settings → Secrets; never commit):

- `CURSEFORGE_TOKEN`, `CURSEFORGE_PROJECT_ID`
- `MODRINTH_TOKEN`, `MODRINTH_PROJECT_ID`

## test server

See `server/README.md`. The CurseForge Generic egg tracks the last published CurseForge file, not `main`. After a store upload, reinstall the egg. Overlay files must be re-copied after reinstall.
```

- [ ] **Step 5: Guard against version literals in docs**

```powershell
Select-String -Path AGENTS.md,CLAUDE.md,CONTRIBUTING.md,README.md -Pattern "1\.20|47\.4"
```

Expected: no matches.

- [ ] **Step 6: Line count**

```powershell
(Get-Content AGENTS.md | Measure-Object -Line).Lines
```

Expected: under 200.

- [ ] **Step 7: Commit**

```powershell
git add AGENTS.md CLAUDE.md CONTRIBUTING.md README.md
git commit -m "docs: add packwiz workflow conventions and contributor loop"
```

---

### Task 7: Agent skills

**Files:**
- Create: `.agents/skills/add-mod/SKILL.md`
- Create: `.agents/skills/test-server/SKILL.md`
- Create: `.agents/skills/publish-release/SKILL.md`

**Interfaces:**
- Consumes: `pack/pack.toml`, CONTRIBUTING/server README
- Produces: skills any agent tool can load from `.agents/skills/`

- [ ] **Step 1: Write `.agents/skills/add-mod/SKILL.md`**

```markdown
---
name: add-mod
description: Search CurseForge or Modrinth, verify the candidate matches pack.toml Minecraft and loader versions, add it with packwiz, and run packwiz refresh. Use when adding a mod to Lead and Leylines pack.
---

# Add a mod

Do not hardcode Minecraft or loader versions. Read them from `pack/pack.toml` (`[versions]`).

## Steps

1. Read `minecraft` and the loader key/version from `pack/pack.toml` (or `python scripts/read_pack_versions.py`).
2. Search CurseForge and/or Modrinth for the requested mod.
3. Open the file/version that claims support for that Minecraft version and loader. If none exists, stop and tell the user. Do not add it "to try".
4. From `pack/`, install:
   - `packwiz curseforge install <slug-or-url>` or
   - `packwiz modrinth install <slug-or-url>`
   Aliases `packwiz cf add` / `packwiz mr add` are fine.
5. Accept dependencies only when they also match the pack versions (or packwiz will prompt).
6. `packwiz refresh`.
7. Stage TOML only (`mods/*.pw.toml`, `index.toml`, `pack.toml` if changed). Never stage `.jar` files.

## Side

Set packwiz `side` to `client`, `server`, or `both` based on the mod's documented environment. Client-only mods must not be treated as server requirements.
```

- [ ] **Step 2: Write `.agents/skills/test-server/SKILL.md`**

```markdown
---
name: test-server
description: Restart the panel-hosted test server (CurseForge Generic egg), wait for boot, pull recent console output, and flag crash or error patterns. Use when testing the pack on the dedicated server.
---

# Test dedicated server

The test server uses the CurseForge Generic egg and tracks the last published CurseForge file, not live git. See `server/README.md`.

If no CurseForge project/file exists yet, report **blocked-on-publish** and stop. Do not invent a GitHub raw pack.toml fallback.

## Steps

1. Confirm egg vars in the panel (do not print secret values):
   - `PROJECT_ID` — CurseForge modpack id
   - `VERSION_ID` — `latest` on the test box
   - `API_KEY` — present in the panel, never in git
2. Reinstall or restart so the egg pulls the current CurseForge file.
3. Wait until the console shows a boot-complete pattern (Forge "Done" / "For help, type") or a crash.
4. Pull recent console output.
5. Flag:
   - `Exception`, `Error`, crash reports
   - egg message that the file is not a server pack (expected until a distinct server pack exists; still report it)
   - missing overlay after reinstall (`ops.json`, `user_jvm_args.txt` not re-copied)

## Dedicated server API (placeholder)

Replace these when an MCP or API client exists. Do not guess URLs, keys, or server UUIDs.

```text
# TODO panel API: authenticate (panel URL + API key from user/MCP, never commit)
# TODO panel API: POST reinstall or power restart for the test server
# TODO panel API: GET websocket/console log since restart
# TODO panel API: map HTTP errors (401/404) to a clear operator message
```

Until those exist, ask the user to reinstall/restart in the panel and paste console output, then apply the flag rules above.
```

- [ ] **Step 3: Write `.agents/skills/publish-release/SKILL.md`**

```markdown
---
name: publish-release
description: Align pack.toml version with a vX.Y.Z tag, push the tag, and let GitHub Actions export and publish. Use only when the user explicitly types /publish-release.
disable-model-invocation: true
---

# Publish a release

Do not upload zip/mrpack files from the agent machine. CI does export and publish.

## Steps

1. Confirm `main` is the intended commit (clean working tree, PR merged).
2. Read `pack_version` from `pack/pack.toml` via `python scripts/read_pack_versions.py`.
3. If the user asked for a new version, edit `pack.toml` `version` to `X.Y.Z` (no `v`), `packwiz refresh`, commit on a branch/PR as usual, merge to `main`.
4. Tag `vX.Y.Z` where `X.Y.Z` equals `pack.toml` `version`. Push the tag only after the user confirms the push.
5. Point the user at the Actions run and the GitHub Release. Store uploads happen only if `CURSEFORGE_*` / `MODRINTH_*` secrets are set; otherwise those steps skip.

Never write tokens or project IDs into files.
```

- [ ] **Step 4: Confirm publish-release frontmatter includes `disable-model-invocation: true` and no version literals in any skill**

```powershell
Select-String -Path .agents/skills/*/SKILL.md -Pattern "1\.20|47\.4"
Select-String -Path .agents/skills/publish-release/SKILL.md -Pattern "disable-model-invocation"
```

- [ ] **Step 5: Commit**

```powershell
git add .agents/skills
git commit -m "chore: add add-mod, test-server, and publish-release skills"
```

---

### Task 8: Local empty-pack export proof

**Files:**
- Test: `pack/*.zip`, `pack/*.mrpack` (gitignored)

**Interfaces:**
- Consumes: Tasks 2–4
- Produces: evidence that empty export works; stop if packwiz refuses zero mods

- [ ] **Step 1: Refresh and export**

```powershell
Set-Location pack
packwiz refresh
packwiz curseforge export
packwiz modrinth export
Set-Location ..
```

If either export errors because the pack has no mods, **stop and report**. Do not add a dummy mod.

- [ ] **Step 2: Confirm artifacts are ignored**

```powershell
git status
```

Expected: zip/mrpack untracked or ignored; no jars.

- [ ] **Step 3: Inspect manifests without extracting into git**

```powershell
python -c "import zipfile,json,glob,pathlib; p=pathlib.Path('pack');
z=next(p.glob('*.zip'));
m=json.loads(zipfile.ZipFile(z).read('manifest.json'));
print('cf mc', m['minecraft']['version'], 'loaders', m['minecraft']['modLoaders']);
print('cf files', m.get('files', []));
mr=next(p.glob('*.mrpack'));
idx=json.loads(zipfile.ZipFile(mr).read('modrinth.index.json'));
print('mr deps', idx.get('dependencies'));
print('mr files', idx.get('files', []))"
```

Expected: Minecraft/loader in the exports match `python scripts/read_pack_versions.py`. `files` lists are empty (zero mods).

- [ ] **Step 4: Prism (operator)**

Follow CONTRIBUTING.md on the machine with Prism. Success: installer fetches `http://localhost:8080/pack.toml` and the empty pack reaches the title screen. If Prism is not available in this session, record that the operator must do this before calling Phase 1 complete locally; CI proof is still the tag.

---

### Task 9: Push and tag (explicit user approval only)

**Files:** none new

**Interfaces:**
- Consumes: all prior commits on `main`
- Produces: GitHub Release `v0.0.1` with zip + mrpack; store steps skip unless secrets exist

- [ ] **Step 1: Stop and ask**

Do not run `git push` or `git tag` until the user explicitly says to push and tag. Show `git log --oneline` and `git status`.

- [ ] **Step 2: After approval, push `main`**

```powershell
git push -u origin main
```

- [ ] **Step 3: After approval, tag `v0.0.1`** (must match `pack.toml` `version`)

```powershell
git tag v0.0.1
git push origin v0.0.1
```

- [ ] **Step 4: Verify Actions**

Confirm the workflow: exports succeed, GitHub Release has zip + mrpack, CurseForge/Modrinth skip with the missing-secret log (unless the user added secrets). Job must fail if export or Release failed.

---

## Self-review

**Spec coverage:** Layout, packwiz init seed, `.gitignore`/`.gitattributes`, `pack.toml` SoT, version reader, release workflow, server README, AGENTS/CLAUDE/CONTRIBUTING/README, three skills, empty export proof, push/tag gated on approval. the panel is documented, not a Phase 1 gate.

**Placeholders:** the panel API `# TODO` lines are required by the spec (skill placeholders until MCP exists), not incomplete plan steps.

**Type consistency:** `pack_version` / `minecraft` / `loader` / `loader_version` from `scripts/read_pack_versions.py` match workflow outputs and skill instructions.
