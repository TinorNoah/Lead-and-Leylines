# Deferred and not-yet-ported mods

Not an install list. Each row still needs a fresh 1.21.1 NeoForge research pass and explicit file approval. Minecraft / loader: [`pack/pack.toml`](../../pack/pack.toml). History of the old pack: branch `forge-1.20.1`.

Installed today: [manifest.md](manifest.md). Performance decisions: [performance.md](performance.md).

## Named list — remaining only (2026-09-18)

Installed this wave: Sodium Extra, Flerovium, AsyncParticles, More Culling, Cloth Config, SLO, Resourceful Config, Ksyxis, Disconnect Packet Fix, quick pack, CrashExploitFixer, Async Logger, ResourcePackCached, Chunk Pregenerator, Carbon Config, Create, Iris Flywheel Compat, Create Better FPS, Create Threaded Trains, Architectury, FTB Library / Teams / Quests / Quests Optimizer, Pipez, Pipez Lag Fix, TxniLib, Cerulean, Bye?Pregen!, Twilight Forest, Lost Cities, TerraBlender, GeckoLib, CorgiLib, Oh The Trees You'll Grow, Oh The Biomes We've Gone, Regions Unexplored, Global Packs, Jade, EMI, Terralith, GeckolibBetterFPS, Feature Recycler, and the 1.21.1 NeoForge worldgen set. Removed to make room: Noisium, Achievements Optimizer. See [manifest.md](manifest.md).

This file lists **what was not added**.

### Held — file exists but not a fit yet

| Named as | Why not |
|---|---|
| sodium lights + Sodium Options API + Options Mod Compat | Matching jars are from 2025-01 / 2025-04, before Sodium 0.8. Extra 0.9.4 does not need Options API. Wait for 0.8-era files. |
| Particle Core + Fzzy Config + Kotlin for Forge | Incompatible with AsyncParticles (already in). Kotlin + Fzzy Config is extra library. |
| Redirected + TxniLib | 1.21.1 files exist (2025-02). Stale vs current NeoForge; enum intern is a tiny gain. |
| EMI Enchants | Last file is 1.20.4. No 1.21.1 NeoForge build. |
| ServerCore 1.5.19 | Entity Activation Range is a distant-entity freezer. Pack policy: do not add those. |
| Gnetum | HUD-over-frames. Overlaps ImmediatelyFast. |
| LightSpeedRe | Launch shortcut. Overlaps ModernFix. |
| Put A Plug In it! (PAPI) | Same leak-patch niche as AllTheLeaks. |

### Overlaps something already in the pack

| Named as | Why not |
|---|---|
| (Sodium) Chloride | Same Extra job (leaves, fog, FPS overlay, entity distance). ARR. Extra is the license we want. |
| Sodium Extras (Txni) | Third Extra. Last 1.21.1 file 2025-04; needs old Options API. Official Extra 0.9.4 covers this. |
| Sodium Leaf Culling | Extra / Chloride already do leaves. 2025-04 Sodium-era file. |
| OptiLeaves | Same leaf-culling niche. ARR. |
| Despawn Tweaks | Let Me Despawn is already installed. Also TxniLib. |
| NoisiumForked 2.7.0 | Do not stack on ByePregen. Noisium itself was removed as incompatible. |
| Idle Boost | Dynamic FPS already lowers unfocused FPS. 2024-09 file. |
| Better Block Entities | Same draw-cost space as Flerovium. Pick one. |
| Performance Tweaks | Same project as Adaptive Performance Tweaks (listed twice in the original doc). |

### Needs a parent mod we have not ported

| Named as | Missing parent / file |
|---|---|
| Vanillin (`flw-vanillin`) | Flywheel is in Create, but Vanillin is **shader-incompatible**. Iris is in, so this stays out. |
| LC²H [Lost Cities: Multithreaded] | Lost Cities is in. LC²H is still 1.20.1 Forge only. |
| TwilightForest Thread Safety Addon | Twilight Forest is in. Addon still has no 1.21.1 NeoForge file. |

