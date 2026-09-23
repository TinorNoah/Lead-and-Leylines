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
