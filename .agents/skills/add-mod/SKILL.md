---
name: add-mod
description: Use after minecraft-modding approval when installing a researched mod into Lead and Leylines with packwiz. Trigger when the user approved a specific file, or when running packwiz install/refresh for this pack. Do not use this skill to skip compatibility research.
---

# Add a mod

Do not run this until `minecraft-modding` Steps 1–4 are done and the user approved the specific file. This skill is Step 6 (install) only.

Do not hardcode Minecraft or loader versions. Read them from `pack/pack.toml` (`[versions]`).

## Steps

1. Re-verify the approved store file still lists this pack's Minecraft version and loader.
2. **Try CurseForge first, always** — `packwiz curseforge install <slug-or-url>` (aliases: `packwiz cf install`). Only use `packwiz modrinth install` if the mod is confirmed **not** published on CurseForge at all. See `docs/mods/distribution.md`. Using Modrinth as a *mod source* for files that are not on CurseForge is unrelated to whether this pack is published *to* the Modrinth store.
   - Only install **required** deps that also match this pack's MC version/loader.
   - If a slug is ambiguous or not found, retry with explicit IDs: `packwiz cf install --addon-id <id> --file-id <id>`. Don't give up and fall back to Modrinth just because a plain slug search missed — confirm the mod truly isn't on CurseForge before switching platforms.
   - Pin Modrinth (fallback case) with `packwiz modrinth install --project-id <id> --version-id <id> -y` (do not pass a slug together with `--version-id`).
3. **Verify the metadata actually landed.** Open the new `pack/mods/<name>.pw.toml` and confirm it has an `[update.curseforge]` (or, for the fallback case, `[update.modrinth]`) block with real IDs — not just a bare `[download]` URL. A mod added successfully but missing this block will silently get embedded as a jar at export time instead of referenced. If it's missing and the mod is on CurseForge, redo the install with explicit `--addon-id`/`--file-id` rather than proceeding.
4. Set packwiz `side` to `client`, `server`, or `both` as approved. Server-logic mods needed in singleplayer are `both`.
5. `packwiz refresh`.
6. Update `docs/mods/manifest.md` (and the relevant `docs/mods/` decision log). Confirm it matches `pack/mods/*.pw.toml`.
7. Add or remove the row in `docs/installed/catalog.toml` (category, group, blurb, tags). This file is hand-edited; packwiz does not update it. Policy: [docs/installed/MAINTENANCE.md](../../../docs/installed/MAINTENANCE.md).
8. Run `python3 scripts/installed_catalog.py`, then `python3 scripts/installed_catalog.py --check`. Stage the regenerated markdown and `catalog.json` with the TOML.
9. Call `update-changelog` to log the mod addition/removal in `[Unreleased]`.
10. Stage TOML and docs only. Never stage `.jar` files.

## Side

Client-only mods must not be treated as server requirements. Dedicated-server-only `side = "server"` is rare; do not leave packwiz's default `server` on mods that should run in Prism singleplayer.