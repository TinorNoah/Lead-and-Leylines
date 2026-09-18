# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Git tags are `vX.Y.Z`. Headers here are `## [X.Y.Z]` with no `v`.

Minecraft 1.20.1 Forge history lives on branch `forge-1.20.1` (tag `archive/forge-1.20.1`). Do not reuse tags `v0.0.1`–`v0.0.9`. The first 1.21.1 NeoForge GitHub/store ship is `v0.1.0`.

## [Unreleased]

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

### Fixed

- New worlds no longer crash during generation when Terralith biomes share decoration order with Oh The Biomes We've Gone.

### Removed

- Noisium (incompatible with Bye?Pregen!) and Achievements Optimizer (replaced by Cerulean).
