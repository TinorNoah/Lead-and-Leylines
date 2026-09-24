# Lead and Leylines — mod manifest

Synced with `pack/mods/*.pw.toml` on 2026-09-22. Minecraft, loader, and pack version: see [`pack/pack.toml`](../../pack/pack.toml). Decision logs: [performance.md](performance.md), [utility.md](utility.md), [storage.md](storage.md), [nether.md](nether.md), [worldgen.md](worldgen.md), [content.md](content.md). Config notes: [configs.md](configs.md). Distribution: [distribution.md](distribution.md). Not-yet-added candidates and remaining Forge mods: [deferred.md](deferred.md).

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
| Smooth Chunk Save | `smoothchunk-1.21-4.1.jar` | CurseForge 582327 / 6296628 | both | IO | Spreads chunk saves. | Cupboard | defaults | 2026-09-17 |
| Cupboard | `cupboard-1.21.1-4.2.jar` | CurseForge 326652 / 8889050 | both | library | Smooth Chunk Save dependency. | none | defaults | 2026-09-17 |
| BadOptimizations | `BadOptimizations-2.4.1-1.21.1.jar` | CurseForge 949555 / 7338300 | client | renderer | Client skip work. | none | defaults | 2026-09-17 |
| Dynamic FPS | `dynamic-fps-3.11.4+minecraft-1.21.0-neoforge.jar` | CurseForge 335493 / 7546938 | client | client QoL | Lowers FPS when unfocused. | none | defaults | 2026-09-17 |
| Crash Assistant | `CrashAssistant-neoforge-1.20.6-1.21.4-1.11.12.jar` | CurseForge 1154099 / 8636685 | client | stability | Crash dump helper (client-only). | none | defaults | 2026-09-17 |
| Entity Culling | `entityculling-neoforge-1.11.2-mc1.21.1.jar` | CurseForge 448233 / 8942303 | client | renderer | Occlusion culling. | none | defaults | 2026-09-17 |
| Sodium Extra | `sodium-extra-neoforge-0.9.4+mc1.21.1.jar` | CurseForge 447673 / 8892306 | client | renderer | Official Sodium extras (fog, particles, FPS overlay). Not Chloride. | Sodium (client) | See [configs.md](configs.md) if leaves stack with More Culling | 2026-09-18 |
| Flerovium | `flerovium-neoforge-1.21.1-1.1.3-all.jar` | CurseForge 1142875 / 8862415 | client | renderer | Item/entity/particle draw. Not Better Block Entities. | Sodium (client) | defaults | 2026-09-18 |
| AsyncParticles | `AsyncParticles-21.1.4.4+1.21.1.jar` | CurseForge 1215753 / 8887358 | client | renderer | Particle thread. Not Particle Core. | none (Cloth optional) | defaults | 2026-09-18 |
| More Culling | `moreculling-neoforge-1.21.1-1.0.10.jar` | CurseForge 630104 / 8833217 | client | renderer | Extra culling next to Entity Culling. | Cloth Config | See [configs.md](configs.md) | 2026-09-18 |
| Cloth Config | `cloth-config-15.0.140-neoforge.jar` | CurseForge 348521 / 5729127 | both | library | More Culling dependency. | none | defaults | 2026-09-18 |
| Structure Layout Optimizer | `structure_layout_optimizer-neoforge-1.0.12.jar` | CurseForge 1087831 / 7439136 | both | worldgen | Jigsaw/NBT structure gen. | Resourceful Config | defaults | 2026-09-18 |
| Resourceful Config | `resourcefulconfig-neoforge-1.21-3.0.11.jar` | CurseForge 714059 / 6467772 | both | library | SLO dependency. | none | defaults | 2026-09-18 |
| Ksyxis | `Ksyxis-1.4.4.jar` | CurseForge 537533 / 8891330 | both | worldgen | Unloads unused spawn chunks. | none | defaults | 2026-09-18 |
| Disconnect Packet Fix | `disconnect-packet-fix-neoforge-2.0.1.jar` | CurseForge 1173964 / 6064142 | both | stability | MC-271325 disconnect packets. | none | defaults | 2026-09-18 |
| quick pack | `quick-pack-neoforge-1.5.0+1.21.1.jar` | CurseForge 1380888 / 8619206 | both | IO | Faster zip pack parse. | none | defaults | 2026-09-18 |
| CrashExploitFixer | `crashexploitfixer-neoforge-2.0.0+1.21.4.jar` | CurseForge 1079896 / 8071070 | both | stability | Server crash-exploit filter; file tags 1.21.1–1.21.4. | none | defaults | 2026-09-18 |
| Async Logger | `asynclogger-2.2.2+1.21.1-neoforge.jar` | CurseForge 1491426 / 8631010 | client | IO | Async log writes. | none | defaults | 2026-09-18 |
| ResourcePackCached | `rpc-1.2.5+1.20.5-1.21.4-neoforge.jar` | CurseForge 1125284 / 7602181 | client | client QoL | Keeps server resource packs across rejoins. | none | defaults | 2026-09-18 |
| Chunk Pregenerator | `Chunk-Pregenerator-Neoforge-1.21-4.5.4.jar` | CurseForge 267193 / 8748909 | both | worldgen | Operator pregen. | Carbon Config | defaults | 2026-09-18 |
| Carbon Config | `CarbonConfig-Neoforge-1.21.1-2.0.2.1.jar` | CurseForge 898104 / 8119979 | both | library | Chunk Pregenerator dependency. | none | defaults | 2026-09-18 |
| Create | `create-1.21.1-6.0.10.jar` | CurseForge 328085 / 7963363 | both | tech | Contraptions and kinetics. | none (Flywheel embedded) | defaults | 2026-09-18 |
| Sable | `sable-neoforge-1.21.1-2.0.5.jar` | CurseForge 1312371 / 8673825 | both | library | Physics sub-levels for Aeronautics. Mixin-heavy. | none (ImGuiMC optional, not added) | defaults | 2026-09-22 |
| Create Aeronautics | `create-aeronautics-bundled-1.21.1-1.3.2.jar` | CurseForge 676721 / 8763471 | both | tech | Planes, airships, vehicles. World data. Iris visual issues. | Create, Sable | defaults | 2026-09-22 |
| Create Regions Unexplored Compat: Crushing | `create_ru_compat-1.0.0.jar` | CurseForge 1431845 / 7469182 | both | tech | Crushing recipes for RU blocks. | Create, RU | defaults | 2026-09-22 |
| Create: Oh The Biomes We've Gone Compat | `create-otbwg-compat-1.0.jar` | CurseForge 1285600 / 6645097 | both | tech | Create recipes for OTBWG. File also tags 1.20.1 Forge. | Create, OTBWG | defaults | 2026-09-22 |
| Ametrin API | `ametrin-1.21.1-0.2.4.jar` | CurseForge 670599 / 5608814 | both | library | Required by Block Variants. Pinned 1.21.1; later files are 1.21.11. | none | defaults | 2026-09-22 |
| Block Variants | `block_variants-1.21.1-6.1.1.jar` | CurseForge 481119 / 8581915 | both | content | Extra block variants. World data. | Ametrin | defaults | 2026-09-22 |
| Block Variants - Oh The Biomes We've Gone | `block_variants_bwg-1.21.1-1.0.1.jar` | CurseForge 1503165 / 8705273 | both | content | OTBWG wood variants. World data. | Block Variants, OTBWG | defaults | 2026-09-22 |
| Create Better FPS | `createbetterfps-1.21.1-1.1.5.jar` | CurseForge 1217518 / 8908301 | client | renderer | Create FPS with shader packs. Compatible with Colorwheel. | Create | defaults | 2026-09-18 |
| Create: Threaded Trains | `createthreadedtrains-neoforge-1.21.1-1.0.0.jar` | CurseForge 1381890 / 7208558 | both | optimizer | Train network off the server thread. | Create | See [configs.md](configs.md) | 2026-09-18 |
| Architectury API | `architectury-13.0.11-neoforge.jar` | CurseForge 419699 / 8492726 | both | library | FTB dependency. | none | defaults | 2026-09-18 |
| FTB Library | `ftb-library-neoforge-2101.1.36.jar` | CurseForge 404465 / 8858846 | both | library | FTB Quests/Teams. | Architectury | defaults | 2026-09-18 |
| FTB Teams | `ftb-teams-neoforge-2101.1.11.jar` | CurseForge 404468 / 8724782 | both | utility | Shared quest progress. | FTB Library, Architectury | defaults | 2026-09-18 |
| FTB Quests | `ftb-quests-neoforge-2101.1.36.jar` | CurseForge 289412 / 8885017 | both | quests | Quest book. | FTB Library, FTB Teams, Architectury | defaults | 2026-09-18 |
| FTB Quests Optimizer | `FTBQuestsOptimizer-neoforge-3.2.0-1.21.1.jar` | CurseForge 912469 / 7576461 | both | optimizer | Quest tick cost. | FTB Quests | See [configs.md](configs.md) | 2026-09-18 |
| Pipez | `pipez-neoforge-1.21.1-1.2.31.jar` | CurseForge 443900 / 8351631 | both | logistics | Item/fluid/energy pipes. | none | defaults | 2026-09-18 |
| Pipez Lag Fix | `pipezlagfix-1.21.1-1.1.0.jar` | CurseForge 1446489 / 8113984 | both | optimizer | Eco mode when item-pipe destinations are full. | Pipez | defaults | 2026-09-18 |
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
| Just Enough Items (JEI) | `jei-1.21.1-neoforge-19.57.0.447.jar` | CurseForge 238222 / 8946440 | both | recipes | Recipe viewer. Replaces EMI + TMRV so Polymorph (≥19.52) and Sophisticated (≥19.32) get a real JEI version. Server side registers the recipe-transfer channel Move Items uses. | MezzConfig | defaults | 2026-09-22 |
| MezzConfig | `mezz_config-1.21.1-neoforge-0.6.3.jar` | CurseForge 1689768 / 8932688 | both | library | Required by current JEI on both sides. | none | defaults | 2026-09-22 |
| JEI / REI / EMI WorldGen | `jeiworldgen-neoforge-1.21.1-1.4.5.jar` | CurseForge 1509527 / 8897773 | both | recipes | Worldgen pages in JEI. Server side sends the data the client displays. | JEI | defaults | 2026-09-23 |
| AE2 JEI Integration | `ae2jeiintegration-1.2.1.jar` | CurseForge 1074338 / 7727898 | client | recipes | Extra AE2 JEI pages. | JEI, AE2 | defaults | 2026-09-22 |
| Refined Storage - JEI Integration | `refinedstorage-jei-integration-neoforge-1.0.0.jar` | CurseForge 1230497 / 6359014 | client | recipes | RS recipe transfer. 2.0.x is Minecraft 26.1.2. | JEI, RS | defaults | 2026-09-22 |
| JEIOptimizer | `jeioptimizer-1.21.1-1.2.0-19.56.jar` | CurseForge 1570444 / 8872445 | client | recipes | Faster JEI filter on join. ARR. Built against JEI 19.56; pack has 19.57. | JEI | defaults | 2026-09-22 |
| Sophisticated JEI Index | `sophisticated_jei_index-1.2.3+1.21.1.jar` | CurseForge 1482785 / 8848988 | client | recipes | Backpack recipe transfer. | JEI, Sophisticated | defaults | 2026-09-22 |
| Smithing Template Viewer | `smithingtemplateviewer-1.0.4.jar` | CurseForge 1133580 / 7452053 | client | recipes | Armor trim preview. 1.1.0 is 26.1.2-only. | JEI | defaults | 2026-09-22 |
| Create JEI Compat | `createjeicompat-1.0.3.jar` | CurseForge 1422344 / 8534122 | client | recipes | Paginated sequenced assembly (7+ steps). | JEI, Create | defaults | 2026-09-22 |
| JEI Stuff | `jeistuff-1.21.1-1.2.1.jar` | CurseForge 978621 / 8938121 | both | recipes | Extra JEI helpers. Required network channels need the jar on dedicated servers. | JEI | defaults | 2026-09-23 |
| JEI QuickCraft | `jei-quickcraft-1.21.1-neoforge-1.0.jar` | CurseForge 1520978 / 8429819 | both | recipes | Craft from JEI using inventory. ARR. Required network channels need the jar on dedicated servers. | JEI | defaults | 2026-09-23 |
| SpectrumJEI | `SpectrumJEI-21.1.11.1+neoforge.jar` | CurseForge 1258607 / 8752438 | client | recipes | Spectrum pages in JEI. | JEI, Spectrum | defaults | 2026-09-22 |
| FTB JEI Extras | `ftb-jei-extras-21.1.7.jar` | CurseForge 1103259 / 6695679 | client | recipes | FTB quest/filter pages in JEI. | JEI, FTB | defaults | 2026-09-22 |
| MekaGenJei | `mekagenjei-1.2.jar` | CurseForge 1347827 / 7224975 | client | recipes | Mekanism Generators JEI pages. | JEI, Mekanism Generators | defaults | 2026-09-22 |
| Just Enough Mekanism Multiblocks | `JustEnoughMekanismMultiblocks-1.21.1-7.21.jar` | CurseForge 898746 / 8903943 | client | recipes | Multiblock overlays in JEI. | JEI, Mekanism | defaults | 2026-09-22 |
| Mekanism: Ponders | `mekanism_ponders-1.0.3-1.21.1.jar` | CurseForge 1448575 / 8007326 | client | recipes | Create ponder scenes for Mekanism. | Create, Mekanism | defaults | 2026-09-22 |
| Just Enough TaCZ | `just_enough_tacz-1.2.0.jar` | CurseForge 1536413 / 8180476 | client | recipes | TaCZ gun recipes in JEI. | JEI, TaCZ, Berezka's library | defaults | 2026-09-22 |
| Just Enough Resources (JER) | `JustEnoughResources-NeoForge-1.21.1-1.6.0.17.jar` | CurseForge 240630 / 6506298 | client | recipes | Ore/mob pages in JEI. Not Fabric 26.x. | JEI | defaults | 2026-09-22 |
| GeckolibBetterFPS | `gbf-1.21.1-1.0.2.jar` | CurseForge 1455983 / 8582640 | client | optimizer | Faster GeckoLib entity rendering. Alpha. | GeckoLib | defaults | 2026-09-18 |
| Terralith | `Terralith_1.21.x_v2.6.2.jar` | CurseForge 513688 / 8222737 | both | worldgen | Overworld biomes. World data. | Lithostitched | `pack/config/terralith.json` terrain slabs off | 2026-09-18 |
| Feature Recycler | `Feature-Recycler-neoforge-2.0.0.jar` | CurseForge 1077985 / 5829420 | both | worldgen | Reorders biome features so Terralith + OTBWG do not crash. ARR. | none | defaults | 2026-09-18 |
| Nullscape | `Nullscape_1.21.x_v1.2.14.jar` | CurseForge 570354 / 7078265 | both | worldgen | End overhaul. World data. | none | defaults | 2026-09-18 |
| YACL | `yet_another_config_lib_v3-3.8.2+1.21.1-neoforge.jar` | CurseForge 667299 / 7437845 | both | library | Required by Structurify. | none | defaults | 2026-09-18 |
| Structurify | `structurify-neoforge-2.0.37+mc1.21.1.jar` | CurseForge 1087551 / 8888619 | both | worldgen | Structure spacing. | YACL | global multiplier 2.0 | 2026-09-18 |
| When Dungeons Arise | `DungeonsArise-1.21.1-2.1.68-release.jar` | CurseForge 442508 / 7150870 | both | worldgen | Extra dungeons. World data. ARR. | none | defaults | 2026-09-18 |
| When Dungeons Arise - Seven Seas | `DungeonsAriseSevenSeas-1.21.x-1.0.4-neoforge.jar` | CurseForge 953637 / 7142896 | both | worldgen | Ocean structures. World data. ARR. | none | defaults | 2026-09-18 |
| Library Ferret | `libraryferret-neoforge-1.21.1-4.0.0.jar` | Modrinth DOB2l4oJ / AKcIMUil | both | library | Required by Awesome Dungeon. No CF NeoForge 1.21.1 file. ARR. | none | defaults | 2026-09-18 |
| Awesome Dungeon | `awesomedungeon-neoforge-1.21.1-3.2.0.jar` | Modrinth ptzsjBKT / 5vFWzKiI | both | worldgen | Extra dungeons. World data. ARR. | Library Ferret | defaults | 2026-09-18 |
| YUNG's API (NeoForge) | `YungsApi-1.21.1-NeoForge-5.1.9.jar` | CurseForge 1015100 / 8894736 | both | library | Required by YUNG's structure mods. | none | defaults | 2026-09-18 |
| YUNG's Better Caves | `YungsBetterCaves-1.21.1-NeoForge-3.1.6.jar` | CurseForge 340583 / 8806071 | both | worldgen | Cave overhaul. World data. | YUNG's API | defaults | 2026-09-18 |
| YUNG's Cave Biomes | `YungsCaveBiomes-1.21.1-NeoForge-3.1.1.jar` | CurseForge 1111586 / 6913179 | both | worldgen | Cave biomes. World data. Packwiz tried to pull TerraBlender Forge `563928`; that was removed. Use NeoForge `940057`. | YUNG's API, GeckoLib, TerraBlender NF | defaults | 2026-09-22 |
| Codxlib | `codxlib-1.6.1-neoforge+1.21.1.jar` | CurseForge 1633207 / 8893360 | both | library | Required by Alex's Caves Continued. Not Citadel. | none | defaults | 2026-09-22 |
| Alex's Caves Continued | `alexscaves-1.1.1-neoforge+1.21.1.jar` | CurseForge 1645389 / 8918377 | both | worldgen | Cave biomes. World data. | Codxlib | defaults | 2026-09-22 |
| Compat API | `compatapi-1.0.3.jar` | CurseForge 1393220 / 7767181 | both | library | Required by Compat Structure. | none | defaults | 2026-09-22 |
| Compat Structure | `compatstructures-1.0.3.jar` | CurseForge 1248133 / 7768220 | both | worldgen | Extra structures. World data. | Compat API | defaults | 2026-09-22 |
| Bad Wither No Cookie - Reloaded | `bwncr-neoforge-1.21.1-3.20.4.jar` | CurseForge 261251 / 8135209 | client | QoL | Mutes wither/dragon/raid music. | none | defaults | 2026-09-22 |
| Ecliptic Seasons | `EclipticSeasons-1.21.1-neoforge-0.15.0-rc-3-1.jar` | CurseForge 1118306 / 8849038 | both | seasons | Solar-term seasons. World data. ARR. | none | defaults | 2026-09-22 |
| Ecliptic Seasons : Bundles | `EclipticSeasons-Bundles-0.18.0.3.jar` | CurseForge 1449802 / 8946676 | both | seasons | Crop/datapack seasonal packs. | Ecliptic Seasons | defaults | 2026-09-22 |
| Ecliptic Seasons: MultiMod Patch | `Ecliptic-Seasons-MultiMod-Patch-1.21.1-neoforge-0.32.1.jar` | CurseForge 1316748 / 8813347 | both | seasons | Extra mod seasonal hooks. | Ecliptic Seasons | defaults | 2026-09-22 |
| Serene Seasons API Stub | `ecliptic-seasons-serene-api-bridge-1.21.1-neoforge-10.1.0.3-patch11-1.jar` | CurseForge 1476693 / 8828410 | both | seasons | Lets Serene-Seasons-API mods talk to Ecliptic. Do not add Serene Seasons. | Ecliptic Seasons | defaults | 2026-09-22 |
| SeasonHud | `seasonhud-neoforge-1.21.1-2.0.10.jar` | CurseForge 690971 / 8778897 | client | HUD | Season on HUD / Xaero. | none (ES optional) | defaults | 2026-09-22 |
| YUNG's Better Nether Fortresses | `YungsBetterNetherFortresses-1.21.1-NeoForge-3.1.5.jar` | CurseForge 1015118 / 6606621 | both | worldgen | Fortress overhaul. World data. | YUNG's API | defaults | 2026-09-18 |
| YUNG's Bridges | `YungsBridges-1.21.1-NeoForge-5.1.1.jar` | CurseForge 1015149 / 5812553 | both | worldgen | River bridges. World data. | YUNG's API | defaults | 2026-09-18 |
| Moog's Structure Lib | `MoogsStructureLib-neoforge-1.21.1-3.3.1.jar` | CurseForge 1337167 / 8885814 | both | library | Required by Moog's Mineshafts. | none | defaults | 2026-09-18 |
| MMR - Moog's Mineshafts Reimagined | `MoogsMineshaftsReimagined-1.21-1.0.3.jar` | Modrinth z25hqseO / gQlqjs2o | both | worldgen | Mineshaft overhaul. World data. | Moog's Structure Lib | defaults | 2026-09-18 |
| Epic Structures: Villages | `epic-structures-villages-2.0.0.jar` | CurseForge 1308486 / 8830175 | both | worldgen | Village overhaul. World data. ARR. | none | defaults | 2026-09-18 |
| Epic Structures: Witch Huts | `Epic Witch Huts v1.3.1.jar` | CurseForge 1335768 / 8383193 | both | worldgen | Witch hut overhaul. World data. ARR. | none | defaults | 2026-09-18 |
| Epic Structures: Jungle Temples | `Epic Jungle Temples v1.0.2.jar` | CurseForge 1600197 / 8611815 | both | worldgen | Jungle temple overhaul. World data. ARR. | none | defaults | 2026-09-18 |
| Amplified Nether | `Amplified_Nether_26.2_v1.2.16.jar` | CurseForge 552176 / 8425271 | both | worldgen | Taller Nether. World data. | none | defaults | 2026-09-18 |
| Infernal Expansion Redux | `infernalexp-neoforge-1.21.1-0.3.16.jar` | CurseForge 1407992 / 8916189 | both | worldgen | Nether biomes. World data. | Lithostitched, GeckoLib | defaults | 2026-09-18 |
| Countered's Terrain Slabs | `terrain_slabs-neoforge-3.1.2.jar` | CurseForge 1125437 / 8216091 | both | worldgen | Terrain slabs. World data. | Architectury | defaults | 2026-09-18 |
| Fragmentum (NeoForge) | `fragmentum-5.0.0+1.21.1-neoforge.jar` | CurseForge 1123977 / 8921953 | both | library | Required by Aquamirae. | none | defaults | 2026-09-18 |
| Aquamirae | `aquamirae-neoforge-1.21.1-7.2.10.jar` | Modrinth k23mNPhZ / iUPJ8ziU | both | content | Ocean structures and boss. World data. | GeckoLib, Fragmentum | defaults | 2026-09-18 |
| FastBoot | `fastboot-1.21.x-v1.3neo.jar` | CurseForge 1030285 / 6998687 | client | optimizer | Early-load mixins; skips per-version data conversion on boot. ARR. | none | defaults | 2026-09-18 |
| Fluidium | `fluidium-1.21.1-1.4.0.jar` | CurseForge 1306029 / 7481400 | both | optimizer | Distant fluid ticks delayed (default 32 blocks, 50% skip). Claimed/force-loaded chunks stay full-speed. | Duplicationless | defaults | 2026-09-18 |
| Duplicationless | `duplicationless-1.21.1-1.2.1.jar` | CurseForge 1380105 / 8646414 | both | library | Required by Fluidium (`mandatory=true` `[1.1.5,)`). Not DoesPotatoTick. | none | defaults | 2026-09-18 |
| LC²H [Lost Cities: Multithreaded] | `lc2h-omni-4.2.4-LTS.jar` | CurseForge 1325431 / 8928853 | both | worldgen | Async Lost Cities gen. Omni jar tags 1.21.1 NeoForge. BRSSLA V2.0.0. | Lost Cities, Quantified API | defaults | 2026-09-18 |
| Quantified API | `quantified api-omni-2.2.3.jar` | CurseForge 1397967 / 8830709 | both | library | Required by LC²H (`quantified` `[2.2.2,)`). Omni jar tags 1.21.1 NeoForge. | none | defaults | 2026-09-18 |
| BiomeSpy | `biomespy-neoforge-1.21.1-1.3.3.jar` | CurseForge 1376024 / 7488072 | both | worldgen | Faster `/locate` biome/structure search. No worldgen change. | none | defaults | 2026-09-18 |
| DarkSleep - RPG Sleep Percentage | `darksleep-neoforge-1.21.1-1.0.1.jar` | CurseForge 1106281 / 5741536 | both | QoL | Sets `playersSleepingPercentage` to 50 on load. ARR. | none | defaults | 2026-09-18 |
| MemGuard | `memguard-1.0.4.jar` | CurseForge 1468440 / 8192435 | both | stability | Lightweight heap-usage log after Create 6 mixin strip. Complements AllTheLeaks. | none | defaults | 2026-09-18 |
| Balm | `balm-neoforge-1.21.1-21.0.65.jar` | CurseForge 531761 / 8645517 | both | library | Waystones, Crafting Tweaks, TrashSlot, Default Options. | none | defaults | 2026-09-18 |
| Iceberg | `Iceberg-1.21.1-neoforge-1.3.2.jar` | CurseForge 520110 / 6423863 | both | library | Equipment Compare, Item Borders. | none | defaults | 2026-09-18 |
| Prism | `Prism-1.21.1-neoforge-1.0.11.jar` | CurseForge 638111 / 6372979 | both | library | Item Borders. | none | defaults | 2026-09-18 |
| Curios API | `curios-neoforge-9.5.1+1.21.1.jar` | CurseForge 309927 / 6529130 | both | library | Elytra Slot (and later Ars). | none | defaults | 2026-09-18 |
| Caelus API | `caelus-neoforge-7.0.1+1.21.1.jar` | CurseForge 308989 / 5694215 | both | library | Elytra Slot. | none | defaults | 2026-09-18 |
| Bookshelf | `bookshelf-neoforge-1.21.1-21.1.81.jar` | CurseForge 228525 / 7606240 | both | library | Botany Pots/Trees. | none | defaults | 2026-09-18 |
| Prickle | `prickle-neoforge-1.21.1-21.1.11.jar` | CurseForge 1023259 / 6961457 | both | library | Botany Pots/Trees. | none | defaults | 2026-09-18 |
| Moonlight Lib | `moonlight-1.21.1-3.6.8-neoforge.jar` | CurseForge 499980 / 8941470 | both | library | Supplementaries, Amendments. | none | defaults | 2026-09-18 |
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
| Waystones | `waystones-neoforge-1.21.1-21.1.45.jar` | CurseForge 245755 / 8873000 | both | utility | Teleport stones. World data. | Balm | defaults | 2026-09-18 |
| AppleSkin | `appleskin-neoforge-mc1.21-3.0.9.jar` | CurseForge 248787 / 7854442 | both | QoL | Hunger/saturation HUD. | none | defaults | 2026-09-18 |
| Mouse Tweaks | `MouseTweaks-neoforge-mc1.21-2.26.1.jar` | CurseForge 60089 / 5637846 | client | QoL | Inventory drag-transfer. | none | defaults | 2026-09-18 |
| ETF | `entity_texture_features-7.2.4-1.21-neoforge.jar` | CurseForge 568563 / 8908931 | client | renderer | Entity texture variants. | none | defaults | 2026-09-18 |
| EMF | `entity_model_features-3.3.9-1.21-neoforge.jar` | CurseForge 844662 / 8909425 | client | renderer | Entity model variants. | ETF | defaults | 2026-09-18 |
| Athena | `athena-neoforge-1.21.1-4.0.6.jar` | CurseForge 841890 / 8061947 | both | library | Connected textures. | none | defaults | 2026-09-18 |
| Crafting Tweaks | `craftingtweaks-neoforge-1.21.1-21.1.11.jar` | CurseForge 233071 / 8697050 | both | QoL | Crafting grid buttons. | Balm | defaults | 2026-09-18 |
| Controlling | `Controlling-neoforge-1.21.1-19.0.5.jar` | CurseForge 250398 / 6368976 | client | QoL | Keybind search. | Searchables | defaults | 2026-09-18 |
| Harvest with ease | `harvest-with-ease-neoforge-1.21-9.4.0.jar` | CurseForge 602171 / 5968872 | both | QoL | Right-click harvest. | Cobweb | defaults | 2026-09-18 |
| Clean Swing Through Grass | `cleanswing-1.10-1.21.jar` | CurseForge 915308 / 8746293 | both | QoL | Swing through plants. | none | defaults | 2026-09-18 |
| Cosmetic Armor Reworked | `cosmeticarmorreworked-1.21.1-v1-neoforge.jar` | CurseForge 237307 / 5610814 | both | QoL | Cosmetic armor slots. | none | defaults | 2026-09-18 |
| Elytra Slot | `elytraslot-neoforge-9.0.2+1.21.1.jar` | CurseForge 317716 / 5778461 | both | QoL | Elytra in Curios. | Curios, Caelus | defaults | 2026-09-18 |
| Durability Tooltip | `durabilitytooltip-1.2.0-neoforge-mc1.21.jar` | CurseForge 511040 / 8830219 | client | QoL | Durability numbers. | SuperMartijn642 Config | defaults | 2026-09-18 |
| Equipment Compare | `EquipmentCompare-1.21.1-neoforge-1.3.13.jar` | CurseForge 502561 / 6375501 | client | QoL | Shift-compare gear. | Iceberg | defaults | 2026-09-18 |
| Item Borders | `ItemBorders-1.21-neoforge-1.2.5.jar` | CurseForge 513769 / 5591010 | client | QoL | Rarity item borders. | Iceberg, Prism | defaults | 2026-09-18 |
| Tooltip Overhaul | `tooltipoverhaul-neoforge-1.21.1-2.0.2.jar` | CurseForge 1327508 / 8942013 | client | QoL | Item tooltip frames by type, mod, and rarity. | none | `custom_frames.json` | 2026-09-23 |
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
| Lootr | `lootr-neoforge-1.21.1-1.11.38.126.jar` | CurseForge 361276 / 8927571 | both | utility | Per-player loot chests. World data. | none | defaults | 2026-09-18 |
| Polymorph | `polymorph-neoforge-1.2.0+1.21.1.jar` | CurseForge 388800 / 8849478 | both | recipes | Duplicate recipe picker. | none | defaults | 2026-09-18 |
| Almost Unified | `almostunified-neoforge-1.21.1-1.4.2.jar` | CurseForge 633823 / 8127603 | both | recipes | Ore unification. | none | defaults | 2026-09-18 |
| ATO - All the Ores | `alltheores-3.2.0_neoforge_1.21.1.jar` | CurseForge 405593 / 7825464 | both | worldgen | Extra ores. World data. | none | defaults | 2026-09-18 |
| Supplementaries | `supplementaries-1.21.1-3.9.9-neoforge.jar` | CurseForge 412082 / 8852720 | both | content | Decor and utility blocks. World data. | Moonlight | defaults | 2026-09-18 |
| Amendments | `amendments-1.21-2.1.10-neoforge.jar` | CurseForge 896746 / 8825641 | both | content | Vanilla block tweaks. World data. | Moonlight | defaults | 2026-09-18 |
| NeoAuth | `NeoAuth-1.21.1-1.0.1.jar` | CurseForge 1140741 / 7069504 | client | auth | Microsoft auth helper. | none | defaults | 2026-09-18 |
| Better Compatibility Checker | `better-compatability-checker-neoforge-21.1.8.jar` | CurseForge 551894 / 7404415 | both | utility | Join-time modlist check. | none | defaults | 2026-09-18 |
| Crash Utilities | `crashutilities-9.0.4.jar` | CurseForge 371813 / 5993450 | both | stability | Extra crash helpers. | none | defaults | 2026-09-18 |
| Sophisticated Core | `sophisticatedcore-1.21.1-1.5.1.2341.jar` | CurseForge 618298 / 8838842 | both | library | Sophisticated storage/backpacks. | none | defaults | 2026-09-18 |
| Sophisticated Backpacks | `sophisticatedbackpacks-1.21.1-3.26.3.2158.jar` | CurseForge 422301 / 8845926 | both | storage | Backpacks. World data. | Sophisticated Core | defaults | 2026-09-18 |
| Sophisticated Storage | `sophisticatedstorage-1.21.1-1.5.91.2127.jar` | CurseForge 619320 / 8687896 | both | storage | Barrels/chests. World data. | Sophisticated Core | defaults | 2026-09-18 |
| Functional Storage | `functionalstorage-1.21.1-1.5.8.jar` | CurseForge 556861 / 8459097 | both | storage | Drawers. World data. | Titanium | defaults | 2026-09-18 |
| Botany Pots | `botanypots-neoforge-1.21.1-21.1.44.jar` | CurseForge 353928 / 8243851 | both | farming | Crop pots. World data. | Bookshelf, Prickle | defaults | 2026-09-18 |
| Botany Trees | `botanytrees-neoforge-1.21.1-21.1.7.jar` | CurseForge 411357 / 8188485 | both | farming | Tree pots. World data. | Bookshelf, Prickle | defaults | 2026-09-18 |
| Trash Cans | `trashcans-1.1.0-neoforge-mc1.21.jar` | CurseForge 394535 / 8646611 | both | storage | Trash blocks. World data. | SuperMartijn642 Core + Config | defaults | 2026-09-18 |
| TrashSlot | `trashslot-neoforge-1.21.1-21.1.11.jar` | CurseForge 235577 / 8163135 | both | QoL | Inventory trash slot. | Balm | defaults | 2026-09-18 |
| Packing Tape | `PackingTape-1.21.1-0.15.6.jar` | CurseForge 238659 / 6667874 | both | storage | Pickup tile entities. | none | defaults | 2026-09-18 |
| FTB Chunks | `ftb-chunks-neoforge-2101.1.22.jar` | CurseForge 314906 / 8791113 | both | utility | Chunk claims. World data. ARR. | FTB Library, Architectury | defaults | 2026-09-18 |
| FTB Essentials | `ftb-essentials-neoforge-2101.1.10.jar` | CurseForge 410811 / 8442866 | both | utility | `/home` and related commands. ARR. | FTB Library | defaults | 2026-09-18 |
| FTB Ultimine | `ftb-ultimine-neoforge-2101.1.15.jar` | CurseForge 386134 / 8231400 | both | utility | Vein mine. ARR. | FTB Library | defaults | 2026-09-18 |
| FTB Filter System | `ftb-filter-system-neoforge-21.1.4.jar` | CurseForge 943925 / 7429011 | both | library | Item filters. ARR. | FTB Library | defaults | 2026-09-18 |
| FTB XMod Compat | `ftb-xmod-compat-neoforge-21.1.12.jar` | CurseForge 889915 / 8909889 | both | utility | FTB cross-mod hooks. ARR. | FTB Library | defaults | 2026-09-18 |
| Create Ultimine | `createultimine-1.21.1-neoforge-1.3.2.jar` | CurseForge 1231381 / 8086425 | both | optimizer | Create-aware vein mine. | Create | defaults | 2026-09-18 |
| Create: Sky Village | `create_sky_village-0.0.38 NeoForge 1.21.1.jar` | CurseForge 1104939 / 8004708 | both | worldgen | Create village structure. World data. | Create | defaults | 2026-09-18 |
| Sophisticated Backpacks Create Integration | `sophisticatedbackpackscreateintegration-1.21.1-0.2.0.168.jar` | CurseForge 1238567 / 8833933 | both | storage | Create contraptions + backpacks. | Create, Backpacks, Core | defaults | 2026-09-18 |
| Sophisticated Storage Create Integration | `sophisticatedstoragecreateintegration-1.21.1-0.1.21.209.jar` | CurseForge 1226755 / 8503147 | both | storage | Create + storage. | Create, Storage, Core | defaults | 2026-09-18 |
| Create: Sophisticated Backpacks Compat | `create_sophback_compat-1.0.jar` | CurseForge 1320115 / 6844021 | both | storage | Create recipes for backpacks (complement to 1238567). | Create, Backpacks | defaults | 2026-09-22 |
| Sophisticated Backpacks: Ars Compat | `arssophisticatedcompat-0.3.0.jar` | CurseForge 1653477 / 8653384 | both | storage | Ars items in backpacks. | Ars, Backpacks | defaults | 2026-09-22 |
| Sophisticated Storage: Ars Compat | `arssophisticatedstoragecompat-0.3.0.jar` | CurseForge 1653878 / 8655579 | both | storage | Ars items in Sophisticated storage. | Ars, Storage | defaults | 2026-09-22 |
| Sophisticated Tactical Backpacks | `militarybackpack-2.0.0-beta.jar` | CurseForge 1665194 / 8863583 | both | storage | Tactical backpacks + ammo reload. Beta. World data. | Backpacks | defaults | 2026-09-22 |
| Mekanism + Sophisticated Backpacks Compat | `mekanismsophisticatedbackpacks-neoforge-1.21.1-1.0.1+mc1.21.1-neoforge.jar` | CurseForge 1682131 / 8810041 | both | storage | Chemical tanks in backpacks. | Mekanism, Backpacks | defaults | 2026-09-22 |
| Sophisticated Item Actions | `sophisticateditemactions-1.21.1-0.5.16.423.jar` | CurseForge 1419142 / 8820579 | both | storage | Pinned 1.21.1 file, not 1.21.11. | Core | defaults | 2026-09-22 |
| Yukami's Sophisticated Backpack Tab | `yukamibackpacktab-1.21.1-2.2.0-neoforge.jar` | CurseForge 1343253 / 8900066 | client | storage | Backpack tab in inventory. | Backpacks | defaults | 2026-09-22 |
| Sophisticated Inventory Interactions | `sophisticatedinventoryinteractions-1.21.1-0.1.13.218.jar` | CurseForge 1491239 / 8660377 | both | storage | Inventory transfer helpers. | Core | defaults | 2026-09-22 |
| Sophisticated Chest Optimized | `sophisticated_chest_optimized-1.0.1.jar` | CurseForge 1609784 / 8470473 | client | renderer | Pinned NeoForge 1.0.1; later files are Fabric. | Storage | defaults | 2026-09-22 |
| Sophisticated Backpacks RS Bridge | `backpackrs-1.0.0+mc1.21.1-neoforge.jar` | CurseForge 1664334 / 8710301 | both | storage | Quick deposit into RS. | Backpacks, RS | defaults | 2026-09-22 |
| Demagnetizer | `demagnetizer-neoforge-0.1.0-beta.1.jar` | CurseForge 1698500 / 8896229 | both | QoL | Stops item magnet in a radius. Beta. Pinned NeoForge, not Fabric. | none | defaults | 2026-09-22 |
| C2ME | `c2me-neoforge-mc1.21.1-0.4.0-alpha.0.122.jar` | CurseForge 533097 / 8896937 | both | optimizer | Threaded chunk gen/IO. Alpha. ByePregen disables C2ME FluidPostProcessingFilter. OpenCL module not shipped (Java 25). | none | defaults | 2026-09-18 |
| Applied Energistics 2 | `appliedenergistics2-19.2.17.jar` | CurseForge 223794 / 7027323 | both | storage | ME network. World data. | GuideME | defaults | 2026-09-18 |
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
| Create Aeronautics: Mekanism Compatibility | `create_mekanism_compat-0.1.21.jar` | CurseForge 1536749 / 8299825 | both | tech | Aeronautics + Mekanism. | Aeronautics, Mekanism | defaults | 2026-09-22 |
| Mekanism Extras | `mekanism_extras-1.21.1-1.4.1.jar` | CurseForge 1026040 / 8677677 | both | tech | Extra Mekanism machines. World data. | Mekanism | defaults | 2026-09-22 |
| Patchouli | `Patchouli-1.21.1-93-NEOFORGE.jar` | CurseForge 306770 / 7730942 | both | library | Guidebooks. Required by Mekanism Elements. | none | defaults | 2026-09-23 |
| Mekanism Elements | `MekanismElements-1.21.1-3.0.16-NeoForge.jar` | CurseForge 1103224 / 8839186 | both | tech | Extra element processing. World data. | Mekanism, Patchouli | defaults | 2026-09-22 |
| Ars Nouveau | `ars_nouveau-1.21.1-5.13.1.jar` | CurseForge 401955 / 8721482 | both | magic | Spellcrafting. World data. | none | defaults | 2026-09-18 |
| Spectrum | `spectrum-1.12.7-1.21.1-neo.jar` | CurseForge 556967 / 8866762 | both | magic | Progression magic. World data. | Revelationary, Modonomicon, Curios | defaults | 2026-09-18 |
| Complementary Reimagined | `ComplementaryReimagined_r5.9.3.zip` | CurseForge 627557 / 8884654 | client | shader | Matches Euphoria r5.9.3. | Iris | defaults | 2026-09-18 |
| Complementary Unbound | `ComplementaryUnbound_r5.9.3.zip` | CurseForge 385587 / 8884656 | client | shader | Matches Euphoria r5.9.3. | Iris | defaults | 2026-09-18 |
| BSL Shaders | `BSL_v10.1.1.zip` | CurseForge 322506 / 7588844 | client | shader | Latest CF 1.21.1-tagged BSL. | Iris | defaults | 2026-09-18 |
| Euphoria Patches | `EuphoriaPatcher-1.10.5-r5.9.3-neoforge.jar` | CurseForge 915902 / 8884680 | client | shader | Complementary extras. | Colorwheel | defaults | 2026-09-18 |
| Colorwheel | `colorwheel-neoforge-1.3.0-beta3+mc1.21.1.jar` | CurseForge 1254143 / 8845482 | client | renderer | Iris shader extras. Beta. | none | defaults | 2026-09-18 |
| Colorwheel Patcher | `colorwheel_patcher-neoforge-1.0.5+mc1.21.1.jar` | CurseForge 1285475 / 7924942 | client | renderer | Colorwheel companion. | Colorwheel | defaults | 2026-09-18 |
| [UNOFFICIAL] TaCZ NeoForge Port | `tacz-neoforge-1.21.1-1.1.8-hotfix-r6.jar` | CurseForge 1353462 / 8547439 | both | combat | Unofficial 1.21.1 TaCZ. World data. Not compatible with 1.20.1 TaCZ worlds. | none | defaults | 2026-09-22 |
| TaCZ Pack Upgrader | `tacz-pack-upgrader-2.1.3.jar` | CurseForge 1353465 / 8387504 | both | combat | Converts 1.20.1 gun packs for this port. | TaCZ | defaults | 2026-09-22 |
| TaCZ addon | `taczaddon-1.1.8.2-neoforge-1.21.1.jar` | CurseForge 1238419 / 8836214 | both | combat | Extra TaCZ features. | TaCZ | defaults | 2026-09-22 |
| [TaCZ] Tactical Breaching | `tacz_tactical_breaching-neoforge-1.21.1-1.0.5.jar` | CurseForge 1552880 / 8752892 | both | combat | Breaching, glass damage, shells, smoke. | TaCZ | distant-gunshot debug off | 2026-09-22 |
| TaCZ x Guns Lights Addon | `tacz_x_guns_lights_addon-neoforge-1.21.1-2.8.2.jar` | CurseForge 1325673 / 8784270 | both | combat | Pinned 2.8.2 NeoForge; 2.9.0 is 1.20.x. | TaCZ | defaults | 2026-09-22 |
| [TaCZ] Curios For Ammo Box | `curios_for_ammo_box-1.21.1-1.2.0.jar` | CurseForge 1339813 / 8191224 | both | combat | Ammo box curios slot. | TaCZ, Curios | defaults | 2026-09-22 |
| [TaCZ] Applied Ammo Box | `applied_ammo_box-1.21.1-1.2.3-hotfix2.jar` | CurseForge 1338332 / 8618447 | both | combat | AE2 ammo box. | TaCZ, AE2 | defaults | 2026-09-22 |
| Elite X Quality Guns (TACZ) | `Elite x Quality Guns Neoforge v5.1 - 1.21.1.jar` | CurseForge 1084662 / 7952386 | both | combat | Gun pack. | TaCZ | defaults | 2026-09-22 |
| TACZ Turrets | `taczturrets-2.0.0-all.jar` | CurseForge 1376660 / 8834773 | both | combat | Placeable turrets. World data. | TaCZ | defaults | 2026-09-22 |
| TACZ Aeronautics compat | `tacz_aero_compat-1.8.0.jar` | CurseForge 1530288 / 8195668 | both | combat | Guns on Aeronautics vehicles. | TaCZ, Aeronautics | defaults | 2026-09-22 |
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
| TaCZ: Blueprints Reforged | `tacz-blueprints-reforged-1.0.1.jar` | CurseForge 1589398 / 8331907 | both | combat | Blueprint crafting. World data. | TaCZ | defaults | 2026-09-22 |
| Punchy! | `punchy-2.8a-neoforge-1.21.1.jar` | CurseForge 1374153 / 8891106 | client | renderer | First-person punch anims. Required by Don't Punch My TACZ. Hidden while Epic Fight mode is on. | none | defaults | 2026-09-22 |
| Don't Punch My TACZ | `dont-punch-my-tacz-v0.5.2-1.21.1-neo.jar` | CurseForge 1691793 / 8932034 | client | combat | Pinned NeoForge jar, not Fabric. | TaCZ, Punchy | defaults | 2026-09-22 |
| Epic Fight X Punchy! Neo | `punchy_epicfight_neoforge.jar` | CurseForge 1491729 / 7789794 | client | combat | Hides Punchy first-person arms while Epic Fight mode is active. Client-only. | Punchy, Epic Fight | defaults | 2026-09-23 |
| [UNOFFICIAL] LesRaisins Tactical Equipements | `LesRaisins-Tactical-Equipements-1.21.1-0.4.3.jar` | CurseForge 1432620 / 8745260 | both | combat | Tactical gear pack. | TaCZ | defaults | 2026-09-22 |
| MCS2 gun pack | `MCS2_Gunpack_v1.0.4_AWP_tacz1.1.4_hotfix3.zip` | CurseForge 1113043 / 6083203 | both | combat | CS2-style guns. Zip in `pack/tacz/` for Pack Upgrader. Addon jar 1285238 is 1.20.1-only and does not load. | TaCZ, Pack Upgrader | defaults | 2026-09-23 |
| Daffa's Arsenal | `daffas_arsenal-3.7.1.1.jar` | CurseForge 1254350 / 8862167 | both | combat | 1.20.1 gun pack in `pack/tacz/`. Forge creative-tab classes stay out of `mods/`. World data. | TaCZ, Pack Upgrader | defaults | 2026-09-23 |
| CS+ | `csplus-1.3.1-hotfix2.zip` | CurseForge 1623678 / 8867307 | both | combat | Counter-Strike gun pack. CurseForge file is a 1.20.1 jar; local name is `.zip` so Pack Upgrader reads root `gunpack.meta.json`. World data. | TaCZ, Pack Upgrader | defaults | 2026-09-23 |
| Vic's Point Blank | `pointblank-neoforge-1.21-2.2.0.jar` | CurseForge 961053 / 8855569 | both | combat | Guns beside TaCZ. World data. GeckoLib `[4.9.2,)`. | GeckoLib | defaults | 2026-09-23 |
| Point Blank Aeronautics compat | `pointblank_aero_compat-1.0.0.jar` | CurseForge 1540250 / 8073109 | both | combat | Bullets hit Aeronautics physics objects. | Point Blank, Aeronautics | defaults | 2026-09-23 |
| Point Blank Extended Edition | `pbext-ext 1.0.zip` | CurseForge 1403532 / 7327102 | both | combat | Official gun pack in `pack/pointblank/`. | Point Blank | defaults | 2026-09-23 |
| Point Blank Gun Gale Pack | `ggo-ext 1.0.zip` | CurseForge 1379446 / 7191282 | both | combat | Official Gun Gale pack in `pack/pointblank/`. | Point Blank | defaults | 2026-09-23 |
| Point Blank Half Life Pack | `halflife-ext v0.8.zip` | CurseForge 1163691 / 8805527 | both | combat | Official Half-Life pack in `pack/pointblank/`. | Point Blank | defaults | 2026-09-23 |
| Cyberpunk 2077 Guns for Vic's Point Blank | `Cyberpunk_2077_Guns_Pack_1.19.zip` | CurseForge 1013546 / 8076165 | both | combat | Community gun pack in `pack/pointblank/`. No third-party distribution. | Point Blank | defaults | 2026-09-23 |
| Berezka's library | `berezka_api-1.2.9.5-fix-neoforge-1.21.1.jar` | CurseForge 1160598 / 8624655 | both | library | Required by Just Enough TaCZ. | none | defaults | 2026-09-22 |
| Resourceful Lib | `resourcefullib-neoforge-1.21-3.0.12.jar` | CurseForge 570073 / 5973188 | both | library | Required by Variants&Ventures. Pinned 1.21.1; later files are 1.21.11. | none | defaults | 2026-09-22 |
| Variants&Ventures | `variantsandventures-neoforge-1.0.26+mc1.21.1.jar` | CurseForge 981139 / 8190696 | both | content | Mob variants. World data. | Resourceful Lib, YACL | defaults | 2026-09-22 |
| Elysium API | `ElysiumAPI-1.21.1-2.0.1.jar` | CurseForge 1158628 / 8707151 | both | library | Required by Jaden's Nether Expansion. | none | defaults | 2026-09-22 |
| Lodestone | `lodestone-1.21.1-1.8.2.jar` | CurseForge 616457 / 7264731 | both | library | Required by Jaden's Nether Expansion. | none | defaults | 2026-09-22 |
| Jaden's Nether Expansion | `Jadens-Nether-Expansion-2.4.1.jar` | CurseForge 1111833 / 8707156 | both | worldgen | Extra Nether biomes/mobs. World data. | Elysium, Lodestone | defaults | 2026-09-22 |
| Jaden's Nether Expansion Delight | `jadensnetherexpansiondelight-1.21.1-1.0.4a-neoforge.jar` | CurseForge 1190275 / 8232964 | both | farming | Delight recipes for Jaden's. | FD, Jaden's | defaults | 2026-09-22 |
| Netherite Tweaks & Fixes | `netherite_tweaks_luna-1.2.2-neoforge-1.21.1.jar` | CurseForge 1239001 / 7282661 | both | QoL | Netherite tweaks. | none | defaults | 2026-09-22 |
| Puzzles Lib | `PuzzlesLib-v21.1.60-mc1.21.1-NeoForge.jar` | CurseForge 495476 / 8829114 | both | library | Required by Eternal Nether. | none | defaults | 2026-09-22 |
| Eternal Nether | `EternalNether-v21.1.3-1.21.1-NeoForge.jar` | CurseForge 1252482 / 6751611 | both | worldgen | Extra Nether structures. World data. | Puzzles Lib | defaults | 2026-09-22 |
| WunderLib: New Dawn | `wunderlib-21.0.10.jar` | CurseForge 1422273 / 7469725 | both | library | BetterNether New Dawn stack. Pinned 21.0.x. | none | defaults | 2026-09-22 |
| WorldWeaver: New Dawn | `worldweaver-21.0.25.jar` | CurseForge 1422284 / 8594162 | both | library | BetterNether New Dawn stack. Pinned 21.0.x. | BCLib New Dawn | defaults | 2026-09-22 |
| BCLib: New Dawn | `bclib-21.0.26.jar` | CurseForge 1422283 / 8608827 | both | library | BetterNether New Dawn stack. Pinned 21.0.x. | none | defaults | 2026-09-22 |
| BetterNether: New Dawn | `BetterNether-21.0.27.jar` | CurseForge 1422293 / 8896389 | both | worldgen | Nether biomes/blocks. World data. | New Dawn libs | defaults | 2026-09-22 |
| Nether Remastered | `nether_remastered-2.6-neoforge-1.21.1.jar` | CurseForge 872516 / 8145295 | both | worldgen | Nether structures. World data. | none | defaults | 2026-09-22 |
| Nether Villager Trader | `nethervillagertrader-2.0.0-neoforge-1.21.1.jar` | CurseForge 989053 / 7154899 | both | QoL | Nether trading. | none | defaults | 2026-09-22 |
| Just-In NETHER | `just_in_nether-1.2.1-neoforge-1.21.1.jar` | CurseForge 1074911 / 8919842 | both | worldgen | Extra Nether content. World data. | none | defaults | 2026-09-22 |
| Farmer's Cutting: BetterNether | `farmers-cutting-betternether-1.21.1-1.0-neoforge.jar` | CurseForge 1114065 / 7649818 | both | farming | Cutting recipes for BetterNether. | FD, BetterNether | defaults | 2026-09-22 |
| playerAnimator | `player-animation-lib-forge-2.0.4+1.21.1.jar` | CurseForge 658587 / 7389814 | both | library | Required by Epic Fight. Filename says forge; file tags NeoForge 1.21.1. | none | defaults | 2026-09-22 |
| Epic Fight | `epic-fight-21.17.3.1-mc1.21.1-neoforge.jar` | CurseForge 405076 / 8175609 | both | combat | Souls-like combat. World data. | playerAnimator | defaults | 2026-09-22 |
| AAA Particles | `aaa_particles-neoforge-1.21.1-2.2.3.jar` | CurseForge 979809 / 8402817 | both | combat | Effekseer particle effects. Kept without Nightfall. Architectury embedded. KubeJS optional, not added. | none | defaults | 2026-09-23 |
| Knight Lib | `knightlib-neoforge-1.21.1-2.0.2.jar` | CurseForge 1105855 / 8933799 | both | library | Required by Olympus!. | none | defaults | 2026-09-23 |
| Olympus! | `olympusmythology-neoforge-1.21.1-1.0.8.jar` | CurseForge 1667111 / 8935108 | both | content | Greek artifacts, mobs, and structures. World data. | Curios, Knight Lib | defaults | 2026-09-23 |
| Archaion: Echoes of the Fallen | `archaion-1.21.1-1.4.3.jar` | CurseForge 1620396 / 8784992 | both | content | Ancient Keep, trial spawners, and a boss. World data. ARR. | AAA Particles | defaults | 2026-09-23 |
| Weapons of Miracles | `WeaponsOfMiracles-2.0.178.jar` | CurseForge 918614 / 8829395 | both | combat | Required by EF × Twilight Forest. World data. | Epic Fight | defaults | 2026-09-22 |
| P1nero's Epic Bow | `p1nero_bow-neoforge1.21.1-21.16.1.0-neoforge.jar` | CurseForge 1338443 / 7922741 | both | combat | Required by EF × Twilight Forest. | Epic Fight | defaults | 2026-09-22 |
| Epic Fight × Twilight Forest Compat | `TwilightForestEFCompat-1.1.6-Fix-1.21.1-Neoforge.jar` | CurseForge 1555371 / 8784163 | both | combat | TF animations in Epic Fight. | Weapons of Miracles, Epic Bow | defaults | 2026-09-22 |
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
| AE2 Utility | `ae2utility-1.7.9.jar` | CurseForge 1521605 / 8805305 | both | storage | Pull from the ME network into machines; one-click patterns. | AE2, JEI (client) | defaults | 2026-09-24 |
| Pattern Converter | `patternconverter-1.0.0.jar` | CurseForge 1311295 / 6795530 | both | storage | Convert AE2 and Refined Storage patterns. World data. | none | defaults | 2026-09-24 |
| AE2 Universal Press | `ae_universal_press-2.1.1-neoforge-1.21.1.jar` | CurseForge 1222746 / 8306511 | both | storage | One press for every processor. World data. | AE2 | defaults | 2026-09-24 |
| Climbable Ropes for Create Aeronautics | `climbable_ropes-2.1.3.jar` | CurseForge 1528764 / 8769644 | both | tech | Climb Aeronautics ropes. | Aeronautics, Sable, Create | defaults | 2026-09-24 |
| Create - Xaero's map | `sablexaeromaps-1.21.1-1.4.0.jar` | CurseForge 1622142 / 8736099 | client | map | Aeronautics contraptions on Xaero maps. | Sable, Xaero's World Map | defaults | 2026-09-24 |
| Create Aeronautics x Curios API Compat | `createaeronauticscurios-neoforge-1.21.1-2.2.jar` | CurseForge 1532334 / 8547039 | both | tech | Aviator goggles in a Curios slot. | Aeronautics, Curios | defaults | 2026-09-24 |
| Akashic Tome | `AkashicTome-1.8-30.jar` | CurseForge 250577 / 7773841 | both | utility | One book that holds other books. | none | defaults | 2026-09-24 |
| CreativeCore | `CreativeCore_NEOFORGE_v2.13.48_mc1.21.1.jar` | CurseForge 257814 / 8947159 | both | library | Required by AmbientSounds. | none | defaults | 2026-09-24 |
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
| Ars Nouveau Refresh | `Ars Nouveau Refresh 1.2.0.zip` | CurseForge 1080571 / 6068071 | client | resource pack | Ars item textures. | Ars Nouveau | Global Packs required | 2026-09-24 |
| Better Sophisticated Backpack Upgrades | `Better SB Upgrades.zip` | CurseForge 1138140 / 7964810 | client | resource pack | Backpack upgrade icons. | Sophisticated Backpacks | Global Packs required | 2026-09-24 |
| Boss Refreshed | `boss-refreshed-v2-1.19-1.21.zip` | CurseForge 882133 / 6597394 | client | resource pack | Dragon, wither, warden, and elder guardian models. EMF. | EMF | Global Packs required | 2026-09-24 |

