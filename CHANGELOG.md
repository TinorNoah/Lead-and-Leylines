# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Git tags are `vX.Y.Z`. Headers here are `## [X.Y.Z]` with no `v`.

Minecraft 1.20.1 Forge history lives on branch `forge-1.20.1` (tag `archive/forge-1.20.1`). Do not reuse tags `v0.0.1`–`v0.0.9`. The first 1.21.1 NeoForge GitHub/store ship is `v0.1.0`.

## [Unreleased]

### Added

### Changed

### Fixed

### Removed

## [0.1.10] - 2026-09-26

### Added

- Sort inventories, lock slots, save gear sets, and move items with more mouse gestures.
- Mute chosen sounds, add more sound effects, and hear reverb through blocks.
- More glass, a tape measure, laser mining gadgets, elevators, and one-click multiblock building.
- Programmable routers, including Mekanism parts and Modern Industrialization energy.
- Modern Industrialization and Just Dire Things, as extra automation beside Create and Mekanism.
- Request stock in Applied Energistics, and wear a portable QIO on a Curios slot.
- Iron's jewelry, more Ars Nouveau glyphs, and Neo Vitae blood magic.
- Compact redstone, and modded loot in When Dungeons Arise chests.
- The vanilla recipe book is gone. JEI stays.
- KubeJS can script recipes and loot. No scripts ship with this yet.
- Modern Dynamics pipes, XNet channels, and simple conveyor belts for logistics.
- Rechiseled (with Chipped, Create, and Applied Energistics bridges) beside Chipped.
- A large Create factory wave: Enchantment Industry, Central Kitchen, New Age, Big Cannons, TFMG, Alloyed, Diesel Generators, Ore Excavation, and related addons.
- Extended and Solar Industrialization, Flux Networks, DimStorage, Construction Sticks, Tempad, Mob Grinding Utils, Agritech, and BuffMobs.
- Inventory Essentials beside Inventory Profiles Next.
- Better Advanced Tooltips so the latest KubeJS can load.

### Changed

- KubeJS is on build 377 (needs Better Advanced Tooltips).

### Fixed

- Dropped Modern Industrialization Extentended Integrations: it crashes MI 2.5.8 looking for casing `modern_industrialization:iv`.

### Removed

- Pipez and Pipez Lag Fix. Use Modern Dynamics, XNet, and conveyors instead.

## [0.1.9] - 2026-09-26

### Added

