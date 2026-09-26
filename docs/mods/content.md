# Content — considered, chosen, dropped

Target is whatever Minecraft + NeoForge are in [`pack/pack.toml`](../../pack/pack.toml). Re-check store pages before a file bump.

**Status:** Create + Aeronautics, FTB extras, Twilight Forest, Lost Cities, Aquamirae, Supplementaries, AE2, RS, Mekanism, Ars, Farmer's Delight, Spectrum, TaCZ guns, Vic's Point Blank, Epic Fight + ParCool, Ice and Fire CE. Remaining Create kitchen addons: [deferred.md](deferred.md).

## Chosen

| Mod | Pinned file | `side` | Why |
|---|---|---|---|
| Create | `create-1.21.1-6.0.10.jar` | both | Contraptions and kinetics. Flywheel is embedded. World data. |
| Sable | `sable-neoforge-1.21.1-2.0.5.jar` | both | Physics sub-levels for Aeronautics. Mixin-heavy; author warns about other mods. |
| Create Aeronautics | `create-aeronautics-bundled-1.21.1-1.3.2.jar` | both | Planes, airships, cars. World data. Known visual issues with Iris. Climbable Ropes, Curios goggles, and a client Xaero map overlay are in. |
| Architectury API | `architectury-13.0.11-neoforge.jar` | both | Required by FTB. |
| FTB Library | `ftb-library-neoforge-2101.1.36.jar` | both | Required by FTB Quests / Teams. ARR. |
| FTB Teams | `ftb-teams-neoforge-2101.1.11.jar` | both | Shared quest progress. ARR. |
| FTB Quests | `ftb-quests-neoforge-2101.1.36.jar` | both | Quest book. World data. ARR. |
| The Twilight Forest | `twilightforest-1.21.1-4.8.3345-universal.jar` | both | Dimension. World data. Thread-safety addon still 1.20.1-only. Bosses Resurrection and Dungeons & Villages are in. |
| The Lost Cities | `lostcities-1.21-8.4.4.jar` | both | City generation. World data. LC²H 4.2.3-LTS is in for multithreaded gen. |
| Aquamirae | `aquamirae-neoforge-1.21.1-7.2.10.jar` | both | Ocean structures, boss, and items. World data. Requires GeckoLib and Fragmentum. Modrinth pin. |
| Supplementaries | `supplementaries-1.21.1-3.9.9-neoforge.jar` | both | Decor and utility blocks. World data. Moonlight. |
| Knight Lib | `knightlib-neoforge-1.21.1-2.0.2.jar` | both | Required by Olympus!. |
| Olympus! | `olympusmythology-neoforge-1.21.1-1.0.8.jar` | both | Greek artifacts, mobs, and structures. World data. Curios + Knight Lib. |
| Archaion: Echoes of the Fallen | `archaion-1.21.1-1.4.3.jar` | both | Ancient Keep, trial spawners, and a boss. World data. AAA Particles. |
| Amendments | `amendments-1.21-2.1.10-neoforge.jar` | both | Vanilla block tweaks. World data. Moonlight. |
| Create Ultimine | `createultimine-1.21.1-neoforge-1.3.2.jar` | both | Create-aware vein mine with FTB Ultimine. |
| Create Crafts & Additions | `createaddition-1.7.1.jar` | both | Electric motor and alternator. World data. Create `[6.0.7,6.1.0)`. |
| Create Deco | `createdeco-2.1.3.jar` | both | Decoration blocks. World data. Create `[6.0.7,6.1.0)`. |
| Create Encased | `Create Encased-1.21.1-1.9.0-ht3.jar` | both | Encased shafts and cogwheels. World data. Create `[6.0.10,)`. |
| Crystalix | `crystalix-3.0.1.jar` | both | Colored glass. World data. Framed Blocks optional, not installed. |
| Chipped | `chipped-neoforge-1.21.1-4.0.2.jar` | both | Block variants. World data. ARR. Resourceful Lib + Athena. Block Variants stays the biome-wood set. |
| Handcrafted | `handcrafted-neoforge-1.21.1-4.0.3.jar` | both | Furniture. World data. Terrarium Licence. Resourceful Lib. |
| Macaw's Doors | `mcw-doors-1.1.5-mc1.21.1neoforge.jar` | both | Extra doors. World data. MIT. |
| Macaw's Windows | `mcw-mcwwindows-2.4.2-mc1.21.1neoforge.jar` | both | Windows, blinds, shutters, and curtains. World data. ARR. |
| Macaw's Fences and Walls | `mcw-mcwfences-1.2.1-mc1.21.1neoforge.jar` | both | Fences, walls, and gates. World data. MIT. |
| Macaw's Furniture | `mcw-furniture-3.4.1-mc1.21.1neoforge.jar` | both | Furniture beside Supplementaries and Handcrafted. World data. ARR. |
| Fusion (Connected Textures) | `fusion-1.3.15b-neoforge-mc1.21.1.jar` | client | Connected textures. ARR. Client only. Fusion 3D Items and Fusion Connected Glass are forced resource packs. Continuity stays out. |
| Artifacts | `artifacts-neoforge-13.2.5.jar` | both | Exploration curios. World data. Curios integration is in the jar. |
| Epitaphs | `epitaphs-2.2.0_neoforge_1.21.1.jar` | both | Player-locked graves. World data. |
| Comforts | `comforts-neoforge-9.0.5+1.21.1.jar` | both | Sleeping bags and hammocks. World data. |
| Building Gadgets | `buildinggadgets2-1.3.9.jar` | both | Copy, paste, and build gadgets. World data. Project 298187's 1.21.1 file. |
| Create: Sky Village | `create_sky_village-0.0.38 NeoForge 1.21.1.jar` | both | Create village structure. World data. |
| FTB Chunks | `ftb-chunks-neoforge-2101.1.22.jar` | both | Chunk claims. World data. ARR. |
| FTB Essentials | `ftb-essentials-neoforge-2101.1.10.jar` | both | `/home` and related commands. ARR. |
| FTB Ultimine | `ftb-ultimine-neoforge-2101.1.15.jar` | both | Vein mine. ARR. |
| Farmer's Delight | `FarmersDelight-1.21.1-1.3.4.jar` | both | Kitchen. World data. Corn Delight, My Nether's Delight, Twilight's Flavors, Farmer's Cutting (RU, OTBWG, TF, BetterNether), Spice of Life Carrot, Autochef's Delight, Barbeque's Delight. Delightful still has no 1.21.1 NF file. |
| Applied Energistics 2 | `appliedenergistics2-19.2.17.jar` | both | ME network. World data. GuideME, ExtendedAE, AdvancedAE, AE Additions, AE2 Things (beta), MEGA Things, WTLib, Applied Mekanistics, AEInfinityBooster, Crafting Tree, Schematic Energistics, Not Enough Patterns, AE2 Utility, Universal Press, Pattern Converter, Infinity Drives, Ars Énergistique (beta). |
| Refined Storage | `refinedstorage-neoforge-2.0.9.jar` | both | RS 2. World data. Quartz Arsenal, Cable Tiers, Extra Disks (beta), ExtraStorage, Interdimensional Wireless Transmitter. |
| Mekanism | `Mekanism-1.21.1-10.7.19.85.jar` | both | Machines. World data. Generators, Tools, More Machine, Extras, Elements (Patchouli), RS/Aeronautics/Soph backpacks compat. Covers dropped (Sodium 0.8.13 mixin crash). |
| Ars Nouveau | `ars_nouveau-1.21.1-5.13.1.jar` | both | Spellcrafting. World data. Additions, Creo, Elemental, Elemancy, Controle, Technica, Flavors & Delight, Énergistique. Refresh is a forced client texture pack. |
| Spectrum | `spectrum-1.12.7-1.21.1-neo.jar` | both | Progression magic. World data. Revelationary + Modonomicon. |
| Alchemistry | `alchemistry-1.21.1-2.4.5.jar` | both | Chemistry. World data. AlchemyLib + ChemLib. |
| [UNOFFICIAL] TaCZ NeoForge Port | `tacz-neoforge-1.21.1-1.1.8-hotfix-r6.jar` | both | Guns. World data. Unofficial 1.21.1 port + Pack Upgrader. Not compatible with 1.20.1 TaCZ worlds. Addons: addon, Tactical Breaching, Curios/Applied ammo boxes, Elite X, Turrets, Aeronautics/Create compat, Bandits, armed pillagers/skeletons/piglins, Applied TaCZ, Refit, Runtime Compat, LesRaisins. Gun packs in `pack/tacz/` (instance `tacz/`, both sides, upgraded on boot): MCS2 (1113043), Daffa's Arsenal 3.7.1.1 (1254350), and CS+ 1.3.1 (1623678). Those three are 1.20.1 packs, so they stay out of `mods/`. Warzone 1.1.8B is dropped: models and textures are only in `recursion/taczpack.dat`, which this port does not unpack. The MCS2Gun-addon jar (1285238) is not shipped: it is a 1.20.1 Forge mod with an encrypted inner zip, and Pack Upgrader quarantines it without registering the guns. Client: JET, EMF Compat, Punchy, Don't Punch My TACZ (NeoForge pin). Immersive Ballistic + Tweaks dropped (Iris vertex-format conflict). |
| Vic's Point Blank | `pointblank-neoforge-1.21-2.2.0.jar` | both | Second gun system beside TaCZ. World data. GeckoLib 4.9.2+ (pack has 4.9.3). NeoForge range `[21.0,21.3)`. Content packs in `pack/pointblank/` (instance `pointblank/`, both sides): Extended Edition, Gun Gale, Half-Life v0.8, Cyberpunk 2077 1.19. No Vic's Point Blank Interaction (passthrough while holding a gun). Aeronautics bullet collision is both. No Point Blank: Recipe. No Jelly (that fork replaces this mod). No Epic Fight bridge. TaCZ's first-person compat forces vanilla mode only while a TaCZ gun is held, so it does not cover these guns. Punchy still hides its arms whenever Epic Fight mode is on, including while a Point Blank gun is out. Aim Point Blank guns with Epic Fight mode off. |
| Epic Fight | `epic-fight-21.17.3.1-mc1.21.1-neoforge.jar` | both | Souls-like combat. World data. ParCool bridge, Twilight Forest / TaCZ first-person / Curios / Ice and Fire armor compat, Bosses' Rise, Progressive Difficulty, CompatLink, client tweaks, FPS optimizer, Punchy battle-mode hide. playerAnimator required. AAA Particles stays (Effekseer). Do not re-add Nightfall (dedicated-server VFX config crash). |
| ParCool! | `ParCool-1.21.1-4.0.0.5.jar` | both | Parkour movement. Compatibility++ addon in. |
| IceAndFire Community Edition | `iceandfire-2.1.3.jar` | both | Dragons. World data. Jupiter + Uranus. Not original Ice and Fire `264231` (1.20.1-only). Pixie villages and fire dragon roosts/caves generate in the Nether. Worldgen dragon skeletons are off; a killed dragon still leaves a corpse. |
| Alex's Caves Continued | `alexscaves-1.1.1-neoforge+1.21.1.jar` | both | Cave biomes and mobs. World data. Codxlib. Cooking recipes via Alex's Caves Continued Delight. Spellbooks addon uses this port; do not add the unofficial Alex's Caves jar or Citadel. |
| Alex's Mobs Continued | `alexsmobs-2.2.2-neoforge+1.21.1.jar` | both | Mobs. World data. Codxlib. Tweaks and Farmer's Delight recipes are in. Project 1635121. |
| Quark | `Quark-4.1-485.jar` | both | Small vanilla tweaks. World data. Zeta. Biolith is embedded. |
| Iron's Spells 'n Spellbooks | `irons_spellbooks-1.21.1-3.16.3.jar` | both | Spellbooks beside Ars Nouveau. World data. Iron's Lib. Addons: Twilight Forest, Create, Aeronautics teleports, Farmer's Delight, Alex's Caves, Epic Fight animations, Apotheosis gear. Ace's Spell Utils and AzureLib (Twilight spellbooks loads AzureLib even though its metadata does not list it). |
| Apotheosis | `Apotheosis-1.21.1-8.8.0.jar` | both | Affixes and gems. World data. Apothic Attributes, Enchanting, and Spawners. Compat for Iron's Spells, Point Blank, TaCZ, and Create. Fallen Gems. Flight potions and charms are off. Balance numbers are in the configurator. Tooltip Cleanup is client-only and does not replace Tooltip Overhaul. |
| Illager Arena, Qliphoth Awakening, Bosses of Mass Destruction, Spawn, Critters and Companions, Companions, Armageddon, Born in Chaos, Mutant Monsters, Illager Invasion, Mowzie's Mobs, Myths & Legends, Legendary Monsters | see manifest | both | Extra mobs and bosses. World data. Integrated BOMD and Integrated Mowzie's Mobs need Quark. Integrated Patches fixes Integrated API worldgen. Born in Chaos has a config mod and a Jade ore label. Armageddon tooltips label tool tiers. |
| Unusual End, BetterEnd: New Dawn, Forbidden and Arcanus, Pam's HarvestCraft 2, Dungeon Now Loading | see manifest | both | End expansion (Nullscape + Unusual End + BetterEnd New Dawn), magic content, a second kitchen beside Farmer's Delight, and an unofficial dungeon port. World data. Farmer's Cutting covers BetterEnd. |
| Ecliptic Seasons | `EclipticSeasons-1.21.1-neoforge-0.15.0-rc-3-1.jar` | both | 24 solar-term seasons, weather, snow, and crops. World data. Bundles + MultiMod Patch + Serene Seasons API stub. Do not add Serene Seasons. |
| Glassential Renewed | `Glassential-renewed-1.21.1-3.4.7.jar` | both | Extra glass. World data. Fusion is already in. FastPipes and Lampicus were not added. |
| Iron's Gems 'n Jewelry | `irons_jewelry-1.21.1-2.0.2.jar` | both | Wearable gems. World data. Curios, Iron's Lib, Atlas API. Apotheosis gems stay. |
| Not Enough Glyphs | `not_enough_glyphs-1.21.1-4.6.2.jar` | both | Extra Ars glyphs. World data. SauceLib is embedded. |
| Neo Vitae | `neovitae-1.21.1-1.1.27.jar` | both | Blood altars, sigils, and a demon dungeon. World data. GeckoLib and Modonomicon. |
| Just Dire Things | `justdirethings-1.5.7.jar` | both | Automation tools and blocks beside Create and Mekanism. World data. 1.5.7 is the 1.21.1 file. |
| Modern Industrialization | `Modern-Industrialization-2.5.8.jar` | both | Separate factory tech tree. World data. GuideME. GrandPower is embedded. Router energy upgrades are in. |
| Modular Routers | `modular-routers-13.2.7+mc1.21.1.jar` | both | Programmable routers beside Modern Dynamics / XNet. World data. Mekanistic Routers adds Mekanism modules. |
| Little Big Redstone | `little-big-redstone-1.9.11-1.21.1.jar` | both | Compact redstone. World data. Tesseract API and GuideME. |
| Mining Gadgets | `mininggadgets-1.18.8.jar` | both | Laser mining. World data. Create Ultimine and FTB Ultimine stay. |
| ME Requester | `merequester-neoforge-1.21.1-1.5.0.jar` | both | AE2 stock requests. World data. |
| Mekanism Curios | `mekanismcurios-1.21.1-1.2.1.jar` | both | Portable QIO on a Curios slot. |
| Multi Builder Tool | `MultiBuilderTool-1.21.1-1.1.29.jar` | both | One-click multiblocks. |
| Loot Integrations: When Dungeons Arise | `lootintegration_wda-1.8.jar` | both | Modded loot in When Dungeons Arise chests. |
| OpenBlocks Elevator | `elevatorid-neoforge-1.21.1-1.11.4.jar` | both | Elevator blocks. World data. |