World-data: Create, Create Aeronautics, Pipez, FTB Quests/Chunks, Twilight Forest, Lost Cities, Regions Unexplored, Oh The Biomes We've Gone, Terralith, Nullscape, dungeon/structure mods, Amplified Nether, Infernal Expansion Redux, BetterNether New Dawn, Jaden's Nether, Eternal Nether, Nether Remastered, Cave Biomes, Alex's Caves Continued, Compat Structure, Terrain Slabs, Aquamirae, Archaion, Olympus!, Waystones, Lootr, ATO, Supplementaries, Amendments, Sophisticated/Functional storage, Botany, Trash Cans, Create Sky Village, AE2, Refined Storage, Mekanism (plus Extras/Elements/Covers), Ars Nouveau, Farmer's Delight cluster, Alchemistry, Spectrum, TaCZ, Vic's Point Blank, Epic Fight, Ice and Fire CE, Variants&Ventures, Block Variants, Ecliptic Seasons, Crystalix, Create Deco, Create Encased, Create Crafts & Additions, Epitaphs, Comforts, Artifacts, Ars Controle, Ars Elemancy, Ars Technica, Ars Flavors, Autochef's Delight, Barbeque's Delight, Building Gadgets, Infinity Drives, Pattern Converter, Schematic Energistics, and AE2 MEGA Things write blocks/items/dimensions/terrain/biomes/season state. Those are not a clean uninstall. New world required for the 1.21.1 cutover. Removing Tectonic does not rewrite already-generated chunks.

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
| Ksyxis, Disconnect Packet Fix, quick pack | See CurseForge pages | MIT | CurseForge reference. |
| CrashExploitFixer | See CurseForge page | GPL-3.0-only | CurseForge reference. |
| Async Logger | See CurseForge page | LGPL-3.0-only | CurseForge reference. |
| ResourcePackCached | See CurseForge page | GPL-3.0-only | CurseForge reference. |
| Chunk Pregenerator | Speiger | See CurseForge page | CurseForge metadata only; do not embed the jar. |
| Carbon Config | Carbon Config Project | Apache-2.0 | CurseForge reference. |
| Create | simibubi / Creators of Create | Create Mod License | CurseForge reference; do not rehost the jar. |
| Sable, Create Aeronautics | ryanhcode / Simulated | PolyForm Shield / Simulated Project License | CurseForge metadata; do not rehost the jars. |
| Create Better FPS | See CurseForge page | MIT | CurseForge reference. |
| Create: Threaded Trains | See CurseForge page | GPL-3.0-or-later | CurseForge reference. |
| Architectury API | architectury | LGPL-3.0-only | CurseForge reference. |
| FTB Library, Teams, Quests | Feed The Beast | ARR | CurseForge metadata only; do not embed the jars. |
| FTB Quests Optimizer | See CurseForge page | MIT | CurseForge reference. |
| Pipez | henkelmax | ARR | CurseForge metadata only; do not embed the jar. |
| Pipez Lag Fix | Almana21 | ARR | CurseForge metadata only; do not embed the jar. |
| TxniLib | Txni | MIT | CurseForge reference. |
| Cerulean | Txni | GPL-3.0-only | CurseForge reference. |
| Bye?Pregen! | MoePus | LGPL-3.0-only | CurseForge reference. |
| The Twilight Forest | TeamTwilight | See CurseForge page | CurseForge reference. |
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
| JEI / REI / EMI WorldGen | See CurseForge page | See CurseForge page | CurseForge reference. |
| AE2 JEI Integration, Create JEI Compat, Smithing Template Viewer, Sophisticated JEI Index, SpectrumJEI, JEI Stuff | See CurseForge pages | MIT / LGPL-3.0-only / see pages | CurseForge reference. |
| JEIOptimizer, JEI QuickCraft | See CurseForge pages | ARR | CurseForge metadata only; do not embed the jars. |
| Refined Storage - JEI Integration | raoulvdberge | MIT | CurseForge reference. |
| FTB JEI Extras, MekaGenJei, Just Enough Mekanism Multiblocks, Mekanism Ponders, Just Enough TaCZ, Just Enough Resources | See CurseForge pages | See each page | CurseForge metadata; do not embed ARR jars. |
| Mekanism addons (Extras, Elements, RS/Aeronautics/Soph compat, MekaJade) | See CurseForge pages | Mix of MIT/ARR | CurseForge metadata; do not embed ARR jars. |
| Patchouli | Vazkii | Custom | CurseForge reference. |
| Sophisticated addons (Ars, tactical, item actions, Yukami, inventory, chest optimized, RS bridge) | See CurseForge pages | Mix of MIT/ARR | CurseForge metadata; do not embed ARR jars. |
| TaCZ unofficial port and addons | See CurseForge pages | Mix of MIT/ARR; unofficial 1.21.1 port | CurseForge metadata; do not embed ARR jars. |
| MCS2 gun pack | See CurseForge page | ARR | CurseForge metadata. Zip stays in `pack/tacz/`. Do not ship MCS2Gun-addon 1285238 (encrypted 1.20.1 Forge jar). |
| Daffa's Arsenal | DaffaTheOne | CC-BY-NC-4.0; inner pack header says all rights reserved | CurseForge metadata in `pack/tacz/`. Do not embed the jar. |
| CS+ | lolokeia | CC BY-NC-4.0 | CurseForge metadata in `pack/tacz/`. Do not embed the jar. |
| Vic's Point Blank and official packs | vic4games | ARR | CurseForge metadata; do not embed the jars or zips. |
| Point Blank Aeronautics compat | Glaiden_ | MIT | CurseForge reference. |
| Cyberpunk 2077 Guns for Vic's Point Blank | TheScepticBlock | ARR; no third-party distribution | CurseForge metadata only; do not embed the zip. |
| Epic Fight, ParCool, Ice and Fire CE, BetterNether New Dawn, Jaden's Nether, Alex's Caves Continued, and related addons | See CurseForge pages | Mix of MIT/ARR | CurseForge metadata; do not embed ARR jars. |
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
| Library Ferret, Awesome Dungeon | JTL | ARR | Modrinth metadata; do not embed the jars. |
| YUNG's API / Better Caves / Better Nether Fortresses / Bridges | YUNG | LGPL-3.0-only | CurseForge reference. |
| Moog's Structure Lib / Mineshafts | Moog | See project pages | CurseForge / Modrinth metadata. |
| Epic Structures | See CurseForge pages | ARR | CurseForge metadata only; do not embed the jars. |
| Infernal Expansion Redux | See CurseForge page | See CurseForge page | CurseForge reference. |
| Countered's Terrain Slabs | Countered | See CurseForge page | CurseForge reference. |
| Fragmentum, Aquamirae | Obscuria | Obscuria licenses | CurseForge / Modrinth metadata; do not embed the jars. |
| FastBoot | dnlayu | ARR | CurseForge metadata only; do not embed the jar. |
| Fluidium, Duplicationless | Kall | MIT | CurseForge reference. |
| LC²H | Admany | BRSSLA V2.0.0 | CurseForge metadata only; do not embed the jar. |
| Quantified API | Admany | See CurseForge page | CurseForge metadata only; do not embed the jar. |
| BiomeSpy | MoePus | LGPL-3.0-only | CurseForge reference. |
| DarkSleep | GamerPotion | ARR | CurseForge metadata only; do not embed the jar. |
| MemGuard | See CurseForge project 1468440 | MIT (in-jar) | CurseForge reference. |
| Wave 1 QoL/storage/FTB (Xaero, Waystones, Sophisticated, etc.) | See each CurseForge page | Mix of MIT/ARR/LGPL | CurseForge metadata; do not embed ARR jars. |
| Tooltip Overhaul | Xylonity | GPL-3.0-only | CurseForge metadata only; do not embed the jar. |
| Tag Tooltips | Jagm | CC-BY-SA-4.0 | Modpack use allowed. CurseForge metadata only; do not embed the jar. |

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