### Wrong renderer, missing file, or not a single pack mod

| Named as | Why not |
|---|---|
| Bocchium | No 1.21.1 NeoForge project found. Old Embeddium/Rubidium bedrock-face cull. |
| FastBoot | No matching 1.21.1 NeoForge mod. Still not a pack mod. |
| Fluidium | No project found. |
| DarkTimer - RPG Clear Entity Lag | No 1.21.1 NeoForge file. Entity-delete lag clear. ARR. |

### Gameplay-changing, crashy, or too much library for the gain

| Named as | Correction |
|---|---|
| DoesPotatoTick? | Skip. Distant-entity freeze. CurseForge 1.21.1 file exists (`doespotatotick-1.21.1-5.6.4`) and **requires Duplicationless** (original missed). Do not add. |
| Immersive Optimization | Same entity-scheduler idea. Skip. |
| Adaptive Performance Tweaks | Auto-cuts view distance / spawns / items. Skip. |
| TCT ClearLag | Deletes entities. ARR + TCT Core. Skip. |
| Dimensional Threading Reforked | One world per thread. Skip. |
| Invasive Optimizations | Author: disable this first if anything breaks. Optional Create / Pipez patches on a mixed pack. Skip. |
| ScalableLux | Alpha lighting engine. Skip. |
| Ixeris | Moves input off-thread. Skip. |
| Krypton Reno | Original looked up Fabric `krypton`. Real project is `krypton-fnp` (`krypton_fnp-neoforge-1.21.1-0.2.28.1`). File exists. Still hold: network mixins next to Lithium / NeoForge. |
| Fast Item Frames | New block-entity type (world data) + Puzzles Lib. Skip. |
| BetterGrassify | Required Forgified Fabric API. Skip. |
| Loading Backgrounds | Cosmetic + Architectury + ARR. Skip. |
| Too Many Entities | Client limiter + Architectury + Cloth. Skip. |
| GPUTape | ToadLib. Modest vs Sodium/Iris/ImmediatelyFast. Skip. |
| MemGuard | ARR; forces GC. Skip. |
| DarkSleep - RPG Sleep Percentage | Sleep rule, not an optimizer. ARR. Skip. |
| BiomeSpy | `/locate` rewrite, not FPS. Revisit in a worldgen / locate wave. |

Shader packs and Colorwheel stay deferred. Extra is in; wait for a clean boot before shader packs. See [performance.md](performance.md).

## 1.20.1 Forge pack — not on 1.21.1 NeoForge yet

Source: `pack/mods/*.pw.toml` on branch `forge-1.20.1` (239 mods). Already represented on NeoForge: AllTheLeaks, Almanac Lib, Architectury API, Awesome Dungeon, BadOptimizations, Chunk Pregenerator (new), Cloth Config, Clumps, CorgiLib, Crash Assistant, Create, Cupboard, Dynamic FPS, EMI, Entity Culling, FastFurnace, FastSuite, FastWorkbench, FerriteCore, FTB Library / Teams / Quests, GeckoLib, ImmediatelyFast, Infernal Expansion Redux, Jade, Let Me Despawn, Lithostitched, ModernFix, Neruina, Nullscape, Oh The Biomes We've Gone, Oh The Trees You'll Grow, Pipez, Placebo, Regions Unexplored, Resourceful Config, Smooth Chunk Save, Sodium Extra, Structurify, Tectonic, TerraBlender, Terralith, The Lost Cities, The Twilight Forest, When Dungeons Arise, YUNG's API / Better Caves / Better Nether Fortresses / Bridges.

Replaced, do not port as-is: Embeddium → Sodium, Oculus → Iris, Radium → Lithium, Rubidium Extra → Sodium Extra.

Configurable is new on NeoForge (Neruina dependency) and was not on the Forge list. Carbon Config, Iris Flywheel Compat, Create Better FPS, Create Threaded Trains, FTB Quests Optimizer, Pipez Lag Fix, TxniLib, Cerulean, Bye?Pregen!, Lithostitched, Tectonic 3, Global Packs, GeckolibBetterFPS, and Feature Recycler are new with this pack.

