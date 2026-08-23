---
name: add-mod
description: Search CurseForge or Modrinth, verify the candidate matches pack.toml Minecraft and loader versions, add it with packwiz, and run packwiz refresh. Use when adding a mod to The End Game pack.
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
