# What ATM-10's 208 KubeJS scripts do, and what is worth reimplementing

Read-only analysis of `../_reference_pack/kubejs/`. **No ATM-10 code is copied here and none may be.** Every file in that tree carries:

> *"As all AllTheMods packs are licensed under All Rights Reserved, this file is not allowed to be used in any public packs not released by the AllTheMods Team, without explicit permission."*

This pack is MIT and public. So the only transferable thing is **mechanism and intent**. Anything adopted below is to be written from scratch against this pack's own mod list.

## Shape of the tree

| Folder | Files | Purpose |
|---|---|---|
| `startup_scripts/` | 19 | Registry patching, compatibility guards, creative tabs, update checks |
| `server_scripts/` | 174 | Recipes (122), tags (18), generated datapacks (7), gameplay hooks (~27) |
| `client_scripts/` | 15 | Ponder animations (9), tooltips (2), banlist sync, crash guards |

By API surface:

| Pattern | Files |
|---|---|
| `ServerEvents.recipes` | 122 |
| Tag add/remove (`ServerEvents.tags`) | 18 |
| `ServerEvents.generateData` (write a datapack at boot) | 7 |
| `PlayerEvents` / `ItemEvents` / `BlockEvents` / `EntityEvents` | 11 |
| `StartupEvents.*` | 9 |
| Client (`ClientEvents`, `modifyTooltips`, Ponder) | 15 |

**Overwhelmingly recipe content.** 122 of 208 add, remove, or reshape recipes for individual mods. That is the bulk of the work and most of it does not transfer — it is `AlmostUnified`-style unification and per-mod compatibility for mods this pack does not have.

## The seven patterns worth understanding

### 1. Self-healing suppression via `Item.exists()` — the best idea in the tree

`server_scripts/mods/Bibliocraft/Recipes.js`:

```js
woodTypes.forEach(wood => {
  if (!Item.exists(`bibliocraft:${wood}_fancy_sign`)) {
    allthemods.json(`bibliocraft:recipe/wood/${wood}/fancy_sign`,
      {"neoforge:condition": [{"type": "neoforge:false"}]})
  }
})
```

It asks a **live question** — does this item exist right now? — and only suppresses the recipe when the answer is no. The suppression disappears by itself the moment the mod fixes its registration.

This pack's 63 disabled recipes are 63 hand-written JSON files that answer that question *statically*, frozen on 2026-09-27. That is exactly why revalidation is a five-batch project in `docs/mods/load-fixes-inventory.md`. **The question can be asked every boot instead.**

### 2. `generateData` writes a datapack at runtime

The same script uses `ServerEvents.generateData("after_mods", ...)` to emit `data/<ns>/recipe/...` JSON. No datapack is committed to the repo; the file materialises during datapack generation.

Consequence for this pack: a suppression list becomes **data, not code** — one JSON array of ids instead of N files, and it can be computed rather than curated. Note ATM-10's `Tweaks/disable_loot_table_ids.json` is exactly this for 962 loot tables.

### 3. Tag repair, overwhelmingly additive

24 of the 25 tag scripts *add*; only one removes. The additions fall into recognisable shapes:

- **Cross-mod tag fixups** — `farmersdelight:tools/knives` ← `#c:tools/knife`, so a newer common tag is honoured by an older mod
- **Seed fan-out** — one loop over a seed list adding `minecraft:crops`, `c:seeds`, `mysticalagriculture:seeds`, `minecraft:bee_growables`, `cucumber:mineable/sickle` and six more per seed
- **Deny lists** — `buildinggadgets2:deny` for ender-storage tanks, `ars_nouveau:whirlisprig/denied_drop` for seeds
- **Animal foods** — `c:animal_foods` for MineColonies crops

The seed fan-out is the notable one: one data list, ~15 target tags, so adding a crop is a one-line change. This pack already has an equivalent problem class documented — seven broken tags behind the "some tags are a bit cooked" startup warning (`CHANGELOG.md`, Unreleased).

### 4. Crash guards for known-bad interactions

