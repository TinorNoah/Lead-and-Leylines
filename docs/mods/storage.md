# Storage — considered, chosen, dropped

Research snapshot: 2026-09-15. Target is whatever Minecraft + Forge are in [`pack/pack.toml`](../../pack/pack.toml). Re-check store pages before a file bump.

**Status:** this cut **installed** (2026-09-15). Drawers, upgradeable chests, and backpacks are three jobs, not one. Create integrations ship because Create is already in. packwiz `side` is `both` for all of these.

## Side (packwiz)

| `side` | Meaning |
|---|---|
| `both` | Must run in singleplayer’s integrated server **and** on the dedicated server. |

## Decision rules

1. One drawer mod. Functional Storage, not Storage Drawers, and not both.
2. One upgradeable chest/barrel line. Sophisticated Storage, not Iron Chests.
3. One backpack mod. Sophisticated Backpacks. Curios for the back slot so it does not eat the chestplate.
4. AE2 (when it lands) is the storage *network*. Do not add Tom’s Simple Storage as a second network.
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

## Dropped / skipped this cut

| Asked as | Outcome |
|---|---|
| Storage Drawers | **Skipped.** Functional Storage is the drawer line. |
| Iron Chests | **Skipped.** Sophisticated Storage is the chest-upgrade line. |
| Tom’s Simple Storage | **Skipped.** Would be a second item network next to planned AE2. |
| JEI (optional on Sophisticated pages) | **Skipped.** EMI is the recipe viewer. |

## Held

None for this cut. AE2 wireless / backpack-network bridges wait until AE2 is in.

## Incompatibility (this set)

Do not combine Functional Storage with Storage Drawers. Do not add a second backpack mod. Do not omit the Create integration jars while Create is installed — moving Sophisticated Storage on a contraption has a documented item dupe without them.

JEI stays out. Sophisticated lists it as optional; EMI covers recipes.

## Configs worth documenting

| Mod | Why a pack note |
|---|---|
| Sophisticated Backpacks | Open defaults to **B**. Unbind in Controls if that fights something later. Cannot pack `options.txt`. |
| Functional Storage / Sophisticated Storage | Defaults. World data: drawers and chests stay in the save if the mod is removed. |
