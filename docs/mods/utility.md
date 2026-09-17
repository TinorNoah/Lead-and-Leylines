# QoL, FTB suite, maps, and Create — considered, chosen, dropped

Research snapshot: 2026-09-13. Target is whatever Minecraft + Forge are in [`pack/pack.toml`](../../pack/pack.toml) (at snapshot: Minecraft 1.20.1, Forge 47.4.23). Re-check store pages before a file bump.

**Status:** this cut **installed** (2026-09-13). Kitchen-sink QoL **installed** (2026-09-16): extra EMI pages, Inventory Essentials, graves/travel/build sticks. JEI, Item Filters, and Iris/Oculus Flywheel Compat were skipped on purpose. Colorwheel (beta) is the Create + Oculus path. packwiz `side` is set as in the tables.

## Side (packwiz)

| `side` | Meaning |
|---|---|
| `client` | Prism / player instance only. Dedicated server must not require it. |
| `both` | Must run in singleplayer’s integrated server **and** on the dedicated server. |

## What “a second claim mod or second map mod” means

FTB Chunks is the **claim / forceload** system (and it also ships its own minimap and large map). Xaero’s Minimap + World Map are the **map UI**. Those jobs overlap if you also add:

- Another claim mod (Open Parties and Claims, FTB Chunks *and* something else doing the same land-protection)
- Another fullscreen map (JourneyMap, Antique Atlas as a second world map, etc.)

We ship **one claim system** (FTB Chunks) and **one map UI** (Xaero). FTB’s own minimap is turned off. FTB’s large map stays installed so claiming still has a UI (sidebar / claim manager); it is not the everyday map.

Both FTB “Open Map” and Xaero World Map default to **M**. That is the accidental-open conflict, not a second mod.

## Decision rules

1. One recipe browser (EMI + TMRV). TMRV is incompatible with JEI — do not add JEI.
2. FTB Filter System, not Item Filters (FTB Quests on this version wants Filter System).
3. Colorwheel + Colorwheel Patcher with Oculus + Create 6. Do **not** add Iris/Oculus Flywheel Compat; Colorwheel lists that as incompatible.
4. One claim mod. One map UI. Do not add JourneyMap or Open Parties and Claims next to this set.
5. Create writes world data. Back up existing worlds before first boot with Create in.
6. One in-game session re-login (NeoAuth). Do not also add Auth Me or AuthAgain.

---

## Chosen