`client_scripts/crashing_items.js` is one line: cancel the right-click on `ars_additions:advanced_dominion_wand`, a wand that crashes. A **content blacklist by interaction**, not by mod removal.

`startup_scripts/incompatible_versions.js` asserts five version pins and warns on two mods. This pack's equivalent history exists — JET 0.14.1 killed JEI outright on 2026-09-30 — but the record lives in `docs/mods/manifest.md` rather than an assertion that fails at boot.

### 5. Gameplay hooks via events, not config

- `Tweaks/fix_death_bug.js` — repair NaN health/absorption on login (not applicable here; checked in `docs/mods/phase2-followups.md` §4)
- `Tweaks/registry_fix.js` — add a biome alias at runtime with `Java.loadClass` (not applicable; `biomeswevegone` is not installed)
- `announcements/announcements.js` — join broadcast plus a public command
- `debug/freeze_server.js` — `tick freeze` on load, for reproducing bugs
- `client_scripts/tooltips.js` — `ItemEvents.modifyTooltips` adding mining-tier hints

### 6. Creative-tab and registry mutation at startup

`startup_scripts/CustomAdditions.js` uses `StartupEvents.modifyCreativeTab`; several others use `StartupEvents.registry` to register items. This is how ATM-10 adds its own `kubejs:` items (alloy tools, star items, ATT items) without shipping a content mod.

### 7. Ponder animations — the only substantial client investment

Nine `client_scripts/ponder/*.js` files add in-world Ponder scenes for Mekanism fission, fusion and SPS multiblocks.

## Assessment for this pack

| Pattern | Adopt? | Why |
|---|---|---|
| 1. `Item.exists()` self-healing suppression | **Yes — highest value** | Converts the 63 static recipe overrides from a maintenance chore into something that self-corrects. Same idea applies to loot tables: ask whether the *block* exists before keeping an empty table. |
| 3. Seed fan-out tag repair | **Yes** | Directly addresses the seven broken tags already logged in `CHANGELOG.md`. One list, many target tags. |
| 3. Cross-mod tag fixups | **Maybe** | Only if a concrete broken tag is identified. Currently three of seven are documented as upstream bugs in other mods. |
| 4. Crash-guard blacklist | **No, not yet** | Sound mechanism, but this pack has no reported crash-by-interaction to guard. Adding one would be speculative. |
| 4. Startup version assertions | **Consider** | Would have caught JET 0.14.1 at boot rather than in a smoke log. But it is also how you brick a pack on a false positive. |
| 7. Ponder scenes | **No** | Large authoring effort for a convenience feature this pack's players have not asked for. |
| 6. `kubejs:` custom items | **No** | Content mod territory; the pack ships real content mods instead. |
| 2. `generateData` runtime datapack | **Only alongside pattern 1** | Worth it when the suppression is *computed*. Pointless for a static list, and it makes overrides invisible in a PR diff — a real downside against the current committed-JSON approach. |

## What is deliberately not being copied

- **The 122 recipe scripts.** Almost all are `AlmostUnified` unification and per-mod compatibility for mods absent from this pack. Copying any of it would be both an ARR violation and dead weight.
- **The 962-id loot-table list.** 928 entries are Bibliocraft. This pack's mod mix does not have that problem, and its 120 empties are hand-audited with per-row undo steps.
- **Any code, verbatim.** Mechanisms only.

## Open questions

1. **Pattern 1 needs a decision about where the truth lives.** If suppression becomes computed at boot, `docs/mods/load-fixes-inventory.md` stops being a list of files and becomes a list of *questions* plus the reason each was asked. Is that better? It loses git-diffable overrides, which is currently the pack's main advantage over ATM-10.
2. **Or keep the committed JSON and only compute the "should this still be suppressed?" half** — a script that logs which overrides are now unnecessary, leaving the files in place until a human deletes them. Safer, keeps reviewability, still surfaces the revalidation answer automatically.
3. **The seven broken tags** in `CHANGELOG.md` are described as upstream bugs. Pattern 3 could mask them, but masking an upstream bug is not fixing it. Which does this pack want?