Create performance companions (Colorwheel, Create Better FPS, Threaded Trains) and FTB Quests Optimizer: [performance.md](performance.md). Modern Dynamics / XNet and Sophisticated/Functional storage: [storage.md](storage.md).

## Considered / held / dropped

| Mod | Status | Why |
|---|---|---|
| Call of Duty Warzone gun pack | Dropped | CurseForge 1196617 file 8811574 (1.1.8B) stores models and textures in encrypted `recursion/taczpack.dat`. The 1.21.1 TaCZ port does not read that archive, so guns and the buy station render as missing textures. Do not re-add until an unencrypted 1.21 pack exists. |
| TaCZ x Guns Lights Addon | Dropped | Removed on request. Do not re-add. 2.9.0 is still 1.20.x; the pack had pinned 2.8.2. |
| TaCZ: Blueprints Reforged | Dropped | Removed on request. Blueprint items already in a world will be missing. Do not re-add. |
| Point Blank: Recipe | Held | User declined. CurseForge 1016608 has no 1.21.1 NeoForge file. The weapon printer plus JEI stays the crafting path. |
| Pointblank: Jelly | Dropped | Fork that replaces Vic's Point Blank. Official 2.2.0 is newer. Do not install both. |
| Continuity | Held | `continuity-3.0.0+1.21.neoforge.jar` needs Sinytra Connector and Forgified Fabric API, and it targets Sodium 0.6. Fusion is the connected-texture mod. Do not re-add those libraries. |
| Slice & Dice and remaining Create kitchen addons | Deferred | Farmer's Delight, Autochef, Barbeque, Create Deco, Encased, Crafts & Additions, Central Kitchen, Applied Kinetics, and Integrated Farming are in. |
| Alex's Caves / Create compat | Held | Parent is now Alex's Caves Continued; Create compat still needs its own 1.21.1 NF file. |
| AdventureZ | Held | Project 390991's 1.21.1 file is Fabric only. |
| ANARCHY Minibosses | Held | Requires Spell Engine, Spell Power, AzureLib, and Accessories beside Curios. |
| Myths of the Sea | Held | Requires GeckoLib 4.7.4. The pack is on 4.9.3. |
| Somake Spells | Held | Apothic Attributes is in. Still requires Cataclysm. |
| Weapons of Legendary Monsters | Held | Forge 1.20.1 only. |
| Eternal Hunts | Held | Requires Cataclysm, which is not in the pack. |
| Apothic Nerf | Held | Rewrites the same affixes as Apotheosis Balance Configurator. |
| Alex's Caves unofficial port, Citadel unofficial port | Dropped | Spellbooks listed them as CurseForge relations. Continued is the caves mod. Do not re-add Citadel. |
| Vanillin | Dropped | Shader-incompatible with Iris. |
| Serene Seasons | Dropped | Ecliptic Seasons plus the Serene Seasons API stub covers this. Do not stack. |
| Mekanism Covers | Dropped | Beta Sodium mixin fails on join with Sodium 0.8.13; no newer 1.21.1 build. |
| Farmer's Delight Cutting Compat | Dropped | Kept the Farmer's Cutting mods. The datapack is pack format 15 with `recipes/` (1.20.1 layout), so it does not load on 1.21.1, and it only adds flower dyes. The mods strip logs and cover doors, signs, and bark (OTBWG 165, Regions Unexplored 195, Twilight Forest 50, BetterNether 51, BetterEnd Cutting separate). BetterNether is not in the datapack at all. |
| Supplementaries Compat | Dropped | Datapack pack format 15. 1.21.1 datapacks need format 48, so Moonlight jar data in that zip never loads. |
