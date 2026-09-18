# Content — considered, chosen, dropped

Target is whatever Minecraft + NeoForge are in [`pack/pack.toml`](../../pack/pack.toml). Re-check store pages before a file bump.

**Status:** Create, FTB Quests, Twilight Forest, Lost Cities, Aquamirae. Remaining Create addons and the rest of the 1.20.1 list: [deferred.md](deferred.md).

## Chosen

| Mod | Pinned file | `side` | Why |
|---|---|---|---|
| Create | `create-1.21.1-6.0.10.jar` | both | Contraptions and kinetics. Flywheel is embedded. World data. |
| Architectury API | `architectury-13.0.11-neoforge.jar` | both | Required by FTB. |
| FTB Library | `ftb-library-neoforge-2101.1.36.jar` | both | Required by FTB Quests / Teams. ARR. |
| FTB Teams | `ftb-teams-neoforge-2101.1.11.jar` | both | Shared quest progress. ARR. |
| FTB Quests | `ftb-quests-neoforge-2101.1.36.jar` | both | Quest book. World data. ARR. |
| The Twilight Forest | `twilightforest-1.21.1-4.8.3345-universal.jar` | both | Dimension. World data. Thread-safety addon still 1.20.1-only. |
| The Lost Cities | `lostcities-1.21-8.4.4.jar` | both | City generation. World data. LC²H still 1.20.1 Forge-only. |
| Aquamirae | `aquamirae-neoforge-1.21.1-7.2.7.jar` | both | Ocean structures, boss, and items. World data. Requires GeckoLib and Fragmentum. Modrinth pin. |

Create performance companions (Iris Flywheel Compat, Create Better FPS, Threaded Trains) and FTB Quests Optimizer: [performance.md](performance.md). Pipez: [storage.md](storage.md).

## Considered / held / dropped

| Mod | Status | Why |
|---|---|---|
| Create Ultimine, Slice & Dice, Central Kitchen, Applied Kinetics, remaining Create addons | Deferred | Parent Create is in; research each addon before adding. |
| FTB Chunks / Essentials / Ultimine | Deferred | Parent FTB Library/Teams are in; not requested this wave. |
| Vanillin | Dropped | Shader-incompatible with Iris. |
