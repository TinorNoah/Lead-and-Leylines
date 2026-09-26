# Worldgen — considered, chosen, dropped

Target is whatever Minecraft + NeoForge are in [`pack/pack.toml`](../../pack/pack.toml). Re-check store pages before a file bump.

**Status:** Lithostitched, Terralith, Nullscape, Regions Unexplored, Oh The Biomes We've Gone, Feature Recycler, structure mods, Lost Cities, Bye?Pregen! for generation cost. Tectonic is out.

## Chosen

| Mod | Pinned file | `side` | Why |
|---|---|---|---|
| Lithostitched | `lithostitched-1.8.0-neoforge-21.1.jar` | both | Required by Regions Unexplored and Terralith. Tectonic removed 2026-09-22. RU `lithostitched:in_structure` placed features are overridden (see below). |
| TerraBlender (NeoForge) | `TerraBlender-neoforge-1.21.1-4.1.0.8.jar` | both | Required by Oh The Biomes We've Gone. Pack config sets region sizes to 6 (max) so biome mods do not speckle into each other. See [configs.md](configs.md). |
| GeckoLib | `geckolib-neoforge-1.21.1-4.9.3.jar` | both | Required by Oh The Biomes We've Gone. |
| CorgiLib | `Corgilib-NeoForge-1.21.1-5.0.0.9.jar` | both | Required by Oh The Biomes We've Gone. |
| Oh The Trees You'll Grow | `Oh-The-Trees-Youll-Grow-neoforge-1.21.1-5.3.2.jar` | both | Required by Oh The Biomes We've Gone. |
| Oh The Biomes We've Gone | `Oh-The-Biomes-Weve-Gone-NeoForge-2.6.0.jar` | both | Overworld biomes. World data. WTHIT optional; not added. |
| Regions Unexplored | `regions-unexplored-0.6.2-neoforge-21.1.jar` | both | Overworld biomes. World data. Eight placed features that used `lithostitched:in_structure` are overridden. |
| Global Packs | `globalpacks-neoforge-1.21.1-21.0.6.jar` | both | Loads `pack/global_packs/required_data/` (RU Lithostitched override, large-climate noise, Nether pixie villages, disabled vanilla stone blobs). Unpacked folders (`.packwizignore` blocks `*.zip`). ARR. |
| Terralith | `Terralith_1.21.x_v2.6.2.jar` | both | Overworld biome datapack-as-mod. World data. Requires Lithostitched. Stacks with OTBWG and RU. Built-in terrain slabs off (Countered's Terrain Slabs is the pack's slab layer). |
| Nullscape | `Nullscape_1.21.x_v1.2.14.jar` | both | End overhaul. World data. Stardust companion to Terralith. |
| BetterEnd: New Dawn | `BetterEnd-21.0.35.jar` | both | End biomes/mobs/gear. World data. Shares New Dawn BCLib/WorldWeaver/WunderLib with BetterNether. Stacks with Nullscape and Unusual End. |
| YACL | `yet_another_config_lib_v3-3.8.2+1.21.1-neoforge.jar` | both | Required by Structurify. |
| Structurify | `structurify-neoforge-2.0.41+mc1.21.1.jar` | both | Structure spacing/control. Global multiplier 2.0. Better Sparse Structures skipped (same job). |
| When Dungeons Arise | `DungeonsArise-1.21.1-2.1.68-release.jar` | both | Extra overworld dungeons. World data. ARR. |
| When Dungeons Arise - Seven Seas | `DungeonsAriseSevenSeas-1.21.x-1.0.4-neoforge.jar` | both | Ocean structures. World data. ARR. |
| Library Ferret | `libraryferret-neoforge-1.21.1-4.0.0.jar` | both | Required by Awesome Dungeon. No CurseForge NeoForge 1.21.1 file; Modrinth pin. ARR. |
| Awesome Dungeon | `awesomedungeon-neoforge-1.21.1-3.2.0.jar` | both | Extra dungeons. World data. Modrinth pin. ARR. |
| YUNG's API (NeoForge) | `YungsApi-1.21.1-NeoForge-5.1.9.jar` | both | Required by YUNG's structure mods. Separate CF project from Forge 421850. |
| YUNG's Better Caves | `YungsBetterCaves-1.21.1-NeoForge-3.1.6.jar` | both | Cave overhaul. World data. |
| YUNG's Cave Biomes | `YungsCaveBiomes-1.21.1-NeoForge-3.1.1.jar` | both | Cave biomes. World data. Uses pack TerraBlender NeoForge; do not add TerraBlender (Forge) `563928`. |
| Alex's Caves Continued | — | — | Removed 2026-09-26 with Delight and Spellbooks. Codxlib stays for Alex's Mobs. |
| Compat Structure | `compatstructures-1.0.3.jar` | both | Extra structures. World data. Compat API. |
| YUNG's Better Nether Fortresses | `YungsBetterNetherFortresses-1.21.1-NeoForge-3.1.5.jar` | both | Nether fortress overhaul. World data. |
| YUNG's Bridges | `YungsBridges-1.21.1-NeoForge-5.1.1.jar` | both | River bridges. World data. |
| YUNG's Better Dungeons | `YungsBetterDungeons-1.21.1-NeoForge-5.1.4.jar` | both | Dungeon overhaul. World data. NeoForge `1015112`. |
| YUNG's Better Strongholds | `YungsBetterStrongholds-1.21.1-NeoForge-5.1.3.jar` | both | Stronghold overhaul. World data. NeoForge `1015105`. |
| YUNG's Better End Island | `YungsBetterEndIsland-1.21.1-NeoForge-3.1.2.jar` | both | Central End island. World data. NeoForge `1015127`. |
| YUNG's Better Ocean Monuments | `YungsBetterOceanMonuments-1.21.1-NeoForge-4.1.2.jar` | both | Ocean monument overhaul. World data. NeoForge `1015115`. |
| YUNG's Better Desert Temples | `YungsBetterDesertTemples-1.21.1-NeoForge-4.1.5.jar` | both | Desert temple overhaul. World data. NeoForge `1015114`. |
| Luki's Ancient Cities | `lukis-ancient-cities-v1.2.jar` | both | Ancient city variants. World data. |
| Luki's Woodland Mansions | `lukis-woodland-mansions-v1.0-1.21-1.21.4.jar` | both | Woodland mansion variants. World data. |
| Moog's Structure Lib | `MoogsStructureLib-neoforge-1.21.1-3.3.1.jar` | both | Required by Moog's Mineshafts. |
| MMR - Moog's Mineshafts Reimagined | `MoogsMineshaftsReimagined-1.21-1.0.3.jar` | both | Mineshaft overhaul. World data. Modrinth pin. |
| Epic Structures: Villages | `epic-structures-villages-2.0.0.jar` | both | Village overhaul. World data. ARR. |
| Epic Structures: Witch Huts | `Epic Witch Huts v1.3.1.jar` | both | Witch hut overhaul. World data. ARR. |
| Epic Structures: Jungle Temples | `Epic Jungle Temples v1.0.2.jar` | both | Jungle temple overhaul. World data. ARR. |
| Amplified Nether | `Amplified_Nether_26.2_v1.2.16.jar` | both | Taller Nether terrain. World data. |
| Infernal Expansion Redux | `infernalexp-neoforge-1.21.1-0.3.16.jar` | both | Nether biomes/content. World data. Requires Lithostitched and GeckoLib. More Nether biome mods: [nether.md](nether.md). |
| Countered's Terrain Slabs | `terrain_slabs-neoforge-3.1.2.jar` | both | Smooth terrain slabs. World data. Architectury already in. |
| The Lost Cities | `lostcities-1.21-8.4.4.jar` | both | City worlds. World data. |
| LC²H [Lost Cities: Multithreaded] | `lc2h-omni-4.2.4-LTS.jar` | both | Async city gen on top of Lost Cities 8.4.4. Quantified API required. C2ME is now also in. |
| Quantified API | `quantified api-omni-2.2.3.jar` | both | LC²H scheduler / optional GPU path. Dedicated Mac smoke fell back to CPU (`liblwjgl.dylib` missing in the isolated probe). |
| BiomeSpy | `biomespy-neoforge-1.21.1-1.3.3.jar` | both | Faster `/locate`. TerraBlender-aware. Does not change generated biomes. |
| Bye?Pregen! | `byepregen-1.21.1-1.1.2.5.jar` | both | Generation MSPT. See [performance.md](performance.md). |
| Feature Recycler | `Feature-Recycler-neoforge-2.0.0.jar` | both | Breaks Minecraft feature-order cycles so Terralith + Oh The Biomes We've Gone can generate. ARR. Not a second structure-spacing mod. |
| ATO - All the Ores | `alltheores-3.2.0_neoforge_1.21.1.jar` | both | Extra ores. World data. Almost Unified is in for unification. |
| Create: Sky Village | `create_sky_village-0.0.38 NeoForge 1.21.1.jar` | both | Create village structure. World data. Optional Create dep lookup failed for this MC/loader; the village jar itself listed 1.21.1 NeoForge. |
| C2ME | `c2me-neoforge-mc1.21.1-0.4.0-alpha.0.122.jar` | both | Threaded chunk gen/IO. Alpha. ByePregen auto-disables C2ME FluidPostProcessingFilter. OpenCL module not shipped (Java 25). |

