---
name: add-mod
description: Use after minecraft-modding approval when installing a researched mod into Lead and Leylines with packwiz. Trigger when the user approved a specific file, or when running packwiz install/refresh for this pack. Do not use this skill to skip compatibility research.
---

# Add a mod

Do not run this until `minecraft-modding` Steps 1–4 are done and the user approved the specific file. This skill is Step 6 (install) only.

Do not hardcode Minecraft or loader versions. Read them from `pack/pack.toml` (`[versions]`).

## Steps

1. Re-verify the approved store file still lists this pack’s Minecraft version and loader.
2. From `pack/`, install only that file (and **required** deps that also match):
   - `packwiz curseforge install <slug-or-url>` or
   - `packwiz modrinth install <slug-or-url>`
   - Pin Modrinth with `packwiz modrinth install --project-id <id> --version-id <id> -y` (do not pass a slug together with `--version-id`)
3. Set packwiz `side` to `client`, `server`, or `both` as approved. Server-logic mods needed in singleplayer are `both`.
4. `packwiz refresh`.
5. Update `docs/mods/manifest.md` (and the relevant `docs/mods/` decision log). Confirm it matches `pack/mods/*.pw.toml`.
6. Call `update-changelog` to log the mod addition/removal in `[Unreleased]`.
7. Stage TOML and docs only. Never stage `.jar` files.

## Side

Client-only mods must not be treated as server requirements. Dedicated-server-only `side = "server"` is rare; do not leave packwiz’s default `server` on mods that should run in Prism singleplayer.
