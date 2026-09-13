# QoL, FTB suite, maps, and Create — considered, chosen, dropped

Research snapshot: 2026-09-13. Target is whatever Minecraft + Forge are in [`pack/pack.toml`](../../pack/pack.toml) (at snapshot: Minecraft 1.20.1, Forge 47.4.23). Re-check store pages before a file bump.

**Status:** this cut **installed** (2026-09-13). JEI, Item Filters, and Iris/Oculus Flywheel Compat were skipped on purpose. Colorwheel (beta) is the Create + Oculus path. packwiz `side` is set as in the tables.

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
| EMI | [modrinth.com/mod/emi](https://modrinth.com/mod/emi) `1.1.24` (`Axuu9I9R`) | both | Recipe browser. Not JEI |
| Too Many Recipe Viewers | [modrinth.com/mod/tmrv](https://modrinth.com/mod/tmrv) (`PSC3dlCl`) | client | EMI layout helper. Incompatible with JEI |
| Accelerated Decay | CurseForge file `4863307` (`3.0.1+mc1.20.1`) | both | Leaves/decay catch-up. Last Forge 1.20.1 file |
| Create | [modrinth.com/mod/create](https://modrinth.com/mod/create) `6.0.8` (`8amzvn9x`) | both | Kinetic content. Bundles Flywheel |
| Create Ultimine | [modrinth.com/mod/create-ultimine](https://modrinth.com/mod/create-ultimine) (`v1WWGazc`) | both | Ultimine + Create blocks. Needs Kotlin |
| Colorwheel | [modrinth.com/mod/colorwheel](https://modrinth.com/mod/colorwheel) `1.3.0-beta3` (`RwUrKFGe`) | client | Create Flywheel under Oculus shaders. **Beta** |
| Colorwheel Patcher | [modrinth.com/mod/colorwheel-patcher](https://modrinth.com/mod/colorwheel-patcher) (`REyG66M8`) | client | Required companion for Colorwheel |
| Xaero's Minimap | [modrinth.com/mod/xaeros-minimap](https://modrinth.com/mod/xaeros-minimap) (`Juh6inLY`) | client | HUD map |
| Xaero's World Map | [modrinth.com/mod/xaeros-world-map](https://modrinth.com/mod/xaeros-world-map) (`rlPmwaQX`) | client | Fullscreen map (keep **M**) |

## Dropped / skipped this cut

| Asked as | Outcome |
|---|---|
| JEI | **Skipped.** TMRV cannot sit next to JEI. EMI is the browser. |
| Item Filters | **Skipped.** FTB Filter System is the 1.20.1 FTB Quests filter mod. |
| Iris & Oculus Flywheel Compat | **Skipped.** Colorwheel is incompatible with it. Create 6 + Oculus uses Colorwheel instead. |
| JourneyMap / voxelmap / a second world map | **Dropped.** Xaero is the map UI. |
| Open Parties and Claims (or any second claim mod) | **Dropped.** FTB Chunks is the claim system. |
| EMI QoL Tweaks | **Removed.** CurseForge file `8713840` is excluded from the third-party API, so packwiz-installer cannot download it. No Modrinth/GitHub file. EMI + TMRV + FTB XMod Compat stay. |

## Held

| Mod | Why wait |
|---|---|
| Default Options | Would let the pack unbind FTB Chunks “Open Map” without touching `options.txt`. Not installed. Unbind in Controls instead (see [configs.md](configs.md)). |
| FTB Chunks × Xaero’s Compat | Third-party claim overlay on Xaero. Not requested. Claim UI stays FTB sidebar / claim manager. |
| Create: Nowheel | Entity Culling + Create contraptions. Watch for invisible contraptions before adding. |
| Shader packs | Loader + Colorwheel are in; packs still chosen later. |

## Incompatibility (this set)

| Pair | Result |
|---|---|
| EMI/TMRV + JEI | TMRV refuses JEI |
| Colorwheel + Iris/Oculus Flywheel Compat | Colorwheel lists incompat |
| FTB Chunks minimap + Xaero minimap | Two HUD maps. Pack disables FTB minimap |
| FTB Open Map (M) + Xaero World Map (M) | Both fire. Unbind FTB Open Map |
| Two claim mods | Overlapping protection / UX |
| Create without a world backup | Sticky block entities / contraption data |
