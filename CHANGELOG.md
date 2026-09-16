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

## [0.0.8] - 2026-09-16

### Added

- Cross-mod glue: Jade Addons (Create, Lootr, Supplementaries), Ars Creo (Ars on Create contraptions), Slice & Dice and Create: Central Kitchen (Farmer’s Delight automation), Create + Alex’s Caves recipes, Create: Applied Kinetics (AE2 machines), and AE2 wireless terminals.
- Farmer’s Delight cutting recipes for Regions Unexplored, Oh The Biomes We’ve Gone, and Twilight Forest woods.
- Nullscape End biomes. New End chunks only; restart required.

### Changed

- Overworld biomes are a bit smaller (Tectonic climate scale 0.16). New chunks only; restart required.
- New Overworld chunks generate cheaper: Tectonic extra caves, jungle pillars, underground rivers, lava tunnels, rolling hills, and ocean islands are off; Streams uses the Potato accuracy preset with sparser rivers. Restart required; already-generated land is unchanged.

### Removed

- Distant Horizons. Far terrain LODs are gone; vanilla/shader view distance is the cap.

## [0.0.7] - 2026-09-16

### Added

- AppleSkin hunger and saturation overlay on the HUD.
- NeoAuth in-game Microsoft re-login when a session expires (client only).
- Ten Iris shader packs for testing (Complementary Reimagined and Unbound, BSL, Photon, MakeUp Ultra Fast, Super Duper Vanilla, Mellow, Miniature, Noble, Solas). None is on by default; pick one in Video Settings → Shader Packs.

### Changed

- Overworld terrain is about 40 blocks lower (Tectonic vertical scale 0.80; Terralith still only adds biomes). New chunks only; restart required.

## [0.0.6] - 2026-09-16

### Added

- Ice and Fire Community Edition (dragons and other mythical creatures). The original Ice and Fire jar cannot sit next to it.
- Timeless and Classics Zero with extra gun packs: LesRaisins Tactical, LesRaisins Append, Gucci attachments, and Daffa's Arsenal.
- Simply Swords, Simply More, and Better Combat melee (guns stay TACZ).
- Ars Elemental foci and glyphs on top of Ars Nouveau.
- Placeable Trash Cans for item/fluid/energy voids. The inventory trash slot is unchanged.
- Legendary Tooltips and Equipment Compare.
- Amendments, so Supplementaries wall lanterns, skull candles, ceiling pots/banners, and skull piles stay.

### Changed

- Streams Reflowing 2.13.7 with **LOW** river accuracy so new land generates faster on Tectonic (currents still arrive with the land; dedicated worlds no longer rebuild every stream network on each start). Rivers in new chunks are coarser.

### Fixed

- Epic Structure dungeons no longer spawn item frames with 1.21 item data (empty frames, hanging-entity errors, and a chunk-gen hitch). Dungeons pin the 1.20-native 1.0 jar.

## [0.0.5] - 2026-09-16

### Changed

- Distant Horizons uses ZGC (`user_jvm_args.txt`) so far terrain does not hitch on the default G1 collector.

### Fixed

- The overlapping-recipe picker no longer crashes on launch with EMI.

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
