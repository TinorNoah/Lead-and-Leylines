# Lead and Leylines — mod manifest

Synced with `pack/mods/*.pw.toml` on 2026-09-17. Minecraft, loader, and pack version: see [`pack/pack.toml`](../../pack/pack.toml). Decision logs: [performance.md](performance.md), [utility.md](utility.md), [storage.md](storage.md), [nether.md](nether.md), [worldgen.md](worldgen.md), [content.md](content.md). Config notes: [configs.md](configs.md). Distribution: [distribution.md](distribution.md). Not-yet-added candidates and remaining Forge mods: [deferred.md](deferred.md).

First 1.21.1 NeoForge wave: performance and client smoothness only.

## Installed

| Mod | Pinned file | Source | `side` | Category | Why | Required deps | Config | Date added |
|---|---|---|---|---|---|---|---|---|
| Sodium | `sodium-neoforge-0.8.13+mc1.21.1.jar` | CurseForge 394468 / 8756580 | client | renderer | Official NeoForge Sodium. Replaces Embeddium. | none | defaults | 2026-09-17 |
| Iris Shaders | `iris-neoforge-1.8.14-beta.1+mc1.21.1.jar` | CurseForge 455508 / 8242804 | client | shaders | Official shaders for Sodium 0.8.x. Oculus has no 1.21.1 NeoForge file. | Sodium (client) | defaults | 2026-09-17 |
| Lithium | `lithium-neoforge-0.15.4+mc1.21.1.jar` | CurseForge 360438 / 8330365 | both | optimizer | Official gameplay/tick optimizer. Replaces Radium. | none | defaults | 2026-09-17 |
| FerriteCore | `ferritecore-7.0.3-neoforge.jar` | CurseForge 429235 / 7524151 | both | memory | Memory. | none | defaults | 2026-09-17 |
| ModernFix | `modernfix-neoforge-5.27.24+mc1.21.1.jar` | CurseForge 790626 / 8774737 | both | optimizer | Launch and mixin fixes. | none | defaults | 2026-09-17 |
| ImmediatelyFast | `ImmediatelyFast-NeoForge-1.6.14+1.21.1.jar` | CurseForge 686911 / 8875640 | client | renderer | Immediate-mode rendering. | none | defaults | 2026-09-17 |
| FastWorkbench | `FastWorkbench-1.21.1-9.1.3.jar` | CurseForge 288885 / 6751534 | both | optimizer | Crafting lookup. | Placebo | defaults | 2026-09-17 |
| FastFurnace | `FastFurnace-1.21.1-9.0.1.jar` | CurseForge 299540 / 6751551 | both | optimizer | Furnace tick. | Placebo | defaults | 2026-09-17 |
| FastSuite | `FastSuite-1.21.1-6.0.7.jar` | CurseForge 475117 / 7527945 | both | optimizer | Recipe manager. | Placebo | defaults | 2026-09-17 |
| Placebo | `Placebo-1.21.1-9.9.2.jar` | CurseForge 283644 / 8463693 | both | library | Fast* dependency. | none | defaults | 2026-09-17 |
| Let Me Despawn | `letmedespawn-1.21.x-neoforge-1.5.0.jar` | CurseForge 663477 / 6311236 | both | entities | Pickup-mobs despawn. | Almanac Lib | defaults | 2026-09-17 |
| Almanac Lib | `Almanac-1.21.1-2-neoforge-1.5.2.jar` | CurseForge 1115285 / 7489091 | both | library | Let Me Despawn dependency. | none | defaults | 2026-09-17 |
| Neruina | `neruina-3.3.3+1.21.1-neoforge.jar` | CurseForge 851046 / 8451084 | both | stability | Ticking-entity isolation. | Configurable | defaults | 2026-09-17 |
| Configurable | `configurable-3.5.2+1.21.1-neoforge.jar` | CurseForge 1092048 / 8438541 | both | library | Neruina dependency. | none | defaults | 2026-09-17 |
| Clumps | `Clumps-neoforge-1.21.1-19.0.0.1.jar` | CurseForge 256717 / 5623731 | both | entities | XP orb merge. | none | defaults | 2026-09-17 |
| Noisium | `noisium-neoforge-2.3.0+mc1.21-1.21.1.jar` | CurseForge 930207 / 5650508 | both | worldgen | Worldgen noise. Archived upstream; this file is the 1.21.1 NeoForge build. | none | defaults | 2026-09-17 |
| AllTheLeaks | `alltheleaks-1.1.12+1.21.1-neoforge.jar` | CurseForge 1091339 / 8648639 | both | stability | Leak patches. | none | defaults | 2026-09-17 |
| Smooth Chunk Save | `smoothchunk-1.21-4.1.jar` | CurseForge 582327 / 6296628 | both | IO | Spreads chunk saves. | Cupboard | defaults | 2026-09-17 |
| Cupboard | `cupboard-1.21.1-4.2.jar` | CurseForge 326652 / 8889050 | both | library | Smooth Chunk Save dependency. | none | defaults | 2026-09-17 |
| BadOptimizations | `BadOptimizations-2.4.1-1.21.1.jar` | CurseForge 949555 / 7338300 | client | renderer | Client skip work. | none | defaults | 2026-09-17 |
| Dynamic FPS | `dynamic-fps-3.11.4+minecraft-1.21.0-neoforge.jar` | CurseForge 335493 / 7546938 | client | client QoL | Lowers FPS when unfocused. | none | defaults | 2026-09-17 |
| Crash Assistant | `CrashAssistant-neoforge-1.20.6-1.21.4-1.11.12.jar` | CurseForge 1154099 / 8636685 | client | stability | Crash dump helper (client-only). | none | defaults | 2026-09-17 |
| Entity Culling | `entityculling-neoforge-1.10.5-mc1.21.1.jar` | CurseForge 448233 / 8287097 | client | renderer | Occlusion culling. | none | defaults | 2026-09-17 |