- Chipped block variants, Handcrafted and Macaw's furniture, and Macaw's doors, windows, and fences.
- Glass connects, and many items use 3D models.
- Enchantment tooltips say what each enchantment does.
- Items stay visible on crafting tables.
- Twilight Forest boss respawns, villages, and dungeons.
- BetterEnd: New Dawn (with Farmer's Cutting), beside Nullscape and Unusual End.
- YUNG rebuilt dungeons, strongholds, desert temples, ocean monuments, and the End island; Luki's ancient cities and woodland mansions.
- Particle rain, subtle ambient effects, Colourful Everywhere GUI recolor, BetterF3, loot pickup toasts, prettier enchanted books, and enchantment icons.
- Cross-dimension Refined Storage wireless, Fast Item Frames, and DarkLoot mob loot (editable datapack).

### Changed

### Fixed

### Removed

- Gun lights and gun blueprints are gone from Timeless and Classics Zero.

## [0.1.8] - 2026-09-25

### Added

- The leyline emblem is the pack icon.

### Changed

### Fixed

- The loading screen no longer crashes while Armageddon models load.

### Removed

## [0.1.7] - 2026-09-25

### Added

- New mobs and bosses: a desert illager arena, Qliphoth Awakening, Bosses of Mass Destruction (including integrated structures), Spawn, Critters and Companions, Companions, Armageddon, and Born in Chaos.
- Alex's Mobs Continued, with tweaks and cooking recipes. Alex's Caves animals can be cooked too.
- Iron's Spells, with Twilight Forest spells, Create spell tools, Farmer's Delight spells, Alex's Caves spells, and teleport spells that still work on Aeronautics ships.
- Quark's small vanilla tweaks. Armageddon tools show their tier, and Jade names Born in Chaos infected diamond ore as diamond ore.
- Apotheosis affixes and gems, including enchanting, movable spawners, Iron's Spells gear, Point Blank and TaCZ guns, and Create machines. Flight potions and charms are off. Affix numbers can be changed in the balance config. Affix tooltips are shorter.
- More bosses and places: Mutant Monsters, Illager Invasion, Mowzie's Mobs, Myths & Legends, Legendary Monsters, an expanded End, Forbidden and Arcanus, and extra dungeons.
- Pam's HarvestCraft foods, crops, and fruit trees, beside Farmer's Delight.

### Changed

- The installed-mod browser uses a leyline restyle with clearer filters, card and list views, and a mod detail drawer.

### Fixed

### Removed

## [0.1.6] - 2026-09-24

### Added

- AE2 extras: crafting tree, schematic cannon link, mega disks, pattern-provider compat, infinite water/lava/cobblestone drives, machine pulling, an AE2/Refined Storage pattern converter, and one universal processor press.
- Create extras: electric motor and alternator, decoration blocks, encased parts, climbable Aeronautics ropes, aviator goggles in a Curios slot, and Aeronautics vehicles drawn on Xaero's maps.
- Ars extras: spell control, dual-element gear, Create glyphs and tools, Ars foods, and refreshed item textures.
- Crystalix colored glass, Artifacts curios, player graves, sleeping bags and hammocks, Building Gadgets, Autochef's Delight, and Barbeque's Delight.
- Ambient sounds, a book that holds other books, attribute fixes, bridge assist, a clearer mods screen, and client annoyance toggles.
- Backpack upgrade icons, and new models for the ender dragon, wither, warden, and elder guardian.

### Removed

- Vic's Point Blank Interaction. Holding a Point Blank gun no longer opens or uses the block or mob you are looking at.
- Structure Compass. Explorer's Compass still finds structures.

## [0.1.5] - 2026-09-24

### Fixed

- Vic's Point Blank Interaction no longer stops multiplayer from starting. Using blocks and mobs while holding a Point Blank gun still works.
- Point Blank no longer writes a log line for every normal block and mob interaction.
- Distant TaCZ gunshot echoes stay on. The per-shot debug trace is off.
- Bastion hoglin-stable and treasure chests include My Nether's Delight loot again.
- Terralith caves, gravel deserts, and savannas use Ecliptic Seasons' current rain tags.
- Ocelots in Regions Unexplored forests count as creatures, and sand snappers in Lost Caves count as monsters.
- Nether Expansion recipes for items that are not in this version no longer fail to load.

### Removed

- Call of Duty Warzone guns. Their models and textures do not load on this version, so those items were missing-texture blocks.
- Distant terrain LOD. Voxy, Voxy Server Side, and Forgified Fabric API are gone.

## [0.1.4] - 2026-09-23

### Changed

- Structures that use normal structure spacing are about twice as far apart.
- Fire dragons live in the Nether. Dragon skeletons no longer generate on their own; a dragon you kill still leaves a corpse.

### Fixed

- Boot no longer warns about Terralith's disabled andesite, diorite, and granite blobs. Those stones still generate from Terralith.
- You can join with Vic's Point Blank Interaction installed. The server now has the `pointblank_passthrough:interaction` channel.
- JEI's Move Items button can fill a crafting grid in multiplayer. JEI and MezzConfig ship on both sides.
- Skeletons and the other Epic Fight mobs render as Epic Fight models again. Fresh Animations and Darkest Ages no longer replace those mobs.

## [0.1.3] - 2026-09-23

### Added

- Archaion (the Ancient Keep) and Olympus! (Greek artifacts, mobs, and structures).
- Fresh Animations with its extensions, Darkest Ages mob looks, restyled boss bars, and Xaero's map icons.
- Hold the tag key (semicolon, rebindable) to list an item's tags inside its tooltip.
- Vic's Point Blank, with Extended Edition, Gun Gale, Half-Life, and Cyberpunk 2077 guns. You can use blocks while holding one, and the shots hit Aeronautics vehicles.
- MCS2 guns for Timeless and Classics Zero.
- Daffa's Arsenal, CS+, and Call of Duty Warzone guns for Timeless and Classics Zero.

### Changed

- Item tooltips are framed by item type, and untagged items from each major mod get that mod's frame.
- Parkour, Epic Fight, and both gun mods no longer share keys. M opens Xaero's world map only. Reload stays R. Epic Fight mode is the tilde key, dodge is C, and lock-on is T. ParCool dodges are left Alt, TaCZ zoom is middle mouse, and prone is Z. Shader reload and the shader toggle are unbound. Ultimine is Tab.

### Fixed

- Epic Fight combat no longer leaves the normal first-person hand floating. Punchy hides its arms while Epic Fight mode is on.

### Removed

- Legendary Tooltips, Simply Tooltips, and Better Advanced Tooltips. Fzzy Config left with Simply Tooltips.

## [0.1.2] - 2026-09-23

### Fixed

- Epic Fight × Curios Compat is client-only again, so dedicated servers no longer crash loading `ClientCuriosCompat`.
- Empty-override datapack clears orphan Mekanism More Machine / Extras / ExtendedAE loot tables that pointed at unregistered items (boot parse spam).
- JEI QuickCraft and JEI Stuff ship on both sides so their required network channels exist on dedicated servers.
- JEI WorldGen ships on both sides, so world-gen pages can load when you join instead of asking for the mod on the server.

### Removed

- JEI++ (client crash on join: its bookmark mixin still calls JEI's old `mezz.jei.gui.input.IUserInputHandler`, which JEI 19.57 moved).
- Ecliptic Seasons : Voxy Compact and Voxy - Make it compatible (client crash applying mixins when unofficial Voxy is not installed; Voxy cannot ship in the pack).
- Epic Fight Nightfall and Invincible Lib (Nightfall reads client VFX config on dedicated servers and crashes when mobs gain effects). AAA Particles stays.
- Mekanism Covers (beta Sodium mixin fails on join with Sodium 0.8.13; no newer 1.21.1 build).

## [0.1.1] - 2026-09-23

### Added

- Just Enough Items (JEI) 19.57, with MezzConfig, as the recipe viewer.
- JEI companions: JEI++, AE2 JEI Integration, Refined Storage JEI Integration, JEIOptimizer, Sophisticated JEI Index, Smithing Template Viewer, Create JEI Compat, JEI Stuff, JEI QuickCraft, and SpectrumJEI. JEI WorldGen was already in.
- Create Aeronautics 1.3.2 (planes, airships, vehicles) with Sable 2.0.5. Shaders may look wrong on those contraptions.
- Mekanism extras: generator/multiblock JEI pages, Jade upgrades, covers (beta), Extras, Elements, Refined Storage chemicals, Aeronautics compat, Create ponders, and chemical tanks in Sophisticated backpacks.
- Sophisticated backpacks/storage companions: Ars Nouveau, Create recipes, tactical backpacks (beta), item actions, inventory helpers, Yukami tab, chest renderer (NeoForge pin), Jade, Refined Storage quick-deposit, and Demagnetizer (beta, NeoForge pin).
- Patchouli (guidebooks; required by Mekanism Elements).
- Timeless and Classics Zero (unofficial 1.21.1 port) with Pack Upgrader, gun packs, ammo, turrets, armed mobs, Aeronautics/Create/AE2 bridges, and JEI/Jade helpers. Guns Lights is 2.8.2 (2.9.0 is 1.20.x).
- Create crushing/compat for Regions Unexplored and Oh The Biomes We've Gone, plus Block Variants for OTBWG.
- Just Enough Resources (ore/mob pages in JEI), YUNG's Cave Biomes, and Variants & Ventures.
- Nether extras: Jaden's Nether Expansion (and Delight), BetterNether: New Dawn, Eternal Nether, Nether Remastered, Just-In Nether, Nether Villager Trader, and Netherite Tweaks. Farmer's Cutting for BetterNether is in; Cutting for RU and OTBWG was already in.
- Epic Fight with ParCool, Nightfall (AAA Particles), Twilight Forest / TaCZ / Curios / Ice and Fire compat, Bosses' Rise, and related helpers. Ice and Fire: Community Edition is in so that armor compat works.
- Alex's Caves Continued (Codxlib, not Citadel), Compat Structure, and Bad Wither No Cookie Reloaded (quiets boss-fight music).
- Ecliptic Seasons (solar-term weather, snow, and crops) with SeasonHUD, crop bundles, multimod patches, and a Serene Seasons API bridge. Do not add Serene Seasons itself.
- Distant terrain LOD streaming (Voxy Server Side) and Voxy compatibility patches. The Voxy renderer jar is All Rights Reserved and is not redistributed; build the unofficial NeoForge port locally.

### Changed

- Updated sixteen other 1.21.1 NeoForge mods, including Chunk Pregenerator, Entity Culling, Create Better FPS, ExtendedAE, Aquamirae, and Lithostitched.
- Overworld, Nether, and End biome regions are as large as TerraBlender allows, so Terralith, Oh The Biomes We've Gone, Regions Unexplored, and vanilla sit in big continents instead of mixed patches. Individual biomes inside those continents use Large Biomes climate scale, with a bit less speckle at the edges. Alex's Caves biomes are larger and farther apart. New world required. Do not pick the Large Biomes world type.
- Ice and Fire pixie villages generate in the Nether instead of overworld forests. New Nether chunks required.
- BetterNether / WorldWeaver no longer opens the BetterX welcome setup screen on launch.

### Fixed

- Create, Sophisticated, and Polymorph recipe pages load under real JEI instead of TooManyRecipeViewers' fake 19.27 stub.

### Removed

- TaCZ: Immersive Ballistic and TaCZ Tweaks (alpha; Iris vertex-format conflict on load).
- TaCZ / Sophisticated Backpacks ammo addon (it requires a different TaCZ mod id than the unofficial 1.21.1 port).
- EMI, EMI Ores, EMI Enchanting, EMI QoL Tweaks, and TooManyRecipeViewers.
- Iris Flywheel Compat (mixin conflict with Colorwheel; Colorwheel stays for Create + shaders).
- Tectonic. New chunks use vanilla-height terrain plus the remaining biome and structure mods; already-generated Tectonic land stays until those chunks are regenerated.

## [0.1.0] - 2026-09-18

### Changed

- The pack is rebuilt for Minecraft 1.21.1 NeoForge. New world required.
- Discontinued Modrinth as a publishing target; CurseForge is now the sole public store listing.

### Added

- First performance and smoothness stack: Sodium and Iris (replacing Embeddium and Oculus), Lithium, FerriteCore, ModernFix, ImmediatelyFast, FastWorkbench / FastFurnace / FastSuite, and related leak, crash, and entity helpers.
- Extra renderer and smoothness mods: Sodium Extra, Flerovium, AsyncParticles, More Culling, Structure Layout Optimizer, Ksyxis, Disconnect Packet Fix, quick pack, CrashExploitFixer, Async Logger, ResourcePackCached, and Chunk Pregenerator.
- Create (with Iris Flywheel Compat, Create Better FPS, and Threaded Trains), FTB Quests (Library, Teams, Optimizer), and Pipez.
- Pipez Lag Fix, Cerulean (with TxniLib), Bye?Pregen!, The Twilight Forest, The Lost Cities, and Tectonic (with Lithostitched).
- Regions Unexplored and Oh The Biomes We've Gone, with TerraBlender, GeckoLib, CorgiLib, and Oh The Trees You'll Grow. A pack datapack drops Regions Unexplored's Lithostitched structure checks so world generation does not freeze.
- Jade, EMI (with QoL Tweaks and WorldGen pages), Terralith, GeckolibBetterFPS, Nullscape, Structurify, When Dungeons Arise, YUNG's caves/fortresses/bridges, Moog's mineshafts, Epic Structures, Amplified Nether, Infernal Expansion Redux, Terrain Slabs, Awesome Dungeon, and Aquamirae.
- Feature Recycler, so Terralith and Oh The Biomes We've Gone can generate in the same world.
- FastBoot (faster client load), Fluidium (distant fluids tick less), LC²H (multithreaded Lost Cities), BiomeSpy (faster `/locate`), DarkSleep (half the players can skip the night), and MemGuard (heap monitor next to AllTheLeaks).
- Maps, storage, and QoL: Xaero's maps, compasses, Waystones, Sophisticated Backpacks/Storage, Functional Storage, Botany Pots/Trees, FTB Chunks/Essentials/Ultimine, Lootr, Supplementaries, and Better Advanced Tooltips (F3+H item tags).
- Applied Energistics 2 (including AE2 Things), Refined Storage (with Quartz Arsenal and Cable Tiers), Mekanism, Ars Nouveau (including Ars Énergistique), Farmer's Delight, Spectrum, Complementary/BSL shaders with Euphoria Patches, and C2ME. The C2ME OpenCL module is not included: it requires Java 25.

### Fixed

- New worlds no longer crash during generation when Terralith biomes share decoration order with Oh The Biomes We've Gone.

### Removed

- Noisium (incompatible with Bye?Pregen!) and Achievements Optimizer (replaced by Cerulean).
