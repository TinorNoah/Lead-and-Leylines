# Deferred and not-yet-ported mods

Not an install list. Each row still needs a fresh 1.21.1 NeoForge research pass and explicit file approval. Minecraft / loader: [`pack/pack.toml`](../../pack/pack.toml). History of the old pack: branch `forge-1.20.1`.

Installed today: [manifest.md](manifest.md). Performance decisions: [performance.md](performance.md).

## Named list (2026-09-18) — not added

None of these were installed. “Recommended” means researched as a possible next wave; do not treat it as approved.

### Researched as a possible next wave (waiting on approval)

| Named as | Project | Why not in the pack yet |
|---|---|---|
| sodium extras | Sodium Extra 0.9.4 | Extra now has a 1.21.1 NeoForge file for Sodium 0.8.13. Held until you pick Extra vs Chloride (not both). |
| sodium lights | Sodium Dynamic Lights + Sodium Options API | Client lights addon. Waiting on approval. |
| Sodium/Embeddium Options Mod Compat | Sodium Options Mod Compat | Needs Sodium Options API. Waiting on approval. |
| server core | ServerCore 1.5.19 | Vanilla-safe defaults; leave Entity Activation Range off unless tuned. Waiting on approval. |
| Particle Core | Particle Core + Fzzy Config + Kotlin for Forge | Pulls Kotlin into the pack. Waiting on approval. |
| Redirected | Redirected + TxniLib | Enum intern. Waiting on approval. |
| Chunk-Pregenerator | Chunk Pregenerator 4.5.3 (CurseForge) | Operator pregen; not on Modrinth for this loader. Waiting on approval. |
| Structure Layout Optimizer | SLO + Resourceful Config | Structure gen. Waiting on approval. |
| More culling | More Culling + Cloth Config | Complements Entity Culling; watch Iris. Waiting on approval. |
| Crash exploit filter | CrashExploitFixer 2.0.0 | File tags 1.21.1–1.21.4. Waiting on approval. |
| Flevorium | Flerovium 1.1.3 | Entity / block-entity draw cost. Do not stack with Better Block Entities. Waiting on approval. |
| AsyncParticles | AsyncParticles 21.1.4.4 | Particle thread. Waiting on approval. |
| Gnetum | Gnetum 3.3.6 | Spreads HUD updates. Waiting on approval. |
| Ksyxis | Ksyxis 1.4.4 | Faster spawn-region load. Waiting on approval. |
| Achievements Optimizer | Achievements Optimizer 2.1.0 | Advancement tick. Waiting on approval. |
| LightSpeedRe | LightSpeedRe 1.2.3 | Launch. Waiting on approval. |
| quick pack | quick pack 1.5.0 | Faster pack reload. Waiting on approval. |
| Disconnect Packet Fix | Disconnect Packet Fix 2.0.1 | Bad disconnect packets. Waiting on approval. |
| Async Logger | Async Logger 2.2.2 | Log I/O. Waiting on approval. |
| Put A Plug In it! (PAPI) | PAPI 1.2.1 | Extra leak plugs beside AllTheLeaks. Waiting on approval. |
| ResourcePackCached | ResourcePackCached 1.2.5 | Client pack cache. Waiting on approval. |

### Overlaps something already in the pack or in the recommended set

| Named as | Why not |
|---|---|
| (Sodium) Chloride | Same job as Sodium Extra (leaves, fog, FPS overlay, entity distance). ARR. Extra is the better license. Do not run both. |
| Sodium Extras (Txni, not Extra) | Older third Extra. Official Extra covers this. |
| Sodium Leaf Culling | Extra / Chloride already do leaves. |
| OptiLeaves | Same leaf-culling niche. |
| Despawn Tweaks | Let Me Despawn is already installed. |
| NoisiumForked | Noisium 2.3.0 is already installed. Do not stack. Later we can *replace* 2.3.0 with Forked 2.7.0. |
| Idle Boost | Dynamic FPS already lowers FPS when unfocused. |
| Better Block Entities | Same draw-cost space as Flerovium. |
| Cerulean | Same advancement-tick space as Achievements Optimizer. |
| Bye?Pregen! | Second pregen/gen-spike tool next to Chunk Pregenerator. |
| Performance Tweaks | Search lands on Adaptive Performance Tweaks again. |

### Needs a parent mod we have not ported

| Named as | Missing parent |
|---|---|
| Iris and oculus flywheel compat | Flywheel / Create |
| Create Better FPS | Create |
| Create: Threaded Trains | Create |
| Vanillin | Flywheel |
| FTB Quests Optimizer | FTB Quests |
| GeckolibBetterFPS | GeckoLib |
| LC²H [Lost Cities: Multithreaded] | Lost Cities (no 1.21.1 NeoForge file anyway) |
| TwilightForest Thread Safety Addon | Twilight Forest (no 1.21.1 file) |
| Pipez Lag Fix | Pipez (no matching project found) |

### Wrong renderer, missing file, or not a single pack mod

| Named as | Why not |
|---|---|
| Bocchium | Bedrock-face cull for Embeddium / Rubidium. This pack uses Sodium. |
| FastBoot | The Modrinth hit is a whole modpack `.mrpack`, not one mod. |
| Fluidium | No 1.21.1 NeoForge project found. |
| DarkTimer - RPG Clear Entity Lag | No 1.21.1 NeoForge file. |

### Gameplay-changing, crashy, or too much library for the gain

