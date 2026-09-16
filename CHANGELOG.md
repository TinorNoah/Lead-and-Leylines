# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Git tags are `vX.Y.Z`. Headers here are `## [X.Y.Z]` with no `v`.

## [Unreleased]

### Added

### Changed

### Fixed

### Removed

## [0.0.4] - 2026-09-16

### Added

- Distant Horizons is in but **off**. Turn it on in Options → Distant Horizons if you want LODs; quality stays at the floor until you raise it.
- Ars Nouveau, Applied Energistics 2 (recipes show in EMI), Twilight Forest, Supplementaries, Waystones, Lootr, and target dummies.
- QoL: searchable keybinds, inventory mouse drag, better advancement UI, crafting-grid buttons, overlapping-recipe picker, Nether portal linking, inventory trash slot, and a loading-screen framework. FTB Chunks **Open Map** is unbound on new installs so it does not fight Xaero on **M**.

### Changed

- Terralith, Regions Unexplored, and Oh The Biomes We’ve Gone biomes are larger (Tectonic climate scale 0.125, TerraBlender regions at max size).
- Create Sky Villages spawn more often and higher, so Tectonic mountains are less likely to eat them.
- After a crash, Crash Assistant **Request Help** opens the Lead and Leylines Discord.

### Fixed

- Tectonic now loads: Lithostitched 1.4.11 is in the pack (Tectonic 3.0.17 requires it).
- `/rtp` no longer searches 25,000 blocks (that hung on new Tectonic terrain). It now stays within 2,000 blocks of origin and gives up after 3 tries.
- Fast travel (Create trains and similar) should no longer rubber-band with “moved too quickly”.
- `/locate` and Explorer’s Compass should stop pointing at empty spots. StructureOverlapless was skipping placement (including Create Sky Villages and When Dungeons Arise towers) after the start was already registered. Needs a **new world**. Sky villages sit high — look up from the locate ground Y. In the amplified Nether, fortress locate still uses `~` for Y.

### Removed

- StructureOverlapless (it skipped colliding structures instead of moving them, so locates were empty).
- When Dungeons Arise Sparse Structures compat packs (they made WDA almost unfindable).

## [0.0.3] - 2026-09-16

### Added

- Drawers (Functional Storage), upgradeable chests and barrels (Sophisticated Storage), and Sophisticated Backpacks with a Curios back slot. Create integrations so they work on contraptions.
- Taller Nether (Amplified Nether) with BetterNether biomes, YUNG fortresses, Infernal Expansion Redux, and Bygone Nether. Extra dungeons from Stalwart and Awesome Dungeon (overworld and Nether). Farmer's Delight cooking with My Nether's Delight. Moog's Mineshafts Reimagined (not YUNG mineshafts).
- Overworld biomes from Terralith, Regions Unexplored, and Oh The Biomes We've Gone, plus Aquamirae and Alex's Caves. Tectonic terrain (not Lithosphere). YUNG caves and bridges, extra structures (When Dungeons Arise, Epic Structures, Create Sky Village), Nature's Compass, Explorer's Compass, and Chunky for pregen.

## [0.0.2] - 2026-09-13

### Added

- QoL and Create cut: FTB (claims, quests, teams, ultimine), EMI recipe viewer, Jade, Xaero maps, and Create.
- Colorwheel (and Colorwheel Patcher) so Create's renderer works under Oculus shaders.
- FTB Chunks is the claim layer with its minimap off; Xaero is the everyday map UI.

### Removed

- EMI QoL Tweaks — CurseForge blocked API downloads for that file.

## [0.0.1] - 2026-09-13

### Added

- First playable cut: Forge performance and shader stack (Embeddium, Oculus, FerriteCore, ModernFix, and related smoothness mods). Shader packs are not shipped yet.