Twilight Forest: [content.md](content.md).

`lead-leylines-large-climate/` overrides Terralith's Overworld temperature and vegetation noise to vanilla Large Biomes scale (and slightly damps high-frequency octaves). That stretches individual biomes inside a TerraBlender region without switching to the Large Biomes world type. New world required. See [configs.md](configs.md).

`lead-leylines-nether-pixies/` moves Ice and Fire pixie villages from overworld forests into `#minecraft:is_nether`. Pixies only spawn from those villages. New Nether chunks required.

`lead-leylines-nether-fire-dragons/` moves fire dragon roosts and caves onto the same Nether biome tags. Ice and lightning dragons stay on their own biome tags. Structurify's global multiplier is 2.0, so those structure sets are also twice as far apart in new chunks.

`lead-leylines-no-vanilla-stone/` removes Terralith's disabled `ore_andesite_*`, `ore_diorite_*`, and `ore_granite_*` placed features from overworld biome lists (plus Ars Elemental biomes that still reference them). Those features already had `count: 0`. Stone still comes from Terralith. Keep `vanilla_stone_gen` off.

The RU override datapack drops `minecraft:block_predicate_filter` steps whose predicate is `lithostitched:in_structure` from: `patch/ash_vents_inferno`, `patch/cave_bioshrooms`, `patch/dropleaf`, `patch/prismarite_cluster`, `patch/redstone_bud`, `patch/redstone_bulb`, `special/lava_fall`, `special/overworld_lava_delta`. That predicate joins a chunk future on a worldgen worker; dedicated servers freeze in `ChunkMap.processUnloads` / “Saving worlds”. Reproduced **without** ByePregen or C2ME (ATM10 Aeronautics dump, Lithostitched beta4; same predicate in beta6). Those eight features can now place inside structures.

