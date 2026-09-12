# Mod manifest template

Copy this shape into `docs/mods/manifest.md`. Keep it synchronized with `pack/mods/*.pw.toml` (not with a launcher `mods/` folder).

Minecraft, loader, and pack version: read from `pack/pack.toml` at the time of the entry; do not leave stale hardcoded ecosystem versions in the header after a bump.

## Header

- Pack:
- Pack version:
- Minecraft:
- Loader + version:
- Last synced with `pack/mods/`:

## Installed

One subsection per mod.

### [Mod name]

- Pinned file / version:
- Download source: (Modrinth/CurseForge project URL + file/version id, enough to fetch the identical file)
- packwiz `side`: client / server / both
- Category:
- Why chosen:
- Required dependencies:
- Optional dependencies:
- Recommended companions:
- Config changes: (exact file + setting + why, or “none — defaults”)
- World-data / removability:
- License / attribution:
- Date added:

## Credits / Attribution

| Mod | Author / project | License note | Required credit |
|---|---|---|---|

## Future / Deferred Mods

| Mod | Why not now | What would change that |
|---|---|---|

## Deferred Ecosystem Upgrades

| Proposed change | Why a candidate wanted it | Status |
|---|---|---|

## Removed

| Mod | Removed on | Why | Re-add? |
|---|---|---|---|