| Named as | Why not |
|---|---|
| DoesPotatoTick? | Freezes distant entities. Overlaps ServerCore’s optional EAR. Easy farm/machine breakage. |
| Immersive Optimization | Same entity-scheduler idea. |
| Adaptive Performance Tweaks | Auto-cuts view distance, spawns, items. Changes how the world plays. |
| TCT ClearLag | Deletes entities. ARR. |
| Dimensional Threading Reforked | One world per thread. High crash rate in mixed packs. |
| Invasive Optimizations | Author: disable this first if anything breaks. Optional Create / Pipez / AE2 patches we do not have. |
| ScalableLux | Alpha lighting engine. |
| Ixeris | Moves input off-thread. Breaks some launchers / overlays. |
| Krypton Reno | Network mixins. Fragile next to NeoForge / Lithium. |
| Fast Item Frames | New block-entity type (world data) + Puzzles Lib. |
| BetterGrassify | Pulls Forgified Fabric API for better grass. |
| Loading Backgrounds | Cosmetic + Architectury. |
| Too Many Entities | Client entity limiter + Architectury + Cloth. |
| GPUTape | GPU booster + ToadLib; modest vs the renderer stack we already have. |
| MemGuard | ARR; forces GC. Can hitch more than it helps. |
| DarkSleep - RPG Sleep Percentage | Sleep-percentage RPG rule, not an optimizer. ARR. |
| BiomeSpy | Biome lookup utility, not FPS/TPS. |

Shader packs and Colorwheel stay deferred until the renderer wave is approved. See [performance.md](performance.md).

## 1.20.1 Forge pack — not on 1.21.1 NeoForge yet

Source: `pack/mods/*.pw.toml` on branch `forge-1.20.1` (239 mods). Already represented on NeoForge: AllTheLeaks, Almanac Lib, BadOptimizations, Clumps, Crash Assistant, Cupboard, Dynamic FPS, Entity Culling, FastFurnace, FastSuite, FastWorkbench, FerriteCore, ImmediatelyFast, Let Me Despawn, ModernFix, Neruina, Noisium, Placebo, Smooth Chunk Save.

Replaced, do not port as-is: Embeddium → Sodium, Oculus → Iris, Radium → Lithium, Rubidium Extra → Sodium Extra (held).

Configurable is new on NeoForge (Neruina dependency) and was not on the Forge list.

Count still to research: **216**. Do not dump-install.

### Create

Create; Create Ultimine; Slice & Dice; Central Kitchen; Applied Kinetics; Alex's Caves Compat; Sky Village; Sophisticated Backpacks / Storage Create integrations.

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

Tectonic; Terralith; TerraBlender; Oh The Biomes We've Gone; Oh The Trees You'll Grow; Regions Unexplored; Nullscape; Lithostitched; Structurify; Better Sparse Structures; Alex's Caves; Citadel; The Lost Cities; The Twilight Forest; When Dungeons Arise; Seven Seas; Awesome Dungeon; Awesome Dungeon Nether; YUNG's API / Better Caves / Better Nether Fortresses / Bridges; Stalwart Dungeons; Moog's Structure Lib; MMR Mineshafts; Epic Structures (Villages, Jungle Temples, Witch Huts); Amplified Nether; Bygone Nether; BetterNether Forge; Infernal Expansion Redux; Aquamirae; Countered's Terrain Slabs.

### Farmer's Delight cluster

Farmer's Delight; Delightful; Corn Delight; My Nether's Delight; Twilight's Flavor & Delight; Farmer's Cutting (BWG, Regions Unexplored, Twilight Forest).

### Storage / backpacks / logistics

Sophisticated Core / Backpacks / Storage; Functional Storage; Botany Pots; Botany Trees; Trash Cans; TrashSlot; Packing Tape; Cable Tiers; Titanium.

### FTB

FTB Library; Teams; Chunks; Quests; Essentials; Ultimine; Filter System; XMod Compat.

### Maps / compasses / QoL

Xaero's Minimap; Xaero's World Map; Jade; Jade Addons; Nature's Compass; Explorer's Compass; Structure Compass; Waystones; AppleSkin; Mouse Tweaks; Inventory Essentials; Inventory Tweaks ReFoxed; Crafting Tweaks; Controlling; Searchables; Harvest with ease; Clean Swing Through Grass; No trampling on farmland; Cosmetic Armor Reworked; Elytra Slot; Durability Tooltip; Equipment Compare; Legendary Tooltips; Item Borders; Colorful Hearts; Simply Tooltips; Better Advancements; Clickable advancements; Toast Control; Default Options; Login Protection; NetherPortalFix; Packet Fixer; Too Fast; Accelerated Decay; MmmMmmMmmMmm; Observable; Bad Wither No Cookie; Construction Sticks; Connected Glass; Fusion; Model Gap Fix; Tempad; Perfect Graves; Lootr; Polymorph; Almost Unified; ATO - All the Ores; Supplementaries; Amendments; Dyenamics; Dyenamics and Friends.

### UI / loading / recipes

EMI; TooManyRecipeViewers; EMI Enchants; EMI QoL Tweaks; JEI WorldGen; FancyMenu; Drippy Loading Screen; Konkrete; Melody; Colorwheel; Colorwheel Patcher; Euphoria Patches.

### Auth / compat

NeoAuth; Better Compatibility Checker.

### Libraries (only with a consumer)

Architectury API; Balm; Bookshelf; Caelus; Cloth Config; Cobweb; CorgiLib; Curios API; Fzzy Config; Geckolib; Iceberg; Jupiter; Kotlin for Forge; Library Ferret; Moonlight Lib; Mysterious Mountain Lib; Patchouli; Prism; Resourceful Config; Resourceful Lib; SuperMartijn642 Config / Core; YACL; BCLib Forge; WunderLib Forge; Fragmentum; EdivadLib; Uranus.

### Other Forge leftovers

Chunky; Crash Utilities. Any other slug on `forge-1.20.1` `pack/mods/` not named above is still not ported — compare that tree to `pack/mods/*.pw.toml` on this branch.