Terralith 2.6.2 + Oh The Biomes We've Gone 2.6.0 hit `IllegalStateException: Feature order cycle found` during Lithostitched biome injectors (`terralith:skylands_spring` with `biomeswevegone:coconino_meadow` / `sakura_grove` and vanilla plains/savanna). Feature Recycler 2.0.0 reorders placed features so that cycle does not crash chunk gen. Do not drop Terralith to “fix” it.

## Considered / held / dropped

| Mod | Status | Why |
|---|---|---|
| WTHIT | Dropped | Overlaps Jade. Optional OTBWG tooltip dep; not added. |
| Better Sparse Structures | Dropped | Same structure-spacing job as Structurify. Do not stack. |
| Sparse Structures | Dropped | Different project from Better Sparse Structures; also overlaps Structurify. |
| Alex's Caves + Citadel / Continued | Removed | Continued removed 2026-09-26 with its Delight and Spellbooks. Do not re-add Citadel or the unofficial caves port. |
| Stalwart Dungeons | Held | No 1.21.1 NeoForge file. |
| Bygone Nether | Held | No 1.21.1 NeoForge file. |
| BetterNether | Removed | Old Forge project had no 1.21.1 NF file. BetterNether: New Dawn `1422293` is in. |
| Awesome Dungeon Nether | Held | No 1.21.1 NeoForge file (later MC only). |
| YUNG's Better Dungeons | Installed | NeoForge project `1015112` (not the Forge slug `510089`). |
| WWOO | Held | Chart companion for terrain overhauls + ByePregen; not in the 1.20.1 pack. |
| Tectonic | Removed | Player request 2026-09-22. Lithostitched stays. Existing Tectonic chunks remain until regenerated. |
| Noisium | Dropped | Incompatible with ByePregen. |
| FastNoise | Dropped | Compatible with ByePregen unless RTF is also in. Exclusive Tectonic-era smoke: no CPS gain vs Tectonic-only baseline. |
| Chunky | Dropped for now | Use NeoForge `/neoforge generate` for operator pregen. Chunky was in a freeze report only as the pregen driver, not the root cause. |
| Chunk Pregenerator | Removed 2026-09-26 | Non-daemon `Pregen Chunk Task Queue` threads hang dedicated-server stop after saves finish. Carbon Config removed with it. |