Do not dump-install the rest.

### Create

Create Ultimine; Slice & Dice; Central Kitchen; Applied Kinetics; Alex's Caves Compat; Sky Village; Sophisticated Backpacks / Storage Create integrations.

### Applied Energistics 2

AE2; GuideME; Glodium; Extended AE; AdvancedAE; AE Additions; AE2 Things; AE2 Import Export Card; AEInfinityBooster; Applied Flux; MEGA Cells; Applied Mekanistics; Ars Énergistique; Polymorphic Energistics; Better P2P; Wireless Terminals.

### Refined Storage

Refined Storage; RS Addons; Extra Disks; ExtraStorage; Refined Polymorphism.

### Mekanism

Mekanism; Generators; Tools; More Machine.

### Magic

Ars Nouveau; Ars Additions; Ars Creo; Ars Elemental; Alchemistry; AlchemyLib; ChemLib.

### Combat / guns / movement

Timeless and Classics Zero and TaCZ addons (Additions, Tweaks, Labs, Immersive Ballistic, Daffa's Arsenal, Gucci & Vuitton, LesRaisins packs, Curios Ammo Box, Guns Lights); Epic Fight; Official Epic x ParCool; ParCool; Simply Swords; Simply More; Ice and Fire CE.

### Worldgen / structures / dimensions

Alex's Caves; Citadel; Stalwart Dungeons; Bygone Nether; BetterNether Forge; Awesome Dungeon Nether.

### Farmer's Delight cluster

Farmer's Delight; Delightful; Corn Delight; My Nether's Delight; Twilight's Flavor & Delight; Farmer's Cutting (BWG, Regions Unexplored, Twilight Forest).

### Storage / backpacks / logistics

Sophisticated Core / Backpacks / Storage; Functional Storage; Botany Pots; Botany Trees; Trash Cans; TrashSlot; Packing Tape; Cable Tiers; Titanium.

### FTB

FTB Chunks; Essentials; Ultimine; Filter System; XMod Compat.

### Maps / compasses / QoL

Xaero's Minimap; Xaero's World Map; Nature's Compass; Explorer's Compass; Structure Compass; Waystones; AppleSkin; Mouse Tweaks; Inventory Essentials; Inventory Tweaks ReFoxed; Crafting Tweaks; Controlling; Searchables; Harvest with ease; Clean Swing Through Grass; No trampling on farmland; Cosmetic Armor Reworked; Elytra Slot; Durability Tooltip; Equipment Compare; Legendary Tooltips; Item Borders; Colorful Hearts; Simply Tooltips; Better Advancements; Clickable advancements; Toast Control; Default Options; Login Protection; NetherPortalFix; Packet Fixer; Too Fast; Accelerated Decay; MmmMmmMmmMmm; Observable; Bad Wither No Cookie; Construction Sticks; Connected Glass; Fusion; Model Gap Fix; Tempad; Perfect Graves; Lootr; Polymorph; Almost Unified; ATO - All the Ores; Supplementaries; Amendments; Dyenamics; Dyenamics and Friends.

### UI / loading / recipes

EMI Enchants; TooManyRecipeViewers; FancyMenu; Drippy Loading Screen; Konkrete; Melody; Colorwheel; Colorwheel Patcher; Euphoria Patches.

### Auth / compat

NeoAuth; Better Compatibility Checker.

### Libraries (only with a consumer)

Balm; Bookshelf; Caelus; Cobweb; Curios API; Fzzy Config; Iceberg; Jupiter; Kotlin for Forge; Moonlight Lib; Mysterious Mountain Lib; Patchouli; Prism; Resourceful Lib; SuperMartijn642 Config / Core; BCLib Forge; WunderLib Forge; EdivadLib; Uranus.

### Other Forge leftovers

Chunky; Crash Utilities. Any other slug on `forge-1.20.1` `pack/mods/` not named above is still not ported — compare that tree to `pack/mods/*.pw.toml` on this branch.
