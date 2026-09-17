# Overworld biomes, terrain, structures — considered, chosen, dropped

Research snapshot: 2026-09-16. Target is whatever Minecraft + Forge are in [`pack/pack.toml`](../../pack/pack.toml). Re-check store pages before a file bump.

**Status:** this cut **installed** (2026-09-16) with the later Nether/mineshaft calls applied (Amplified Nether + BetterNether, not Incendium; MMR, not YUNG mineshafts). packwiz `side` is `both` for all of these.

## Side (packwiz)

| `side` | Meaning |
|---|---|
| `both` | Must run in singleplayer’s integrated server **and** on the dedicated server. |

## Decision rules

1. One Overworld *height/noise* line. Tectonic 3.0.17 (toned-down pack config), not Lithosphere, not both.
2. Terratonic is datapack-only Terralith+Tectonic. This pack uses the Forge **mod** jars; Tectonic already blends with Terralith.
3. Do not stack William Wythers’ Expanded Ecosphere with Regions Unexplored / Oh The Biomes We’ve Gone (Feature Order Cycle).
4. Terralith + RU + BWG is three surface biome injectors. Terralith would become postage stamps at TerraBlender defaults. Pack ships `overworld_region_size` 6 and Tectonic climate scale 0.16.
5. One mineshaft line: MMR (already in). Do not add YUNG’s Better Mineshafts.
6. YUNG Better Caves is Overworld-only (`#minecraft:is_overworld`). Leave the Nether to Amplified Nether + BetterNether.

---

## Chosen

