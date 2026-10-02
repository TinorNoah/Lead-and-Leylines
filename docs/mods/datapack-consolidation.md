# Datapack consolidation

Replacing small data-only mods with pack-owned datapacks, so the mods can leave
`pack/mods/`. Nothing here needs new Java: every mod in scope ships only JSON
(plus, in two cases, a dummy class or a single load-time gamerule).

Status: **done and verified 2026-10-03.** Seven mods removed, 567 recipes and
one gamerule ported. Recipe count before and after removal is identical.

Minecraft and loader version: [`pack/pack.toml`](../../pack/pack.toml).

## Why data-only and not code folding

A separate effort considered folding small Java mods into one pack-owned mod.
That was rejected as a bad trade — see [the reasoning](#rejected-alternative).

For data-only mods the trade is different and clearly good: the JAR contributes
nothing but JSON, so the JSON can be committed to the pack as a normal datapack
and the dependency disappears. No new code to maintain.

## Scope

Seven mods. All JARs downloaded from CurseForge and **SHA1-verified against the
packwiz pins** before inspection — no claim below rests on a JAR we did not open.

| Mod | CF project/file | JAR bytes | Classes | Data files | Recipe type |
|---|---|---|---|---|---|
| Farmer's Cutting: BetterNether | 1114065 / 7649818 | 38,654 | **0** | 51 `data/fcbn/recipe` | `farmersdelight:cutting` |
| Farmer's Cutting: Twilight Forest | 1131152 / 5859455 | 39,901 | **0** | 50 `data/fctf/recipe` | `farmersdelight:cutting` |
| Farmer's Cutting: BetterEnd | 1146834 / 7648264 | 51,361 | **0** | 76 `data/fcbe/recipe` | `farmersdelight:cutting` |
| Farmer's Cutting: Oh The Biomes We've Gone | 1094819 / 6274107 | 100,636 | **0** | 165 `data/fcbwg/recipe` | `farmersdelight:cutting` |
| Farmer's Cutting: Regions Unexplored | 1133629 / 7642854 | 113,172 | **0** | 195 `data/fcru/recipe` | `farmersdelight:cutting` |
| Create: Regions Unexplored Compat | 1431845 / 7469182 | 14,704 | 1 (dummy) | 30 `data/create_ru_compat/recipe/crushing` | `create:crushing` |
| DarkSleep — RPG Sleep Percentage | 1106281 / 5741536 | 5,538 | 2 | 1 function + 1 tag | n/a |

**567 recipes + 1 function + 1 tag.** 365,000 bytes of JAR becomes 570 tracked pack
files.

### Verified properties

Checked across all seven JARs, not assumed:

- All five Farmer's Cutting JARs contain **zero `.class` files** and ship a
  `pack.mcmeta` — they were never code mods, they are Modrinth datapacks
  packaged as JARs.
- Every recipe uses one of exactly **two** serializers,
  `farmersdelight:cutting` (537) and `create:crushing` (30). Both are provided
  by mods that **stay** in the pack, so no serializer disappears with the JARs.
- Every data file sits under its own mod's namespace. No cross-namespace
  spill, no self-references.
- All 567 files parse as JSON.
- `create_ru_compat`'s `META-INF/accesstransformer.cfg` is **0 bytes** and its
  single class is an empty-constructor dummy whose only job is making the JAR a
  valid mod container. There is no access transformer and no mixin to lose.
- DarkSleep's entire behaviour is
  `gamerule playersSleepingPercentage 50` in a `#minecraft:load` function.

### Licenses

| Source | License | Note |
|---|---|---|
| Farmer's Cutting ×5 | MIT in each JAR's `neoforge.mods.toml` | Repo `Joshcraft2002/farmers-cutting` has **no LICENSE file**; MIT is declared on Modrinth only. Recipes are machine-generated from `fcgenerator.py`, which is itself evidence they are pure data. |
| Create: Regions Unexplored Compat | MIT in `neoforge.mods.toml` | No repo found; 5,183 total downloads. Treat as effectively unmaintained — the committed datapack is then our only copy, so keep it in git history deliberately. |
| DarkSleep | `All Rights Reserved` | Copying its data would be a license question. It is **not copied**: the behaviour is one vanilla gamerule, reimplemented as our own function in our own namespace. |

## Plan

- [x] Verify the existing datapack layout and `pack_format` (all nine use `48`)
- [x] Download all seven JARs, SHA1-verify against packwiz pins — 7/7 byte-identical
- [x] Full census: class count, data files, recipe types, namespace check
- [x] Extract 567 recipes into `pack/global_packs/required_data/lead-leylines-compat-recipes/`
- [x] Reimplement DarkSleep as a pack-owned `#minecraft:load` function
- [x] Byte-compare extracted JSON against the JARs — **567/567 identical**
- [x] `packwiz refresh` (570 new indexed entries)
- [x] Canary boot **with the mods still installed** — datapack loads and overrides by recipe ID
- [x] Remove the seven `packwiz` entries, `packwiz refresh`
- [x] Verify: `Loaded 47540 recipes` both before and after removal, 0 attributable errors
- [x] Hand-edit `docs/installed/catalog.toml`; `scripts/installed_catalog.py` then `--check` (594 rows, exit 0)
- [x] Update `docs/mods/manifest.md`, `nether.md`, `utility.md`, `content.md`, MAINTENANCE.md
- [x] Add `CHANGELOG.md` `[Unreleased]` bullets
- [ ] **Client check: confirm the cutting recipes appear in JEI.** Not covered by the
      dedicated-server smoke test, which never loads client mods.

## Layout decisions

**One new datapack for all 567 recipes**, `lead-leylines-compat-recipes/`, even
though they come from six mods. They are all the same shape (a recipe, one
vanilla-or-mod serializer, no behaviour), and splitting by origin would produce
six near-identical folders. The origin namespace (`fcbn`, `fctf`, `fcbe`,
`fcbwg`, `fcru`, `create_ru_compat`) is preserved inside each path, so
provenance is still obvious and a future re-sync is per-namespace.

**DarkSleep goes into the existing `lead-leylines-load-fixes/` datapack**, not a
new folder. Its whole mechanism is a `#minecraft:load` function, and
load-fixes already exists to correct things at load time (bastion loot, season
rain tags, spawn categories, Spawn Clams, disabled recipes). The function will
be renamed into a pack-owned namespace rather than keeping `darksleep`.

**No `"replace": true` anywhere.** `#minecraft:load` is additive by default and
no other pack datapack currently declares that tag, but keeping it additive
means any mod-provided load functions still run.

## Rejected alternative: folding Java mods into one owned mod

Considered and declined. Recorded here so it is not re-litigated.

- NeoForge 21.1.x **jar-in-jar does not reduce the number of loaded mods.** A
  bundled mod keeps its own mod ID, its own `config/<modid>-*.toml`, its own
  Mods-screen entry, and its own world-save entry. JiJ is declared in
  `META-INF/jarjar/metadata.json`, and only cuts downloads, never mod count.
- Multi-mod-ID in one JAR *is* possible via repeated `[[mods]]` blocks, but it
  is lossy: one `loaderVersion`, one AT list, one `services` list, the first mod
  ID becomes the JPMS module name, and duplicate config filenames hard-crash
  `ConfigTracker`.
- packwiz `side` is per-file, so a client-only mod cannot be bundled into a
  `both` bundle selectively.
- Of the Java mods surveyed, only `MemGuard` hooked a stable public NeoForge
  API (`ServerTickEvent.Post`). Everything else injects into vanilla internals,
  so folding them means permanently owning per-Minecraft-bump revalidation.
- Licensing was the hard blocker on several popular ones: `ResourcePackCached`
  (GPL-3.0), `GeckolibBetterFPS` and `Almanac Lib` (LGPL),
  `Akashic Tome` (CC-BY-NC-SA, noncommercial), `Cosmetic Armor Reworked` (MMPL,
  which forbids commercial distribution), and `Epic Fight FPS Optimizer` (an
  explicit no-derivatives grant). Epic Fight itself is GPLv3 code with
  All-Rights-Reserved assets and forbids redistributing those assets.

The whole survey would have retired ~35 of 581 jars (6%) and 709 KB — **0.04% of
the 1.66 GB pack**. Not worth a permanent maintenance liability.

## Data-only families that must NOT be datapacked

Checked and rejected, so this is not retried:

- **Loot Integrations + its 8 addons (9 JARs).** The parent has 9 classes,
  including a mixin on `LootTable.getRandomItems`, an access transformer, and a
  private DSL reload listener reading `loot/` (not vanilla `loot_table/`). The
  addons hook **436 host tables across 21 namespaces**. No vanilla datapack can
  express "roll table B and splice its rolled output into table A's return list".
- **`Refined Storage – Curios Integration`** registers a Curios slot type and a
  third-party addon targets it. Curios slot types *are* datapack-driven, but this
  mod's value is the slot itself; it stays. (Also correctly pinned: `2.0.x` is
  Minecraft 26.1.2, not 1.21.1 — see `docs/mods/utility.md`.)
- **`FastWorkbench`** has an undeclared compat mixin inside Polymorph referencing
  `dev.shadowsoffire.fastbench.net.RecipePayload`. Repackaging breaks Polymorph
  silently.
- **`Almanac Lib`** is hard-required by Let Me Despawn; **`Polymorph`** is
  hard-required by Ars Polymorphia.

## Re-sync procedure

These six upstream projects are ports of generated data and are close to
dormant, so a re-sync should be rare. When one is needed:

1. `packwiz` re-add the mod temporarily, or download the JAR from CurseForge.
2. Diff the JAR's `data/` tree against the matching namespace in
   `lead-leylines-compat-recipes/`.
3. Copy changed JSON, run `packwiz refresh`, then `scripts/smoke_test.py`.
4. Update the byte counts in the table above.

Because the upstream repos are quiet, git history in this repo is the only
audit trail for what changed and when. Do not squash the migration commit.