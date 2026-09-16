# Storage — considered, chosen, dropped

Research snapshot: 2026-09-15. Target is whatever Minecraft + Forge are in [`pack/pack.toml`](../../pack/pack.toml). Re-check store pages before a file bump.

**Status:** this cut **installed** (2026-09-15). Kitchen-sink expansion **installed** (2026-09-16): AE2 kits stacked on request; Refined Storage is a second network. Drawers, upgradeable chests, and backpacks are three jobs, not one. Create integrations ship because Create is already in. packwiz `side` is `both` for all of these.

## Side (packwiz)

| `side` | Meaning |
|---|---|
| `both` | Must run in singleplayer’s integrated server **and** on the dedicated server. |

## Decision rules

1. One drawer mod. Functional Storage, not Storage Drawers, and not both.
2. One upgradeable chest/barrel line. Sophisticated Storage, not Iron Chests.
3. One backpack mod. Sophisticated Backpacks. Curios for the back slot so it does not eat the chestplate.
4. AE2 is the primary storage *network*. Refined Storage is also in (explicit dual-network request). Do not add Tom’s Simple Storage as a third network.
5. Create is already in. Ship the official Sophisticated Create integration jars so chests/backpacks on contraptions do not dupe.

---

## Chosen

| Mod | Project | `side` | Why add |
|---|---|---|---|
| Functional Storage | [modrinth.com/mod/functional-storage](https://modrinth.com/mod/functional-storage) `1.20.1-1.2.14` (`XJ0p2eID`) | both | Same-item drawers (compacting, void, linking) |
| Titanium | [modrinth.com/mod/titanium](https://modrinth.com/mod/titanium) `1.20.1-3.8.35` (`LMqbm4db`) | both | Required by Functional Storage |
| Sophisticated Core | [modrinth.com/mod/sophisticated-core](https://modrinth.com/mod/sophisticated-core) `1.20.1-1.5.1.2335` (`1Xl7lP0L`) | both | Library for Sophisticated Storage / Backpacks |
| Sophisticated Storage | [modrinth.com/mod/sophisticated-storage](https://modrinth.com/mod/sophisticated-storage) `1.20.1-1.4.86.2131` (`JCxeJIsN`) | both | Upgradeable chests, barrels, shulkers |
| Sophisticated Backpacks | [modrinth.com/mod/sophisticated-backpacks](https://modrinth.com/mod/sophisticated-backpacks) `1.20.1-3.26.3.2157` (`XxOZuQnU`) | both | Wearable / placeable backpacks |
| Curios API | [modrinth.com/mod/curios](https://modrinth.com/mod/curios) `5.14.1+1.20.1` (`IPQlZkz1`) | both | Back slot so a backpack does not occupy chest armor |
| Sophisticated Storage Create Integration | [modrinth.com/mod/sophisticated-storage-create-integration](https://modrinth.com/mod/sophisticated-storage-create-integration) `1.20.1-0.1.24.221` (`o8dwHKKj`) | both | Stops contraption dupes; Create is already in |
| Sophisticated Backpacks Create Integration | [modrinth.com/mod/sophisticated-backpacks-create-integration](https://modrinth.com/mod/sophisticated-backpacks-create-integration) `1.20.1-0.1.10.167` (`gzpoJdRt`) | both | Same for backpacks on contraptions |
| Applied Energistics 2 | [modrinth.com/mod/ae2](https://modrinth.com/mod/ae2) `15.4.10` (`7KVs6HMQ`) | both | Item/fluid network. Native EMI in this file. See [content.md](content.md) |
| GuideME | [modrinth.com/mod/guideme](https://modrinth.com/mod/guideme) `20.1.15` (`i7Tp1AHw`) | both | Required by AE2 15.4 |
| Applied Energistics 2 Wireless Terminals | [modrinth.com/mod/applied-energistics-2-wireless-terminals](https://modrinth.com/mod/applied-energistics-2-wireless-terminals) `15.3.3` (`z8QXeyI0`) | both | Wireless crafting/pattern terminals |
| Glodium | [modrinth.com/mod/glodium](https://modrinth.com/mod/glodium) `1.20-1.5` (`eoUaDkZf`) | both | Library for Extended AE and Applied Flux |
| Extended AE | [modrinth.com/mod/extended-ae](https://modrinth.com/mod/extended-ae) `1.4.18` (`uq3lO4ER`) | both | Extra AE2 machines. Stacked with AdvancedAE + Applied Flux on purpose. |
| AdvancedAE | [modrinth.com/mod/advancedae](https://modrinth.com/mod/advancedae) `1.3.6` (`d83Wdhdn`) | both | Extra AE2 machines. GeckoLib already in. |
| Applied Flux | [modrinth.com/mod/appflux](https://modrinth.com/mod/appflux) `1.3.7` (`cAcdjzEn`) | both | FE on the AE network. |
| MEGA Cells | [modrinth.com/mod/mega](https://modrinth.com/mod/mega) `2.4.6` (`SH2D1n3s`) | both | 1M–256M cells. Cloth Config already in. |
| AE Additions | [modrinth.com/mod/ae-additions](https://modrinth.com/mod/ae-additions) `5.1.1` (`BlkC64Gz`) | both | ExtraCells2 fork. Overlaps MEGA; both requested. |
| Better P2P | [modrinth.com/mod/betterp2p](https://modrinth.com/mod/betterp2p) `1.5.0` (`9fICjMvt`) | both | P2P GUI. Architectury + Kotlin already in. |
| AE2 Import Export Card | [modrinth.com/mod/ae2-import-export-card](https://modrinth.com/mod/ae2-import-export-card) `1.3.0` (`v8c3El4q`) | both | Jul 2024 file vs AE2 15.4.10. |
| AE2 Things [Forge] | CurseForge `ae2-things-forge` file `4616683` (`1.2.1`) | both | DISK cells. Last 1.20.1 file Jun 2023 vs AE2 15.4.10 — watch boot. |
| Applied Mekanistics | [modrinth.com/mod/applied-mekanistics](https://modrinth.com/mod/applied-mekanistics) `1.4.3` (`9n9p68Qq`) | both | AE2 chemicals. Mekanism is in. |
| Refined Storage | [modrinth.com/mod/refined-storage](https://modrinth.com/mod/refined-storage) `1.12.4` (`ZITLFjjf`) | both | Second item network. Last 1.20.1 Forge file Nov 2023. |
| Extra Disks | [modrinth.com/mod/extra-disks](https://modrinth.com/mod/extra-disks) `3.0.3` (`bBzUlSat`) | both | Bigger RS disks. |
| ExtraStorage | [modrinth.com/mod/extrastorage](https://modrinth.com/mod/extrastorage) `4.0.7` (`LSn2z31g`) | both | Needs EdivadLib. |
| Cable Tiers | [modrinth.com/mod/cable-tiers](https://modrinth.com/mod/cable-tiers) `1.2.2` (`i99hKWi2`) | both | Faster RS cables. |
| Refined Storage Addons | [modrinth.com/mod/refined-storage-addons](https://modrinth.com/mod/refined-storage-addons) `0.10.0` (`tdH61AWD`) | both | Wireless crafting grid. Archived; last file Jul 2023. |
| Refined Polymorphism | [modrinth.com/mod/refined-polymorphism](https://modrinth.com/mod/refined-polymorphism) `0.1.1` (`XSjAWIAk`) | both | Polymorph in RS GUIs. Polymorph stays 0.49.10. |
| Polymorphic Energistics | [modrinth.com/mod/polymorphic-energistics](https://modrinth.com/mod/polymorphic-energistics) `0.1.1` (`tCb9SvuL`) | both | Polymorph in AE2 terminals. Apr 2024 vs AE2 15.4.10. |
| AEInfinityBooster | CurseForge file `6482257` (`1.20.1-1.0.0+51`) | both | Infinite/dimension wireless cards. File lists AE2 15.4.10. |

## Dropped / skipped this cut

| Asked as | Outcome |
|---|---|
| Storage Drawers | **Skipped.** Functional Storage is the drawer line. |
| Iron Chests | **Skipped.** Sophisticated Storage is the chest-upgrade line. |
| Tom’s Simple Storage | **Skipped.** Would be a third item network next to AE2 and RS. |
| Refined Storage – Mekanism Integration | **Skipped.** Official project is 1.21.1 NeoForge only. Applied Mekanistics covers AE2 chemicals. |
| JEI (optional on Sophisticated pages) | **Skipped.** EMI is the recipe viewer. |

## Held

None for this cut. Extended AE, AdvancedAE, and Applied Flux are stacked on purpose (2026-09-16 request).

## Incompatibility (this set)

Do not combine Functional Storage with Storage Drawers. Do not add a second backpack mod. Do not omit the Create integration jars while Create is installed — moving Sophisticated Storage on a contraption has a documented item dupe without them.

JEI stays out. Sophisticated lists it as optional; EMI covers recipes.

## Configs worth documenting

| Mod | Why a pack note |
|---|---|
| Sophisticated Backpacks | Open defaults to **B**. Unbind in Controls if that fights something later. Cannot pack `options.txt`. |
| Functional Storage / Sophisticated Storage | Defaults. World data: drawers and chests stay in the save if the mod is removed. |