World-data: none of these add blocks, items, or dimensions. Removable without a world wipe. New world still required because this is the 1.21.1 NeoForge cutover, not because of this wave.

## Credits / Attribution

| Mod | Author / project | License note | Required credit |
|---|---|---|---|
| Sodium | CaffeineMC | Polyform Shield 1.0.0 | Keep the CurseForge reference; do not rehost the jar. |
| Iris Shaders | IrisShaders | LGPL-3.0-only | CurseForge reference. |
| Lithium | CaffeineMC | LGPL-3.0-only | CurseForge reference. |
| FerriteCore | malte0811 | MIT | CurseForge reference. |
| ModernFix | embeddedt | LGPL-3.0-only | CurseForge reference. |
| ImmediatelyFast | RaphiMC | LGPL-3.0-or-later | CurseForge reference. |
| FastWorkbench, FastFurnace, FastSuite, Placebo | Shadows_of_Fire | See each CurseForge page | CurseForge reference. |
| Let Me Despawn, Almanac Lib | frikinjay | LGPL-3.0-only | CurseForge reference. |
| Neruina | bawnorton | See CurseForge page | CurseForge reference. |
| Configurable | See CurseForge project 1092048 | See CurseForge page | CurseForge reference. |
| Clumps | jaredlll08 | MIT | CurseForge reference. |
| Noisium | Steveplays28 | LGPL-3.0-only | CurseForge reference (archived project). |
| AllTheLeaks | Uncandango | See CurseForge page | CurseForge reference. |
| Smooth Chunk Save, Cupboard | someaddon | See CurseForge pages | CurseForge reference. |
| BadOptimizations | thosea | See CurseForge page | CurseForge reference. |
| Dynamic FPS | juliand665 | See CurseForge page | CurseForge reference. |
| Crash Assistant | kr0stik | See CurseForge page | CurseForge reference. |
| Entity Culling | tr7zw | Custom protective license | CurseForge metadata only; do not bundle the jar. |

## Future / Deferred Mods

Long lists: [deferred.md](deferred.md).

| Mod | Why not now | What would change that |
|---|---|---|
| Sodium Extra 0.9.4 | Researched; waiting on Extra vs Chloride | Explicit install approval for Extra (not Chloride). |
| Shader packs | Renderer first | After Sodium + Iris boot cleanly. |
| Colorwheel | Shader companion | Same as shader packs. |
| Rest of the 1.20.1 Forge list (216 mods) | Needs a fresh 1.21.1 NeoForge pass per wave | User picks the next wave. See [deferred.md](deferred.md). |

## Deferred Ecosystem Upgrades

| Proposed change | Why a candidate wanted it | Status |
|---|---|---|

## Removed

| Mod | Removed on | Why | Re-add? |
|---|---|---|---|
| Entire 1.20.1 Forge pack | 2026-09-17 | Loader and Minecraft cutover. History is on `forge-1.20.1`. | Research each mod again for 1.21.1 NeoForge. |
| Embeddium, Oculus, Radium | 2026-09-17 | No 1.21.1 NeoForge ports we will ship. | No; Sodium / Iris / Lithium are the replacements. |
