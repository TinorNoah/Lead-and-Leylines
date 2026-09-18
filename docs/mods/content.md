# Content — considered, chosen, dropped

Target is whatever Minecraft + NeoForge are in [`pack/pack.toml`](../../pack/pack.toml). Re-check store pages before a file bump.

**Status:** Create, FTB extras, Twilight Forest, Lost Cities, Aquamirae, Supplementaries, AE2, RS, Mekanism, Ars, Farmer's Delight, Spectrum. Remaining Create kitchen addons: [deferred.md](deferred.md).

## Chosen

| Mod | Pinned file | `side` | Why |
|---|---|---|---|
| Create | `create-1.21.1-6.0.10.jar` | both | Contraptions and kinetics. Flywheel is embedded. World data. |
| Architectury API | `architectury-13.0.11-neoforge.jar` | both | Required by FTB. |
| FTB Library | `ftb-library-neoforge-2101.1.36.jar` | both | Required by FTB Quests / Teams. ARR. |
| FTB Teams | `ftb-teams-neoforge-2101.1.11.jar` | both | Shared quest progress. ARR. |
| FTB Quests | `ftb-quests-neoforge-2101.1.36.jar` | both | Quest book. World data. ARR. |
| The Twilight Forest | `twilightforest-1.21.1-4.8.3345-universal.jar` | both | Dimension. World data. Thread-safety addon still 1.20.1-only. |
| The Lost Cities | `lostcities-1.21-8.4.4.jar` | both | City generation. World data. LC²H 4.2.3-LTS is in for multithreaded gen. |
| Aquamirae | `aquamirae-neoforge-1.21.1-7.2.7.jar` | both | Ocean structures, boss, and items. World data. Requires GeckoLib and Fragmentum. Modrinth pin. |
| Supplementaries | `supplementaries-1.21.1-3.9.9-neoforge.jar` | both | Decor and utility blocks. World data. Moonlight. |
| Amendments | `amendments-1.21-2.1.10-neoforge.jar` | both | Vanilla block tweaks. World data. Moonlight. |
| Create Ultimine | `createultimine-1.21.1-neoforge-1.3.2.jar` | both | Create-aware vein mine with FTB Ultimine. |
| Create: Sky Village | `create_sky_village-0.0.38 NeoForge 1.21.1.jar` | both | Create village structure. World data. |
| FTB Chunks | `ftb-chunks-neoforge-2101.1.22.jar` | both | Chunk claims. World data. ARR. |
| FTB Essentials | `ftb-essentials-neoforge-2101.1.10.jar` | both | `/home` and related commands. ARR. |
| FTB Ultimine | `ftb-ultimine-neoforge-2101.1.15.jar` | both | Vein mine. ARR. |
| Farmer's Delight | `FarmersDelight-1.21.1-1.3.4.jar` | both | Kitchen. World data. Corn Delight, My Nether's Delight, Twilight's Flavors, Farmer's Cutting, Spice of Life Carrot. Delightful still has no 1.21.1 NF file. |
| Applied Energistics 2 | `appliedenergistics2-19.2.17.jar` | both | ME network. World data. GuideME, ExtendedAE, AdvancedAE, AE Additions, AE2 Things (beta), WTLib, Applied Mekanistics, Ars Énergistique (beta). |
| Refined Storage | `refinedstorage-neoforge-2.0.9.jar` | both | RS 2. World data. Quartz Arsenal, Cable Tiers, Extra Disks (beta), ExtraStorage. |
| Mekanism | `Mekanism-1.21.1-10.7.19.85.jar` | both | Machines. World data. Generators, Tools, More Machine. |
| Ars Nouveau | `ars_nouveau-1.21.1-5.13.1.jar` | both | Spellcrafting. World data. Additions, Creo, Elemental, Énergistique. |
| Spectrum | `spectrum-1.12.7-1.21.1-neo.jar` | both | Progression magic. World data. Revelationary + Modonomicon. |
| Alchemistry | `alchemistry-1.21.1-2.4.5.jar` | both | Chemistry. World data. AlchemyLib + ChemLib. |

Create performance companions (Iris Flywheel Compat, Create Better FPS, Threaded Trains) and FTB Quests Optimizer: [performance.md](performance.md). Pipez and Sophisticated/Functional storage: [storage.md](storage.md).

## Considered / held / dropped

| Mod | Status | Why |
|---|---|---|
| Slice & Dice, Central Kitchen, Applied Kinetics, remaining Create addons | Deferred | Farmer's Delight is in; kitchen Create addons still a later wave. |
| Alex's Caves / Create compat | Held | No 1.21.1 NeoForge file. |
| Vanillin | Dropped | Shader-incompatible with Iris. |
