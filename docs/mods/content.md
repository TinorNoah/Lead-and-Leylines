# Content — considered, chosen, dropped

Target is whatever Minecraft + NeoForge are in [`pack/pack.toml`](../../pack/pack.toml). Re-check store pages before a file bump.

**Status:** Create + Aeronautics, FTB extras, Twilight Forest, Lost Cities, Aquamirae, Supplementaries, AE2, RS, Mekanism, Ars, Farmer's Delight, Spectrum, TaCZ guns, Epic Fight + ParCool, Ice and Fire CE. Remaining Create kitchen addons: [deferred.md](deferred.md).

## Chosen

| Mod | Pinned file | `side` | Why |
|---|---|---|---|
| Create | `create-1.21.1-6.0.10.jar` | both | Contraptions and kinetics. Flywheel is embedded. World data. |
| Sable | `sable-neoforge-1.21.1-2.0.5.jar` | both | Physics sub-levels for Aeronautics. Mixin-heavy; author warns about other mods. |
| Create Aeronautics | `create-aeronautics-bundled-1.21.1-1.3.2.jar` | both | Planes, airships, cars. World data. Known visual issues with Iris. |
| Architectury API | `architectury-13.0.11-neoforge.jar` | both | Required by FTB. |
| FTB Library | `ftb-library-neoforge-2101.1.36.jar` | both | Required by FTB Quests / Teams. ARR. |
| FTB Teams | `ftb-teams-neoforge-2101.1.11.jar` | both | Shared quest progress. ARR. |
| FTB Quests | `ftb-quests-neoforge-2101.1.36.jar` | both | Quest book. World data. ARR. |
| The Twilight Forest | `twilightforest-1.21.1-4.8.3345-universal.jar` | both | Dimension. World data. Thread-safety addon still 1.20.1-only. |
| The Lost Cities | `lostcities-1.21-8.4.4.jar` | both | City generation. World data. LC²H 4.2.3-LTS is in for multithreaded gen. |
| Aquamirae | `aquamirae-neoforge-1.21.1-7.2.10.jar` | both | Ocean structures, boss, and items. World data. Requires GeckoLib and Fragmentum. Modrinth pin. |
| Supplementaries | `supplementaries-1.21.1-3.9.9-neoforge.jar` | both | Decor and utility blocks. World data. Moonlight. |
| Amendments | `amendments-1.21-2.1.10-neoforge.jar` | both | Vanilla block tweaks. World data. Moonlight. |
| Create Ultimine | `createultimine-1.21.1-neoforge-1.3.2.jar` | both | Create-aware vein mine with FTB Ultimine. |
| Create: Sky Village | `create_sky_village-0.0.38 NeoForge 1.21.1.jar` | both | Create village structure. World data. |
| FTB Chunks | `ftb-chunks-neoforge-2101.1.22.jar` | both | Chunk claims. World data. ARR. |
| FTB Essentials | `ftb-essentials-neoforge-2101.1.10.jar` | both | `/home` and related commands. ARR. |
| FTB Ultimine | `ftb-ultimine-neoforge-2101.1.15.jar` | both | Vein mine. ARR. |
| Farmer's Delight | `FarmersDelight-1.21.1-1.3.4.jar` | both | Kitchen. World data. Corn Delight, My Nether's Delight, Twilight's Flavors, Farmer's Cutting (RU, OTBWG, TF, BetterNether), Spice of Life Carrot. Delightful still has no 1.21.1 NF file. |
| Applied Energistics 2 | `appliedenergistics2-19.2.17.jar` | both | ME network. World data. GuideME, ExtendedAE, AdvancedAE, AE Additions, AE2 Things (beta), WTLib, Applied Mekanistics, Ars Énergistique (beta). |
| Refined Storage | `refinedstorage-neoforge-2.0.9.jar` | both | RS 2. World data. Quartz Arsenal, Cable Tiers, Extra Disks (beta), ExtraStorage. |
| Mekanism | `Mekanism-1.21.1-10.7.19.85.jar` | both | Machines. World data. Generators, Tools, More Machine, Extras, Elements (Patchouli), RS/Aeronautics/Soph backpacks compat. Covers dropped (Sodium 0.8.13 mixin crash). |
| Ars Nouveau | `ars_nouveau-1.21.1-5.13.1.jar` | both | Spellcrafting. World data. Additions, Creo, Elemental, Énergistique. |
| Spectrum | `spectrum-1.12.7-1.21.1-neo.jar` | both | Progression magic. World data. Revelationary + Modonomicon. |
| Alchemistry | `alchemistry-1.21.1-2.4.5.jar` | both | Chemistry. World data. AlchemyLib + ChemLib. |
| [UNOFFICIAL] TaCZ NeoForge Port | `tacz-neoforge-1.21.1-1.1.8-hotfix-r6.jar` | both | Guns. World data. Unofficial 1.21.1 port + Pack Upgrader. Not compatible with 1.20.1 TaCZ worlds. Addons: addon, Tactical Breaching, Guns Lights 2.8.2, Curios/Applied ammo boxes, Elite X, Turrets, Aeronautics/Create compat, Bandits, armed pillagers/skeletons/piglins, Applied TaCZ, Refit, Runtime Compat, Blueprints, LesRaisins. Client: JET, EMF Compat, Punchy, Don't Punch My TACZ (NeoForge pin). Immersive Ballistic + Tweaks dropped (Iris vertex-format conflict). |
| Epic Fight | `epic-fight-21.17.3.1-mc1.21.1-neoforge.jar` | both | Souls-like combat. World data. ParCool bridge, Twilight Forest / TaCZ first-person / Curios / Ice and Fire armor compat, Bosses' Rise, Progressive Difficulty, CompatLink, client tweaks, FPS optimizer. playerAnimator required. AAA Particles stays (Effekseer). Do not re-add Nightfall (dedicated-server VFX config crash). |
| ParCool! | `ParCool-1.21.1-4.0.0.5.jar` | both | Parkour movement. Compatibility++ addon in. |
| IceAndFire Community Edition | `iceandfire-2.1.3.jar` | both | Dragons. World data. Jupiter + Uranus. Not original Ice and Fire `264231` (1.20.1-only). Pixie villages generate in the Nether (`lead-leylines-nether-pixies`). |
| Alex's Caves Continued | `alexscaves-1.1.1-neoforge+1.21.1.jar` | both | Cave biomes and mobs. World data. Codxlib. |
| Ecliptic Seasons | `EclipticSeasons-1.21.1-neoforge-0.15.0-rc-3-1.jar` | both | 24 solar-term seasons, weather, snow, and crops. World data. Bundles + MultiMod Patch + Serene Seasons API stub. Do not add Serene Seasons. |

Create performance companions (Colorwheel, Create Better FPS, Threaded Trains) and FTB Quests Optimizer: [performance.md](performance.md). Pipez and Sophisticated/Functional storage: [storage.md](storage.md).

## Considered / held / dropped

| Mod | Status | Why |
|---|---|---|
| Slice & Dice, Central Kitchen, Applied Kinetics, remaining Create addons | Deferred | Farmer's Delight is in; kitchen Create addons still a later wave. |
| Alex's Caves / Create compat | Held | Parent is now Alex's Caves Continued; Create compat still needs its own 1.21.1 NF file. |
| Vanillin | Dropped | Shader-incompatible with Iris. |
| Serene Seasons | Dropped | Ecliptic Seasons plus the Serene Seasons API stub covers this. Do not stack. |
| Mekanism Covers | Dropped | Beta Sodium mixin fails on join with Sodium 0.8.13; no newer 1.21.1 build. |
