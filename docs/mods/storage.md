# Storage — considered, chosen, dropped

Target is whatever Minecraft + NeoForge are in [`pack/pack.toml`](../../pack/pack.toml). Re-check store pages before a file bump.

**Status:** Pipez, Sophisticated/Functional storage, AE2, Refined Storage (Quartz Arsenal, Cable Tiers).

## Side (packwiz)

| `side` | Meaning |
|---|---|
| `both` | Must run in singleplayer’s integrated server **and** on the dedicated server. |

## Chosen

| Mod | Pinned file | `side` | Why |
|---|---|---|---|
| Pipez | `pipez-neoforge-1.21.1-1.2.31.jar` | both | Item/fluid/energy pipes. ARR. World data. |
| Pipez Lag Fix | `pipezlagfix-1.21.1-1.1.0.jar` | both | Eco mode when item-pipe destinations are full. ARR. |
| Sophisticated Core | `sophisticatedcore-1.21.1-1.5.1.2341.jar` | both | Shared lib for backpacks/storage. |
| Sophisticated Backpacks | `sophisticatedbackpacks-1.21.1-3.26.3.2158.jar` | both | Backpacks. World data. |
| Sophisticated Storage | `sophisticatedstorage-1.21.1-1.5.91.2127.jar` | both | Barrels/chests. World data. |
| Sophisticated Backpacks Create Integration | `sophisticatedbackpackscreateintegration-1.21.1-0.2.0.168.jar` | both | Create recipes for backpacks. |
| Sophisticated Storage Create Integration | `sophisticatedstoragecreateintegration-1.21.1-0.1.21.209.jar` | both | Create recipes for storage. |
| Functional Storage | `functionalstorage-1.21.1-1.5.8.jar` | both | Drawers. World data. Titanium. |
| Botany Pots | `botanypots-neoforge-1.21.1-21.1.44.jar` | both | Crop pots. World data. Bookshelf + Prickle. |
| Botany Trees | `botanytrees-neoforge-1.21.1-21.1.7.jar` | both | Tree pots. World data. |
| Trash Cans | `trashcans-1.1.0-neoforge-mc1.21.jar` | both | Trash blocks. World data. SuperMartijn642 Core + Config. |
| Packing Tape | `PackingTape-1.21.1-0.15.6.jar` | both | Pickup tile entities. |
| Applied Energistics 2 | `appliedenergistics2-19.2.17.jar` | both | ME network. World data. |
| Refined Storage | `refinedstorage-neoforge-2.0.9.jar` | both | RS 2. World data. |
| Quartz Arsenal | `refinedstorage-quartz-arsenal-neoforge-1.0.8.jar` | both | Wireless crafting grid. Replaces RS Addons. |
| Cable Tiers | `cabletiers-neoforge-1.21.1-0.6.14.jar` | both | Faster RS importer/exporter tiers. |

## Considered / held / dropped

RS Addons has no 1.21.1 file (Quartz Arsenal instead). Refined Polymorphism and Polymorphic Energistics: [deferred.md](deferred.md).