| Mod | Project | `side` | Why add |
|---|---|---|---|
| Aquamirae | [modrinth.com/mod/aquamirae](https://modrinth.com/mod/aquamirae) `7.1.13` (`72GwOBcB`) | both | Ice/ocean dungeon + sea mobs |
| Fragmentum | [modrinth.com/mod/fragmentum](https://modrinth.com/mod/fragmentum) `1.5.2` (`1nysmgB4`) | both | Required by Aquamirae |
| Regions Unexplored | [modrinth.com/mod/regions-unexplored](https://modrinth.com/mod/regions-unexplored) `F-0.5.6+1.20.1` (`XTrgsfIB`) | both | Extra Overworld/Nether biomes |
| Oh The Biomes We've Gone | [modrinth.com/mod/oh-the-biomes-weve-gone](https://modrinth.com/mod/oh-the-biomes-weve-gone) `1.8.0-Forge` (`8L5cwpjz`) | both | BYG sequel |
| CorgiLib | [modrinth.com/mod/corgilib](https://modrinth.com/mod/corgilib) `4.0.3.5` (`HXTB2EAy`) | both | Required by BWG |
| Oh The Trees You'll Grow | [modrinth.com/mod/oh-the-trees-youll-grow](https://modrinth.com/mod/oh-the-trees-youll-grow) `1.20.1-1.7.0` (`AAp1NdQX`) | both | Required by BWG |
| TerraBlender | [modrinth.com/mod/terrablender](https://modrinth.com/mod/terrablender) `3.0.1.10` (`zGconCHG`) | both | Shared by RU and BWG. Pack `overworld_region_size` 6, `nether_region_size` 6 |
| Tectonic | [modrinth.com/mod/tectonic](https://modrinth.com/mod/tectonic) `3.0.17` (`KLmvRxwh`) | both | Big terrain, toned down. Vertical Scale `0.80`. Climate scale `0.16`. Extra gen off. |
| Lithostitched | [modrinth.com/mod/lithostitched](https://modrinth.com/mod/lithostitched) `1.4.11-forge-1.20` (`srPoHKt8`) | both | Required by Tectonic 3.0.17. Modrinth does not list the dep; the jar still requires it. |
| Alex's Caves | [modrinth.com/mod/alexs-caves](https://modrinth.com/mod/alexs-caves) `2.0.2` (`lC8HHXOF`) | both | Six rare cave biomes |
| Citadel | [modrinth.com/mod/citadel](https://modrinth.com/mod/citadel) `2.6.3` (`lTAAe4sZ`) | both | Required by Alex's Caves |
| Terralith | [modrinth.com/mod/terralith](https://modrinth.com/mod/terralith) `2.5.4` (`WeYhEb5d`) | both | Extra Overworld biomes |
| Nullscape | [modrinth.com/mod/nullscape](https://modrinth.com/mod/nullscape) `1.2.8` (`QsRKydVt`) | both | End biomes. Stardust; Forge jar. New End chunks. |
| YUNG's Bridges | [modrinth.com/mod/yungs-bridges](https://modrinth.com/mod/yungs-bridges) `1.20-Forge-4.0.3` (`KgO1gfM2`) | both | River bridges. Rate is baked into the jar (`rarity_filter` chance 3) |
| YUNG's Better Caves | [modrinth.com/mod/yungs-better-caves](https://modrinth.com/mod/yungs-better-caves) `1.20.1-Forge-2.0.7` (`BO1vVvun`) | both | Overworld caves only |
| Structurify | [modrinth.com/mod/structurify](https://modrinth.com/mod/structurify) `2.0.38` (`J0nvhron`) | both | Structure Control. Global spacing modifier **off** |
| YetAnotherConfigLib | [modrinth.com/mod/yacl](https://modrinth.com/mod/yacl) `3.6.6+1.20.1-forge` (`sCWgXDYQ`) | both | Required by Structurify |
| Better Sparse Structures | [curseforge.com/minecraft/mc-mods/better-sparse-structures](https://www.curseforge.com/minecraft/mc-mods/better-sparse-structures) `1.2.0.1` (file `7889912`) | both | Minimum gap between structures. `globalSpacingRadiusChunks` 4. Alex's Caves + Create sky villages are whitelisted. |
| Epic Structures: Villages / Witch Huts / Jungle Temples | Modrinth `hCRa4eFr` / `WAWShTQy` / `aN4PmOt6` | both | Vanilla-structure overhauls. Dungeons jar is out (see Dropped). |
| When Dungeons Arise | [modrinth.com/mod/when-dungeons-arise](https://modrinth.com/mod/when-dungeons-arise) `2.1.58` (`6hQpx5Tc`) | both | Extra dungeons |
| When Dungeons Arise: Seven Seas | `DungeonsAriseSevenSeas-1.20.x-1.0.2-forge.jar` (`Ak226ElN`) | both | Ocean dungeons. Not the 1.19.2-named jar |
| Create: Sky Village | [modrinth.com/mod/create-sky-village](https://modrinth.com/mod/create-sky-village) `0.0.38` (`630wzTP1`) | both | Create is already in. Spacing 80 / height offset 64 |
| Countered's Terrain Slabs | [modrinth.com/mod/countereds-terrain-slabs](https://modrinth.com/mod/countereds-terrain-slabs) `4.0.3-beta` (`fhdOSK5I`) | both | Smooth terrain steps. **Beta** |
| Nature's Compass | [modrinth.com/mod/natures-compass](https://modrinth.com/mod/natures-compass) `1.12.0` (`eRSDvCjN`) | both | Find biomes |
| Explorer's Compass | [modrinth.com/mod/explorers-compass](https://modrinth.com/mod/explorers-compass) `1.4.0` (`7ZdJbCOx`) | both | Find structures |
| Chunky | [modrinth.com/mod/chunky](https://modrinth.com/mod/chunky) `1.3.146` (`4FTDk9wv`) | both | Pregen. Writes chunks |
| The Lost Cities | [modrinth.com/mod/the-lost-cities](https://modrinth.com/mod/the-lost-cities) `1.20-7.5.5` (`Ec9sXB06`) | both | City worldgen. Store tag is server; packwiz `both` for Prism. New chunks. `/rtp` cost. |

GeckoLib was already in from Infernal Expansion Redux.

## Dropped / skipped this cut

| Asked as | Outcome |
|---|---|
| Epic Structures: Dungeons | **Removed 2026-09-16.** 1.0 bakes illegal loot IDs (`epic:chests/DungeonZombie`, `DungeonPoop1`) into chest NBT; 1.20.1 throws `ResourceLocationException` during feature placement. 1.1+ (including 1.20-tagged `wr3NbwpD` / `6480mNYC`) lowercases those IDs but stores 1.21 `components` on item frames. Do not re-add until a 1.20.1 file has lowercase loot IDs and 1.20 item NBT. |
| Streams Reflowing | **Removed 2026-09-16 (held).** `/rtp` test. Re-add only if rivers are wanted back on vanilla terrain. |
| Incendium | **Skipped.** Incompatible with Amplified Nether (already in). |
| Expanded Ecosphere | **Skipped.** Feature Order Cycle with RU + BWG. |
| Terratonic | **Skipped.** Datapack-only blend. Forge mods use Tectonic + Terralith jars. |
| Lithosphere | **Skipped.** Same noise job as Tectonic. Do not add as a second height line. |
| YUNG’s Better Mineshafts | **Skipped.** MMR is the mineshaft line. |
| Sodium / Enhanced Block Entities | **Skipped.** Embeddium + Oculus is the renderer. |
| Larion / Atmospherics / Wet Sand / Luki’s Ancient Cities / Voxy | **Skipped.** No usable Forge 1.20.1 file. |
| Fast Item Frames | **Skipped.** Requires Forge Config API Port; that project has no Forge 1.20.1 jar (Fabric only). |
| StructureOverlapless | **Removed 2026-09-16.** Skips placement when a chunk section is “occupied,” including by the same structure start. `/locate` and Explorer’s Compass still report that start. Dedicated logs skipped `create_sky_village:skyvillage` and `dungeons_arise:bandit_towers` at the locate coords. Do not re-add unless a relocate-not-skip tool exists. |
| Sparse Structures | **Removed 2026-09-17.** Replaced by Better Sparse Structures (gap + overlap reject, not a global spread factor). |
| WDA Sparse Structures compat | **Removed 2026-09-16.** Extra thinning on top of Sparse made WDA unfindable. Do not re-add on top of Better Sparse Structures. |

## Configs worth documenting

| Mod | Why a pack note |
|---|---|
| All of this cut | New world. Old chunks stay old-gen. |
| Tectonic | `pack/config/tectonic.json`: Continents Scale `0.11`, Ocean Offset `-0.92`, temperature/vegetation scale `0.16` (Tectonic default `0.25` — smaller scale = larger biomes). Vertical Scale `0.80` so typical highlands sit ~40 blocks lower than Tectonic default. Elevation Boost stays `0.0`. Extra gen off for live `/rtp`: cheese/noodle/spaghetti caves, jungle pillars, underground rivers, river lanterns, rolling hills, lava tunnels, ocean islands. Vanilla carvers stay on. Do not raise Ocean Offset toward `0`. New chunks; 1.20 restart. |
| TerraBlender | `pack/config/terrablender.toml`: `overworld_region_size` 6 (max), `nether_region_size` 6 (max). Do not lower size — that shrinks regions and mixes biome mods more. |
| Better Sparse Structures | `pack/defaultconfigs/bettersparsestructures-server.toml`: `globalSpacingRadiusChunks` 4, size-scaled 3D spacing, `allowStructureOverlap` false. Whitelist `alexscaves:*` and `create_sky_village:*`. Forge Type.SERVER — existing worlds already have `world/serverconfig/bettersparsestructures-server.toml`; copy those keys or delete that file so the default is copied on next start. Overlap reject skips placement (same `/locate` empty-spot risk as StructureOverlapless). Do not re-add Sparse Structures next to this. |
| Structurify | `pack/config/structurify.json`: global spacing modifier **off**. |
| Create: Sky Village | `pack/config/create_sky_village-common.toml`: spacing 80 / separation 40 (author default), height offset 64 so Tectonic peaks are less likely to eat islands. BSS whitelist `create_sky_village:*`. `/locate` still teleports to ground Y — look up. New chunks only. |
| Nullscape | Forge jar `1.2.8`. End biomes only. New End chunks. |
| YUNG’s Bridges | 4.0.3 has `rarity_filter` chance `3` baked into the jar. Tectonic/Terralith can make bridges rarer. No pack toml to turn that up without a datapack overlay. |
| YUNG’s Better Caves | Already Overworld-only. |
| Chunky | Pregen writes the world. Use on purpose; do not leave a huge radius running unattended. Pregen around spawn before relying on `/rtp`. |
| Terrain Slabs | Beta. |
| The Lost Cities | City worldgen. New chunks only. Existing land stays empty of cities. Tune density if `/rtp` stalls. |