| Mod | Project | `side` | Why add |
|---|---|---|---|
| Architectury API | CurseForge file `5137938` (`9.2.14`) | both | FTB suite + EMI library |
| Kotlin for Forge | [modrinth.com/mod/kotlin-for-forge](https://modrinth.com/mod/kotlin-for-forge) `4.12.0` (`Zsh14XeQ`) | both | Create Ultimine |
| FTB Library | CurseForge file `8226927` (`2001.2.13`) | both | Shared FTB UI/config |
| FTB Teams | CurseForge file `7499810` (`2001.3.2`) | both | Parties for FTB Chunks / Quests |
| FTB Chunks | CurseForge file `8216874` (`2001.3.8`) | both | Claims and forceload. Minimap off; Xaero is the map |
| FTB Quests | CurseForge file `8078538` (`2001.4.22`) | both | Quest book for the long campaign |
| FTB Ultimine | CurseForge file `7880472` (`2001.1.8`) | both | Vein-style mining |
| FTB Essentials | CurseForge file `7609948` (`2001.2.4`) | both | Light commands (`/home`, `/spawn`, …) |
| FTB XMod Compat | CurseForge file `6402486` (`forge-2.1.3`) | both | FTB Quests + EMI (and other FTB bridges) |
| FTB Filter System | CurseForge file `6466153` (`20.0.1`) | both | Item filters for FTB Quests. Replaces Item Filters |
| Jade | [modrinth.com/mod/jade](https://modrinth.com/mod/jade) (`xJQHCmWJ`) | both | Block/entity overlay. `both` so server info matches |
| AppleSkin | [modrinth.com/mod/appleskin](https://modrinth.com/mod/appleskin) `2.5.1+mc1.20.1` (`XdXDExVF`) | both | Hunger/saturation HUD. Official squeek502 Forge 1.20.1. `both` so saturation syncs on the dedicated server and Prism singleplayer |
| NeoAuth | [modrinth.com/mod/neoauth](https://modrinth.com/mod/neoauth) `1.0.3` (`9xLXbEMY`) | client | In-game Microsoft session re-login (Auth Me for Forge). Mrbysco. No extra libs. Do not put on the dedicated server |
| EMI | [modrinth.com/mod/emi](https://modrinth.com/mod/emi) `1.1.24` (`Axuu9I9R`) | both | Recipe browser. Not JEI |
| Too Many Recipe Viewers | [modrinth.com/mod/tmrv](https://modrinth.com/mod/tmrv) (`PSC3dlCl`) | client | EMI layout helper. Provides a `jei` stub at 15.20.0.132. Incompatible with a real JEI jar |
| Accelerated Decay | CurseForge file `4863307` (`3.0.1+mc1.20.1`) | both | Leaves/decay catch-up. Last Forge 1.20.1 file |
| Create | [modrinth.com/mod/create](https://modrinth.com/mod/create) `6.0.8` (`8amzvn9x`) | both | Kinetic content. Bundles Flywheel |
| Create Ultimine | [modrinth.com/mod/create-ultimine](https://modrinth.com/mod/create-ultimine) (`v1WWGazc`) | both | Ultimine + Create blocks. Needs Kotlin |
| Colorwheel | [modrinth.com/mod/colorwheel](https://modrinth.com/mod/colorwheel) `1.3.0-beta3` (`RwUrKFGe`) | client | Create Flywheel under Oculus shaders. **Beta** |
| Colorwheel Patcher | [modrinth.com/mod/colorwheel-patcher](https://modrinth.com/mod/colorwheel-patcher) (`REyG66M8`) | client | Required companion for Colorwheel |
| Xaero's Minimap | [modrinth.com/mod/xaeros-minimap](https://modrinth.com/mod/xaeros-minimap) (`Juh6inLY`) | client | HUD map |
| Xaero's World Map | [modrinth.com/mod/xaeros-world-map](https://modrinth.com/mod/xaeros-world-map) (`rlPmwaQX`) | client | Fullscreen map (keep **M**) |
| Default Options | [modrinth.com/mod/default-options](https://modrinth.com/mod/default-options) `18.0.5` (`AVz3mvZZ`) | client | Pack default: FTB Open Map unbound. See [content.md](content.md) |
| Too Fast | [modrinth.com/mod/too-fast](https://modrinth.com/mod/too-fast) `0.4.3.5` (`2pix3xrW`) | server | Dedicated-server “moved too quickly” rubber-band fix. Create trains. |
| EMI Enchants | [modrinth.com/mod/emienchants](https://modrinth.com/mod/emienchants) `1.0.0` (`Lzvq7JEE`) | client | Enchantment pages in EMI. |
| JEI / REI / EMI WorldGen | [modrinth.com/mod/jei-worldgen](https://modrinth.com/mod/jei-worldgen) `1.4.5` (`GVElfR28`) | client | Worldgen pages. No real JEI. TMRV stays. |
| Inventory Essentials | [modrinth.com/mod/inventory-essentials](https://modrinth.com/mod/inventory-essentials) `8.2.19` (`BhuVHyaA`) | both | Extra inventory keys. Mouse Tweaks stays. |
| Item Borders | [modrinth.com/mod/item-borders](https://modrinth.com/mod/item-borders) `1.2.2` (`JUW31p4D`) | client | Rarity borders. Iceberg + Prism already in. Overlaps Legendary Tooltips a bit. |
| Elytra Slot | [modrinth.com/mod/elytra-slot](https://modrinth.com/mod/elytra-slot) `6.4.4+1.20.1` (`k6lA080t`) | both | Curios elytra. Needs Caelus. |
| Caelus API | [modrinth.com/mod/caelus](https://modrinth.com/mod/caelus) `3.2.0+1.20.1` (`mRry0DgY`) | both | Required by Elytra Slot. |
| Cosmetic Armor Reworked | CurseForge file `4600191` (`1.20.1-v1a`) | both | Cosmetic armor slots. Last 1.20.1 file 2023. |
| Colorful Hearts | [modrinth.com/mod/colorfulhearts](https://modrinth.com/mod/colorfulhearts) `4.3.16` (`LkhTyd10`) | client | Heart HUD. |
| Durability Tooltip | [modrinth.com/mod/durabilitytooltip](https://modrinth.com/mod/durabilitytooltip) `1.2.0` (`9fyihfLD`) | client | Durability in tooltip. |
| Toast Control | [modrinth.com/mod/toast-control](https://modrinth.com/mod/toast-control) (`q8jNIVj8`) | client | Toast spam. Placebo already in. |
| Bad Wither No Cookie - Reloaded | [modrinth.com/mod/bwncr](https://modrinth.com/mod/bwncr) `3.17.2` (`lL2MtE37`) | client | Mute wither/dragon sounds. |
| Model Gap Fix | [modrinth.com/mod/modelfix](https://modrinth.com/mod/modelfix) (`QdG47OkI`) | client | Item model gaps. |
| Clean Swing Through Grass | CurseForge `cleanswing-1.20-1.8` | both | Hits through grass. |
| Harvest with ease | [modrinth.com/mod/harvest-with-ease](https://modrinth.com/mod/harvest-with-ease) `9.4.0` (`TqAYmcOy`) | both | Right-click harvest. Store tag is server; packwiz `both` for Prism. |
| No Farmland Trample | [modrinth.com/mod/no-trampling-on-farmland](https://modrinth.com/mod/no-trampling-on-farmland) (`3r3u14ce`) | both | Forge file, not the Fabric-only slug. |
| Login Protection | CurseForge `login-protection` | both | Spawn i-frames after join. |
| Packing Tape | CurseForge `packing-tape` | both | Move tile entities. |
| Packet Fixer | [modrinth.com/mod/packet-fixer](https://modrinth.com/mod/packet-fixer) `3.3.2` (`9F4NGhGR`) | both | Packet size. Cupboard already in. |
| Observable | [modrinth.com/mod/observable](https://modrinth.com/mod/observable) (`QtSVNyjm`) | both | Tick profiler. Architectury + Kotlin already in. |
| Crash Utilities | [modrinth.com/mod/crash-utilities](https://modrinth.com/mod/crash-utilities) `8.1.4` (`2IKVjueV`) | both | Admin crash dump. Not Crash Assistant. Store tag is server; packwiz `both` for Prism. |
| EMI QoL Tweaks | CurseForge file `8713840` (`1.2`) | client | Extra EMI buttons. CurseForge third-party API still excludes this file, so packwiz pins the ForgeCDN URL instead of `metadata:curseforge`. |
| Inventory Tweaks: ReFoxed | [modrinth.com/mod/inventory-tweaks-refoxed](https://modrinth.com/mod/inventory-tweaks-refoxed) `1.20.1-1.2.0` (`eyPkQyNd`) | both | Sort/auto-refill. Store tag is client; packwiz `both` for dedicated auto-refill. Mouse Tweaks + Inventory Essentials stay — watch first boot. |
| Structure Compass | [modrinth.com/mod/structure-compass](https://modrinth.com/mod/structure-compass) `2.3.0` (`B63GJIMm`) | both | Locate a chosen structure. Explorer’s Compass stays. |
| Clickable Advancements | CurseForge file `7886729` (`1.20.1-3.9`) | both | Click chat advancements. Cupboard `4.2` already in. Better Advancements stays. |
| Better Compatibility Checker | [modrinth.com/mod/better-compatibility-checker](https://modrinth.com/mod/better-compatibility-checker) `3.0.3-build.65` (`90T01ZgN`) | both | Rejects mismatched clients. Last 1.20.1 file Sep 2023. |

## Dropped / skipped this cut

| Asked as | Outcome |
|---|---|
| JEI | **Skipped.** TMRV cannot sit next to JEI. EMI is the browser. |
| Item Filters | **Skipped.** FTB Filter System is the 1.20.1 FTB Quests filter mod. |
| Iris & Oculus Flywheel Compat | **Skipped.** Colorwheel is incompatible with it. Create 6 + Oculus uses Colorwheel instead. |
| JourneyMap / voxelmap / a second world map | **Dropped.** Xaero is the map UI. |
| Open Parties and Claims (or any second claim mod) | **Dropped.** FTB Chunks is the claim system. |
| Random Patches | **Skipped.** Conflicts with Too Fast. Too Fast is the speed-limit mixin we want. |
| I'm Fast | **Skipped.** Same job as Too Fast; Too Fast is the maintained Noobanidus file. |
| Auth Me | **Skipped.** Fabric only on 1.20.1. NeoAuth is the Forge port. |
| AuthAgain | **Skipped.** Same session-refresh job as NeoAuth. Do not ship two re-login UIs. |

## Held

| Mod | Why wait |
|---|---|
| FTB Chunks × Xaero’s Compat | Third-party claim overlay on Xaero. Not requested. Claim UI stays FTB sidebar / claim manager. |
| Create: Nowheel | Entity Culling + Create contraptions. Watch for invisible contraptions before adding. |

## Incompatibility (this set)

| Pair | Result |
|---|---|
| EMI/TMRV + JEI | TMRV refuses a real JEI jar |
| TMRV JEI stub + Polymorph 0.49.11+ | Forge treats TMRV's `jei` 15.20.0.132 as too old for Polymorph's optional `[15.57.0.207,)`. Keep Polymorph at 0.49.10. |
| Colorwheel + Iris/Oculus Flywheel Compat | Colorwheel lists incompat |
| FTB Chunks minimap + Xaero minimap | Two HUD maps. Pack disables FTB minimap |
| FTB Open Map (M) + Xaero World Map (M) | Both fire. Unbind FTB Open Map |
| Two claim mods | Overlapping protection / UX |
| Create without a world backup | Sticky block entities / contraption data |
| Too Fast + Random Patches | Author conflict. Do not stack. |
