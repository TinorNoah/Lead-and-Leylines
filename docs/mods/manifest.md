# Lead and Leylines — mod manifest

Synced with `pack/mods/*.pw.toml` on 2026-10-02. Minecraft, loader, and pack version: see [`pack/pack.toml`](../../pack/pack.toml). Browse what is installed, grouped by type: [`docs/installed/`](../installed/README.md). Decision logs: [performance.md](performance.md), [utility.md](utility.md), [storage.md](storage.md), [nether.md](nether.md), [worldgen.md](worldgen.md), [content.md](content.md). Config notes: [configs.md](configs.md). Distribution: [distribution.md](distribution.md). Pack-owned compatibility fixes: [standalone patch repository](https://github.com/TinorNoah/Lead-and-Leylines-Patches#current-fixes). Not-yet-added candidates and remaining Forge mods: [deferred.md](deferred.md).

First 1.21.1 NeoForge wave: performance and client smoothness. Second wave: Extra/culling/Create/FTB Quests/Pipez.

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
| AllTheLeaks | `alltheleaks-1.1.13+1.21.1-neoforge.jar` | CurseForge 1091339 / 8943912 | both | stability | Leak patches. | none | defaults | 2026-09-17 |
| Cupboard | `cupboard-1.21.1-4.2.jar` | CurseForge 326652 / 8889050 | both | library | Fast Async World Save dependency, plus Chunk Sending, Leaky, Login Protection, Loot Integrations, Clickable Advancements, Structure Essentials. | none | defaults | 2026-09-17 |
| BadOptimizations | `BadOptimizations-2.4.1-1.21.1.jar` | CurseForge 949555 / 7338300 | client | renderer | Client skip work. | none | defaults | 2026-09-17 |
| Dynamic FPS | `dynamic-fps-3.11.4+minecraft-1.21.0-neoforge.jar` | CurseForge 335493 / 7546938 | client | client QoL | Lowers FPS when unfocused. | none | defaults | 2026-09-17 |
| Crash Assistant | `CrashAssistant-neoforge-1.20.6-1.21.4-1.11.12.jar` | CurseForge 1154099 / 8636685 | client | stability | Crash dump helper (client-only). | none | defaults | 2026-09-17 |
| Entity Culling | `entityculling-neoforge-1.11.2-mc1.21.1.jar` | CurseForge 448233 / 8942303 | client | renderer | Occlusion culling. | none | defaults | 2026-09-17 |
| Sodium Extra | `sodium-extra-neoforge-0.9.4+mc1.21.1.jar` | CurseForge 447673 / 8892306 | client | renderer | Official Sodium extras (fog, particles, FPS overlay). Not Chloride. | Sodium (client) | See [configs.md](configs.md) if leaves stack with More Culling | 2026-09-18 |
| Flerovium | `flerovium-neoforge-1.21.1-1.2.0-all.jar` | CurseForge 1142875 / 8978392 | client | renderer | Item/entity/particle draw. Not Better Block Entities. | Sodium (client) | defaults | 2026-09-18 |
| AsyncParticles | `AsyncParticles-21.1.4.5+1.21.1.jar` | CurseForge 1215753 / 8978234 | client | renderer | Particle thread. Not Particle Core. | none (Cloth optional) | defaults | 2026-09-18 |
| More Culling | `moreculling-neoforge-1.21.1-1.0.10.jar` | CurseForge 630104 / 8833217 | client | renderer | Extra culling next to Entity Culling. | Cloth Config | See [configs.md](configs.md) | 2026-09-18 |
| Cloth Config | `cloth-config-15.0.140-neoforge.jar` | CurseForge 348521 / 5729127 | both | library | More Culling dependency. | none | defaults | 2026-09-18 |
| Structure Layout Optimizer | `structure_layout_optimizer-neoforge-1.0.12.jar` | CurseForge 1087831 / 7439136 | both | worldgen | Jigsaw/NBT structure gen. | Resourceful Config | defaults | 2026-09-18 |
| Resourceful Config | `resourcefulconfig-neoforge-1.21-3.0.11.jar` | CurseForge 714059 / 6467772 | both | library | SLO dependency. | none | defaults | 2026-09-18 |
| Ksyxis | `Ksyxis-1.4.5.jar` | CurseForge 537533 / 8971236 | both | worldgen | Unloads unused spawn chunks. | none | defaults | 2026-09-18 |
| Disconnect Packet Fix | `disconnect-packet-fix-neoforge-2.0.1.jar` | CurseForge 1173964 / 6064142 | both | stability | MC-271325 disconnect packets. | none | defaults | 2026-09-18 |
| quick pack | `quick-pack-neoforge-1.5.1+1.21.1.jar` | CurseForge 1380888 / 9005037 | both | IO | Faster zip pack parse. | none | defaults | 2026-09-18 |
| CrashExploitFixer | `crashexploitfixer-neoforge-2.0.0+1.21.4.jar` | CurseForge 1079896 / 8071070 | both | stability | Server crash-exploit filter; file tags 1.21.1–1.21.4. | none | defaults | 2026-09-18 |
| Async Logger | `asynclogger-2.2.2+1.21.1-neoforge.jar` | CurseForge 1491426 / 8631010 | client | IO | Async log writes. | none | defaults | 2026-09-18 |
| ResourcePackCached | `rpc-1.2.5+1.20.5-1.21.4-neoforge.jar` | CurseForge 1125284 / 7602181 | client | client QoL | Keeps server resource packs across rejoins. | none | defaults | 2026-09-18 |
| Create | `create-1.21.1-6.0.10.jar` | CurseForge 328085 / 7963363 | both | tech | Contraptions and kinetics. | none (Flywheel embedded) | defaults | 2026-09-18 |

| Ametrin API | `ametrin-1.21.1-0.2.4.jar` | CurseForge 670599 / 5608814 | both | library | Required by Block Variants. Pinned 1.21.1; later files are 1.21.11. | none | defaults | 2026-09-22 |
| Block Variants | `block_variants-1.21.1-6.1.1.jar` | CurseForge 481119 / 8581915 | both | content | Extra block variants. World data. | Ametrin | defaults | 2026-09-22 |
| Block Variants - Oh The Biomes We've Gone | `block_variants_bwg-1.21.1-1.0.1.jar` | CurseForge 1503165 / 8705273 | both | content | OTBWG wood variants. World data. | Block Variants, OTBWG | defaults | 2026-09-22 |
| Create Better FPS | `createbetterfps-1.21.1-1.1.5.jar` | CurseForge 1217518 / 8908301 | client | renderer | Create FPS with shader packs. Compatible with Colorwheel. | Create | defaults | 2026-09-18 |
| Create: Threaded Trains | `createthreadedtrains-neoforge-1.21.1-1.0.0.jar` | CurseForge 1381890 / 7208558 | both | optimizer | Train network off the server thread. | Create | See [configs.md](configs.md) | 2026-09-18 |
| Architectury API | `architectury-13.0.11-neoforge.jar` | CurseForge 419699 / 8492726 | both | library | FTB dependency. | none | defaults | 2026-09-18 |
| FTB Library | `ftb-library-neoforge-2101.1.37.jar` | CurseForge 404465 / 9008089 | both | library | FTB Quests/Teams. | Architectury | defaults | 2026-09-18 |
| FTB Teams | `ftb-teams-neoforge-2101.1.11.jar` | CurseForge 404468 / 8724782 | both | utility | Shared quest progress. | FTB Library, Architectury | defaults | 2026-09-18 |
| FTB Quests | `ftb-quests-neoforge-2101.1.36.jar` | CurseForge 289412 / 8885017 | both | quests | Quest book. | FTB Library, FTB Teams, Architectury | defaults | 2026-09-18 |
| FTB Quests Optimizer | `FTBQuestsOptimizer-neoforge-3.2.0-1.21.1.jar` | CurseForge 912469 / 7576461 | both | optimizer | Quest tick cost. | FTB Quests | See [configs.md](configs.md) | 2026-09-18 |
| TxniLib | `txnilib-neoforge-1.0.24-1.21.1.jar` | CurseForge 1104882 / 6533725 | both | library | Cerulean dependency. | none | defaults | 2026-09-18 |
| Cerulean | `cerulean-neoforge-1.0.0-1.21.1.jar` | CurseForge 1204890 / 6489711 | both | optimizer | Advancement checks (Icterine fork). Replaces Achievements Optimizer. | TxniLib | defaults | 2026-09-18 |
| Bye?Pregen! | `byepregen-1.21.1-1.1.2.5.jar` | CurseForge 1567378 / 8918029 | both | worldgen | Chunk-gen MSPT. Incompatible with Noisium (removed). Not operator pregen. | none | defaults | 2026-09-18 |
| The Twilight Forest | `twilightforest-1.21.1-4.8.3345-universal.jar` | CurseForge 227639 / 7797302 | both | dimension | Twilight Forest dimension. World data. | none | defaults | 2026-09-18 |
| The Lost Cities | `lostcities-1.21-8.4.4.jar` | CurseForge 269024 / 8862503 | both | worldgen | City world type / generation. World data. The One Probe optional. | none | defaults | 2026-09-18 |
| Lithostitched | `lithostitched-1.8.0-neoforge-21.1.jar` | CurseForge 936015 / 8944659 | both | worldgen | Required by Regions Unexplored (and Terralith). RU's `in_structure` features are overridden by the pack datapack. Tectonic removed 2026-09-22. | none | defaults | 2026-09-18 |
| TerraBlender (NeoForge) | `TerraBlender-neoforge-1.21.1-4.1.0.8.jar` | CurseForge 940057 / 6054947 | both | worldgen | Biome injection library. Not the Forge project 563928. Region sizes maxed so biome mods do not speckle. | none | `pack/config/terrablender.toml` | 2026-09-18 |
| GeckoLib | `geckolib-neoforge-1.21.1-4.9.3.jar` | CurseForge 388172 / 8893490 | both | library | Required by Oh The Biomes We've Gone, Aquamirae, and Infernal Expansion Redux. | none | defaults | 2026-09-18 |
| CorgiLib | `Corgilib-NeoForge-1.21.1-5.0.0.9.jar` | CurseForge 693313 / 7773534 | both | library | Required by Oh The Biomes We've Gone. | none | defaults | 2026-09-18 |
| Oh The Trees You'll Grow | `Oh-The-Trees-Youll-Grow-neoforge-1.21.1-5.3.2.jar` | CurseForge 962544 / 8096180 | both | worldgen | Required by Oh The Biomes We've Gone. | none | defaults | 2026-09-18 |
| Oh The Biomes We've Gone | `Oh-The-Biomes-Weve-Gone-NeoForge-2.6.0.jar` | CurseForge 1070751 / 8245253 | both | worldgen | Overworld biomes. World data. ARR. WTHIT optional, not added. | TerraBlender, GeckoLib, CorgiLib, Oh The Trees You'll Grow | defaults | 2026-09-18 |
| Regions Unexplored | `regions-unexplored-0.6.2-neoforge-21.1.jar` | CurseForge 659110 / 8419667 | both | worldgen | Overworld biomes. World data. Eight `lithostitched:in_structure` placed features overridden. | Lithostitched | datapack override | 2026-09-18 |
| Global Packs | `globalpacks-neoforge-1.21.1-21.0.6.jar` | CurseForge 317134 / 6634585 | both | utility | Loads the unpacked RU override datapack. ARR. | none | See [configs.md](configs.md) | 2026-09-18 |
| Jade | `Jade-1.21.1-NeoForge-15.10.6.jar` | CurseForge 324717 / 8591319 | both | utility | Block/entity tooltip. | none | defaults | 2026-09-18 |
| Jade Addons (Neo/Forge) | `JadeAddons-1.21.1-NeoForge-6.1.1.jar` | CurseForge 583345 / 8777229 | both | utility | Extra Jade integrations. ARR. | Jade | defaults | 2026-09-18 |
| MekaJadeUpgrades | `mekajadeupgrade-1.3.jar` | CurseForge 1400118 / 7588752 | both | utility | Mekanism upgrade info on Jade. | Jade, Mekanism | defaults | 2026-09-22 |
| Sophisticated Backpacks / Jade | `jade-sophisticated-backpacks-1.21.1-neoforge-1.0.2.jar` | CurseForge 1668275 / 8734110 | client | utility | Backpack contents on Jade. | Jade, Backpacks | defaults | 2026-09-22 |
| TACZ / Jade Compatibility | `tacz-jade-1.21.1-neoforge-1.0.0.jar` | CurseForge 1662986 / 8703158 | client | utility | Gun info on Jade. | Jade, TaCZ | defaults | 2026-09-22 |
| Just Enough Items (JEI) | `jei-1.21.1-neoforge-19.57.0.450.jar` | CurseForge 238222 / 9009406 | both | recipes | Recipe viewer. Replaces EMI + TMRV so Polymorph (≥19.52) and Sophisticated (≥19.32) get a real JEI version. Server side registers the recipe-transfer channel Move Items uses. | MezzConfig | defaults | 2026-09-30 |
| MezzConfig | `mezz_config-1.21.1-neoforge-0.6.5.jar` | CurseForge 1689768 / 8987766 | both | library | Required by current JEI on both sides. | none | defaults | 2026-09-22 |
| AE2 JEI Integration | `ae2jeiintegration-1.2.1.jar` | CurseForge 1074338 / 7727898 | client | recipes | Extra AE2 JEI pages. | JEI, AE2 | defaults | 2026-09-22 |
| Refined Storage - JEI Integration | `refinedstorage-jei-integration-neoforge-1.0.0.jar` | CurseForge 1230497 / 6359014 | client | recipes | RS recipe transfer. 2.0.x is Minecraft 26.1.2. | JEI, RS | defaults | 2026-09-22 |
| Sophisticated JEI Index | `sophisticated_jei_index-1.2.3+1.21.1.jar` | CurseForge 1482785 / 8848988 | client | recipes | Backpack recipe transfer. | JEI, Sophisticated | defaults | 2026-09-22 |
| Smithing Template Viewer | `smithingtemplateviewer-1.0.4.jar` | CurseForge 1133580 / 7452053 | client | recipes | Armor trim preview. 1.1.0 is 26.1.2-only. | JEI | defaults | 2026-09-22 |
| Create JEI Compat | `createjeicompat-1.0.3.jar` | CurseForge 1422344 / 8534122 | client | recipes | Paginated sequenced assembly (7+ steps). | JEI, Create | defaults | 2026-09-22 |
| JEI Stuff | `jeistuff-1.21.1-1.2.1.jar` | CurseForge 978621 / 8938121 | both | recipes | Extra JEI helpers. Required network channels need the jar on dedicated servers. | JEI | defaults | 2026-09-23 |
| JEI QuickCraft | `jei-quickcraft-1.21.1-neoforge-1.1.jar` | CurseForge 1520978 / 9016974 | both | recipes | Craft from JEI using inventory. ARR. Required network channels need the jar on dedicated servers. | JEI | defaults | 2026-09-23 |
| SpectrumJEI | `SpectrumJEI-21.1.11.1+neoforge.jar` | CurseForge 1258607 / 8752438 | client | recipes | Spectrum pages in JEI. | JEI, Spectrum | defaults | 2026-09-22 |
| FTB JEI Extras | `ftb-jei-extras-21.1.7.jar` | CurseForge 1103259 / 6695679 | client | recipes | FTB quest/filter pages in JEI. | JEI, FTB | defaults | 2026-09-22 |
| MekaGenJei | `mekagenjei-1.2.jar` | CurseForge 1347827 / 7224975 | client | recipes | Mekanism Generators JEI pages. | JEI, Mekanism Generators | defaults | 2026-09-22 |
| Just Enough Mekanism Multiblocks | `JustEnoughMekanismMultiblocks-1.21.1-7.22.jar` | CurseForge 898746 / 8999939 | client | recipes | Multiblock overlays in JEI. | JEI, Mekanism | defaults | 2026-09-22 |
| Mekanism: Ponders | `mekanism_ponders-1.0.3-1.21.1.jar` | CurseForge 1448575 / 8007326 | client | recipes | Create ponder scenes for Mekanism. | Create, Mekanism | defaults | 2026-09-22 |
| Just Enough TaCZ | `just_enough_tacz-1.2.0.jar` | CurseForge 1536413 / 8180476 | client | recipes | TaCZ gun recipes in JEI. | JEI, TaCZ, Berezka's library | defaults | 2026-09-22 |
| Just Enough Resources (JER) | `JustEnoughResources-NeoForge-1.21.1-1.6.0.17.jar` | CurseForge 240630 / 6506298 | client | recipes | Ore/mob pages in JEI. Not Fabric 26.x. | JEI | defaults | 2026-09-22 |
| GeckolibBetterFPS | `gbf-1.21.1-1.0.2.jar` | CurseForge 1455983 / 8582640 | client | optimizer | Faster GeckoLib entity rendering. Alpha. | GeckoLib | defaults | 2026-09-18 |
| Terralith | `Terralith_1.21.x_v2.6.2.jar` | CurseForge 513688 / 8222737 | both | worldgen | Overworld biomes. World data. | Lithostitched | `pack/config/terralith.json` terrain slabs off | 2026-09-18 |
| Feature Recycler | `Feature-Recycler-neoforge-2.0.0.jar` | CurseForge 1077985 / 5829420 | both | worldgen | Reorders biome features so Terralith + OTBWG do not crash. ARR. | none | defaults | 2026-09-18 |
| Nullscape | `Nullscape_1.21.x_v1.2.14.jar` | CurseForge 570354 / 7078265 | both | worldgen | End overhaul. World data. | none | defaults | 2026-09-18 |
| YACL | `yet_another_config_lib_v3-3.8.2+1.21.1-neoforge.jar` | CurseForge 667299 / 7437845 | both | library | Required by Structurify. | none | defaults | 2026-09-18 |
| Structurify | `structurify-neoforge-2.0.42+mc1.21.1.jar` | CurseForge 1087551 / 9017330 | both | worldgen | Structure spacing. | YACL | global multiplier 2.0 | 2026-09-18 |
| When Dungeons Arise | `DungeonsArise-1.21.1-2.1.68-release.jar` | CurseForge 442508 / 7150870 | both | worldgen | Extra dungeons. World data. ARR. | none | defaults | 2026-09-18 |
| When Dungeons Arise - Seven Seas | `DungeonsAriseSevenSeas-1.21.x-1.0.4-neoforge.jar` | CurseForge 953637 / 7142896 | both | worldgen | Ocean structures. World data. ARR. | none | defaults | 2026-09-18 |
| Library Ferret | `libraryferret-neoforge-1.21.1-4.0.0.jar` | Modrinth DOB2l4oJ / AKcIMUil | both | library | Required by Awesome Dungeon. ARR. On CurseForge as 522351 / 6118136 but `allowModDistribution = false`, so it is **not** manifest-referenced; embedded from Modrinth instead. | none | defaults | 2026-09-18 |
| Awesome Dungeon | `awesomedungeon-neoforge-1.21.1-3.2.0.jar` | Modrinth ptzsjBKT / 5vFWzKiI | both | worldgen | Extra dungeons. World data. ARR. On CurseForge as 530465 / 6265989 but `allowModDistribution = false`, so it is **not** manifest-referenced; embedded from Modrinth instead. | Library Ferret | defaults | 2026-09-18 |
| YUNG's API (NeoForge) | `YungsApi-1.21.1-NeoForge-5.1.9.jar` | CurseForge 1015100 / 8894736 | both | library | Required by YUNG's structure mods. | none | defaults | 2026-09-18 |
| YUNG's Better Caves | `YungsBetterCaves-1.21.1-NeoForge-3.1.6.jar` | CurseForge 340583 / 8806071 | both | worldgen | Cave overhaul. World data. | YUNG's API | defaults | 2026-09-18 |
| YUNG's Cave Biomes | `YungsCaveBiomes-1.21.1-NeoForge-3.1.1.jar` | CurseForge 1111586 / 6913179 | both | worldgen | Cave biomes. World data. Packwiz tried to pull TerraBlender Forge `563928`; that was removed. Use NeoForge `940057`. | YUNG's API, GeckoLib, TerraBlender NF | defaults | 2026-09-22 |

| Compat API | `compatapi-1.0.3.jar` | CurseForge 1393220 / 7767181 | both | library | Required by Compat Structure. | none | defaults | 2026-09-22 |
| Compat Structure | `compatstructures-1.0.3.jar` | CurseForge 1248133 / 7768220 | both | worldgen | Extra structures. World data. | Compat API | defaults | 2026-09-22 |
| Bad Wither No Cookie - Reloaded | `bwncr-neoforge-1.21.1-3.20.4.jar` | CurseForge 261251 / 8135209 | client | QoL | Mutes wither/dragon/raid music. | none | defaults | 2026-09-22 |
| Ecliptic Seasons | `EclipticSeasons-1.21.1-neoforge-0.15.2.1.jar` | CurseForge 1118306 / 8981801 | both | seasons | Solar-term seasons. World data. ARR. | none | defaults | 2026-09-22 |
| Ecliptic Seasons : Bundles | `EclipticSeasons-Bundles-0.18.1.jar` | CurseForge 1449802 / 8980702 | both | seasons | Crop/datapack seasonal packs. | Ecliptic Seasons | defaults | 2026-09-22 |
| Ecliptic Seasons: MultiMod Patch | `Ecliptic-Seasons-MultiMod-Patch-1.21.1-neoforge-0.32.1.jar` | CurseForge 1316748 / 8813347 | both | seasons | Extra mod seasonal hooks. | Ecliptic Seasons | defaults | 2026-09-22 |
| Serene Seasons API Stub | `ecliptic-seasons-serene-api-bridge-1.21.1-neoforge-10.1.0.3-patch11-1.jar` | CurseForge 1476693 / 8828410 | both | seasons | Lets Serene-Seasons-API mods talk to Ecliptic. Do not add Serene Seasons. | Ecliptic Seasons | defaults | 2026-09-22 |
| SeasonHud | `seasonhud-neoforge-1.21.1-2.0.10.jar` | CurseForge 690971 / 8778897 | client | HUD | Season on HUD / Xaero. | none (ES optional) | defaults | 2026-09-22 |
| YUNG's Better Nether Fortresses | `YungsBetterNetherFortresses-1.21.1-NeoForge-3.1.5.jar` | CurseForge 1015118 / 6606621 | both | worldgen | Fortress overhaul. World data. | YUNG's API | defaults | 2026-09-18 |
| YUNG's Bridges | `YungsBridges-1.21.1-NeoForge-5.1.1.jar` | CurseForge 1015149 / 5812553 | both | worldgen | River bridges. World data. | YUNG's API | defaults | 2026-09-18 |
| Moog's Structure Lib | `MoogsStructureLib-neoforge-1.21.1-3.4.0.jar` | CurseForge 1337167 / 8998912 | both | library | Required by Moog's Mineshafts. | none | defaults | 2026-09-18 |
| MMR - Moog's Mineshafts Reimagined | `MoogsMineshaftsReimagined-1.21-1.0.3.jar` | CurseForge 1570795 / 8312865 | both | worldgen | Mineshaft overhaul. World data. | Moog's Structure Lib | defaults | 2026-09-18 |
| Epic Structures: Villages | `epic-structures-villages-2.0.0.jar` | CurseForge 1308486 / 8830175 | both | worldgen | Village overhaul. World data. ARR. | none | defaults | 2026-09-18 |
| Epic Structures: Witch Huts | `Epic Witch Huts v1.3.1.jar` | CurseForge 1335768 / 8383193 | both | worldgen | Witch hut overhaul. World data. ARR. | none | defaults | 2026-09-18 |
| Epic Structures: Jungle Temples | `Epic Jungle Temples v1.0.2.jar` | CurseForge 1600197 / 8611815 | both | worldgen | Jungle temple overhaul. World data. ARR. | none | defaults | 2026-09-18 |
| Amplified Nether | `Amplified_Nether_26.2_v1.2.16.jar` | CurseForge 552176 / 8425271 | both | worldgen | Taller Nether. World data. | none | defaults | 2026-09-18 |
| Infernal Expansion Redux | `infernalexp-neoforge-1.21.1-0.3.18.jar` | CurseForge 1407992 / 9006065 | both | worldgen | Nether biomes. World data. | Lithostitched, GeckoLib | defaults | 2026-09-18 |
| Countered's Terrain Slabs | `terrain_slabs-neoforge-3.1.2.jar` | CurseForge 1125437 / 8216091 | both | worldgen | Terrain slabs. World data. | Architectury | defaults | 2026-09-18 |
| Fragmentum (NeoForge) | `fragmentum-5.0.0+1.21.1-neoforge.jar` | CurseForge 1123977 / 8921953 | both | library | Required by Aquamirae. | none | defaults | 2026-09-18 |
| Aquamirae | `aquamirae-neoforge-1.21.1-7.2.10.jar` | CurseForge 536254 / 8931374 | both | content | Ocean structures and boss. World data. | GeckoLib, Fragmentum | defaults | 2026-09-18 |
| FastBoot | `fastboot-1.21.x-v1.3neo.jar` | CurseForge 1030285 / 6998687 | client | optimizer | Early-load mixins; skips per-version data conversion on boot. ARR. | none | defaults | 2026-09-18 |
| Fluidium | `fluidium-1.21.1-1.4.0.jar` | CurseForge 1306029 / 7481400 | both | optimizer | Distant fluid ticks delayed (default 32 blocks, 50% skip). Claimed/force-loaded chunks stay full-speed. | Duplicationless | defaults | 2026-09-18 |
| Duplicationless | `duplicationless-1.21.1-1.2.1.jar` | CurseForge 1380105 / 8646414 | both | library | Required by Fluidium (`mandatory=true` `[1.1.5,)`). Not DoesPotatoTick. | none | defaults | 2026-09-18 |
| LC²H [Lost Cities: Multithreaded] | `lc2h-omni-4.2.4-LTS.jar` | CurseForge 1325431 / 8928853 | both | worldgen | Async Lost Cities gen. Omni jar tags 1.21.1 NeoForge. BRSSLA V2.0.0. | Lost Cities, Quantified API | defaults | 2026-09-18 |
| Quantified API | `quantified api-omni-2.2.3.jar` | CurseForge 1397967 / 8830709 | both | library | Required by LC²H (`quantified` `[2.2.2,)`). Omni jar tags 1.21.1 NeoForge. | none | defaults | 2026-09-18 |
| BiomeSpy | `biomespy-neoforge-1.21.1-1.3.3.jar` | CurseForge 1376024 / 7488072 | both | worldgen | Faster `/locate` biome/structure search. No worldgen change. | none | defaults | 2026-09-18 |
| MemGuard | `memguard-1.0.4.jar` | CurseForge 1468440 / 8192435 | both | stability | Lightweight heap-usage log after Create 6 mixin strip. Complements AllTheLeaks. | none | defaults | 2026-09-18 |
| Balm | `balm-neoforge-1.21.1-21.0.66.jar` | CurseForge 531761 / 8969738 | both | library | Waystones, Crafting Tweaks, TrashSlot, Default Options. | none | defaults | 2026-09-18 |
| Iceberg | `Iceberg-1.21.1-neoforge-1.3.2.jar` | CurseForge 520110 / 6423863 | both | library | Equipment Compare, Item Borders. | none | defaults | 2026-09-18 |
| Prism | `Prism-1.21.1-neoforge-1.0.11.jar` | CurseForge 638111 / 6372979 | both | library | Item Borders. | none | defaults | 2026-09-18 |
| Curios API | `curios-neoforge-9.5.1+1.21.1.jar` | CurseForge 309927 / 6529130 | both | library | Elytra Slot (and later Ars). | none | defaults | 2026-09-18 |
| Caelus API | `caelus-neoforge-7.0.1+1.21.1.jar` | CurseForge 308989 / 5694215 | both | library | Elytra Slot. | none | defaults | 2026-09-18 |
| Bookshelf | `bookshelf-neoforge-1.21.1-21.1.81.jar` | CurseForge 228525 / 7606240 | both | library | Botany Pots/Trees. | none | defaults | 2026-09-18 |
| Prickle | `prickle-neoforge-1.21.1-21.1.11.jar` | CurseForge 1023259 / 6961457 | both | library | Botany Pots/Trees. | none | defaults | 2026-09-18 |
| Moonlight Lib | `moonlight-1.21.1-3.7.0-neoforge.jar` | CurseForge 499980 / 8981395 | both | library | Supplementaries, Amendments. | none | defaults | 2026-09-18 |
| SuperMartijn642's Core Lib | `supermartijn642corelib-1.1.24a-neoforge-mc1.21.jar` | CurseForge 454372 / 8943316 | both | library | Trash Cans. | none | defaults | 2026-09-18 |
| SuperMartijn642's Config Lib | `supermartijn642configlib-1.1.8-neoforge-mc1.21.jar` | CurseForge 438332 / 5546996 | both | library | Trash Cans, Durability Tooltip. | none | defaults | 2026-09-18 |
| Titanium | `titanium-1.21-4.0.50.jar` | CurseForge 287342 / 8760562 | both | library | Functional Storage. | none | defaults | 2026-09-18 |
| Cobweb | `cobweb-neoforge-1.21-1.4.0.jar` | CurseForge 968456 / 7186943 | both | library | Harvest with ease. | none | defaults | 2026-09-18 |
| Kotlin for Forge | `kotlinforforge-5.12.0-all.jar` | CurseForge 351264 / 8335665 | both | library | Language provider for AE Additions, Better P2P, and Create Ultimine. | none | defaults | 2026-09-18 |
| Searchables | `Searchables-neoforge-1.21.1-1.0.2.jar` | CurseForge 858542 / 5831692 | client | library | Controlling. | none | defaults | 2026-09-18 |
| Xaero's Minimap | `xaerominimap-neoforge-1.21.1-26.5.0.jar` | CurseForge 263420 / 8849842 | client | map | Minimap. | none | defaults | 2026-09-18 |
| Icon Xaero's | `Icon Xaero's 1.22.zip` | CurseForge 888795 / 7748284 | client | map | Xaero's map icons. | Xaero's Minimap | Global Packs required | 2026-09-23 |
| Enhanced Boss Bars | `[1.6] Enhanced Boss Bars.zip` | CurseForge 580036 / 8240430 | client | HUD | Boss bar textures. ARR; CurseForge metadata. | none | Global Packs required | 2026-09-23 |
| Fresh Animations | `FreshAnimations_v1.10.4.zip` | CurseForge 453763 / 7670377 | client | renderer | Animated mobs. Beta. ARR; CurseForge metadata. | EMF, ETF | Global Packs required | 2026-09-23 |
| Fresh Animations: Extensions | `FA+All_Extensions-v1.8.1.zip` | CurseForge 813608 / 7953813 | client | renderer | Official Fresh Animations extensions. ARR; CurseForge metadata. | Fresh Animations | Global Packs required | 2026-09-23 |
| Darkest Ages Mobs | `Darkest_Ages_Mobs-1.21.1_1.2.1.zip` | CurseForge 1674178 / 8865293 | client | renderer | Medieval mob look. | EMF, ETF | Global Packs required | 2026-09-23 |
| Darkest Ages Mobs + Fresh Animations | `Darkest_Ages_Mobs+FA-1.21.1_1.2.1.zip` | CurseForge 1691922 / 8865151 | client | renderer | Compat so both mob packs apply. | Fresh Animations, Darkest Ages | Global Packs required | 2026-09-23 |
| Xaero's World Map | `xaeroworldmap-neoforge-1.21.1-1.46.0.jar` | CurseForge 317780 / 8849973 | client | map | World map. | none | defaults | 2026-09-18 |
| Nature's Compass | `NaturesCompass-1.21.1-3.4.0-neoforge.jar` | CurseForge 252848 / 7892954 | both | utility | Locate biomes. | none | defaults | 2026-09-18 |
| Explorer's Compass | `ExplorersCompass-1.21.1-3.4.0-neoforge.jar` | CurseForge 491794 / 7892943 | both | utility | Locate structures. | none | defaults | 2026-09-18 |
| Waystones | `waystones-neoforge-1.21.1-21.1.46.jar` | CurseForge 245755 / 8969751 | both | utility | Teleport stones. World data. | Balm | defaults | 2026-09-18 |
| AppleSkin | `appleskin-neoforge-mc1.21-3.0.9.jar` | CurseForge 248787 / 7854442 | both | QoL | Hunger/saturation HUD. | none | defaults | 2026-09-18 |
| Mouse Tweaks | `MouseTweaks-neoforge-mc1.21-2.26.1.jar` | CurseForge 60089 / 5637846 | client | QoL | Inventory drag-transfer. | none | defaults | 2026-09-18 |
| ETF | `entity_texture_features-7.2.4-1.21-neoforge.jar` | CurseForge 568563 / 8908931 | client | renderer | Entity texture variants. | none | defaults | 2026-09-18 |
| EMF | `entity_model_features-3.3.9-1.21-neoforge.jar` | CurseForge 844662 / 8909425 | client | renderer | Entity model variants. | ETF | defaults | 2026-09-18 |
| Athena | `athena-neoforge-1.21.1-4.0.6.jar` | CurseForge 841890 / 8061947 | both | library | Connected textures. Chipped. | none | defaults | 2026-09-18 |
| Crafting Tweaks | `craftingtweaks-neoforge-1.21.1-21.1.11.jar` | CurseForge 233071 / 8697050 | both | QoL | Crafting grid buttons. | Balm | defaults | 2026-09-18 |
| Controlling | `Controlling-neoforge-1.21.1-19.0.5.jar` | CurseForge 250398 / 6368976 | client | QoL | Keybind search. | Searchables | defaults | 2026-09-18 |
| Harvest with ease | `harvest-with-ease-neoforge-1.21-9.4.0.jar` | CurseForge 602171 / 5968872 | both | QoL | Right-click harvest. | Cobweb | defaults | 2026-09-18 |
| Clean Swing Through Grass | `cleanswing-1.10-1.21.jar` | CurseForge 915308 / 8746293 | both | QoL | Swing through plants. | none | defaults | 2026-09-18 |
| Cosmetic Armor Reworked | `cosmeticarmorreworked-1.21.1-v1-neoforge.jar` | CurseForge 237307 / 5610814 | both | QoL | Cosmetic armor slots. | none | defaults | 2026-09-18 |
| Elytra Slot | `elytraslot-neoforge-9.0.2+1.21.1.jar` | CurseForge 317716 / 5778461 | both | QoL | Elytra in Curios. | Curios, Caelus | defaults | 2026-09-18 |
| Durability Tooltip | `durabilitytooltip-1.2.0-neoforge-mc1.21.jar` | CurseForge 511040 / 8830219 | client | QoL | Durability numbers. | SuperMartijn642 Config | defaults | 2026-09-18 |
| Equipment Compare | `EquipmentCompare-1.21.1-neoforge-1.3.13.jar` | CurseForge 502561 / 6375501 | client | QoL | Shift-compare gear. | Iceberg | defaults | 2026-09-18 |
| Item Borders | `ItemBorders-1.21-neoforge-1.2.5.jar` | CurseForge 513769 / 5591010 | client | QoL | Rarity item borders. | Iceberg, Prism | defaults | 2026-09-18 |
| Tooltip Overhaul | `tooltipoverhaul-neoforge-1.21.1-2.0.6.jar` | CurseForge 1327508 / 8980608 | client | QoL | Item tooltip frames by type, mod, and rarity. | none | `custom_frames.json` | 2026-09-23 |
| Tag Tooltips | `tagtooltips-neoforge-1.21.1-1.2.0.jar` | CurseForge 899941 / 6418051 | client | QoL | Hold semicolon to list item tags inside the tooltip. | none | defaults | 2026-09-23 |
| Colorful Hearts | `colorfulhearts-neoforge-1.21.1-10.5.9.jar` | CurseForge 854213 / 6830399 | client | QoL | Colored heart rows. | none | defaults | 2026-09-18 |
| Better Advancements | `BetterAdvancements-NeoForge-1.21.1-0.4.3.21.jar` | CurseForge 272515 / 5850587 | client | QoL | Advancement GUI. | none | defaults | 2026-09-18 |
| Clickable advancements | `clickadv-1.21-3.8.jar` | CurseForge 511733 / 5551404 | both | QoL | Click toast to open advancement. | none | defaults | 2026-09-18 |
| Toast Control | `ToastControl-1.21.1-9.0.1.jar` | CurseForge 271740 / 6751464 | client | QoL | Toast spam filter. | Placebo | defaults | 2026-09-18 |
| Default Options | `defaultoptions-neoforge-1.21.1-21.1.8.jar` | CurseForge 232131 / 8498229 | client | QoL | Pack default options. | Balm | defaults | 2026-09-18 |
| Login Protection | `logprot-1.21.1-3.6.jar` | CurseForge 358304 / 8824987 | both | QoL | Invuln after join. | none | defaults | 2026-09-18 |
| Packet Fixer | `packetfixer-3.3.1-1.20.5-1.21.X-merged.jar` | CurseForge 689467 / 7221528 | both | stability | Oversized packets. Not Disconnect Packet Fix. | none | defaults | 2026-09-18 |
| Too Fast | `toofast-1.21.0-0.4.3.6.jar` | CurseForge 550678 / 6819714 | both | QoL | Movement packet speed. | none | defaults | 2026-09-18 |
| Accelerated Decay | `accelerated-decay-neoforge-21.0.0.jar` | CurseForge 699872 / 5433036 | both | QoL | Faster leaf decay. | none | defaults | 2026-09-18 |
| WITS | `wits-neoforge-1.3.1.jar` | CurseForge 909375 / 8412915 | both | utility | Structure name overlay. | none | defaults | 2026-09-18 |
| Lootr | `lootr-neoforge-1.21.1-1.11.38.127.jar` | CurseForge 361276 / 8968561 | both | utility | Per-player loot chests. World data. | none | defaults | 2026-09-18 |
| Polymorph | `polymorph-neoforge-1.2.0+1.21.1.jar` | CurseForge 388800 / 8849478 | both | recipes | Duplicate recipe picker. | none | defaults | 2026-09-18 |
| Almost Unified | `almostunified-neoforge-1.21.1-1.4.2.jar` | CurseForge 633823 / 8127603 | both | recipes | Ore unification. | none | defaults | 2026-09-18 |
| ATO - All the Ores | `alltheores-3.2.0_neoforge_1.21.1.jar` | CurseForge 405593 / 7825464 | both | worldgen | Extra ores. World data. | none | defaults | 2026-09-18 |
| Supplementaries | `supplementaries-1.21.1-3.9.9-neoforge.jar` | CurseForge 412082 / 8852720 | both | content | Decor and utility blocks. World data. | Moonlight | defaults | 2026-09-18 |
| Amendments | `amendments-1.21-2.1.10-neoforge.jar` | CurseForge 896746 / 8825641 | both | content | Vanilla block tweaks. World data. | Moonlight | defaults | 2026-09-18 |
| NeoAuth | `NeoAuth-1.21.1-1.0.1.jar` | CurseForge 1140741 / 7069504 | client | auth | Microsoft auth helper. | none | defaults | 2026-09-18 |
| Better Compatibility Checker | `better-compatability-checker-neoforge-21.1.8.jar` | CurseForge 551894 / 7404415 | both | utility | Join-time modlist check. | none | defaults | 2026-09-18 |
| Crash Utilities | `crashutilities-9.0.4.jar` | CurseForge 371813 / 5993450 | both | stability | Extra crash helpers. | none | defaults | 2026-09-18 |
| Sophisticated Core | `sophisticatedcore-1.21.1-1.5.2.2343.jar` | CurseForge 618298 / 8985869 | both | library | Sophisticated storage/backpacks. | none | defaults | 2026-09-18 |
| Sophisticated Backpacks | `sophisticatedbackpacks-1.21.1-3.26.6.2174.jar` | CurseForge 422301 / 9008234 | both | storage | Backpacks. World data. | Sophisticated Core | defaults | 2026-09-18 |
| Sophisticated Storage | `sophisticatedstorage-1.21.1-1.6.0.2136.jar` | CurseForge 619320 / 8985962 | both | storage | Barrels/chests. World data. | Sophisticated Core | defaults | 2026-09-18 |
| Functional Storage | `functionalstorage-1.21.1-1.5.8.jar` | CurseForge 556861 / 8459097 | both | storage | Drawers. World data. | Titanium | defaults | 2026-09-18 |
| Botany Pots | `botanypots-neoforge-1.21.1-21.1.44.jar` | CurseForge 353928 / 8243851 | both | farming | Crop pots. World data. | Bookshelf, Prickle | defaults | 2026-09-18 |
| Botany Trees | `botanytrees-neoforge-1.21.1-21.1.7.jar` | CurseForge 411357 / 8188485 | both | farming | Tree pots. World data. | Bookshelf, Prickle | defaults | 2026-09-18 |
| Trash Cans | `trashcans-1.1.1-neoforge-mc1.21.jar` | CurseForge 394535 / 8972358 | both | storage | Trash blocks. World data. | SuperMartijn642 Core + Config | defaults | 2026-09-18 |
| TrashSlot | `trashslot-neoforge-1.21.1-21.1.11.jar` | CurseForge 235577 / 8163135 | both | QoL | Inventory trash slot. | Balm | defaults | 2026-09-18 |
| Packing Tape | `PackingTape-1.21.1-0.15.6.jar` | CurseForge 238659 / 6667874 | both | storage | Pickup tile entities. | none | defaults | 2026-09-18 |
| FTB Chunks | `ftb-chunks-neoforge-2101.1.22.jar` | CurseForge 314906 / 8791113 | both | utility | Chunk claims. World data. ARR. | FTB Library, Architectury | defaults | 2026-09-18 |
| FTB Essentials | `ftb-essentials-neoforge-2101.1.10.jar` | CurseForge 410811 / 8442866 | both | utility | `/home` and related commands. ARR. | FTB Library | defaults | 2026-09-18 |
| FTB Ultimine | `ftb-ultimine-neoforge-2101.1.15.jar` | CurseForge 386134 / 8231400 | both | utility | Vein mine. ARR. | FTB Library | defaults | 2026-09-18 |
| FTB Filter System | `ftb-filter-system-neoforge-21.1.4.jar` | CurseForge 943925 / 7429011 | both | library | Item filters. ARR. | FTB Library | defaults | 2026-09-18 |
| FTB XMod Compat | `ftb-xmod-compat-neoforge-21.1.12.jar` | CurseForge 889915 / 8909889 | both | utility | FTB cross-mod hooks. ARR. | FTB Library | defaults | 2026-09-18 |
| Create Ultimine | `createultimine-1.21.1-neoforge-1.3.2.jar` | CurseForge 1231381 / 8086425 | both | optimizer | Create-aware vein mine. | Create | defaults | 2026-09-18 |
| Create: Sky Village | `create_sky_village-0.0.38 NeoForge 1.21.1.jar` | CurseForge 1104939 / 8004708 | both | worldgen | Create village structure. World data. | Create | defaults | 2026-09-18 |
| Sophisticated Backpacks Create Integration | `sophisticatedbackpackscreateintegration-1.21.1-0.2.1.171.jar` | CurseForge 1238567 / 8985949 | both | storage | Create contraptions + backpacks. | Create, Backpacks, Core | defaults | 2026-09-18 |
| Sophisticated Storage Create Integration | `sophisticatedstoragecreateintegration-1.21.1-0.1.21.209.jar` | CurseForge 1226755 / 8503147 | both | storage | Create + storage. | Create, Storage, Core | defaults | 2026-09-18 |

| Sophisticated Backpacks: Ars Compat | `arssophisticatedcompat-0.3.0.jar` | CurseForge 1653477 / 8653384 | both | storage | Ars items in backpacks. | Ars, Backpacks | defaults | 2026-09-22 |
| Sophisticated Storage: Ars Compat | `arssophisticatedstoragecompat-0.3.0.jar` | CurseForge 1653878 / 8655579 | both | storage | Ars items in Sophisticated storage. | Ars, Storage | defaults | 2026-09-22 |
| Sophisticated Tactical Backpacks | `militarybackpack-2.0.1.jar` | CurseForge 1665194 / 8981531 | both | storage | Tactical backpacks + ammo reload. Beta. World data. | Backpacks | defaults | 2026-09-22 |
| Mekanism + Sophisticated Backpacks Compat | `mekanismsophisticatedbackpacks-neoforge-1.21.1-1.0.1+mc1.21.1-neoforge.jar` | CurseForge 1682131 / 8810041 | both | storage | Chemical tanks in backpacks. | Mekanism, Backpacks | defaults | 2026-09-22 |
| Sophisticated Item Actions | `sophisticateditemactions-1.21.1-0.5.16.423.jar` | CurseForge 1419142 / 8820579 | both | storage | Pinned 1.21.1 file, not 1.21.11. | Core | defaults | 2026-09-22 |
| Yukami's Sophisticated Backpack Tab | `yukamibackpacktab-1.21.1-2.2.0-neoforge.jar` | CurseForge 1343253 / 8900066 | client | storage | Backpack tab in inventory. | Backpacks | defaults | 2026-09-22 |
| Sophisticated Inventory Interactions | `sophisticatedinventoryinteractions-1.21.1-0.1.13.218.jar` | CurseForge 1491239 / 8660377 | both | storage | Inventory transfer helpers. | Core | defaults | 2026-09-22 |
| Sophisticated Chest Optimized | `sophisticated_chest_optimized-1.0.1.jar` | CurseForge 1609784 / 8470473 | client | renderer | Pinned NeoForge 1.0.1; later files are Fabric. | Storage | defaults | 2026-09-22 |
| Sophisticated Backpacks RS Bridge | `backpackrs-1.0.0+mc1.21.1-neoforge.jar` | CurseForge 1664334 / 8710301 | both | storage | Quick deposit into RS. | Backpacks, RS | defaults | 2026-09-22 |
| Demagnetizer | `demagnetizer-neoforge-0.2.0-beta.1.jar` | CurseForge 1698500 / 8948717 | both | QoL | Stops item magnet in a radius. Beta. Pinned NeoForge, not Fabric. | none | defaults | 2026-09-22 |
| C2ME | `c2me-neoforge-mc1.21.1-0.4.0-alpha.0.122.jar` | CurseForge 533097 / 8896937 | both | optimizer | Threaded chunk gen/IO. Alpha. ByePregen disables C2ME FluidPostProcessingFilter. OpenCL module not shipped (Java 25). | none | defaults | 2026-09-18 |
| Applied Energistics 2 | `appliedenergistics2-19.2.18.jar` | CurseForge 223794 / 8992605 | both | storage | ME network. World data. | GuideME | defaults | 2026-09-18 |
| GuideME | `guideme-21.1.19.jar` | CurseForge 1173950 / 8897145 | both | library | AE2 guidebook. | none | defaults | 2026-09-18 |
| AE2 Things | `AE2-Things-1.4.2-beta.jar` | CurseForge 609977 / 5637783 | both | storage | AE2 disks. Beta 1.4.2. World data. | AE2, GuideME | defaults | 2026-09-18 |
| Ars Énergistique | `arseng-2.1.1-beta.jar` | CurseForge 905641 / 6203425 | both | magic | Ars + AE2 bridge. Beta. | Ars Nouveau, AE2 | defaults | 2026-09-18 |
| Refined Storage | `refinedstorage-neoforge-2.0.9.jar` | CurseForge 243076 / 8211701 | both | storage | RS 2. World data. | none | defaults | 2026-09-18 |
| Quartz Arsenal | `refinedstorage-quartz-arsenal-neoforge-1.0.8.jar` | CurseForge 1230483 / 8103101 | both | storage | RS wireless crafting grid (replaces RS Addons). | RS | defaults | 2026-09-18 |
| Cable Tiers | `cabletiers-neoforge-1.21.1-0.6.14.jar` | CurseForge 454382 / 8705433 | both | storage | Faster RS cables. | RS | defaults | 2026-09-18 |
| Extra Disks | `ExtraDisks-1.21.1-4.0.15.jar` | CurseForge 351491 / 8031115 | both | storage | Larger RS disks. Beta. | RS | defaults | 2026-09-18 |
| ExtraStorage | `ExtraStorage-1.21.1-5.0.10.jar` | CurseForge 410168 / 8330353 | both | storage | Extra RS storage. | RS, EdivadLib | defaults | 2026-09-18 |
| Farmer's Delight | `FarmersDelight-1.21.1-1.3.4.jar` | CurseForge 398521 / 8765184 | both | farming | Kitchen. World data. | none | defaults | 2026-09-18 |
| Spice of Life: Carrot Edition | `solcarrot-1.21.1-1.16.6.jar` | CurseForge 277616 / 7374098 | both | food | Food diversity. | none | defaults | 2026-09-18 |
| Mekanism | `Mekanism-1.21.1-10.7.19.85.jar` | CurseForge 268560 / 7904058 | both | tech | Machines. World data. | none | defaults | 2026-09-18 |
| Refined Storage - Mekanism Integration | `refinedstorage-mekanism-integration-1.1.1.jar` | CurseForge 1230504 / 7163500 | both | storage | RS chemicals. | RS, Mekanism | defaults | 2026-09-22 |
| Mekanism Extras | `mekanism_extras-1.21.1-1.4.1.jar` | CurseForge 1026040 / 8677677 | both | tech | Extra Mekanism machines. World data. | Mekanism | defaults | 2026-09-22 |
| Patchouli | `Patchouli-1.21.1-93-NEOFORGE.jar` | CurseForge 306770 / 7730942 | both | library | Guidebooks. Required by Mekanism Elements. | none | defaults | 2026-09-23 |
| Mekanism Elements | `MekanismElements-1.21.1-3.0.16-NeoForge.jar` | CurseForge 1103224 / 8839186 | both | tech | Extra element processing. World data. | Mekanism, Patchouli | defaults | 2026-09-22 |
| Ars Nouveau | `ars_nouveau-1.21.1-5.13.2.jar` | CurseForge 401955 / 8993194 | both | magic | Spellcrafting. World data. | none | defaults | 2026-09-18 |
| Ars Elemental | `ars_elemental-1.21.1-0.7.10.3.jar` | CurseForge 561470 / 8999174 | both | magic | Elemental spell addon. | Ars Nouveau | defaults | 2026-09-18 |
| Spectrum | `spectrum-1.12.8-1.21.1-neo.jar` | CurseForge 556967 / 9013018 | both | magic | Progression magic. World data. | Revelationary, Modonomicon, Curios | defaults | 2026-09-18 |
| Complementary Reimagined | `ComplementaryReimagined_r5.9.3.zip` | CurseForge 627557 / 8884654 | client | shader | Matches Euphoria r5.9.3. | Iris | defaults | 2026-09-18 |
| Complementary Unbound | `ComplementaryUnbound_r5.9.3.zip` | CurseForge 385587 / 8884656 | client | shader | Matches Euphoria r5.9.3. | Iris | defaults | 2026-09-18 |
| BSL Shaders | `BSL_v10.1.1.zip` | CurseForge 322506 / 7588844 | client | shader | Latest CF 1.21.1-tagged BSL. | Iris | defaults | 2026-09-18 |
| Euphoria Patches | `EuphoriaPatcher-1.10.5-r5.9.3-neoforge.jar` | CurseForge 915902 / 8884680 | client | shader | Complementary extras. | Colorwheel | defaults | 2026-09-18 |
| Colorwheel | `colorwheel-neoforge-1.3.0+mc1.21.1.jar` | CurseForge 1254143 / 8990905 | client | renderer | Iris shader extras. Beta. | none | defaults | 2026-09-18 |
| Colorwheel Patcher | `colorwheel_patcher-neoforge-1.0.5+mc1.21.1.jar` | CurseForge 1285475 / 7924942 | client | renderer | Colorwheel companion. | Colorwheel | defaults | 2026-09-18 |
| [UNOFFICIAL] TaCZ NeoForge Port | `tacz-neoforge-1.21.1-1.1.8-hotfix-r6.jar` | CurseForge 1353462 / 8547439 | both | combat | Unofficial 1.21.1 TaCZ. World data. Not compatible with 1.20.1 TaCZ worlds. | none | defaults | 2026-09-22 |
| TaCZ Pack Upgrader | `tacz-pack-upgrader-2.1.3.jar` | CurseForge 1353465 / 8387504 | both | combat | Converts 1.20.1 gun packs for this port. | TaCZ | defaults | 2026-09-22 |
| TaCZ addon | `taczaddon-1.1.8.2-neoforge-1.21.1.jar` | CurseForge 1238419 / 8836214 | both | combat | Extra TaCZ features. | TaCZ | defaults | 2026-09-22 |
| [TaCZ] Tactical Breaching | `tactical_breaching-tacz-sbw-neoforge-1.21.1-1.0.5.jar` | CurseForge 1552880 / 9001109 | both | combat | Breaching, glass damage, shells, smoke. | TaCZ | distant-gunshot debug off | 2026-09-22 |
| [TaCZ] Curios For Ammo Box | `curios_for_ammo_box-1.21.1-1.2.0.jar` | CurseForge 1339813 / 8191224 | both | combat | Ammo box curios slot. | TaCZ, Curios | defaults | 2026-09-22 |
| [TaCZ] Applied Ammo Box | `applied_ammo_box-1.21.1-1.2.3-hotfix2.jar` | CurseForge 1338332 / 8618447 | both | combat | AE2 ammo box. | TaCZ, AE2 | defaults | 2026-09-22 |
| Elite X Quality Guns (TACZ) | `Elite x Quality Guns Neoforge v5.1 - 1.21.1.jar` | CurseForge 1084662 / 7952386 | both | combat | Gun pack. | TaCZ | defaults | 2026-09-22 |
| TACZ Turrets | `taczturrets-2.0.0-all.jar` | CurseForge 1376660 / 8834773 | both | combat | Placeable turrets. World data. | TaCZ | defaults | 2026-09-22 |
| Create: TaCZ Unofficial Port | `tacz_c-1.0.2+neoforge.1.21.1.jar` | CurseForge 1542760 / 8087867 | both | combat | Create + TaCZ recipes. | TaCZ, Create | defaults | 2026-09-22 |
| TACZ Bandits | `tacz_bandits-1.3.jar` | CurseForge 1547429 / 8936466 | both | combat | Armed bandit spawns. World data. | TaCZ | defaults | 2026-09-22 |
| TACZ Armed Pillagers | `pillagerguns-neoforge-1.21.1-1.1.0.jar` | CurseForge 1560133 / 8454106 | both | combat | Pillagers with guns. | TaCZ | defaults | 2026-09-22 |
| TACZ Armed Skeletons | `armedskeletons-neoforge-1.21.1-1.0.0.jar` | CurseForge 1653884 / 8655521 | both | combat | Skeletons with guns. | TaCZ | defaults | 2026-09-22 |
| TACZ Armed Piglins | `armedpiglins-neoforge-1.21.1-1.0.0.jar` | CurseForge 1636775 / 8564204 | both | combat | Piglins with guns. | TaCZ | defaults | 2026-09-22 |
| Applied TaCZ | `AppliedTaCZ-1.21.1-19.0.1.jar` | CurseForge 1511859 / 8654367 | both | combat | AE2 + TaCZ. | TaCZ, AE2 | defaults | 2026-09-22 |
| [TaCZ] Refit | `tacz_refit-1.21.1-v005.jar` | CurseForge 1545968 / 8863197 | both | combat | Recipe and stats editor. | TaCZ | defaults | 2026-09-22 |
| EMF Compat: Core | `emf_compat_core_1.21.1_2.0.0.jar` | CurseForge 1605113 / 8793794 | client | library | Required by EMF Compat: TACZ. | EMF | defaults | 2026-09-22 |
| EMF Compat: TACZ | `emf_compat_tacz_1.21.1_1.0.0.jar` | CurseForge 1629329 / 8546543 | client | renderer | TaCZ entity models with EMF. | EMF Compat Core, TaCZ | defaults | 2026-09-22 |
| [TaCZ] Runtime Compat | `taczruntimecompat-1.0.1.jar` | CurseForge 1547520 / 8152341 | both | combat | Runtime gun-pack hooks. | TaCZ | defaults | 2026-09-22 |
| Punchy! | `punchy-2.8c-neoforge-1.21.1.jar` | CurseForge 1374153 / 9004863 | client | renderer | First-person punch anims. Required by Don't Punch My TACZ. Hidden while Epic Fight mode is on. | none | defaults | 2026-09-22 |
| Don't Punch My TACZ | `dont-punch-my-tacz-v0.5.2-1.21.1-neo.jar` | CurseForge 1691793 / 8932034 | client | combat | Pinned NeoForge jar, not Fabric. | TaCZ, Punchy | defaults | 2026-09-22 |
| Epic Fight X Punchy! Neo | `punchy_epicfight_neoforge.jar` | CurseForge 1491729 / 7789794 | client | combat | Hides Punchy first-person arms while Epic Fight mode is active. Client-only. | Punchy, Epic Fight | defaults | 2026-09-23 |
| [UNOFFICIAL] LesRaisins Tactical Equipements | `LesRaisins-Tactical-Equipements-1.21.1-0.4.3.jar` | CurseForge 1432620 / 8745260 | both | combat | Tactical gear pack. | TaCZ | defaults | 2026-09-22 |
| MCS2 gun pack | `MCS2_Gunpack_v1.0.4_AWP_tacz1.1.4_hotfix3.zip` | CurseForge 1113043 / 6083203 | both | combat | CS2-style guns. Zip in `pack/tacz/` for Pack Upgrader. Addon jar 1285238 is 1.20.1-only and does not load. | TaCZ, Pack Upgrader | defaults | 2026-09-23 |
| Daffa's Arsenal | `daffas_arsenal-3.7.1.1.jar` | CurseForge 1254350 / 8862167 | both | combat | 1.20.1 gun pack in `pack/tacz/`. Forge creative-tab classes stay out of `mods/`. World data. | TaCZ, Pack Upgrader | defaults | 2026-09-23 |
| CS+ | `csplus-1.3.1-hotfix2.zip` | CurseForge 1623678 / 8867307 | both | combat | Counter-Strike gun pack. CurseForge file is a 1.20.1 jar; local name is `.zip` so Pack Upgrader reads root `gunpack.meta.json`. World data. | TaCZ, Pack Upgrader | defaults | 2026-09-23 |
| Vic's Point Blank | `pointblank-neoforge-1.21-2.2.0.jar` | CurseForge 961053 / 8855569 | both | combat | Guns beside TaCZ. World data. GeckoLib `[4.9.2,)`. | GeckoLib | defaults | 2026-09-23 |
| Point Blank Extended Edition | `pbext-ext 1.0.zip` | CurseForge 1403532 / 7327102 | both | combat | Official gun pack in `pack/pointblank/`. | Point Blank | defaults | 2026-09-23 |
| Point Blank Gun Gale Pack | `ggo-ext 1.0.zip` | CurseForge 1379446 / 7191282 | both | combat | Official Gun Gale pack in `pack/pointblank/`. | Point Blank | defaults | 2026-09-23 |
| Point Blank Half Life Pack | `halflife-ext v0.8.zip` | CurseForge 1163691 / 8805527 | both | combat | Official Half-Life pack in `pack/pointblank/`. | Point Blank | defaults | 2026-09-23 |
| Cyberpunk 2077 Guns for Vic's Point Blank | `Cyberpunk_2077_Guns_Pack_1.19.zip` | CurseForge 1013546 / 8076165 | both | combat | Community gun pack in `pack/pointblank/`. No third-party distribution. | Point Blank | defaults | 2026-09-23 |
| Berezka's library | `berezka_api-1.2.9.5-fix-neoforge-1.21.1.jar` | CurseForge 1160598 / 8624655 | both | library | Required by Just Enough TaCZ. | none | defaults | 2026-09-22 |
| Resourceful Lib | `resourcefullib-neoforge-1.21-3.0.12.jar` | CurseForge 570073 / 5973188 | both | library | Required by Variants&Ventures. Pinned 1.21.1; later files are 1.21.11. | none | defaults | 2026-09-22 |
| Variants&Ventures | `variantsandventures-neoforge-1.0.28+mc1.21.1.jar` | CurseForge 981139 / 8982592 | both | content | Mob variants. World data. | Resourceful Lib, YACL | defaults | 2026-09-22 |
| Elysium API | `ElysiumAPI-1.21.1-2.0.1.jar` | CurseForge 1158628 / 8707151 | both | library | Required by Jaden's Nether Expansion. | none | defaults | 2026-09-22 |
| Lodestone | `lodestone-1.21.1-1.8.2.jar` | CurseForge 616457 / 7264731 | both | library | Required by Jaden's Nether Expansion. | none | defaults | 2026-09-22 |
| Jaden's Nether Expansion | `Jadens-Nether-Expansion-2.4.1.jar` | CurseForge 1111833 / 8707156 | both | worldgen | Extra Nether biomes/mobs. World data. | Elysium, Lodestone | defaults | 2026-09-22 |
| Jaden's Nether Expansion Delight | `jadensnetherexpansiondelight-1.21.1-1.0.4a-neoforge.jar` | CurseForge 1190275 / 8232964 | both | farming | Delight recipes for Jaden's. | FD, Jaden's | defaults | 2026-09-22 |
| Netherite Tweaks & Fixes | `netherite_tweaks_luna-1.2.2-neoforge-1.21.1.jar` | CurseForge 1239001 / 7282661 | both | QoL | Netherite tweaks. | none | defaults | 2026-09-22 |
| Eternal Nether | `EternalNether-v21.1.3-1.21.1-NeoForge.jar` | CurseForge 1252482 / 6751611 | both | worldgen | Extra Nether structures. World data. | Puzzles Lib | defaults | 2026-09-22 |
| WunderLib: New Dawn | `wunderlib-21.0.10.jar` | CurseForge 1422273 / 7469725 | both | library | BetterNether New Dawn stack. Pinned 21.0.x. | none | defaults | 2026-09-22 |
| WorldWeaver: New Dawn | `worldweaver-21.0.25.jar` | CurseForge 1422284 / 8594162 | both | library | BetterNether New Dawn stack. Pinned 21.0.x. | BCLib New Dawn | defaults | 2026-09-22 |
| BCLib: New Dawn | `bclib-21.0.26.jar` | CurseForge 1422283 / 8608827 | both | library | BetterNether New Dawn stack. Pinned 21.0.x. | none | defaults | 2026-09-22 |
| BetterNether: New Dawn | `BetterNether-21.0.27.jar` | CurseForge 1422293 / 8896389 | both | worldgen | Nether biomes/blocks. World data. | New Dawn libs | defaults | 2026-09-22 |
| Nether Remastered | `nether_remastered-2.6-neoforge-1.21.1.jar` | CurseForge 872516 / 8145295 | both | worldgen | Nether structures. World data. | none | defaults | 2026-09-22 |
| Nether Villager Trader | `nethervillagertrader-2.0.0-neoforge-1.21.1.jar` | CurseForge 989053 / 7154899 | both | QoL | Nether trading. | none | defaults | 2026-09-22 |
| Just-In NETHER | `just_in_nether-1.2.1-neoforge-1.21.1.jar` | CurseForge 1074911 / 8919842 | both | worldgen | Extra Nether content. World data. | none | defaults | 2026-09-22 |
| playerAnimator | `player-animation-lib-forge-2.0.4+1.21.1.jar` | CurseForge 658587 / 7389814 | both | library | Required by Epic Fight. Filename says forge; file tags NeoForge 1.21.1. | none | defaults | 2026-09-22 |
| Epic Fight | `epic-fight-21.17.3.1-mc1.21.1-neoforge.jar` | CurseForge 405076 / 8175609 | both | combat | Souls-like combat. World data. | playerAnimator | defaults | 2026-09-22 |
| AAA Particles | `aaa_particles-neoforge-1.21.1-2.3.1.jar` | CurseForge 979809 / 8995061 | both | combat | Effekseer particle effects. Kept without Nightfall. Architectury embedded. KubeJS optional, not added. | none | defaults | 2026-09-23 |
| Knight Lib | `knightlib-neoforge-1.21.1-2.0.3.jar` | CurseForge 1105855 / 8958408 | both | library | Required by Olympus!. | none | defaults | 2026-09-23 |
| Olympus! | `olympusmythology-neoforge-1.21.1-1.0.9.jar` | CurseForge 1667111 / 8962781 | both | content | Greek artifacts, mobs, and structures. World data. | Curios, Knight Lib | defaults | 2026-09-23 |
| Archaion: Echoes of the Fallen | `archaion-1.21.1-1.4.4.jar` | CurseForge 1620396 / 8983496 | both | content | Ancient Keep, trial spawners, and a boss. World data. ARR. | AAA Particles | defaults | 2026-09-23 |
| Weapons of Miracles | `WeaponsOfMiracles-2.0.178.jar` | CurseForge 918614 / 8829395 | both | combat | Required by EF × Twilight Forest. World data. | Epic Fight | defaults | 2026-09-22 |
| P1nero's Epic Bow | `p1nero_bow-neoforge1.21.1-21.16.1.0-neoforge.jar` | CurseForge 1338443 / 7922741 | both | combat | Required by EF × Twilight Forest. | Epic Fight | defaults | 2026-09-22 |
| Epic Fight × Twilight Forest Compat | `TwilightForestEFCompat-1.1.7-1.21.1-Neoforge.jar` | CurseForge 1555371 / 8968963 | both | combat | TF animations in Epic Fight. | Weapons of Miracles, Epic Bow | defaults | 2026-09-22 |
| Bosses' Rise | `block_factorys_bosses-2.1.2-neo-1.21.1.jar` | CurseForge 1314084 / 8123167 | both | combat | Extra bosses. World data. | GeckoLib | defaults | 2026-09-22 |
| Epic Fight: Curios Compat | `Epic Fight x Curios Compat 2.2.jar` | CurseForge 1389133 / 7865987 | client | combat | Curios slots in Epic Fight. Client-only (loads `ClientCuriosCompat`; crashes dedicated server if `both`). | Epic Fight, Curios | defaults | 2026-09-23 |
| Epic Fight × TacZ First-Person Compat | `epictaczcompat_1.21.1_0.6.0.jar` | CurseForge 1544620 / 8759254 | client | combat | First-person guns with Epic Fight. Forces vanilla mode while a TaCZ gun is held. | Epic Fight, playerAnimator | defaults | 2026-09-22 |
| ParCool! | `ParCool-1.21.1-4.0.0.5.jar` | CurseForge 482378 / 8921237 | both | movement | Parkour. | none | defaults | 2026-09-22 |
| Epic Fight X Parcool | `epicfightxparcool-1.0.0.jar` | CurseForge 1063523 / 8620103 | both | combat | Parkour during Epic Fight. | Epic Fight, ParCool | defaults | 2026-09-22 |
| Epic Fight Client Tweaks | `efct-1.0.7.jar` | CurseForge 968141 / 8620068 | client | combat | Client Epic Fight extras. | Epic Fight | defaults | 2026-09-22 |
| Epic Fight FPS Optimizer | `EpicFight-FPS-Optimizer-1.21.1-NeoForge-v1.0.3.jar` | CurseForge 1619890 / 8876879 | client | renderer | Epic Fight draw cost. | Epic Fight | defaults | 2026-09-22 |
| Epic Fight Progressive Difficulty | `efprogressivediff-1.2.2.jar` | CurseForge 1465641 / 8733763 | both | combat | Scales Epic Fight difficulty. | Epic Fight | defaults | 2026-09-22 |
| CompatLink | `compatlink-neoforge-1.3.0.jar` | CurseForge 1607536 / 8872766 | both | combat | Epic Fight weapon bridges. | none | defaults | 2026-09-22 |
| Jupiter | `jupiter-2.3.7-1.21.1-neoforge.jar` | CurseForge 1072905 / 7738312 | both | library | Required by Ice and Fire CE. | none | defaults | 2026-09-22 |
| Uranus | `uranus-3.0-beta.1.jar` | CurseForge 1010827 / 8682870 | both | library | Required by Ice and Fire CE. Beta. | none | defaults | 2026-09-22 |
| IceAndFire Community Edition | `iceandfire-2.1.3.jar` | CurseForge 1040076 / 8929517 | both | content | Dragons. World data. Required so Ice and Fire × Epic Fight does anything. | Jupiter, Uranus | no worldgen skeletons; fire dragons in the Nether | 2026-09-22 |
| Ice and Fire X Epic Fight | `iceandfire-ce-epicfight-armor-compat-1.0.0.jar` | CurseForge 1634414 / 8552314 | both | combat | IAF armor animations. | Ice and Fire CE, Epic Fight | defaults | 2026-09-22 |
| ParCool+ Compatibility++ | `ParCool-CompatibilityAddon-1.21.1-3.4.3.3-1.2.1.jar` | CurseForge 1501234 / 8824743 | both | movement | Extra ParCool compat. | ParCool | defaults | 2026-09-22 |
| Epitaphs | `epitaphs-2.2.0_neoforge_1.21.1.jar` | CurseForge 1325482 / 8741091 | both | utility | Player-locked graves. World data. | none | defaults | 2026-09-24 |
| AE2: Crafting Tree | `ae2ct-1.21.1-1.1.1.jar` | CurseForge 1086241 / 7182163 | both | storage | AE2 craft tree. | AE2 | defaults | 2026-09-24 |
| Schematic Energistics | `schematicenergistics-1.21.1-1.5.4a.jar` | CurseForge 1283481 / 8465295 | both | storage | Schematicannon pulls from AE2. World data. | AE2, Create | defaults | 2026-09-24 |
| AE2 MEGA Things | `AE2MEGAThings-1.21.1-2.0.4.jar` | CurseForge 1150075 / 6203833 | both | storage | Untyped mega disks, including chemicals. World data. | AE2 Things, MEGA Cells, Applied Mekanistics optional | defaults | 2026-09-24 |
| Not Enough Patterns | `nep-1.21.1-0.5.1.jar` | CurseForge 1624304 / 8724404 | both | storage | AE2 pattern providers on other machines. | AE2 | defaults | 2026-09-24 |
| Infinity Drives | `infinitystorage-1.21.1-1.0.1.jar` | CurseForge 1386843 / 7238406 | both | storage | Infinite water, lava, and cobblestone. World data. | none | defaults | 2026-09-24 |
| AE2 Utility | `ae2utility-1.8.0.jar` | CurseForge 1521605 / 8973751 | both | storage | Pull from the ME network into machines; one-click patterns. | AE2, JEI (client) | defaults | 2026-09-24 |
| AE2 Universal Press | `ae_universal_press-2.1.1-neoforge-1.21.1.jar` | CurseForge 1222746 / 8306511 | both | storage | One press for every processor. World data. | AE2 | defaults | 2026-09-24 |
| Akashic Tome | `AkashicTome-1.8-30.jar` | CurseForge 250577 / 7773841 | both | utility | One book that holds other books. | none | defaults | 2026-09-24 |
| CreativeCore | `CreativeCore_NEOFORGE_v2.13.50_mc1.21.1.jar` | CurseForge 257814 / 9009568 | both | library | Required by AmbientSounds. | none | defaults | 2026-09-24 |
| AmbientSounds 6 | `AmbientSounds_NEOFORGE_v6.3.8_mc1.21.1.jar` | CurseForge 254284 / 8043019 | both | utility | Ambient audio. | CreativeCore | defaults | 2026-09-24 |
| Ars Controle | `ars_controle-1.21.1-1.6.16.jar` | CurseForge 1061812 / 8847869 | both | magic | Extra Ars spell control. World data. | Ars Nouveau, Curios | defaults | 2026-09-24 |
| Ars Elemancy | `ars_elemancy-1.21.1-1.18.3.jar` | CurseForge 1153666 / 8349780 | both | magic | Dual-element Ars Elemental gear. World data. | Ars Nouveau, Ars Elemental | defaults | 2026-09-24 |
| Ars Nouveau's Flavors & Delight | `arsdelight-2.2.2.jar` | CurseForge 1131668 / 8297420 | both | farming | Ars foods. World data. | Ars Nouveau, Farmer's Delight | defaults | 2026-09-24 |
| Ars Technica | `ars_technica-1.21.1-2.7.6.jar` | CurseForge 1096161 / 7642730 | both | magic | Create glyphs and tools beside Ars Creo. World data. | Ars Nouveau, Create | defaults | 2026-09-24 |
| Artifacts | `artifacts-neoforge-13.2.5.jar` | CurseForge 312353 / 8791899 | both | content | Exploration curios. World data. | Curios (optional integration) | defaults | 2026-09-24 |
| AttributeFix | `attributefix-neoforge-1.21.1-21.1.3.jar` | CurseForge 280510 / 7115922 | both | utility | Attribute id fixes. | Bookshelf, Prickle | defaults | 2026-09-24 |
| Autochef's Delight | `AutochefsDelight-1.21.1-NeoForge-2.0.3.jar` | CurseForge 964282 / 8013519 | both | farming | Automated Farmer's Delight cooking. World data. ARR. | Farmer's Delight | defaults | 2026-09-24 |
| Barbeque's Delight | `barbequesdelight-1.3.0.jar` | CurseForge 1007788 / 8004721 | both | farming | Grill foods. World data. | Farmer's Delight | defaults | 2026-09-24 |
| Better Modlist | `better_modlist-21.1.1.jar` | CurseForge 1089803 / 8605756 | client | utility | Mods screen. Client. | none | defaults | 2026-09-24 |
| Bridging Mod | `BridgingMod-2.6.2+1.21.1.neoforge-release.jar` | CurseForge 533942 / 6269728 | client | utility | Bridge assist. | YACL | defaults | 2026-09-24 |
| Building Gadgets | `buildinggadgets2-1.3.9.jar` | CurseForge 298187 / 6850515 | both | utility | Copy, paste, and build gadgets. World data. | none | defaults | 2026-09-24 |
| Client Tweaks | `clienttweaks-neoforge-1.21.1-21.1.15.jar` | CurseForge 251407 / 8696976 | both | utility | Client annoyance toggles. Required on the server. ARR. | Balm | defaults | 2026-09-24 |
| Comforts | `comforts-neoforge-9.0.5+1.21.1.jar` | CurseForge 276951 / 7515858 | both | utility | Sleeping bags and hammocks. World data. | none | defaults | 2026-09-24 |
| Create Crafts & Additions | `createaddition-1.7.1.jar` | CurseForge 439890 / 8887653 | both | tech | Forge energy and Create kinetics. World data. | Create | defaults | 2026-09-24 |
| Create Deco | `createdeco-2.1.3.jar` | CurseForge 509285 / 7943181 | both | tech | Create decoration blocks. World data. | Create | defaults | 2026-09-24 |
| Create Encased | `Create Encased-1.21.1-1.9.0-ht3.jar` | CurseForge 829380 / 8549840 | both | tech | Encased Create blocks. World data. | Create | defaults | 2026-09-24 |
| Crystalix | `crystalix-3.0.1.jar` | CurseForge 1187033 / 8767589 | both | content | Colored glass. World data. | none | defaults | 2026-09-24 |
| FDLib | `fdlib-1.0.9-1.21.1.jar` | CurseForge 1271749 / 7844741 | both | library | Required by Qliphoth Awakening. | none | defaults | 2026-09-24 |
| CERBON's API | `CerbonsAPI-NeoForge-1.21-1.3.0.jar` | CurseForge 955605 / 6483943 | both | library | Required by Bosses of Mass Destruction. | none | defaults | 2026-09-24 |
| Teal Lib | `teallib-1.3.teal.jar` | CurseForge 1597849 / 8507094 | both | library | Required by Spawn. | none | defaults | 2026-09-24 |
| Iron's Lib | `irons_lib-1.21.1-2.2.0.jar` | CurseForge 1492763 / 8973642 | both | library | Required by Iron's Spells 3.16.3. | none | defaults | 2026-09-24 |
| Ace's Spell Utils | `aces_spell_utils-1.2.7.2-1.21.1.jar` | CurseForge 1299492 / 8789930 | both | library | Required by Twilight spellbooks. | Iron's Spells | defaults | 2026-09-24 |
| AzureLib | `azurelib-neo-1.21.1-3.1.13.jar` | CurseForge 817423 / 8986133 | both | library | Required by Twilight spellbooks at runtime. Not declared in that mod's metadata. | none | defaults | 2026-09-24 |
| Illager Arena | `illager_arena-1.0.1-neoforge-1.21.1.jar` | CurseForge 1358983 / 7077445 | both | content | Desert illager structure. World data. | none | defaults | 2026-09-24 |
| Qliphoth Awakening | `fdbosses-3.2-1.21.1.jar` | CurseForge 1271707 / 8373639 | both | content | Boss fights. World data. ARR. | FDLib | defaults | 2026-09-24 |
| Bosses of Mass Destruction | `BOMD-NeoForge-1.21-1.3.3.jar` | CurseForge 941573 / 8448640 | both | content | Boss fights. World data. LGPL. | CERBON's API, GeckoLib, Cloth Config | defaults | 2026-09-24 |
| Spawn | `spawn-4.0.8-1.21.1.jar` | CurseForge 935694 / 8881073 | both | content | Extra mobs. World data. ARR. | Teal Lib | defaults | 2026-09-24 |
| Critters and Companions | `crittersandcompanions-neoforge-1.21.1-2.7.0.jar` | CurseForge 574913 / 8646976 | both | content | Pets. World data. ARR. | Architectury, GeckoLib. YACL on the client. | defaults | 2026-09-24 |
| Companions! | `companions-neoforge-1.21.1-1.3.5.jar` | CurseForge 1300341 / 8962932 | both | content | Pets. World data. GPL-3.0. | Knight Lib | defaults | 2026-09-24 |
| Armageddon | `Armageddon for NeoForge 1.21.1 (v3.2.0) - Polished.jar` | CurseForge 1110642 / 8854138 | both | content | Horror mobs. World data. | GeckoLib. Curios optional. | model-name aliases in `global_packs/required_resources/lead-leylines-armageddon-models/` | 2026-09-24 |
| Armageddon Tooltips | `armageddontooltips-1.0.0.jar` | CurseForge 1627435 / 8519061 | both | utility | Armageddon tool-tier labels. | none | defaults | 2026-09-24 |
| Born in Chaos | `born_in_chaos_[Neoforge]_1.21.1_1.7.6.jar` | CurseForge 686437 / 8268280 | both | content | Apocalypse mobs. World data. ARR. | none. GeckoLib optional. | defaults | 2026-09-24 |
| Born In Configuration | `borninconfiguration-3.2.2.jar` | CurseForge 1019091 / 8122961 | both | utility | Born in Chaos config. MIT. | Born in Chaos | defaults | 2026-09-24 |
| Born in Chaos Jade compat | `infected_ore_info-1.1.0.jar` | CurseForge 1510842 / 8700301 | both | utility | Jade shows infected diamond ore as diamond ore. MIT. | Born in Chaos, Jade | defaults | 2026-09-24 |
| Iron's Spells 'n Spellbooks | `irons_spellbooks-1.21.1-3.16.3.jar` | CurseForge 855414 / 8680204 | both | magic | Spellbooks beside Ars Nouveau. World data. ARR. Pin this file; the Create addon accepts only 3.16.x. | Iron's Lib, GeckoLib, playerAnimator, Curios | defaults | 2026-09-24 |
| Spellbooks of Twilight | `twilight_spellbooks-0.0.4.jar` | CurseForge 1683668 / 9014615 | both | magic | Twilight Forest spells for Iron's Spells. ARR. Metadata does not declare the parents. | Ace's Spell Utils, AzureLib. Twilight Forest and Iron's Spells are in. | defaults | 2026-09-24 |
| Iron's Spells Create Additions | `ISS-Create-Additions-2.18.0-battery-network-fix.jar` | CurseForge 1698578 / 8985084 | both | magic | Create spell tools. MIT. Matches Create 6.0.10 and NeoForge 21.1.250. | Iron's Spells 3.16.3, Create | defaults | 2026-09-24 |
| Farmer's Spell 'n Spell Book | `farmers-spell-n-spellbook-1.0.6.0-1.21.1.jar` | CurseForge 1631240 / 9008722 | both | magic | Farmer's Delight spells. ARR. | Farmer's Delight, Iron's Spells, GeckoLib | defaults | 2026-09-24 |

| Apothic Attributes | `ApothicAttributes-1.21.1-2.11.0.jar` | CurseForge 898963 / 9006294 | both | library | Required by Apotheosis 8.8.0. | Placebo | defaults | 2026-09-25 |
| Apotheosis | `Apotheosis-1.21.1-8.8.0.jar` | CurseForge 313970 / 8826922 | both | magic | Affixes, gems, and gear. World data. MIT code, ARR assets. CurseForge metadata. | Apothic Attributes, Placebo | defaults | 2026-09-25 |
| Apothic Enchanting | `ApothicEnchanting-1.21.1-1.6.2.jar` | CurseForge 1063926 / 8797650 | both | magic | Enchanting overhaul. World data. | Apothic Attributes, Placebo | defaults | 2026-09-25 |
| Apothic Spawners | `ApothicSpawners-1.21.1-1.4.0.jar` | CurseForge 986583 / 8469405 | both | magic | Movable spawners. World data. | Placebo | defaults | 2026-09-25 |
| Apotheosis x Iron's Spellbooks | `irons_apothic-2.2.5.jar` | CurseForge 1244863 / 8968087 | both | magic | Apotheosis gear for Iron's Spells. | Apotheosis, Iron's Spells | defaults | 2026-09-25 |
| Apotheosis x Point Blank | `apothic-pointblank-1.2.0.jar` | CurseForge 1600496 / 8534962 | both | combat | Affixes and gems on Point Blank guns. | Apotheosis, Apothic Enchanting, Point Blank | defaults | 2026-09-25 |
| Apotheosis Modern Ragnarok: Zero | `apotheosis_modern_ragnarok-neoforge-1.21.1-tacz1.1.8-7.0.1.jar` | CurseForge 966582 / 8483829 | both | combat | Affixes on TaCZ guns. GPL-3.0. | Apotheosis, Gunsmith Lib, TaCZ | defaults | 2026-09-25 |
| Gunsmith Lib | `gunsmithlib-neoforge-1.21.1-tacz1.1.8-6.4.4.jar` | CurseForge 1264058 / 8799282 | both | library | Required by Ragnarok Zero. Matches TaCZ 1.1.8. | TaCZ | defaults | 2026-09-25 |
| Create: Apokinetics | `apokinetics-1.0.6.jar` | CurseForge 1606442 / 8790422 | both | tech | Apotheosis on Create machines. | Apotheosis, Create 6.0.10 | defaults | 2026-09-25 |
| Create: Metalwork | `createmetalwork-neoforge-1.21.1-3.0.0.jar` | CurseForge 966104 / 8995820 | both | tech | Extra Create metal blocks and parts. | Create | defaults | 2026-09-26 |
| Apothic Compats | `apothic_compats-0.2.4.3.jar` | CurseForge 1188699 / 8936047 | both | magic | Apotheosis datapack compat. | Apotheosis, Placebo | defaults | 2026-09-25 |
| Fallen Gems & Affixes | `fallen_gems_affixes-1.21.1-1.0.0.jar` | CurseForge 1286177 / 6927716 | both | magic | Extra gems and affixes. World data. | Apotheosis, Additional Attributes, Patchouli | defaults | 2026-09-25 |
| Additional Attributes | `additional_attributes-1.21.1-1.2.2.jar` | CurseForge 986624 / 6388896 | both | library | Required by Fallen Gems. | none | defaults | 2026-09-25 |
| Apotheosis No Flight | `apotheosisnoflight-1.21.1-1.0.0.jar` | CurseForge 1612036 / 8529729 | both | magic | Turns off Apotheosis flight potions and charms. | Apotheosis, Apothic Attributes | defaults | 2026-09-25 |
| Apotheosis Balance Configurator | `apotheosis_balance-1.21.1-2.1.0.jar` | CurseForge 1379530 / 8210944 | both | magic | Affix numbers live in a config. Do not also add Apothic Nerf. | Apotheosis, Apothic Attributes | defaults | 2026-09-25 |
| Apothic Tooltip Cleanup | `apothic_tooltip_cleanup-1.3.0.jar` | CurseForge 1536956 / 8270836 | client | QoL | Shortens affix and gem lines. Tooltip Overhaul stays the frame. | Apotheosis | defaults | 2026-09-25 |
| Epic Fight x Iron's Spells | `efiscompat-2.6.0-neoforge-1.21.1-port.jar` | CurseForge 1476569 / 7704805 | both | combat | Spell animations in Epic Fight. GPL-3.0. | Epic Fight, Iron's Spells | defaults | 2026-09-25 |
| Puzzles Lib | `puzzleslib-v21.1.62-mc1.21.1+neoforge.jar` | CurseForge 495476 / 9007719 | both | library | Required by Eternal Nether, Mutant Monsters, and Illager Invasion. | none | defaults | 2026-09-22 |
| Mutant Monsters | `MutantMonsters-v21.1.1-1.21.1-NeoForge.jar` | CurseForge 852665 / 7232511 | both | content | Mutant mobs, some boss-tier. World data. AGPL-3.0-or-later. | Puzzles Lib | defaults | 2026-09-25 |
| Illager Invasion | `IllagerInvasion-v21.1.6-1.21.1-NeoForge.jar` | CurseForge 891324 / 6492670 | both | content | Illager expansion port. World data. MIT. Extensible Enums is embedded. | Puzzles Lib | defaults | 2026-09-25 |
| Mowzie's Mobs | `mowziesmobs-1.21.1-1.8.2.jar` | CurseForge 250498 / 7760267 | both | content | Overworld bosses. World data. Custom license; credit the CurseForge page. | GeckoLib | defaults | 2026-09-25 |
| Myths & Legends | `mythsandlegends-1.0.7.jar` | CurseForge 1133244 / 8922514 | both | content | Folklore mobs and structures. World data. ARR. | GeckoLib, Curios | defaults | 2026-09-25 |
| Unusual End | `unusualend-2.3.1b.jar` | CurseForge 617757 / 8856390 | both | content | End expansion. World data. ARR. | Blueprint | defaults | 2026-09-25 |
| Blueprint | `blueprint-1.21.1-8.2.0.jar` | CurseForge 382216 / 8819375 | both | library | Required by Unusual End. | none | defaults | 2026-09-25 |
| Forbidden and Arcanus | `forbidden_arcanus-2.6.1.jar` | CurseForge 309858 / 6875895 | both | magic | Magic content. World data. ARR. | Valhelsia Core | defaults | 2026-09-25 |
| Valhelsia Core | `valhelsia_core-neoforge-1.21.1-1.1.5.jar` | CurseForge 416935 / 6296775 | both | library | Required by Forbidden and Arcanus. | none | defaults | 2026-09-25 |
| Pam's HarvestCraft 2 - Food Core | `pamhc2foodcore-NEOFORGE-1.21.1-1.0.4.jar` | CurseForge 372534 / 6919485 | both | farming | Extra foods. ARR. CurseForge metadata. | none | defaults | 2026-09-25 |
| Pam's HarvestCraft 2 - Crops | `pamhc2crops-NEOFORGE-1.21.1-1.0.9.jar` | CurseForge 361385 / 8064883 | both | farming | Garden bushes. World data. ARR. | none | defaults | 2026-09-25 |
| Pam's HarvestCraft 2 - Trees | `pamhc2trees-NEOFORGE-1.21.1-1.0.9.jar` | CurseForge 365460 / 7847533 | both | farming | Fruit trees. World data. ARR. | none | defaults | 2026-09-25 |
| Pam's HarvestCraft 2 - Food Extended | `pamhc2foodextended-NEOFORGE-1.21.1-1.0.0.jar` | CurseForge 402231 / 6221521 | both | farming | Foods that use the crops and trees. ARR. | Crops and Trees (page requirement; jar does not declare them) | defaults | 2026-09-25 |
| Loot Integrations | `lootintegrations-1.21.1-4.7.jar` | CurseForge 580689 / 6640970 | both | content | Mixes structure loot tables. | Cupboard | defaults | 2026-09-25 |
| Dungeon Now Loading | `dungeonnowloading-neoforge-1.21.1-2.11.5.jar` | CurseForge 1585912 / 8948129 | both | worldgen | Unofficial 1.21.1 port. World data. C0-1.0. | none | defaults | 2026-09-25 |
| Ars Nouveau Refresh | `Ars Nouveau Refresh 1.2.0.zip` | CurseForge 1080571 / 6068071 | client | resource pack | Ars item textures. | Ars Nouveau | Global Packs required | 2026-09-24 |
| Better Sophisticated Backpack Upgrades | `Better SB Upgrades.zip` | CurseForge 1138140 / 7964810 | client | resource pack | Backpack upgrade icons. | Sophisticated Backpacks | Global Packs required | 2026-09-24 |
| Boss Refreshed | `boss-refreshed-v2-1.19-1.21.zip` | CurseForge 882133 / 6597394 | client | resource pack | Dragon, wither, warden, and elder guardian models. EMF. | EMF | Global Packs required | 2026-09-24 |
| Enchantment Descriptions | `enchdesc-neoforge-1.21.1-21.1.11.jar` | CurseForge 250419 / 8693034 | client | QoL | Enchantment lines on item tooltips. LGPL-2.1. | Bookshelf, Prickle | Apothic inline descriptions on | 2026-09-25 |
| Fusion (Connected Textures) | `fusion-1.3.15b-neoforge-mc1.21.1.jar` | CurseForge 854949 / 8942891 | client | renderer | Connected textures for resource packs. ARR. Continuity stays out. | none | defaults | 2026-09-25 |
| Fusion 3D Items | `Fusion 3D Items v1.0.1 for Minecraft 1.20-1.21.8.zip` | CurseForge 1315462 / 7051086 | client | resource pack | 3D item models. ARR. | Fusion | Global Packs required | 2026-09-25 |
| Fusion Connected Glass | `Fusion Connected Glass v1.0.1 for Minecraft 1.20-1.21.8.zip` | CurseForge 1315459 / 7051090 | client | resource pack | Connecting glass. ARR. Crystalix stays colored glass. | Fusion | Global Packs required | 2026-09-25 |
| Handcrafted | `handcrafted-neoforge-1.21.1-4.0.3.jar` | CurseForge 538214 / 6330030 | both | content | Furniture. World data. Terrarium Licence. | Resourceful Lib | defaults | 2026-09-25 |
| Chipped | `chipped-neoforge-1.21.1-4.0.2.jar` | CurseForge 456956 / 5813117 | both | content | Block variants. World data. ARR. | Resourceful Lib, Athena | defaults | 2026-09-25 |
| Macaw's Doors | `mcw-doors-1.1.5-mc1.21.1neoforge.jar` | CurseForge 378646 / 7618651 | both | content | Extra doors. World data. MIT. | none | defaults | 2026-09-25 |
| Macaw's Windows | `mcw-mcwwindows-2.4.2-mc1.21.1neoforge.jar` | CurseForge 363569 / 7317672 | both | content | Windows and curtains. World data. ARR. | none | defaults | 2026-09-25 |
| Macaw's Fences and Walls | `mcw-mcwfences-1.2.1-mc1.21.1neoforge.jar` | CurseForge 453925 / 7308338 | both | content | Fences, walls, and gates. World data. MIT. | none | defaults | 2026-09-25 |
| Macaw's Furniture | `mcw-furniture-3.4.1-mc1.21.1neoforge.jar` | CurseForge 359540 / 7255584 | both | content | Furniture. World data. ARR. Supplementaries and Handcrafted stay. | none | defaults | 2026-09-25 |
| Visual Workbench | `VisualWorkbench-v21.1.2-1.21.1-NeoForge.jar` | CurseForge 500273 / 8793655 | both | content | Items stay in crafting tables. World data. MPL-2.0. | Puzzles Lib | defaults | 2026-09-25 |
| Twilight Forest Bosses Resurrection | `tfbr-1.21.1-4.2.2.jar` | CurseForge 916943 / 7382236 | both | content | Respawn TF bosses. World data. | Twilight Forest | defaults | 2026-09-26 |
| Twilight Forest - Dungeons & Villages | `tf_dnv-2.0.3.jar` | CurseForge 1271268 / 6614073 | both | worldgen | TF villages and dungeons. World data. | Twilight Forest (undeclared) | defaults | 2026-09-26 |
| Particle Rain | `particlerain-4.0.0-beta.11+1.21.1-neoforge.jar` | CurseForge 421897 / 8720770 | client | renderer | Weather particles. | none | defaults | 2026-09-26 |
| Fzzy Config | `fzzy_config-0.7.7+1.21+neoforge.jar` | CurseForge 1005914 / 8883390 | both | library | Required by Subtle Effects. Kotlin for Forge already in. | Kotlin for Forge | defaults | 2026-09-26 |
| Subtle Effects | `SubtleEffects-neoforge-1.21.1-1.14.3.jar` | CurseForge 1023913 / 8008312 | client | renderer | Ambient particles and sounds. | Fzzy Config | defaults | 2026-09-26 |
| Loot Journal (NeoForge) | `loot_journal-neoforge-1.21.1-6.2.2.jar` | CurseForge 1120395 / 8922056 | client | QoL | Pickup notifier. | Fragmentum | defaults | 2026-09-26 |
| Beautiful Enchanted Books | `BEB-NeoForge-1.21-6.0.0.jar` | CurseForge 1083202 / 7268159 | client | QoL | Enchanted book textures. | none | defaults | 2026-09-26 |
| Enchant Icons | `enchant icons 1.21 v1.3.zip` | CurseForge 861241 / 5424546 | client | resource pack | Enchantment name icons. | none | Global Packs required | 2026-09-26 |
| BetterF3 | `BetterF3-11.0.3-NeoForge-1.21.1.jar` | CurseForge 401648 / 5873258 | client | QoL | Debug HUD. | Cloth Config | defaults | 2026-09-26 |
| Interdimensional Wireless Transmitter | `interdimensionalwirelesstransmitter-neoforge-1.21.1-0.1.5.jar` | CurseForge 452645 / 6845967 | both | storage | RS wireless across dimensions. World data. | Refined Storage | defaults | 2026-09-26 |
| Fast Item Frames | `FastItemFrames-v21.1.6-1.21.1-NeoForge.jar` | CurseForge 1210171 / 6963018 | both | content | Faster item frames. World data. | Puzzles Lib | defaults | 2026-09-26 |
| Colourful Everywhere | `colourfuleverywhere-1.21-1.3.6.jar` | CurseForge 1684964 / 8824518 | client | QoL | Shader GUI recolor. OptiGUI / Colourful Containers stand-in. MIT. | Cloth Config embedded | defaults | 2026-09-26 |
| BetterEnd: New Dawn | `BetterEnd-21.0.35.jar` | CurseForge 1422294 / 8896285 | both | worldgen | End biomes/mobs. World data. Pinned 21.0.x. | New Dawn libs | defaults | 2026-09-26 |
| YUNG's Better Dungeons (NeoForge) | `YungsBetterDungeons-1.21.1-NeoForge-5.1.4.jar` | CurseForge 1015112 / 5954804 | both | worldgen | Dungeon overhaul. World data. | YUNG's API | defaults | 2026-09-26 |
| YUNG's Better Strongholds (NeoForge) | `YungsBetterStrongholds-1.21.1-NeoForge-5.1.3.jar` | CurseForge 1015105 / 6272264 | both | worldgen | Stronghold overhaul. World data. | YUNG's API | defaults | 2026-09-26 |
| YUNG's Better End Island (NeoForge) | `YungsBetterEndIsland-1.21.1-NeoForge-3.1.2.jar` | CurseForge 1015127 / 6300968 | both | worldgen | Central End island. World data. | YUNG's API | defaults | 2026-09-26 |
| YUNG's Better Ocean Monuments (NeoForge) | `YungsBetterOceanMonuments-1.21.1-NeoForge-4.1.2.jar` | CurseForge 1015115 / 5924487 | both | worldgen | Ocean monument overhaul. World data. | YUNG's API | defaults | 2026-09-26 |
| YUNG's Better Desert Temples (NeoForge) | `YungsBetterDesertTemples-1.21.1-NeoForge-4.1.5.jar` | CurseForge 1015114 / 6276955 | both | worldgen | Desert temple overhaul. World data. | YUNG's API | defaults | 2026-09-26 |
| Luki's Ancient Cities | `lukis-ancient-cities-v1.2.jar` | CurseForge 1190728 / 7179736 | both | worldgen | Ancient city variants. World data. | none | defaults | 2026-09-26 |
| Luki's Woodland Mansions | `lukis-woodland-mansions-v1.0-1.21-1.21.4.jar` | CurseForge 1385782 / 7227735 | both | worldgen | Woodland mansion variants. World data. | none | defaults | 2026-09-26 |
| DarkLoot datapack | `pack/global_packs/required_data/darkloot/` | CurseForge 1446380 (vendored) | both | datapack | Buffed mob loot and heads. Edit entity JSON in-repo. pack_format 48. | none | force via Global Packs | 2026-09-26 |
| Rhino | `rhino-2101.2.8-build.91.jar` | CurseForge 416294 / 8463898 | both | library | JavaScript runtime for KubeJS. | none | defaults | 2026-09-26 |
| KubeJS | `kubejs-neoforge-2101.7.2-build.368.jar` | CurseForge 238086 / 8083208 | both | scripting | Recipe and event scripts. Pinned: newer 7.2 builds require Better Advanced Tooltips. | Rhino | defaults | 2026-09-26 |
| KubeJS Iron's Spells | `irons_spells_js-4.0.3.jar` | CurseForge 980834 / 7234865 | both | magic | Spell scripting. File is from 2025-11; Iron's Spells stays pinned at 3.16.3. | KubeJS, Iron's Spells | defaults | 2026-09-26 |
| KubeJS Mekanism | `kubejs-mekanism-neoforge-2101.1.7-build.18.jar` | CurseForge 418651 / 7213666 | both | tech | Mekanism scripting. Beta file. | KubeJS, Mekanism | defaults | 2026-09-26 |
| LootJS | `lootjs-neoforge-1.21.1-3.7.0.jar` | CurseForge 570630 / 8009262 | both | scripting | Loot scripts. | KubeJS | defaults | 2026-09-26 |
| Load My F***ing Tags | `lmft-1.1.1+1.21.9-neoforge.jar` | CurseForge 656346 / 7084444 | both | stability | One bad tag entry does not wipe the tag. Wide-version jar that lists 1.21.1. | none | defaults | 2026-09-26 |
| libIPN | `libIPN-neoforge-1.21.1-6.6.3.jar` | CurseForge 679177 / 7810552 | client | library | Inventory Profiles Next GUI library. | Kotlin for Forge | defaults | 2026-09-26 |
| Inventory Profiles Next | `InventoryProfilesNext-neoforge-1.21.1-2.2.5.jar` | CurseForge 495267 / 7810574 | client | QoL | Sort, locked slots, gear sets. AGPL-3.0-or-later. | libIPN, Kotlin for Forge | defaults | 2026-09-26 |
| More Mouse Tweaks | `moremousetweaks-neoforge-1.1.1+1.21.1.jar` | CurseForge 1134081 / 6958493 | client | QoL | Extra mouse inventory moves. | Mouse Tweaks, Cloth Config | defaults | 2026-09-26 |
| Extreme Sound Muffler | `ExtremeSoundMuffler-3.56_NeoForge-1.21.jar` | CurseForge 363363 / 7895926 | client | QoL | Per-sound muffler. | none | defaults | 2026-09-26 |
| MRU | `mru-1.0.41+1.21.1-neoforge.jar` | CurseForge 669659 / 9004036 | client | library | Sounds dependency. ARR. | none | defaults | 2026-09-26 |
| Sounds | `sounds-2.4.22+lts+1.21.1-neoforge.jar` | CurseForge 925889 / 7325254 | client | QoL | Extra sound effects. CurseForge also lists Fabric API; that dependency does not resolve on this loader and was not installed. | MRU, YACL | defaults | 2026-09-26 |
| Sound Physics Remastered | `sound-physics-remastered-neoforge-1.21.1-1.5.1.jar` | CurseForge 535489 / 7032247 | client | QoL | Reverb and occlusion. Alpha file. | none (Cloth Config optional, already in) | defaults | 2026-09-26 |
| Glassential Renewed | `Glassential-renewed-1.21.1-3.4.7.jar` | CurseForge 945149 / 8871444 | both | building | Extra glass. World data. | Fusion (already in). FastPipes and Lampicus optional, not added | defaults | 2026-09-26 |
| Measurements | `Measurements-neoforge-1.21.1-3.0.3.jar` | CurseForge 478559 / 6956811 | both | QoL | Tape measure. | none | defaults | 2026-09-26 |
| Mining Gadgets | `mininggadgets-1.18.8.jar` | CurseForge 351748 / 8860674 | both | tools | Laser mining. World data. Create Ultimine and FTB Ultimine stay. | none | defaults | 2026-09-26 |
| Multi Builder Tool | `MultiBuilderTool-1.21.1-1.1.29.jar` | CurseForge 827020 / 8797925 | both | tools | One-click multiblocks. | none. Optional parents not in the pack were not added | defaults | 2026-09-26 |
| Tesseract API | `tesseract-api-neoforge-1.12.16-1.21.1.jar` | CurseForge 1067672 / 8708086 | both | library | Little Big Redstone dependency. | none (Modern Industrialization optional) | defaults | 2026-09-26 |
| Little Big Redstone | `little-big-redstone-1.9.11-1.21.1.jar` | CurseForge 1180560 / 8796357 | both | tech | Compact redstone. World data. | Tesseract API, GuideME | defaults | 2026-09-26 |
| OpenBlocks Elevator | `elevatorid-neoforge-1.21.1-1.11.4.jar` | CurseForge 250832 / 6199696 | both | transport | Floor elevator blocks. World data. | none | defaults | 2026-09-26 |
| Modular Routers | `modular-routers-13.2.7+mc1.21.1.jar` | CurseForge 250294 / 8478801 | both | logistics | Programmable routers beside Modern Dynamics / XNet. World data. | none | defaults | 2026-09-26 |
| Mekanistic Routers | `mekanisticrouters-1.2.0.jar` | CurseForge 1148201 / 7511369 | both | logistics | Mekanism modules for Modular Routers. | Modular Routers, Mekanism | defaults | 2026-09-26 |
| ME Requester | `merequester-neoforge-1.21.1-1.5.0.jar` | CurseForge 688367 / 8787722 | both | storage | Stock-keeping for AE2. World data. | AE2. Wireless Terminals optional and already in | defaults | 2026-09-26 |
| Mekanism Curios | `mekanismcurios-1.21.1-1.2.1.jar` | CurseForge 1251061 / 6602973 | both | tech | Portable QIO on a Curios slot. | Mekanism, Curios | defaults | 2026-09-26 |
| Not Enough Glyphs | `not_enough_glyphs-1.21.1-4.6.2.jar` | CurseForge 1023517 / 8880291 | both | magic | Extra Ars glyphs. World data. SauceLib embedded. | Ars Nouveau | defaults | 2026-09-26 |
| OctoLib | `OctoLib-NEOFORGE-0.6.2+1.21.jar` | CurseForge 916747 / 8040848 | both | library | Not Enough Recipe Book dependency. | Architectury | defaults | 2026-09-26 |
| Not Enough Recipe Book | `Not Enough Recipe Book-NEOFORGE-0.4.3+1.21.jar` | CurseForge 738663 / 6880047 | both | QoL | Removes the vanilla recipe book. JEI stays. | Architectury, OctoLib | defaults | 2026-09-26 |
| Observable | `observable-5.4.4.jar` | CurseForge 509575 / 6697124 | both | profiler | In-game lag profiler. | Kotlin for Forge, Architectury | defaults | 2026-09-26 |
| Loot Integrations: When Dungeons Arise | `lootintegration_wda-1.8.jar` | CurseForge 1142880 / 7925521 | both | content | Modded loot in When Dungeons Arise chests. | Loot Integrations, When Dungeons Arise | defaults | 2026-09-26 |
| Atlas API | `atlas_api-1.21.1-1.2.0.jar` | CurseForge 1145462 / 6880789 | both | library | Iron's Jewelry dependency. | none | defaults | 2026-09-26 |
| Iron's Gems 'n Jewelry | `irons_jewelry-1.21.1-2.0.2.jar` | CurseForge 1101111 / 8365016 | both | magic | Wearable gems. World data. Apotheosis gems stay. | Curios, Iron's Lib, Atlas API | defaults | 2026-09-26 |
| Neo Vitae | — | — | — | magic | Removed 2026-09-26 (demon dungeon / world data). BMAddon removed with it. | — | — | 2026-09-26 |
| Just Dire Things | `justdirethings-1.5.7.jar` | CurseForge 1002348 / 7463040 | both | tech | Automation blocks and tools. World data. Newer files are Minecraft 26.1 only. | none | defaults | 2026-09-26 |
| Modern Industrialization | `Modern-Industrialization-2.5.8.jar` | CurseForge 405388 / 8863289 | both | tech | Separate factory tech tree beside Create and Mekanism. World data. GrandPower embedded. | GuideME | defaults | 2026-09-26 |
| Modern Industrial Routers | `modernindustrialrouters-2.1.1.jar` | CurseForge 1012297 / 7674083 | both | logistics | Router upgrades for Modern Industrialization energy. Metadata lists no dependencies. | Modular Routers, Modern Industrialization | defaults | 2026-09-26 |
| Lead and Leylines Patches | `leylines-patches-0.1.0.jar` | Project-owned prerelease (`patches-v0.1.0`; [artifact and source](https://github.com/TinorNoah/Lead-and-Leylines-Patches/releases/tag/patches-v0.1.0)) | both | stability | Pack-side fix for the MI 2.5.8 × Weapons of Miracles null enchantment-lookup crash affecting steam drills and diesel tools. See the [source and regression ledger](https://github.com/TinorNoah/Lead-and-Leylines-Patches#current-fixes). | Minecraft / NeoForge; Modern Industrialization 2.5.8 (exact) | pack-owned Mixin fix | 2026-09-30 |

World-data: Create, Modern Dynamics, XNet, FTB Quests/Chunks, Twilight Forest, Lost Cities, Regions Unexplored, Oh The Biomes We've Gone, Terralith, Nullscape, BetterEnd New Dawn, dungeon/structure mods (including YUNG Better Dungeons/Strongholds/End Island/Ocean Monuments/Desert Temples and Luki ancient cities/mansions, Awesome Dungeon and its Ocean and End editions, and Epic Structures Villages/Jungle Temples/Witch Huts/Dungeons/Igloo), Amplified Nether, Infernal Expansion Redux, BetterNether New Dawn, Jaden's Nether, Eternal Nether, Nether Remastered, Cave Biomes, Compat Structure, Terrain Slabs, Aquamirae, Archaion, Olympus!, Waystones, Lootr, ATO, Supplementaries, Amendments, Sophisticated/Functional storage, Botany, Trash Cans, Create Sky Village, AE2, Refined Storage (plus Interdimensional Wireless Transmitter), Mekanism (plus Extras/Elements/Covers), Ars Nouveau, Farmer's Delight cluster, Alchemistry, Spectrum, TaCZ, Vic's Point Blank, Epic Fight, Ice and Fire CE, Variants&Ventures, Block Variants, Ecliptic Seasons, Crystalix, Create Deco, Create Encased, Create Crafts & Additions, Epitaphs, Comforts, Artifacts, Ars Controle, Ars Elemancy, Ars Technica, Ars Flavors, Autochef's Delight, Barbeque's Delight, Building Gadgets, Infinity Drives, Schematic Energistics, AE2 MEGA Things, Illager Arena, Qliphoth Awakening, Bosses of Mass Destruction, Spawn, Critters and Companions, Companions, Armageddon, Born in Chaos, Iron's Spells and its spell addons, Apotheosis (enchanting, spawners, and Fallen Gems), Mutant Monsters, Illager Invasion, Mowzie's Mobs, Myths & Legends, Unusual End, Forbidden and Arcanus, Pam's HarvestCraft 2, Dungeon Now Loading, Chipped, Handcrafted, Macaw's Doors, Macaw's Windows, Macaw's Fences and Walls, Macaw's Furniture, Macaw's Lights and Lamps, Macaw's Stairs, Additional Lights, FramedBlocks, MmmMmmMmmMmm, Visual Workbench, Fast Item Frames, Twilight Forest Bosses Resurrection / Dungeons & Villages, Glassential Renewed, Iron's Gems 'n Jewelry, Little Big Redstone, Modular Routers, Mekanistic Routers, Modern Industrial Routers, Mining Gadgets, ME Requester, OpenBlocks Elevator, Just Dire Things, Modern Industrialization, Not Enough Glyphs, and the Oritech family (Oritech plus Oritech Things and Applied Oritech — adding ores, the `oritech:oil` fluid, reactor multiblock frames, bedrock resource nodes, oil springs, uranium patches, and the Amethyst Fish) write blocks/items/dimensions/terrain/biomes/season state. Those are not a clean uninstall. New world required for the 1.21.1 cutover. Removing Tectonic does not rewrite already-generated chunks.


## 2026-09-26 logistics and Create factory wave

Removed Pipez + Pipez Lag Fix. Added Modern Dynamics, XNet (+ McJtyLib, RFTools Base), Simple Conveyor Belts, Rechiseled (+ Chipped/Create/AE2), Mob Grinding Utils (+ Vanillafied pack), Inventory Essentials, Better Advanced Tooltips, Construction Sticks (+ Applied), DimStorage, Flux Networks, Charging Gadgets, Recipe Essentials, MI Extended/Solar/Structure Viewer, BuffMobs, Agritech Evolved, Tempad, Jade Sable Compat, KubeJS Additions/Create/Botany Pots/Ponder, Create Dragons Plus, and the approved Create factory wave (Enchantment Industry, Central Kitchen, New Age, Bells & Whistles, Big Cannons + Adv Tech + RPL, Connected, Ore Excavation, Diesel Generators, Aquatic Ambitions, TFMG, Dynamic Village, Enchantable Machinery, Alloyed, Integrated Farming, Applied Kinetics, Nuclear, Metalwork, Shimmer, Wizardry, Fast SchematicCannon, Blaze Burner Fuels). Dropped MI Extentended Integrations (crashes MI 2.5.8 on missing `iv` casing). Skipped Ixeris, Nolijium, Create Copper & Zinc. Catalog regenerated; see `docs/installed/catalog.toml`.

## 2026-09-30 update wave

Updated 29 mods to their latest 1.21.1 NeoForge builds. Apotheosis was deliberately **held at 8.8.0**: 8.9.0 changed `GemCaseTile.upgradeGem`/`getUpgradeMatch` to drop their trailing `net.minecraft.world.Container` parameter, and Apokinetics 1.0.6 (`apokinetics-1.0.6.jar`, newest build, declares `apotheosis [8.5.3,)` so version checks do not catch it) mixins the old 3-arg signature. The mixin fails hard at mod construction and no dedicated-server or client boot completes. Apothic Compats and irons_apothic were reverted alongside Apotheosis so the trio stays on one Apotheosis version; both declare open ranges (`[8.0.1,)` and `[8.6.0,)`) but 0.2.5.5 was compiled against 8.9.0. Revisit when Apokinetics ships a build matching 8.9.0's signature, or if the pack drops Apokinetics. Also held: nothing else. NeoForge `21.1.251`/`21.1.252` were identified but not applied in this change.

## 2026-10-01 structure, loot, and client-comfort wave

Came from a user-supplied candidate list of 69 CurseForge IDs. All 69 were matched to their real projects first, which corrected four earlier misreadings: CurseForge 470193 "Connectivity" is **someaddon's network/login-timeout mod**, not the connected-textures mod the pack's policy bans (that is a different project); `someaddon` is the author of Loot Integrations and Smooth Chunk Save, both already shipped; FlickerFix is a night-vision flicker fix, not a renderer extra; and Overgeared is a vanilla tool/armor forging overhaul. 6 entries were already installed, 2 have no 1.21.1 NeoForge build, 7 are policy-blocked, and the rest need per-mod research before install. Installed in this wave are the natural completions of mods already in the pack, plus small self-contained additions.

| Mod | Pinned file | Source | `side` | Category | Why | Required deps | Config | Date added |
|---|---|---|---|---|---|---|---|---|
| Awesome Dungeon Ocean | `awesomedungeonocean-neoforge-1.21.1-3.3.0.jar` | Modrinth hn56Bq5n / 4oZY86TA | both | worldgen | Ocean dungeons for the installed Awesome Dungeon. World data. ARR. On CurseForge as 533528 / 7033605 but `allowModDistribution = false`, so it is **not** manifest-referenced; embedded from Modrinth instead, like Awesome Dungeon and Library Ferret. | Awesome Dungeon, Library Ferret | defaults | 2026-10-01 |
| Awesome Dungeon The End | `awesomedungeonend-neoforge-1.21.1-3.1.1.jar` | CurseForge 537531 / 7061818 | both | worldgen | Dungeon set in the End. World data. ARR. CurseForge distribution is allowed for this edition. | Awesome Dungeon, Library Ferret | defaults | 2026-10-01 |
| Epic Structures: Dungeons | `epic-structures-dungeons-1.2.5.jar` | CurseForge 1501318 / 8837503 | both | worldgen | Dungeons of varying rarity, same author as the installed Villages/Jungle Temples/Witch Huts. World data. ARR. | none | defaults | 2026-10-01 |
| Epic Structures: Igloo | `epic-structures-igloo-1.0.5 1.21+ 26+.jar` | CurseForge 1511498 / 8528158 | both | worldgen | Igloos, same author. World data. ARR. | none | defaults | 2026-10-01 |
| Loot Integrations: Awesome Dungeon | `lootintegrations_awesome-1.7.jar` | CurseForge 1129961 / 8920888 | both | content | Modded loot in Awesome Dungeon chests. ARR. | Loot Integrations, Awesome Dungeon | defaults | 2026-10-01 |
| Loot Integrations: Born in Chaos | `lootintegrations_borninchaos-1.1.jar` | CurseForge 1420691 / 8922017 | both | content | Modded loot in Born in Chaos chests. ARR. | Loot Integrations, Born in Chaos | defaults | 2026-10-01 |
| Loot Integrations: Ice and Fire | `lootintegrations_iceandfire-1.3.jar` | CurseForge 1272782 / 8914945 | both | content | Modded loot in Ice and Fire chests and boss drops. ARR. | Loot Integrations, Ice and Fire | defaults | 2026-10-01 |
| Loot Integrations: Randomized Loot Compatibility | `lootintegrations_vanilla-1.8.jar` | CurseForge 1128055 / 8913166 | both | content | Modded loot in vanilla chests. ARR. | Loot Integrations | defaults | 2026-10-01 |
| Yung Structures Addon for Loot Integrations | `lootintegrations_yungs-1.6.jar` | CurseForge 1012211 / 8323152 | both | content | Modded loot in YUNG's structure chests. ARR. | Loot Integrations, YUNG's API | defaults | 2026-10-01 |
| Yggdrasils | `Yggdrasil-6.0.0.jar` | CurseForge 1135665 / 7658653 | both | worldgen | Very large Norse dungeon structure set (451 `.nbt` pieces in one `yggdrasil` namespace). Verified against the jar: it ships **no** dimension, biome, or worldgen overrides for any other namespace, so it does not touch the End island or clash with BetterEnd: New Dawn, Nullscape, Unusual End, or YUNG's Better End Island. Placement is `random_spread` spacing 45 / separation 35 / frequency 0.75, which is sparser than a vanilla pillager outpost even with the pack's Structurify 2.0 spacing. Generated by DatapackConverter (`LicenseRef-Datapack`), no mixins. World data. | none | defaults | 2026-10-01 |
| Loot Integrations: Yggdrasils | `lootintegrations_yggdrasils-1.3.jar` | CurseForge 1269854 / 8920687 | both | content | Modded loot in Yggdrasils chests. ARR. Yggdrasils' own 323 loot tables reference only `minecraft:`, so this addon is what makes them modded. | Loot Integrations, Yggdrasils | defaults | 2026-10-01 |
| Macaw's Lights and Lamps | `mcw-lights-1.1.5-mc1.21.1neoforge.jar` | CurseForge 502372 / 7304075 | both | content | Lamps, torches, and street lights beside the four installed Macaw's mods. World data. ARR. No JEI plugin in-jar. | none | defaults | 2026-10-01 |
| Macaw's Stairs | `mcw-mcwstairs-1.0.2-mc1.21.1neoforge.jar` | CurseForge 1119394 / 7317479 | both | content | Stairs, handrails, and balconies. World data. ARR. No JEI plugin in-jar. | none | defaults | 2026-10-01 |
| Additional Lights | `additional_lights-neoforge-1.21-2.1.10.jar` | CurseForge 384991 / 6841545 | both | content | Lantern, torch, and lamp variants. World data. MIT. No JEI plugin in-jar, so the new blocks rely on generic JEI pages. | none | defaults | 2026-10-01 |
| FramedBlocks | `FramedBlocks-10.6.2.jar` | CurseForge 441647 / 8780141 | both | content | Picture frames for any block. World data. LGPL-3. Ships its own JEI plugin; optional deps on EMI/REI stay uninstalled. | none | defaults | 2026-10-01 |
| FTB Ranks | `ftb-ranks-neoforge-2101.1.5.jar` | CurseForge 314905 / 8878560 | both | utility | Ranks and permissions, the companion to the installed FTB Teams. ARR. | FTB Library `[2101.1.12,)` (have 2101.1.37), Architectury API `[13.0.6,)` (have 13.0.11) | defaults | 2026-10-01 |
| Fuel Goes Here | `fuelgoeshere-1.21.1-1.2.0.jar` | CurseForge 659090 / 6003423 | both | gameplay | Fuel goes to the fuel slot even when it is also smeltable. ARR. | none | defaults | 2026-10-01 |
| Get It Together, Drops! | `getittogetherdrops-neoforge-1.21.5-1.4.jar` | CurseForge 411045 / 6775278 | both | gameplay | Merge dropped stacks by tag. MIT. | none | defaults | 2026-10-01 |
| Hey Berry! SHUT UP | `heyberryshutup-1.21.0-2.0.4.jar` | CurseForge 634227 / 5517177 | both | gameplay | Villagers stop taking berry bush damage. ARR. | none | defaults | 2026-10-01 |
| Iris & Oculus Search | `IrisSearch-1.8.1-neoforge.jar` | CurseForge 1583035 / 8871534 | client | rendering | Search bar for Iris shader settings. LGPL-3.0. | Iris (client) | defaults | 2026-10-01 |
| KeyBind Bundles | `keybindbundles-1.4.0.jar` | CurseForge 1172594 / 7508312 | client | client QoL | Collapse several keybinds into one. MIT. | none | defaults | 2026-10-01 |
| KeybindsPurger | `KeybindsPurger-1.4.0-neoforge-1.21.1.jar` | CurseForge 1099143 / 7733186 | client | client QoL | Clear conflicting keybinds. MIT. | none | defaults | 2026-10-01 |
| Borderless Window | `borderless-neoforge-1.21.1-1.7.5_1-all.jar` | CurseForge 378979 / 7604034 | client | client QoL | Borderless fullscreen window. MIT. | none | defaults | 2026-10-01 |
| FlickerFix | `flickerfix-1.21.1-6.1.0.jar` | CurseForge 431430 / 7413025 | client | stability | Stops night vision flicker. ARR. | none | defaults | 2026-10-01 |
| Connectivity | `connectivity-1.21.1-7.7.jar` | CurseForge 470193 / 9008904 | both | stability | Fixes login timeouts, decoder exceptions, oversized payloads, and ghostblocks by raising the vanilla network limits through an access transformer. Replaces Packet Fixer and Disconnect Packet Fix. Mixin config is `required: false` with `defaultRequire: 0`, so a lost injection logs instead of crashing. ARR, CurseForge-only distribution. | Cupboard `[1.21-1.4,)` (have 4.2) | defaults | 2026-10-01 |
| Just Enough Threads | `justenoughthreads-0.14.2+1.21.1.jar` | CurseForge 1605658 / 9025858 | client | info / optimizer | Moves JEI's startup indexing off the main thread. 0.14.2 is the build that fixes the JEI 19.57 break: verified in the jar's bytecode, `hasNativeSearchBuilderContract` now also compares the constructor descriptor `(Lmezz/jei/gui/search/ElementPrefixParser;)V`, so on JEI 19.57 (whose only `ElementSearch` ctor is 3-arg) `shouldApplyMixin` returns false and logs `JEI native bulk builder disabled: … retaining native storage` instead of throwing `InvalidInjectionException`. ARR. **Client-only: the dedicated-server smoke test does not load it, so a Prism client boot is still required to confirm.** | JEI (client) | defaults (`config/justenoughthreads-client.toml`, `enabled = true`) | 2026-10-01 |

NeoForge `21.1.250` → `21.1.252` in the same wave. `21.1.251` deprecates `Level.getSeaLevel` (binary-compatible; 105 installed jars call it) and `21.1.252` changes `StackCopySlot` to take a slot index — **zero** of the 545 installed jars reference `StackCopySlot`, so nothing breaks.

## 2026-10-01 second wave (user-requested, 27 mods)

The user asked for the whole researched shortlist after seeing the per-mod findings, and corrected three of my calls: Macaw's Paths and Pavings *does* have a 1.21.1 NeoForge build (on Modrinth — CurseForge never tagged one), I'm Fast is a movement-desync/log-spam fix rather than a movement mod, and Gravitational Modulating Additional Unit is Mekanism-side. All three were verified and installed. Two hard blockers remain and are **not** installed: **Simply More** and **Overgeared: Universal Compatibility** both have CurseForge distribution disabled, are not on Modrinth, and Simply More additionally needs the Simply Tooltips chain — shipping them would mean rehosting an ARR jar the author chose not to distribute.

**Simply Swords is pinned to 1.62.0 deliberately.** From 1.63.0 its jar declares `simplytooltips` as a **mandatory** dependency. Simply Tooltips is a global item-tooltip frame and cannot be scoped to one mod, so installing it would put a second tooltip frame next to the pack's Tooltip Overhaul for every item in the game. Checked every 1.21.1 NeoForge build: `v1.60.9` through `v1.62.0` have no Simply Tooltips entry at all, `v1.63.0` onward have `mandatory=true`. 1.62.0 gives the weapons with no tooltip change; the cost is the content added in 1.63–1.70. Simply Swords Create Lines declares `simplyswords [0,)`, so it is compatible with the pin.

**Distribution-disabled projects: CurseForge metadata does not work, a direct URL pin does.** `allowModDistribution = false` on CurseForge (Simply More 1095252, Overgeared: Universal Compatibility 1651686) blocks the *CurseForge API*, not the file. Measured, in order:

1. `packwiz curseforge add` downloads both files happily — which is why a CLI test looks fine and is misleading.
2. **`packwiz curseforge export` succeeds** and writes both as `[update.curseforge]` metadata references, so the exported client zip looks correct.
3. **That zip cannot be installed.** `packwiz-installer` — the component every packwiz launcher actually uses — refuses them: `Simply More: java.lang.Exception: This mod is excluded from the CurseForge API and must be downloaded manually.` It then aborts the whole sync ("Update cancelled by user!"), so one excluded mod blocks the entire install.
4. `packwiz modrinth export` also fails outright on the same two files: the Modrinth format cannot reference a project that does not exist there. `overgeared-universal-compatibility` is a 404 on Modrinth, and Modrinth's `simply-more` is an unrelated mod ("Simply m'Ore", different author, zero published versions).

The fix is to pin `[download] url` at CurseForge's own CDN (`https://edge.forgecdn.net/files/<a>/<b>/<file>`) instead of `mode = "metadata:curseforge"`, while keeping the `[update.curseforge]` block so `packwiz update` can still bump the file. Verified with `scripts/update_prism.py`: "Downloaded Simply More", "Downloaded Overgeared: Universal Compatibility", "Finished successfully!". The Modrinth export then also succeeds and writes CDN URLs into `modrinth.index.json` with both hashes and **no jar in the archive**, so nothing is rehosted — the launcher fetches from CurseForge at install time. This is the only arrangement where the mods ship, both artifacts build, and no author's jar is redistributed.

**One consumer path still cannot work, by format.** The client zip that `packwiz curseforge export` builds carries a CurseForge `manifest.json`, whose only per-file fields are `projectID`/`fileID`/`required` — there is no URL field, so it can only express "ask the CurseForge API". Both mods therefore appear in that manifest as API references, and a launcher importing the **zip** through the CurseForge app path will hit the same exclusion. The two paths that matter are fine: packwiz/Prism installs from `pack.toml` (CDN URL, verified), and the `.mrpack` carries the CDN URLs plus sha1 in `modrinth.index.json` with no jar embedded (verified in the published 0.1.23 mrpack). Fixing the zip path would mean putting the two jars in `overrides/mods/`, which is the rehosting this whole change avoids. Revisit when the CurseForge listing goes public: either drop the two mods or accept embedding them there.

This differs on purpose from **Awesome Dungeon**, **Library Ferret**, and **Awesome Dungeon Ocean**, which ship from Modrinth because their authors also publish there. Do not "normalise" those three to a URL pin: Modrinth is the author's own choice for them, while these two are CurseForge-only.

**Both jars are now bundled into the published artifacts, at the user's instruction.** Dropping the `[update.curseforge]` block is what makes packwiz treat an entry as a plain file: the CurseForge export then puts the jar in `overrides/mods/` and drops the project from `manifest.json`, and `pack_artifacts.bundle_unresolvable_mods()` does the same for the mrpack by moving the entry out of `modrinth.index.json` into `overrides/mods/`. So both client artifacts are self-contained and no launcher hits the CurseForge API. The cost, stated plainly: the two All-Rights-Reserved jars now ship inside public archives despite `allowModDistribution = false` on their projects, and dropping `[update]` means `packwiz update` can no longer bump them automatically — they are updated by hand.

Simply Swords moved from the 1.62.0 pin to **1.70.2** (latest) with **Simply Tooltips 0.1.5** added. The tooltip concern turned out to be unfounded: Simply Tooltips ships an item tag whose only value is `#simplyswords:uniques`, so it renders Simply Swords weapons and nothing else. Tooltip Overhaul keeps every other item. Simply Tooltips ships as `side = "both"`, not `client` as its CurseForge tags suggest: the dedicated server hard-fails on `Mod simplymore requires simplytooltips 0.1.3 or above / Currently, simplytooltips is not installed` when it is client-only, because the item tag it ships is server-side data. Its only two mixins are in the `client` array, so the server loads the data without the renderer. Simply Tooltips is `side = client` per its CurseForge tags.

| Mod | Pinned file | Source | `side` | Category | Why | Required deps | Config | Date added |
|---|---|---|---|---|---|---|---|---|
| Simply Swords | `simplyswords-neoforge-1.70.2-1.21.1.jar` | CurseForge 659887 / 8746001 | both | weapons | Katanas, spears, glaives, rapiers, and more, at the latest 1.21.1 NeoForge build. 1.63.0+ hard-requires Simply Tooltips (`[0.1,)`), so that mod is now installed too. Custom "Timefall Development" license; CurseForge metadata only. World data. | Architectury API `[13.0.11,)`, Fzzy Config `[0.6.6,)`, **Simply Tooltips `[0.1,)`** (all in) | defaults | 2026-10-01 |
| Simply Tooltips | `SimplyTooltips-neoforge-0.1.5.jar` | CurseForge 1475755 / 8715141 | both | weapons | Required by Simply Swords 1.63.0+. Its scope is an item tag, not a global override: the shipped `data/simplytooltips/tags/item/simply_swords_compat.json` contains only `#simplyswords:uniques`, so it renders those items and nothing else. That is why it does not add a second tooltip frame next to Tooltip Overhaul. The mod's own description offers opt-in for other items, which this pack does not take. Mixin config is `required: true` with two client mixins on `DrawContext` and `Screen`. Timefall Development License 1.2. | Architectury API, Fzzy Config (both in) | defaults | 2026-10-01 |
| Simply More | `simplymore-forge-1.3.0_alpha.jar` | CurseForge 1095252 / 8736778 | both | weapons | More Simply Swords weapon types. ARR. **CurseForge has `allowModDistribution = false`** — see the distribution note below. The filename really does say `-forge-` even though the file is tagged NeoForge 1.21.1; packwiz's hash matches the CurseForge record exactly. | Architectury API, Fzzy Config, Simply Swords, Simply Tooltips (all in) | defaults | 2026-10-01 |
| simplyswords create lines | `simplyswords_create_lines-1.0.5-neoforge-1.21.1.jar` | CurseForge 1595470 / 8492922 | both | weapons | Create production lines for Simply Swords weapons. ARR. World data. | Simply Swords, Create | defaults | 2026-10-01 |
| Just Enough Professions (JEP) | `JustEnoughProfessions-neoforge-1.21.1-4.0.5.jar` | CurseForge 417645 / 7966681 | **client** | info | Profession workstations and skills in JEI. MIT. Client-only per its CurseForge tags, so the dedicated-server smoke test never loads it. | JEI (optional) | defaults | 2026-10-01 |
| AE2 Network Analyser | `AE2NetworkAnalyzer-1.21-2.1.5-neoforge.jar` | CurseForge 961856 / 7622554 | both | applied-energistics | Visual analyser for ME networks. LGPL-3.0, no mixins, ~2.2M downloads. | AE2, Glodium (both in) | defaults | 2026-10-01 |
| Applied Industrialization | `Applied-Industrialization-1.3.0.jar` | CurseForge 1671614 / 9020730 | both | applied-energistics | AE2 blocks for Modern Industrialization. ARR. Uploaded 2026-09-30 with 3 files, so it is a very new build. One mixin. | none required (AE2/MI optional but both in) | defaults | 2026-10-01 |
| Industrialization Overdrive | `industrialization_overdrive-1.14.0+1.21.1.jar` | CurseForge 1089065 / 8873846 | both | automation | Extra Modern Industrialization machines. MIT. | MI, Tesseract API, GuideME (all in) | defaults | 2026-10-01 |
| Ars Polymorphia | `ars_polymorphia-1.0.3.jar` | CurseForge 1197614 / 6219409 | both | magic | Polymorph support for Ars storage lecterns. LGPL-3.0. | Ars Nouveau, Polymorph (both in) | defaults | 2026-10-01 |
| Ars Unification | `ars_unification-1.2.21.jar` | CurseForge 1165429 / 8784791 | both | magic | Ars Nouveau can craft from other mods' recipes. LGPL-3.0. ~14 optional integrations; **EMI is one of them and must not be installed**. | none required (Ars Nouveau optional but in) | defaults | 2026-10-01 |
| Creeper Overhaul | `CreeperOverhaul-neoforge-1.21.1-4.0.6.jar` | CurseForge 561625 / 6051279 | both | mobs | Overhauled creepers. ARR. Adds custom models, so it is subject to the EMF `modelsNamesDisabled` rule for Epic Fight mobs. | GeckoLib, Resourceful Config (both in, optional) | defaults | 2026-10-01 |
| Enderman Overhaul | `endermanoverhaul-neoforge-1.21.1-2.0.3.jar` | CurseForge 574409 / 7661859 | both | mobs | Overhauled endermen, including new spawn variants. ARR. Same EMF model caveat, and its spawn changes sit beside the pack's spawn datapacks. | Resourceful Lib, Resourceful Config, GeckoLib | defaults | 2026-10-01 |
| AI Improvements: Performance Tuning | `AI-Improvements-1.21-0.5.3.jar` | CurseForge 233019 / 5426792 | both | mobs | Cheaper, smarter mob AI. MIT, no mixins, no deps. **Newest 1.21.x build is 2024-06-14**, so it is two years stale for this branch. | none | defaults | 2026-10-01 |
| Steve's Carts | `stevescarts-1.21-1.2.18-neoforge.jar` | CurseForge 551524 / 7368915 | both | transport | Customisable minecarts for automation. ARR. World data. packwiz pulled PolyLib with it. | PolyLib (added) | defaults | 2026-10-01 |
| PolyLib | `polylib-2100.1.0-build.183-neoforge.jar` | CurseForge 576589 / 7368236 | both | transport | Library Steve's Carts needs. Only that mod uses it, so it lives in the transport group rather than `libraries`. | none | defaults | 2026-10-01 |
| Logistics Network | `logisticsnetworks-1.21.1-1.16.4.jar` | CurseForge 1448257 / 8948051 | both | transport | Item, fluid, and energy logistics. ARR, **4 mixins** plus a JEI plugin, and it overlaps the role already covered by Modern Dynamics / XNet / Simple Conveyor Belts / Modular Routers. | none required (JEI/Mekanism/AE2/RS/Create optional) | defaults | 2026-10-01 |
| Structure Essentials | `structureessentials-1.21.1-5.0.jar` | CurseForge 832882 / 7962596 | **server** | exploration | Faster structure locating, a nearby-structure command, and structure biome compatibility. ARR. Overlaps Explorer's Compass and the Structurify 2.0 spacing config. | Cupboard (in) | defaults | 2026-10-01 |
| In Control! | `incontrol-1.21-10.3.0.jar` | CurseForge 257356 / 8790499 | both | gameplay | Rules for what spawns where. MIT. Overlaps the pack's datapack spawn controls. | none required (Lost Cities, KubeJS optional) | defaults | 2026-10-01 |
| Gravitational Modulating Additional Unit | `GravitationalModulatingAdditionalUnit-1.21.1-6.4.jar` | CurseForge 656136 / 6895172 | both | mekanism | Extra Mekanism-side features. MIT. Verified from the jar: it references only `minecraft`, `gmut`, and `mekanism`, with Mekanism as its one hard dependency, so it does not need a separate parent mod to load. | Mekanism (in) | defaults | 2026-10-01 |
| I'm Fast | `imfast-NEOFORGE-1.21.1-1.0.3.jar` | Modrinth PaUMOeP0 / FWI4gJ6y | both | stability | Stops movement desync kicking players or spamming the server log. MIT. CurseForge has distribution disabled for this project, so it is **not** manifest-referenced; embedded from Modrinth. | none | defaults | 2026-10-01 |
| Macaw's Paths and Pavings | `mcw-mcwpaths-1.1.1-mc1.21.1neoforge.jar` | Modrinth VRLhWB91 / tlymsxUG | both | building | Paths and pavings, beside the other Macaw's mods. MIT. **CurseForge never tagged a 1.21.1 NeoForge file for this project** (only Fabric 1.21.1 and Forge 1.21.1); Modrinth carries `mcw-mcwpaths-1.1.1-mc1.21.1neoforge.jar`. World data. | none | defaults | 2026-10-01 |
| Leaky | `leaky-1.21-3.4.jar` | CurseForge 856906 / 8763884 | **server** | performance | Cleans up item piles and broken farms. ARR. It deletes item entities, so watch Create and Modern Dynamics farms. | Cupboard (in) | defaults | 2026-10-01 |
| Chunk Sending | `chunksending-1.21-3.9.jar` | CurseForge 831663 / 8752593 | **server** | performance | Faster chunk packet delivery. ARR. Sits next to Connectivity's packet mixins. | Cupboard (in) | defaults | 2026-10-01 |
| Fast Async World Save | `fastasyncworldsave-1.21-2.6.jar` | CurseForge 951499 / 6935204 | **server** | performance | Saves the world without tick spikes. ARR. Pairs with the installed Smooth Chunk Save. | Cupboard (in) | defaults | 2026-10-01 |
| Invasive Optimizations | `invasiveopts-1.0.24.jar` | CurseForge 1528432 / 8782897 | both | performance | Deeper optimizations aimed at other mods. MIT. The author ships the warning "If you experience any issues, disable this mod first"; its optional integrations include Pipez (removed from this pack) and Accessories (this pack uses Curios), so those bridges stay inert. | none | defaults | 2026-10-01 |
| Better Fps - Render Distance | `betterfpsdist-1.21.1-6.1.jar` | CurseForge 551520 / 8319712 | **client** | rendering | Cheaper far-chunk rendering. ARR. | Cupboard (in) | defaults | 2026-10-01 |
| fix GPU memory leak | `gpumemleakfix-1.21-1.8.jar` | CurseForge 882495 / 5513549 | **client** | stability | Fixes a client GPU memory leak. ARR. **Newest build is 2024-07-08**, the oldest in this wave. | Cupboard (in) | defaults | 2026-10-01 |
| ATi Structures | `ATi Structures V1.4.7.jar` | CurseForge 964608 / 8984311 | both | worldgen | Overworld structure pack by ATii / HardWater, the same authors as the installed Epic Structures mods. `LicenseRef-All-Rights-Reserved`, 0 downloads on the 1.21.1 file, updated 2026-09-26. World data. | none | defaults | 2026-10-01 |
| Loot Integrations: ATi Structures… | `lootintegrations_ati-1.3.jar` | CurseForge 1420613 / 8920862 | both | content | Modded loot in ATi Structures and Epic Structures villages/witch huts. ARR. | Loot Integrations, ATi Structures | defaults | 2026-10-01 |
| Gateways to Eternity | `GatewaysToEternity-1.21.1-5.1.0.jar` | CurseForge 417802 / 6926284 | both | worldgen | Giant portals, monster hordes, and large rewards, by Shadows_of_Fire (the Applied Flux author). MIT, 1 mixin, ships a JEI plugin. **Newest build 2025-08-25 with 0 downloads on the 1.21.1 file.** World data. | none required (Placebo, Apothic Attributes in) | defaults | 2026-10-01 |

## 2026-10-01 overlays, privacy, and curios wave

Second half of the same user-supplied candidate list, researched one at a time and installed in two groups. The **CurseForge-first rule mattered here**: `packwiz curseforge install` cannot fetch More Overlays Updated at all, because the CurseForge API returns `downloadUrl: null` for *every* file on project 391382 (the CDN itself still serves them). The Modrinth file is byte-identical, so the pack references the Modrinth file and records the CurseForge project and file IDs here for traceability. `StructureOverlapless` was researched and **held** — see [deferred.md](deferred.md) for the Structurify `@WrapMethod` conflict and the save-reset caveat.

| Mod | Pinned file | Source | `side` | Category | Why | Required deps | Config | Date added |
|---|---|---|---|---|---|---|---|---|
| More Overlays Updated | `moreoverlays-1.24.2-mc1.21.1-neoforge.jar` | Modrinth Thy5Pqut / Kq8xaqYi (same bytes as CurseForge 391382 / 6981252, sha1 `21e8bd61…`) | client | client QoL | NEI-style light-level overlay (F7), chunk borders (F9), and JEI item search. MIT; author allows modpack redistribution with credit. One mixin (`DebugRenderer`); no Sodium or Iris dependency. **Its JEI item-search overlay reflects into JEI slot classes** — this pack's recurring breakage class — so that feature is the one to test in a client, and `config/moreoverlays.toml` can turn it off without removing the mod. | JEI `[6.0.0.25,)` optional (have 19.57) | defaults; `config/moreoverlays.toml` | 2026-10-01 |
| No Chat Reports | `NoChatReports-NEOFORGE-1.21.1-v2.9.1.jar` | CurseForge 634062 / 5885735 | both | client QoL | Chat cannot be reported to Mojang and the server name is hidden on the disconnect screen. `side: both` on purpose: the server-side mixins are what let the pack's own test server accept our clients. WTFPL. | none | defaults | 2026-10-01 |
| Refined Storage - Curios Integration | `refinedstorage-curios-integration-1.0.0.jar` | CurseForge 1230729 / 6360514 | both | storage | Two Curios slots so RS network items can be worn. Official Refined Mods addon, MIT, 11 KB. Declares RS `2.0.0-beta.1` as a bare (minimum) version — the installed RS Mekanism Integration uses the same pattern at `beta.17` and boots against 2.0.9. | Refined Storage (have 2.0.9), Curios `[9.2,)` (have 9.5.1) | defaults | 2026-10-01 |
| MmmMmmMmmMmm (Target Dummy) | `dummmmmmy-1.21-2.1.2-neoforge.jar` | CurseForge 225738 / 8903254 | both | content | Placeable target dummy with damage numbers; armor can be equipped on it. Adds one block and one entity, so `side: both`. **Supplementaries Team License v1.5** — see the Credits note. Common mixins wrap `LivingEntity#actuallyHurt`, `Player#actuallyHurt`, `SwordItem#hurtEnemy`, `DiggerItem#hurtEnemy`, and `EnchantmentItem`, all with `defaultRequire: 1`, on the same damage path Epic Fight and ParCool use; a client fight test is the only real proof. No target method overlaps `leylines_patches`, which only injects into MI/EI `getAllEnchantments`. | Moonlight Lib `[1.21-3.2.3,)` (have 3.7.0) | defaults | 2026-10-01 |

## 2026-10-02 Oritech family wave

User-supplied CurseForge IDs for the Oritech family. All five resolved to real 1.21.1 NeoForge releases and installed with **no new dependencies** — Oritech's three hard deps were already present and version-compatible (Architectury API 13.0.11 against `[13.0.2,)`, Athena 4.0.6, GeckoLib 4.9.3), as were AE2 19.2.18 and Create 6.0.10 for the addons. **Three of the five shipped**; two were removed during verification, for the reasons in [Oritech rejections](#oritech-rejections-2026-10-02) below.

Key facts verified from the jars rather than the project pages:

- **Oritech energy is Forge Energy.** `rearth/oritech/neoforge/NeoforgeEnergyApiImpl` registers `net.neoforged.neoforge.capabilities.Capabilities$EnergyStorage` and also handles GrandPower's `ILongEnergyStorage`. So Oritech shares one FE pool with Mekanism, Modern Industrialization, and Create Crafts & Additions rather than adding a third power system. This was the deciding factor.
- **Built-in data compat with the pack's core mods.** Oritech ships centrifuge recipes for Create and Mekanism clumps (lead, osmium, tin, nickel, platinum, uranium, zinc), pulverizer/grinder/laser recipes for AE2 certus, fluix and sky dust, and a `c:` tag tree. It also ships a JEI plugin (`rearth/oritech/init/compat/jei/`) that touches only stable JEI 19.x API — `IRecipeRegistration`, `IGuiHandlerRegistration`, `IGhostIngredientHandler`, `IRecipeCatalystRegistration` — all present in the pack's JEI 19.57.0.450, and it declares **no** hard JEI dependency. Still a JEI-integrating mod, so the client is the real test.
- **No vanilla ore-gen removal.** `OritechConfig` has no "remove vanilla ores" option; worldgen is additive only (oil springs, bedrock resource nodes, uranium patches, nickel and platinum). Safe against the Terralith + TerraBlender region-size-6 setup.
- **Small mixin footprint.** `oritech.mixins.json` is 3 common (`EntityLaserDropsMixin`, `MachineControllerLifecycleMixin`) + 2 client, and `oritech_forge.mixins.json` adds 1 client (`ExtendMachineRenderBounds`).
- **Oritech registers the "Ender IO" metal names itself.** `oritech:adamant_ingot`, `duratium_ingot`, `electrum_ingot`, `energite_ingot`, and `biosteel_ingot` all exist in 1.2.12 and have Oracle Index pages, so the Create-side recipes for them are worth keeping even though Ender IO is not in the pack.

| Mod | Pinned file | Source | `side` | Category | Why | Required deps | Config | Date added |
|---|---|---|---|---|---|---|---|---|
| Oritech | `oritech-neoforge-1.21.1-1.2.12.jar` | CurseForge 1030830 / 8780299 | both | tech | Fourth full tech tree, added on request. Animated multiblocks, processing chains, item/fluid/energy pipes, drones, nuclear reactors, particle accelerators, and a bedrock extractor. **Forge Energy native**, so it shares the pack's existing FE pool. CC0-1.0. World data. | Architectury API `[13.0.2,)` (have 13.0.11), Athena (have 4.0.6), GeckoLib (have 4.9.3) | defaults; see configs.md | 2026-10-02 |
| Applied Oritech | `applied_oritech-1.0.4+1.21.1.jar` | CurseForge 1686167 / 8944224 | both | applied-energistics | ME Dock, ME Pattern Provider addon, and ME Interface addon, so Oritech machines join ME networks for autocrafting and item stocking. **Zero mixins** (`applied_oritech.mixins.json` has empty `mixins` and `client` lists), which is why it is the safest mod in this wave. MIT. The strongest pack-specific case for this family. | Oritech `[1.2.12,)` (exact match), Applied Energistics 2 `[19.2.0,)` (have 19.2.18) | defaults | 2026-10-02 |
| Oritech Things | `oritechthings-0.0.46.jar` | CurseForge 1166849 / 8547739 | both | tech | Largest community addon (4.7M downloads, 6 authors, actively maintained). Tiered Speed/Efficiency/Processing/Capacitor/Acceptor addons tiers 2–9, exo jetpack, particle-accelerator target controller and speed sensor, frame placer, and the Amethyst Fish mob. **License ambiguity accepted by the user — see Credits.** Self-declared alpha. 7 mixins. | Oritech `[1.2.0,)` | defaults | 2026-10-02 |

Verification: `scripts/smoke_test.py` passes at 20.0 TPS with 0 "can't keep up" over 289 generated chunks, and the log confirms `Oritech initialization complete` plus the Oritech Jade plugin loading. `Entity oritechthings:amethyst_fish has no attributes` also appears, but that line is a **pack-wide NeoForge 1.21.1 quirk**, not an Oritech Things defect — hundreds of entities from every installed mod (Twilight Forest, Ars Nouveau, Ice and Fire, Spawn, and so on) log it on every boot.

Open design note for a future pass: Oritech's **Bedrock Extractor** can produce "renewable" metals late-game, which may undercut the Mekanism and Modern Industrialization ore chains. The user chose to leave defaults and evaluate in real play rather than gate it with a KubeJS script or datapack yet. Config candidates not enabled at add time, all reviewable in [configs.md](configs.md): `worldGeneration.easyFindFeatures` (surface markers for oil wells and ore nodes, a real QoL win under large biomes), `reactor.safeMode` (cooldown instead of explosion), and `machineSoundVolumeMultiplier` / `machineVolumeMultiplier`, which are worth checking in a 400-mod pack.

## Create Oritech recipes ported into the pack

`pack/global_packs/required_data/lead-leylines-oritech-create-compat/` carries **18 Create recipes** under `data/lead_leylines/recipe/oritech_create/`, ported from Create Oritech Compat 1.0 (CurseForge 1211589 / 6255439, MIT, FixedDolphin927) after that mod was removed. `global_packs/required_data/` is force-enabled by `global_packs.toml`, so no config edit is needed.

The upstream mod shipped **14 of its 18 recipes in a format Minecraft 1.21.1 cannot parse**, which produced 14 `Parsing error loading recipe` ERROR lines on every server boot. It had been broken since 2025-03-02 with no bug report. Two separate problems were involved:

1. **Result field (14 recipes).** The `results` / `result` objects still used the pre-1.21.1 `"item"` key, which the 1.21.1 `ItemStack` codec rejects. Migrated to `"id"`. The four recipes that did load upstream — `blasting` and `smelting` for nickel and platinum — are the reference shape and confirm the fix.
2. **Non-existent input tags (2 recipes).** `crushing/biomass` used input tag `oritech:biomass` and `mixing/biosteel_ingot` used `oritech:raw_biopolymer`. Neither tag exists in Oritech 1.2.12, so both recipes could never match even with the format fixed. Repointed to the obvious intent: the first to the real Oritech plant-matter tag `oritech:biomatter`, the second to the `oritech:raw_biopolymer` **item** (which does exist).

One trap worth recording: **Create 6.0.10 uses two different codecs in the same recipe file.** Processing `ingredients` / `ingredient` go through Create's own codec and want `"item"` / `"tag"`, while `results` / `result` go through the vanilla 1.21.1 `ItemStack` codec and want `"id"` / `"count"`. Migrating the ingredient side to `"id"` — the obvious blanket fix — breaks all 18. Verified by boot: `Loaded 48034 recipes` with the broken version, `Loaded 48047` after, an exact **+13** for the 13 that were failing, with the 5 already-working recipes unchanged.

Net effect: 18 working Create recipes where the mod previously delivered 4, and zero recipe-parse errors from this family.

## Farmer's Cutting and Create RU recipes ported into the pack

Seven data-only mods removed; their JSON now ships as
`pack/global_packs/required_data/lead-leylines-compat-recipes/`. Full census,
byte-verification and the re-sync procedure are in
[datapack-consolidation.md](datapack-consolidation.md).

| Source mod | CurseForge | Recipes | Namespace |
|---|---|---|---|
| Farmer's Cutting: BetterNether | 1114065 / 7649818 | 51 | `fcbn` |
| Farmer's Cutting: Twilight Forest | 1131152 / 5859455 | 50 | `fctf` |
| Farmer's Cutting: BetterEnd | 1146834 / 7648264 | 76 | `fcbe` |
| Farmer's Cutting: Oh The Biomes We've Gone | 1094819 / 6274107 | 165 | `fcbwg` |
| Farmer's Cutting: Regions Unexplored | 1133629 / 7642854 | 195 | `fcru` |
| Create Regions Unexplored Compat | 1431845 / 7469182 | 30 | `create_ru_compat` |
| **Total** | | **567** | |

Facts verified from the jars, not the project pages:

- **All five Farmer's Cutting JARs contain zero `.class` files** and each ships a
  `pack.mcmeta`. They were never code mods — they are Modrinth datapacks
  packaged as JARs (`lowcodefml`). The upstream repo is a *generator*
  (`fcgenerator.py` plus per-mod folders), which is independent confirmation
  that the recipes are machine-generated pure data.
- **`create_ru_compat` has one class with an empty constructor body.** Its only
  purpose is making the JAR a valid mod container. Its
  `META-INF/accesstransformer.cfg` is **0 bytes**, so there is no access
  transformer and no mixin to lose.
- **Only two recipe serializers are involved**, `farmersdelight:cutting` (537)
  and `create:crushing` (30). Both are registered by mods that **stay** in the
  pack, so no serializer disappears along with the JARs. Every file sits under
  its own source namespace, with no cross-namespace spill and no
  self-references. All 567 parse as JSON.

**Verification is the recipe count, and it matched exactly.** Because the
datapack recipes carry the same IDs as the mod recipes, they override them
while both are installed — so the datapack was added *first* and booted before
anything was removed. That canary proved the datapack loads and overrides;
then the seven mods were removed and the count was re-checked:

| State | Recipes loaded |
|---|---|
| Datapack added, 7 mods still installed | `Loaded 47540 recipes` |
| 7 mods removed, datapack alone | `Loaded 47540 recipes` |

Identical, which is the strongest available proof that the port lost nothing.
Both boots passed with **no ERROR or WARN attributable to any ported
namespace**. The log does contain 17 `RuntimeDistCleaner/DISTXFORM` ERROR lines
and many `Entity <x> has no attributes` lines; both are pre-existing pack-wide
NeoForge 1.21.1 noise unrelated to this change, and the latter is the quirk
already recorded on the Oritech wave.

`DarkSleep` was the seventh mod and is a different shape: its entire behaviour
is `gamerule playersSleepingPercentage 50` in a `#minecraft:load` function. Its
JAR declares `All Rights Reserved`, so **none of its data was copied**. The
gamerule is reimplemented as
`lead-leylines-load-fixes/data/lead_leylines/function/sleep_rules.mcfunction`
and added to `#minecraft:load` in the same datapack, in a pack-owned namespace.
The tag is additive (no `"replace"`), so any mod-provided load functions still
run.

Unlike the Create Oritech port, **no recipe needed fixing** — these were
correct to begin with, which is why the before/after counts are equal rather
than higher.

## Oritech rejections (2026-10-02)

Two of the five requested mods did not ship. Both were installed first, on explicit user request over my recommendation, and then removed because verification showed the recommendation was right for a harder reason than I had given.

| Mod | Source | What verification found | Why it is out |
|---|---|---|---|
| Extended Oritech | CurseForge 1390979 / 7305507 | **Hard crash at mod construction.** `NoClassDefFoundError: rearth/oritech/client/ui/BasicMachineScreenHandler` from `net.cjsah.mod.extendedoritech.init.ModBlockEntities.<clinit>`. That class exists in Oritech **1.0.1** and was **removed before 1.2.6** — confirmed absent in 1.2.6, 1.2.8, 1.2.9, and 1.2.12. | Not a mixin risk but a missing-class failure, and there is **no working version pair on CurseForge**: the only Oritech builds that still ship the class are 1.0.x, which would break Applied Oritech (requires `[1.2.12,)`) and Oritech Things (requires `[1.2.0,)`). Revisit only if the author ships a build against Oritech 1.2.x+. Its 3 required mixins into Oritech internals were a second, smaller risk on top. |
| Create Oritech Compat | CurseForge 1211589 / 6255439 | 14 of 18 recipes fail to parse on 1.21.1; one more references a tag that no longer exists. 21k downloads, one file, last updated 2025-03-02, no bug report. | Content was worth keeping, the mod was not. Ported to `lead-leylines-oritech-create-compat` and removed. Its own jar filename also said `1.20.1` while declaring 1.21.1. |

The Oritech Things license ambiguity was **not** a rejection reason; the user accepted it explicitly. See Credits.

## 2026-10-04 Twilight Delight Neapolitan bridge wave

Added to fix Twilight's Flavors & Delight shipping data for content it only registers when Neapolitan is present. Not a "more desserts" decision — see the note under the table.

| Mod | Pinned file | Source | `side` | Category | Why | Required deps | Config | Date added |
|---|---|---|---|---|---|---|---|---|
| Neapolitan | `neapolitan-1.21.1-6.0.1.jar` | CurseForge 382016 / 7119475 | both | content | **Fixes missing Twilight's Flavors & Delight content.** Also brings its own ice creams, milkshakes, cakes, the `neapolitan:strawberry_fields` biome, chimpanzees, and plantain spiders. World data — hard to remove later. **Abnormals License (ARR)**, see Credits. 7 server mixins with `required: true` / `defaultRequire: 1`, including `LivingEntityMixin` and `ItemMixin`; smoke test is the only real proof. `client_side`/`server_side` are both `required` on Modrinth, hence `side = both`. | Blueprint `[8.0.6,)` (have 8.2.0); Minecraft `[1.21.1]`; NeoForge `[21.1.160,)` (have 21.1.252) — **no ecosystem bump**. Farmer's Delight is soft-compat, not required. | defaults (`config/neapolitan-common.toml`: `blocks.strawberry_bush`, `mobs.chimpanzee`, `mobs.plantain_spider`, `worldgen.suspicious_banana_plant`) | 2026-10-04 |

**Why Neapolitan and not a datapack patch.** Twilight's Flavors & Delight 3.2.3 gates `NeapolitanCakes` and `NeapolitanFood` behind `isLoaded("neapolitan")` (`TwilightDelight.class`, `TagGen.class`; `NeapolitanFoodType extends Neapolitan's IFoodType`, `TDIceCreamItem extends IceCreamItem`) while shipping its tags, recipes, and loot tables unconditionally — an upstream bug. LMFT 1.1.1 logged it as 3 unresolvable tags on every boot: `farmersdelight:item/snacks`, `farmersdelight:item/sweets`, and `diet:item/sugars`, ending in the `It seems that some tags are a bit cooked` error. Neapolitan is the only thing that makes those 15 items register. A tag override could have silenced the log but would have left the content missing and frozen a snapshot of Farmer's Delight's tags.

Restored by this change: 7 disabled recipes under `lead-leylines-load-fixes/data/twilightdelight/recipe/` (`neapolitan/{aurora,glacier,phytochemical,torchberry}_cake_slice`, `rainbow_ice_cream`, `refreshing_ice_cream`, `twilight_ice_cream`) and 4 emptied loot tables under `lead-leylines-orphan-loot/data/twilightdelight/loot_table/blocks/`. `python scripts/smoke_test.py --skip-bench --memory 8192` passes, all three tag warnings are gone, and the restored recipes and loot tables parse without error. Neapolitan's own two `has no attributes` log lines join the existing pack-wide noise of roughly 470 such lines (already tracked in `load-fixes-inventory.md`).

**Still unverified:** `neapolitan:strawberry_fields` is injected as a *vanilla* datapack biome (tagged `c:is_plains` and `c:is_rare`, and spliced into the mineshaft / ruined portal / trial chamber biome tags) on a TerraBlender `overworld_region_size = 6` + Terralith pack. A boot-only smoke test cannot show terrain. Check the biome on a real generated chunk before treating this as settled. Note the pack's `lead-leylines-large-climate` datapack overrides `minecraft/worldgen/noise/temperature.json` and `vegetation.json` rather than listing biomes, so the new biome inherits the pack's climate points with no datapack edit — that part is fine.

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
| AllTheLeaks | Uncandango | See CurseForge page | CurseForge reference. |
| Smooth Chunk Save, Cupboard | someaddon | See CurseForge pages | CurseForge reference. |
| BadOptimizations | thosea | See CurseForge page | CurseForge reference. |
| Dynamic FPS | juliand665 | See CurseForge page | CurseForge reference. |
| Crash Assistant | kr0stik | See CurseForge page | CurseForge reference. |
| Entity Culling | tr7zw | Custom protective license | CurseForge metadata only; do not bundle the jar. |
| Sodium Extra | FlashyReese | LGPL-3.0-only | CurseForge reference. |
| Flerovium, AsyncParticles | See CurseForge pages | LGPL-3.0-only | CurseForge reference. |
| More Culling | FxMorin | GPL-3.0-only | CurseForge reference. |
| Cloth Config | shedaniel | LGPL-3.0-only | CurseForge reference. |
| Structure Layout Optimizer, Resourceful Config | See CurseForge pages | MIT | CurseForge reference. |
| Ksyxis, quick pack | See CurseForge pages | MIT | CurseForge reference. |
| CrashExploitFixer | See CurseForge page | GPL-3.0-only | CurseForge reference. |
| Async Logger | See CurseForge page | LGPL-3.0-only | CurseForge reference. |
| ResourcePackCached | See CurseForge page | GPL-3.0-only | CurseForge reference. |
| Create | simibubi / Creators of Create | Create Mod License | CurseForge reference; do not rehost the jar. |
| Create Better FPS | See CurseForge page | MIT | CurseForge reference. |
| Create: Threaded Trains | See CurseForge page | GPL-3.0-or-later | CurseForge reference. |
| Architectury API | architectury | LGPL-3.0-only | CurseForge reference. |
| FTB Library, Teams, Quests | Feed The Beast | ARR | CurseForge metadata only; do not embed the jars. |
| FTB Quests Optimizer | See CurseForge page | MIT | CurseForge reference. |
| TxniLib | Txni | MIT | CurseForge reference. |
| Cerulean | Txni | GPL-3.0-only | CurseForge reference. |
| Bye?Pregen! | MoePus | LGPL-3.0-only | CurseForge reference. |
| The Twilight Forest | TeamTwilight | See CurseForge page | CurseForge reference. |
| Neapolitan | TeamAbnormals (credits: bageldotjpg, five, Markus1002) | **Abnormals License 1.0 — "All Rights Reserved."** Modpack Clarification permits modpack inclusion provided the copy is an unmodified official download and it is marked as included in the Modpack. | **CurseForge reference only — never rehost the jar.** This row plus the `docs/installed` catalog entry is the "marked as included" half. Credit TeamAbnormals and the three credited authors. |
| Unusual End | TeamAbnormals | **Abnormals License 1.0** — same terms as Neapolitan. Shipped since 2026-09-25 without a Credits row until now. | CurseForge reference only. Credit TeamAbnormals. |
| Blueprint | TeamAbnormals | **Abnormals License 1.0** — same terms as Neapolitan. Shipped since 2026-09-25 without a Credits row until now. | CurseForge reference only. Credit TeamAbnormals. |
| The Lost Cities | McJty | MIT | CurseForge reference. |
| Lithostitched | Apollounknowndev | MIT | CurseForge reference. |
| TerraBlender (NeoForge) | Glitchfiend | LGPL-3.0-only | CurseForge reference. Use project 940057, not Forge 563928. |
| GeckoLib | Gecko | MIT | CurseForge reference. |
| CorgiLib | Corgi_Taco | See CurseForge page | CurseForge reference. |
| Oh The Trees You'll Grow | Corgi_Taco | See CurseForge page | CurseForge reference. |
| Oh The Biomes We've Gone | Potion Studios | ARR | CurseForge metadata only; do not embed the jar. |
| Regions Unexplored | UHQ_GAMES | See CurseForge page | CurseForge reference. |
| Global Packs | JTK222 | ARR | CurseForge metadata only; do not embed the jar. |
| Jade | Snownee | ARR | CurseForge metadata only; do not embed the jar. |
| Jade Addons | Snownee | ARR | CurseForge metadata only; do not embed the jar. |
| Just Enough Items (JEI) | mezz | MIT | CurseForge reference. |
| MezzConfig | mezz | MIT | CurseForge reference. |
| AE2 JEI Integration, Create JEI Compat, Smithing Template Viewer, Sophisticated JEI Index, SpectrumJEI, JEI Stuff | See CurseForge pages | MIT / LGPL-3.0-only / see pages | CurseForge reference. |
| JEIOptimizer, JEI QuickCraft | See CurseForge pages | ARR | CurseForge metadata only; do not embed the jars. |
| Refined Storage - JEI Integration | raoulvdberge | MIT | CurseForge reference. |
| FTB JEI Extras, MekaGenJei, Just Enough Mekanism Multiblocks, Mekanism Ponders, Just Enough TaCZ, Just Enough Resources | See CurseForge pages | See each page | CurseForge metadata; do not embed ARR jars. |
| Mekanism addons (Extras, Elements, RS/Soph compat, MekaJade) | See CurseForge pages | Mix of MIT/ARR | CurseForge metadata; do not embed ARR jars. |
| Patchouli | Vazkii | Custom | CurseForge reference. |
| Sophisticated addons (Ars, tactical, item actions, Yukami, inventory, chest optimized, RS bridge) | See CurseForge pages | Mix of MIT/ARR | CurseForge metadata; do not embed ARR jars. |
| TaCZ unofficial port and addons | See CurseForge pages | Mix of MIT/ARR; unofficial 1.21.1 port | CurseForge metadata; do not embed ARR jars. |
| MCS2 gun pack | See CurseForge page | ARR | CurseForge metadata. Zip stays in `pack/tacz/`. Do not ship MCS2Gun-addon 1285238 (encrypted 1.20.1 Forge jar). |
| Daffa's Arsenal | DaffaTheOne | CC-BY-NC-4.0; inner pack header says all rights reserved | CurseForge metadata in `pack/tacz/`. Do not embed the jar. |
| CS+ | lolokeia | CC BY-NC-4.0 | CurseForge metadata in `pack/tacz/`. Do not embed the jar. |
| Vic's Point Blank and official packs | vic4games | ARR | CurseForge metadata; do not embed the jars or zips. |
| Cyberpunk 2077 Guns for Vic's Point Blank | TheScepticBlock | ARR; no third-party distribution | CurseForge metadata only; do not embed the zip. |
| Epic Fight, ParCool, Ice and Fire CE, BetterNether New Dawn, Jaden's Nether, and related addons | See CurseForge pages | Mix of MIT/ARR | CurseForge metadata; do not embed ARR jars. |
| AAA Particles | chloe_koopa | See CurseForge page | CurseForge reference. Effekseer; kept without Nightfall. |
| Knight Lib, Olympus! | See CurseForge pages | See CurseForge pages | CurseForge reference. |
| Archaion: Echoes of the Fallen | RatRod / aquextheseal | ARR | CurseForge metadata only; do not embed the jar. |
| Fresh Animations, Extensions, Enhanced Boss Bars | See CurseForge pages | ARR; no third-party distribution | CurseForge metadata only; do not embed the zips. |
| Darkest Ages Mobs and Fresh Animations compat, Icon Xaero's | See CurseForge pages | See CurseForge pages | CurseForge reference. |
| Ecliptic Seasons, Bundles, MultiMod Patch, Serene Seasons API Stub | joe_vettek et al. | ARR | CurseForge metadata; do not embed the jars. |
| SeasonHud | IanAnderson | MIT | CurseForge reference. |
| Demagnetizer | See CurseForge page | See CurseForge page | CurseForge metadata. |
| GeckolibBetterFPS | MoePus | LGPL-3.0-or-later | CurseForge reference. |
| Terralith, Nullscape, Amplified Nether | Stardust Labs | See CurseForge pages | CurseForge reference. |
| Feature Recycler | Corgi_Taco | ARR | CurseForge metadata only; do not embed the jar. |
| YACL | isXander | LGPL-3.0-or-later | CurseForge reference. |
| Structurify | See CurseForge page | See CurseForge page | CurseForge reference. |
| When Dungeons Arise / Seven Seas | Aurelj | ARR | CurseForge metadata only; do not embed the jars. |
| Library Ferret, Awesome Dungeon | JTL | ARR | CurseForge has these with distribution disabled, so there is no metadata reference to use. Embedded from Modrinth; that is the author's deliberate choice, not a rehosting mistake. |
| I'm Fast, Macaw's Paths and Pavings | Bielhiss, sketch_macaw | MIT | **Not** distribution-disabled — these two are on Modrinth and CurseForge simply has no usable 1.21.1 NeoForge file. Embedded from Modrinth. |
| YUNG's API / Better Caves / Better Nether Fortresses / Bridges | YUNG | LGPL-3.0-only | CurseForge reference. |
| Moog's Structure Lib / Mineshafts | Moog | See project pages | CurseForge metadata; do not rehost the jars. |
| Epic Structures | See CurseForge pages | ARR | CurseForge metadata only; do not embed the jars. |
| Infernal Expansion Redux | See CurseForge page | See CurseForge page | CurseForge reference. |
| Countered's Terrain Slabs | Countered | See CurseForge page | CurseForge reference. |
| Fragmentum, Aquamirae | Obscuria | Obscuria licenses | CurseForge metadata; do not rehost the jars. |
| FastBoot | dnlayu | ARR | CurseForge metadata only; do not embed the jar. |
| Fluidium, Duplicationless | Kall | MIT | CurseForge reference. |
| LC²H | Admany | BRSSLA V2.0.0 | CurseForge metadata only; do not embed the jar. |
| Quantified API | Admany | See CurseForge page | CurseForge metadata only; do not embed the jar. |
| BiomeSpy | MoePus | LGPL-3.0-only | CurseForge reference. |
| Farmer's Cutting (5 mods) | Joshcraft2002 | MIT (declared in-jar) | Recipes are ported into `lead-leylines-compat-recipes`; no jar ships. Attribution retained. |
| Create Regions Unexplored Compat | Starion | MIT (declared in-jar) | Recipes are ported into `lead-leylines-compat-recipes`; no jar ships. Attribution retained. |
| DarkSleep | GamerPotion | ARR | **No data copied.** Behaviour reimplemented as one vanilla gamerule in a pack-owned datapack. |
| MemGuard | See CurseForge project 1468440 | MIT (in-jar) | CurseForge reference. |
| Wave 1 QoL/storage/FTB (Xaero, Waystones, Sophisticated, etc.) | See each CurseForge page | Mix of MIT/ARR/LGPL | CurseForge metadata; do not embed ARR jars. |
| Tooltip Overhaul | Xylonity | GPL-3.0-only | CurseForge metadata only; do not embed the jar. |
| Tag Tooltips | Jagm | CC-BY-SA-4.0 | Modpack use allowed. CurseForge metadata only; do not embed the jar. |
| Mowzie's Mobs | Bob Mowzie, pau101 | Custom | Credit "Mowzie's Mobs" and link https://www.curseforge.com/minecraft/mc-mods/mowzies-mobs. CurseForge metadata only. |
| Enchantment Descriptions | DarkhaxDev | LGPL-2.1-only | CurseForge reference. |
| Fusion, Fusion 3D Items, Fusion Connected Glass | SuperMartijn642 | ARR | CurseForge metadata only; do not embed the jar or zips. |
| Handcrafted | terrariumearth, AlexNijjar, kekie6 | Terrarium Licence | CurseForge metadata only; do not embed the jar. |
| Chipped | terrariumearth, AlexNijjar | ARR | CurseForge metadata only; do not embed the jar. |
| Macaw's Doors, Macaw's Fences and Walls | sketch_macaw | MIT | CurseForge reference. |
| Macaw's Windows, Macaw's Furniture | sketch_macaw | ARR | CurseForge metadata only; do not embed the jars. |
| Macaw's Lights and Lamps, Macaw's Stairs | sketch_macaw | ARR | CurseForge metadata only; do not embed the jars. |
| Epic Structures: Dungeons, Epic Structures: Igloo | HardWater, ATii | ARR | CurseForge metadata only; do not embed the jars. |
| Awesome Dungeon The End | JTL | ARR | CurseForge metadata only; do not embed the jar. |
| Awesome Dungeon Ocean | JTL | ARR | CurseForge distribution is disabled for the Ocean edition, so it is **not** metadata-referenced. Embedded from Modrinth, as with Awesome Dungeon and Library Ferret. |
| Loot Integrations addons (Awesome Dungeon, Born in Chaos, Ice and Fire, Randomized Loot Compatibility, Yung Structures) | someaddon | ARR | CurseForge metadata only; do not embed the jars. |
| FTB Ranks | FTB | ARR | CurseForge metadata only; do not embed the jar. |
| Fuel Goes Here, Hey Berry! SHUT UP, FlickerFix | LobsterJonn, MutantGumdrop | ARR | CurseForge metadata only; do not embed the jars. |
| Simply Swords, simplyswords create lines | Sweenus, happycookies | Timefall Development License / ARR | CurseForge metadata only; do not embed the jars. |
| Overgeared, Overgeared JEI Compat | stirdrem, DoktorCraft | MIT / Apache-2.0 | CurseForge metadata only; do not embed the jars. |
| Just Enough Professions | Mrbysco, ShyNieke | MIT | CurseForge metadata only; do not embed the jar. |
| Steve's Carts | CreeperHost team | ARR | CurseForge metadata only; do not embed the jar. |
| Logistics Network | Almana21 | ARR | CurseForge metadata only; do not embed the jar. |
| Creeper Overhaul, Enderman Overhaul | joosh_7889 and others | ARR | CurseForge metadata only; do not embed the jars. |
| Gravitational Modulating Additional Unit | gisellevonbingen | MIT | CurseForge metadata only; do not embed the jar. |
| AI Improvements | QueenOfMissiles | MIT | CurseForge metadata only; do not embed the jar. |
| Ars Polymorphia, Ars Unification | qther | LGPL-3.0 | CurseForge metadata only; do not embed the jars. |
| AE2 Network Analyser | GlodBlock | LGPL-3.0 | CurseForge metadata only; do not embed the jar. |
| Industrialization Overdrive, Applied Industrialization | WhitePhantom, Nekomiya_saku | MIT / ARR | CurseForge metadata only; do not embed the jars. |
| Structure Essentials, Leaky, Chunk Sending, Fast Async World Save, Better Fps - Render Distance, fix GPU memory leak | someaddon | ARR | CurseForge metadata only; do not embed the jars. |
| Invasive Optimizations | qther | MIT | CurseForge metadata only; do not embed the jar. |
| In Control! | McJty | MIT | CurseForge metadata only; do not embed the jar. |
| PolyLib | Scorpion911662 | MIT | CurseForge metadata only; do not embed the jar. |
| I'm Fast | Bielhiss | MIT | CurseForge distribution is disabled, so it is **not** metadata-referenced. Embedded from Modrinth. |
| Macaw's Paths and Pavings | sketch_macaw | MIT | CurseForge has no 1.21.1 NeoForge file, so it is **not** metadata-referenced. Embedded from Modrinth. |
| Connectivity | someaddon | ARR | CurseForge metadata only; do not embed the jar. Distributed through CurseForge only. |
| Just Enough Threads | Tonywww | ARR | CurseForge metadata only; do not embed the jar. |
| Visual Workbench | Fuzs | MPL-2.0 | CurseForge reference. |
| MRU | IMB11, Cassian | ARR | CurseForge metadata only; do not embed the jar. |
| Inventory Profiles Next | mirinimi | AGPL-3.0-or-later | CurseForge reference. |
| Rhino | LatvianModder | MPL-2.0 | CurseForge reference. |
| More Overlays Updated | FeldiM2425 (original), RiDGo8 (maintainer) | MIT; author states modpack redistribution is allowed with credit | Keep a credit line naming both authors. The pack references the **Modrinth** file (byte-identical to CurseForge 391382 / 6981252) because the CurseForge API exposes no `downloadUrl` for this project. |
| No Chat Reports | Aizistral | WTFPL | CurseForge reference. |
| Refined Storage - Curios Integration | Refined Mods | MIT | CurseForge reference. |
| MmmMmmMmmMmm (Target Dummy) | MehVahdJukaar and contributors | Supplementaries Team License v1.5 — permits personal use and use "obtained exclusively from Our Sources"; public redistribution of the software is prohibited | Same arrangement as the already-shipped Supplementaries and Amendments: the CurseForge manifest references the official file and the pack never rehosts the jar. Credit the Supplementaries Team. If the pack ever embeds a jar instead of referencing it, remove this mod. |
| Oritech | Rearth | CC0-1.0 (public domain dedication; no rights reserved) | CurseForge reference. Credit Rearth. Some Oritech art is derived from Techarium (CC BY-NC 4.0) and malcolmriley's unused-textures repo (CC BY 4.0); the author credits both in the project description. |
| Applied Oritech | Jiu_Qianqi (beipuo) | MIT | CurseForge reference. Credit the author. |
| Oritech Things | Lumengrid and contributors (Lumengrid, muroalparco, MtcLeo05, DevDyna, Sirios_dev) | **Unverifiable and most likely non-commercial.** The jar's `neoforge.mods.toml` says `license = "CC4.0"` on every published version checked (0.0.9 through 0.0.46), which most plausibly abbreviates CC BY-NC 4.0. The GitHub repository has no real LICENSE file — only an unused NeoForge `TEMPLATE_LICENSE.txt` — and CurseForge reports no license for the project. The user accepted this ambiguity explicitly on 2026-10-02, in the same spirit as the shipped Simply More and Overgeared: Universal Compatibility ARR situation. | **Do not embed this jar.** Keep it CurseForge-metadata-only so the file is fetched from CurseForge, never redistributed by the pack. Credit the author list above. If the author confirms a non-commercial license in writing, decide whether a published MIT pack can carry it at all before the next store release; if they confirm no restriction, record the corrected license here. |
| Create Oritech Compat (recipes ported, mod removed) | FixedDolphin927 (fixdol) | MIT | The mod is **not** shipped. Its 18 Create recipes were ported into `pack/global_packs/required_data/lead-leylines-oritech-create-compat/` and corrected for 1.21.1, so credit the author for the recipe design even though no jar is distributed. Do not re-add the mod while the datapack is in place — the datapack owns this content. |
| Automation and QoL wave (KubeJS build 368, Modern Industrialization, Just Dire Things, routers, jewelry, glyphs, sounds) | See each CurseForge page | Mix of licenses; MRU is ARR | CurseForge metadata; do not embed ARR jars. |

## Future / Deferred Mods

Long lists: [deferred.md](deferred.md).

| Mod | Why not now | What would change that |
|---|---|---|
| TwilightForest Thread Safety Addon | Still 1.20.1 Forge only | 1.21.1 NeoForge file. |
| C2ME OpenCL | Java 25 even on 1.21.1; TerraBlender biome fail; Apple OpenCL unsupported | Pack JVM 25 (separate upgrade) plus TerraBlender-safe OpenCL, or skip. |
| Roxy, voxy-forged | Voxy is out. Roxy needs Fabric Voxy on 1.21.11 and conflicts with voxy-forged. voxy-forged is ARR and cannot ship. | Do not re-add. |

## Deferred Ecosystem Upgrades

| Proposed change | Why a candidate wanted it | Status |
|---|---|---|

## Removed

| Mod | Removed on | Why | Re-add? |
|---|---|---|---|
| Modern Industrialization Extended Integrations (CurseForge 1681995) | 2026-10-04 | Removed on request alongside Pattern Converter. It was healthy (Jade and JEI plugins load, Create-stress hatches work) and nothing in the pack depended on it, but it shipped **23 block loot tables in `modern_industrialization`'s namespace** (`data/modern_industrialization/loot_table/blocks/{iv,ev,superconductor}_*.json`) that drop `modern_industrialization:iv_*_hatch`-style items MI 2.5.8 never registers. Every one of them failed to parse with an ERROR on every boot, and the hatch blocks drop nothing when broken. | Only if Saereth either registers the item forms or drops the loot tables. A pack-side datapack can silence the ERRORs with empty pools, but it cannot give the blocks a drop. |
| Pattern Converter (CurseForge 1311295) | 2026-10-04 | Removed on request. It converts AE2 and Refined Storage patterns, but one of its three converter styles is Integrated Dynamics, which this pack does not carry: its `converter` block model resolves `integrateddynamics:block/logic_programmer_side`, `logic_programmer_top`, and `variablestore_top`, so every client resource reload logged `Missing textures in model patternconverter:converter` for a mod that cannot be added without pulling in a whole unrelated tech tree. It also registered the `patternconverter:converter` block, block entity, item, and a data component, so a world with a placed converter loses it. | Only if Integrated Dynamics is ever added, or if the author gates the ID style behind a config option instead of an always-loaded model. |
| Farmer's Cutting x5 (BetterNether, Twilight Forest, BetterEnd, Oh The Biomes We've Gone, Regions Unexplored) | 2026-10-03 | Ported to `lead-leylines-compat-recipes` (537 `farmersdelight:cutting` recipes). All five JARs contain **zero class files** — they are datapacks packaged as mods. Recipe count before and after removal is identical at 47,540. | No. The ported datapack is byte-identical and verified. |
| Create Regions Unexplored Compat: Crushing | 2026-10-03 | Ported to `lead-leylines-compat-recipes` (30 `create:crushing` recipes). Its only class is an empty-constructor dummy and its access transformer file is 0 bytes. Note this is **not** the same mod as `create-otbwg-compat`, which was also removed the same day. | No. Ported. |
| Create: Oh The Biomes We've Gone Compat | 2026-10-03 | Ported to `lead-leylines-compat-recipes` (86 `create:milling` recipes). **Zero class files** — recipes only. MIT per the JAR's own `neoforge.mods.toml`. CurseForge also reports `allowModDistribution = false`, so `metadata:curseforge` was a latent install failure; the datapack removes that problem. | No. Ported and byte-verified. |
| Create: Sophisticated Backpacks Compat | 2026-10-03 | Ported to `lead-leylines-compat-recipes` (57 `create:milling` recipes). **Zero class files** — recipes only. MIT per the JAR's own `neoforge.mods.toml`. Same `allowModDistribution = false` problem as the mod above. | No. Ported and byte-verified. |
| DarkSleep - RPG Sleep Percentage | 2026-10-03 | Behaviour reimplemented as one vanilla gamerule (`playersSleepingPercentage 50`) in `lead-leylines-load-fixes`. The mod declares **All Rights Reserved**, so no data was copied; only the documented behaviour was reimplemented. | No. A datapack line is not worth a jar. |
| Packet Fixer | 2026-10-01 | Superseded by Connectivity. Both raised the vanilla packet size limit, and together with Disconnect Packet Fix that was three mods patching the same networking internals. | No. Connectivity covers oversized payloads. |
| Disconnect Packet Fix | 2026-10-01 | Superseded by Connectivity; the MC-271325 disconnect-packet class of failure is inside Connectivity's login/play handler mixins. | No. |
| Simply More (CurseForge 1095252) | 2026-10-01 | Never shipped. CurseForge distribution is disabled and the similarly named Modrinth project is a different mod ("Simply m'Ore"); it also hard-requires the Simply Tooltips chain. | If the author enables CurseForge distribution or publishes on Modrinth. |
| Overgeared (CurseForge 1277786) | 2026-10-02 | Removed on request, temporarily. **The reason is a real pack bug, not a preference:** Overgeared 1.6.19 ships stub copies of **44** vanilla recipes under `data/minecraft/recipe/` in which both the ingredient and the result are `minecraft:air`, and 9 of them fail to parse on 1.21.1 (the `{"item": "minecraft:air"}` shape the 1.21.1 `ItemStack` codec rejects). Those 9 were logging a `Parsing error loading recipe` ERROR on every server boot, and the practical effect is that **vanilla diamond armor had no crafting recipe at all**. The other 35 stubs covered all gold, iron and stone tool and armor recipes, `netherite_ingot`, `bucket`, `cauldron`, `shears`, `flint_and_steel`, `arrow` / `spectral_arrow` / `tipped_arrow`, and three iron blast recipes. Verified after removal: recipe-parse errors went 9 → **0**. | If the author ships a 1.21.1 build that stubs those recipes in a parseable form, or stops stubbing them. Re-adding means re-testing for the same 9 errors first. |
| Overgeared addons (5 mods) | 2026-10-02 | Removed with Overgeared because every one declares it as a **required** dependency, so none can stay: Overgeared JEI Compat (`overgeared [1,)`, plus JEI), Overgeared x Ice and Fire (`overgeared [1.21.1-1.6.17,)`, plus Ice and Fire), OvergearedXSimplySwords (`overgeared [1.0.0,)`, plus Simply Swords), Overgearium (`overgeared [0,)`), and Overgeared: Universal Compatibility (`overgeared [1.0,)`). Nothing outside the family depended on Overgeared, and no Overgeared config, KubeJS script, or datapack referenced it, so the removal left no orphans. | With Overgeared. Simply Swords and Ice and Fire both stay in the pack, they only lose their Overgeared forging variants. |
| Overgeared: Universal Compatibility (CurseForge 1651686) | 2026-10-02 | Superseded by the row above. It **did** ship from 2026-10-01, pinned by direct CurseForge CDN URL because `allowModDistribution = false` and it is not on Modrinth; the earlier "never shipped" note on this row was stale. | — |
| Extended Oritech (CurseForge 1390979) | 2026-10-02 | Installed, then removed in the same session. Hard `NoClassDefFoundError: rearth/oritech/client/ui/BasicMachineScreenHandler` at mod construction; the class was removed from Oritech before 1.2.6 and Extended Oritech 1.1.2 was built in Dec 2025 against Oritech 1.0.x. No working version pair exists, because pinning Oritech to 1.0.x would break Applied Oritech and Oritech Things. | Only if the author ships a build against Oritech 1.2.x or later. |
| Create Oritech Compat (CurseForge 1211589) | 2026-10-02 | Installed, then removed in the same session. 14 of its 18 recipes shipped in the pre-1.21.1 `"item"` ingredient format and could not load, causing 14 recipe-parse ERROR lines per boot; a 15th referenced a tag that no longer exists. The content was worth keeping, so it was ported to `pack/global_packs/required_data/lead-leylines-oritech-create-compat/` and corrected. | No, not while the ported datapack is in place. It would re-add 14 broken recipes and duplicate working ones. |
| Epic Fight Compat (CurseForge 1704141) | 2026-10-01 | Never shipped. Its CurseForge project has `allowModDistribution = false` and the author publishes only there, so a metadata reference would not download for players and rehosting the jar would break the author's choice. The pack already runs CompatLink Epic Fight Weapons Compat for the same goal, plus 11 other Epic Fight bridges. | If the author enables CurseForge distribution or publishes on Modrinth. |
| Just Zoom (CurseForge 561885) | 2026-10-01 | Never shipped. License is DSMSLv3 ("Don't Sell My Mods"), which does not grant redistribution in a published pack, and it hard-requires Konkrete, which the pack does not carry. | Only with an OSI-style license. |
| Library Ferret - NeoForge (CurseForge 522351 / 6118136) | 2026-10-01 | packwiz pulled a second, CurseForge-sourced entry for a library the pack already tracks from Modrinth. The existing `library-ferret.pw.toml` pin was kept. | No. The Modrinth pin covers it. |
| TaCZ x Guns Lights Addon | 2026-09-25 | Removed on request. No other mod required it. | No. |
| TaCZ: Blueprints Reforged | 2026-09-25 | Removed on request. World data: placed blueprint items will be missing. No other mod required it. | No. |
| JEI++ | 2026-09-23 | Client join crash: `BookmarkOverlayMixin` needs `mezz.jei.gui.input.IUserInputHandler`, moved in JEI 19.57. Latest file 1.0.5 still targets JEI 19.56. | Only with a JEI 19.57 build. |
| Epic Fight Nightfall, Invincible Lib | 2026-09-23 | Nightfall reads client VFX config on dedicated servers and crashes when mobs gain effects. AAA Particles stays. | Only with a dedicated-server fix. |
| Ecliptic Seasons : Voxy Compact, Voxy - Make it compatible | 2026-09-23 | Mixin crash when the unofficial Voxy client jar is not installed. Voxy cannot ship in the pack. | No. Voxy itself was removed on 2026-09-24. |
| Voxy, Voxy Server Side, Forgified Fabric API | 2026-09-24 | Distant LOD removed on request. Forgified Fabric API existed only for the local Voxy renderer. No other installed mod depends on it. | No. |
| Mekanism Covers | 2026-09-23 | Client join crash: `SodiumBlockRendererMixin.putTranslucentVertexColor` fails on Sodium 0.8.13 (0 targets). Latest file still 1.3-BETA (2025-01-10). Author's `disableAdvancedCoverRendering` config does not skip the mixin. World data. | Only with a Sodium 0.8-compatible build. |
| Entire 1.20.1 Forge pack | 2026-09-17 | Loader and Minecraft cutover. History is on `forge-1.20.1`. | Research each mod again for 1.21.1 NeoForge. |
| EMI, EMI Ores, EMI Enchanting, EMI QoL Tweaks, TMRV | 2026-09-22 | TMRV's fake JEI 19.27 failed Polymorph (≥19.52) and Sophisticated (≥19.32). Replaced with real JEI. | No while JEI is the viewer. |
| Iris Flywheel Compat | 2026-09-22 | Mixin conflict with Colorwheel (`irisflw` any). Colorwheel is the Create + Iris path for Euphoria. | No while Colorwheel is in. |
| TerraBlender (Forge) | 2026-09-22 | Packwiz pulled `563928` as a Cave Biomes dep. Pack uses TerraBlender NeoForge `940057` only. | No; would crash next to the NeoForge jar. |
| Tectonic | 2026-09-22 | Terrain overhaul removed on request. Lithostitched stays for RU and Terralith. Already-generated Tectonic chunks stay until regenerated. | Only with a new worldgen plan. |
| Embeddium, Oculus, Radium | 2026-09-17 | No 1.21.1 NeoForge ports we will ship. | No; Sodium / Iris / Lithium are the replacements. |
| Noisium | 2026-09-18 | Bye?Pregen! marks Noisium incompatible. | No while ByePregen is in. |
| Achievements Optimizer | 2026-09-18 | Overlaps Cerulean (Icterine fork with the same every-few-ticks option). | No while Cerulean is in. |
| C2ME OpenCL | 2026-09-18 | Java 25 class files on a Java 21 pack; TerraBlender listed as biome-placement fail. | No while Java 21. |
| Fast Noise | 2026-09-18 | Tectonic CPS A/B: 7.62 vs 7.73 baseline. | No for CPS. |
| ScalableLux | 2026-09-18 | Tectonic CPS A/B: 4.89 vs 7.73 baseline; lighting analysis errors. | No for CPS. |
| Create Aeronautics, Sable | 2026-09-30 | Physics-vehicle tech removed on request. Sable is the physics sub-level library and had no other use in the pack. World data: existing contraptions, vehicles, and Sable sub-levels in an old world stay in the save and must be deleted by hand. | Only as a deliberate return of the vehicle layer. |
| Create Aeronautics addons and compat | 2026-09-30 | Removed with Create Aeronautics: Climbable Ropes for Create Aeronautics, Create Aeronautics x Curios API Compat, Create Aeronautics: Mekanism Compatibility, Create - Xaero's map (Sable map overlay), Jade Sable Compat, TACZ Aeronautics compat, Point Blank Aeronautics compat, Iron's Spells x Aeronautics. All existed only to teach another mod about Aeronautics. Every remaining reference to `sable` / `aeronautics` in the pack (Colorwheel, Create Big Cannons, Spawn, ParCool compat) is `type = "optional"` in that mod's `neoforge.mods.toml`, so nothing else breaks. | Only alongside Create Aeronautics. |
| JEIOptimizer | 2026-09-28 | Replaced by Just Enough Threads — both mods target the same JEI startup routines and running both risks instability. Built against JEI 19.56 while pack has 19.57. | No while Just Enough Threads is in. |
| Just Enough Threads 0.14.1 | 2026-09-30 | JEI 19.57 killed the whole recipe viewer: `JeiNativeSearchBuilderMixin` wraps `ISearchStorageBuilder.build()` inside the 1-arg `ElementSearch(ElementPrefixParser)` constructor, which JEI replaced with a 3-arg form. The injection is `require = 1`, so the missing target throws `InvalidInjectionException` and JEI reports `RuntimeException: JEI failed to start`. The game keeps running, so JEI was silently dead. JET 0.14.1's own guard only checked that *some* `<init>` calls `build()`, which is still true, so it did not step aside as its changelog promised. Not fixable by downgrading JEI: that constructor is gone from 19.42 onward, while five mods independently floor JEI at 19.51-19.54 (ldlib2, Polymorph, FTB XMod Compat, Sophisticated JEI Index, JEI Stuff). | **Re-added 2026-10-01 as 0.14.2**, which fixes the guard. See the 2026-10-01 wave row. |

## JEI startup optimization

Resolved 2026-10-01: JET 0.14.2 is back in. The 2026-09-30 removal traded a silent dead JEI for a multi-minute client freeze while joining a world — that client run logged `Registering recipes took 7.165 minutes`, with JET's own stall watchdog flagging 88s on a single stage — so the slow index was the lesser evil. 0.14.2's guard now compares the exact `ElementSearch` constructor descriptor, so it adapts to the 3-arg form instead of throwing.

Still unverified: **the client path.** The dedicated-server smoke test never loads a `client`-side mod, so the JEI 19.57 regression must be confirmed from a Prism client boot — check `latest.log` for `JEI native bulk builder disabled: ElementSearch has no verified single-argument constructor build call; retaining native storage` (the fix working) and that JEI opens. If JET ever misbehaves, `config/justenoughthreads-client.toml` with `enabled = false` restores stock JEI without removing the jar.
