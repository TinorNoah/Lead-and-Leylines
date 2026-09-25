# Storage — considered, chosen, dropped

Target is whatever Minecraft + NeoForge are in [`pack/pack.toml`](../../pack/pack.toml). Re-check store pages before a file bump.

**Status:** Pipez, Sophisticated/Functional storage, AE2, Refined Storage (Quartz Arsenal, Cable Tiers), Mekanism chemical RS, Demagnetizer.

## Side (packwiz)

| `side` | Meaning |
|---|---|
| `client` | Prism / player instance only. |
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
| Create: Sophisticated Backpacks Compat | `create_sophback_compat-1.0.jar` | both | Extra Create recipes for backpacks. Complements the contraption integration. |
| Sophisticated Backpacks: Ars Compat | `arssophisticatedcompat-0.3.0.jar` | both | Ars items in backpacks. |
| Sophisticated Storage: Ars Compat | `arssophisticatedstoragecompat-0.3.0.jar` | both | Ars items in Sophisticated storage. |
| Sophisticated Tactical Backpacks | `militarybackpack-2.0.0-beta.jar` | both | Tactical backpacks and ammo reload. Beta. World data. |
| Mekanism + Sophisticated Backpacks Compat | `mekanismsophisticatedbackpacks-neoforge-1.21.1-1.0.1+mc1.21.1-neoforge.jar` | both | Chemical tanks in backpacks. |
| Sophisticated Item Actions | `sophisticateditemactions-1.21.1-0.5.16.423.jar` | both | Pinned 1.21.1; later files are 1.21.11. |
| Yukami's Sophisticated Backpack Tab | `yukamibackpacktab-1.21.1-2.2.0-neoforge.jar` | client | Inventory backpack tab. |
| Sophisticated Inventory Interactions | `sophisticatedinventoryinteractions-1.21.1-0.1.13.218.jar` | both | Inventory transfer helpers. |
| Sophisticated Chest Optimized | `sophisticated_chest_optimized-1.0.1.jar` | client | Pinned NeoForge 1.0.1; later files are Fabric. |
| Sophisticated Backpacks / Jade | `jade-sophisticated-backpacks-1.21.1-neoforge-1.0.2.jar` | client | Backpack contents on Jade. |
| Sophisticated Backpacks RS Bridge | `backpackrs-1.0.0+mc1.21.1-neoforge.jar` | both | Quick deposit into RS. |
| Demagnetizer | `demagnetizer-neoforge-0.1.0-beta.1.jar` | both | Stops item magnet in a radius. Beta. Pinned NeoForge. |
| Refined Storage - Mekanism Integration | `refinedstorage-mekanism-integration-1.1.1.jar` | both | RS chemicals. |
| Functional Storage | `functionalstorage-1.21.1-1.5.8.jar` | both | Drawers. World data. Titanium. |
| Botany Pots | `botanypots-neoforge-1.21.1-21.1.44.jar` | both | Crop pots. World data. Bookshelf + Prickle. |
| Botany Trees | `botanytrees-neoforge-1.21.1-21.1.7.jar` | both | Tree pots. World data. |
| Trash Cans | `trashcans-1.1.0-neoforge-mc1.21.jar` | both | Trash blocks. World data. SuperMartijn642 Core + Config. |
| Packing Tape | `PackingTape-1.21.1-0.15.6.jar` | both | Pickup tile entities. |
| Applied Energistics 2 | `appliedenergistics2-19.2.17.jar` | both | ME network. World data. |
| AE2: Crafting Tree | `ae2ct-1.21.1-1.1.1.jar` | both | Craft tree in the terminal. |
| Schematic Energistics | `schematicenergistics-1.21.1-1.5.4a.jar` | both | Schematicannon uses the ME network. World data. |
| AE2 MEGA Things | `AE2MEGAThings-1.21.1-2.0.4.jar` | both | Untyped disks for items, fluids, and chemicals. World data. |
| Not Enough Patterns | `nep-1.21.1-0.5.1.jar` | both | Pattern providers for other mods' machines. |
| Infinity Drives | `infinitystorage-1.21.1-1.0.1.jar` | both | Infinite water, lava, and cobblestone. World data. |
| AE2 Utility | `ae2utility-1.7.9.jar` | both | Pull from the ME network; one-click patterns. |
| Pattern Converter | `patternconverter-1.0.0.jar` | both | AE2 and Refined Storage pattern conversion. World data. |
| AE2 Universal Press | `ae_universal_press-2.1.1-neoforge-1.21.1.jar` | both | One press for every processor. World data. |
| Refined Storage | `refinedstorage-neoforge-2.0.9.jar` | both | RS 2. World data. |
| Quartz Arsenal | `refinedstorage-quartz-arsenal-neoforge-1.0.8.jar` | both | Wireless crafting grid. Replaces RS Addons. |
| Interdimensional Wireless Transmitter | `interdimensionalwirelesstransmitter-neoforge-1.21.1-0.1.5.jar` | both | RS wireless across dimensions. World data. |
| Cable Tiers | `cabletiers-neoforge-1.21.1-0.6.14.jar` | both | Faster RS importer/exporter tiers. |

## Considered / held / dropped

TaCZ / Sophisticated Backpacks ammo (`tacz-1-21-1` modid) does not load with the unofficial TaCZ port (`tacz`). RS Addons has no 1.21.1 file (Quartz Arsenal instead). Refined Polymorphism and Polymorphic Energistics: [deferred.md](deferred.md).
