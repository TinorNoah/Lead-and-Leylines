# Datapack consolidation

Replacing small data-only mods with pack-owned datapacks, so the mods can leave
`pack/mods/`. Nothing here needs new Java: every mod in scope ships only JSON
(plus, in two cases, a dummy class or a single load-time gamerule).

Status: **done and verified 2026-10-03.** Seven mods removed, 567 recipes and
one gamerule ported. Recipe count before and after removal is identical.

**Second pass, same day (Tier 0):** two more recipe-only Create mods removed and
143 recipes ported. See [Tier 0](#tier-0-create-recipe-only-mods). A third
candidate was **not** datapackable because it registers items rather than just
data — see
[Not datapackable](#not-datapackable-simply-swords-create-lines).

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
- [ ] **Client check: confirm the 143 Tier 0 Create milling recipes appear in JEI** —
      milling an OTBWG block and a Sophisticated Backpacks upgrade. Still open, and
      the dedicated-server smoke test cannot cover it either.

## Tier 0: Create recipe-only mods

A second pass the same day, prompted by a survey of the whole mod list for
clusters that one pack-owned mod could replace. Two recipe-only Create addons
were the cheapest possible win: **no Java at all**.

| Mod | CF project/file | JAR bytes | Classes | Recipes | Recipe type |
|---|---|---|---|---|---|
| Create: Oh The Biomes We've Gone Compat | 1285600 / 6645097 | 517,455 | **0** | 86 | `create:milling` |
| Create: Sophisticated Backpacks Compat | 1320115 / 6844021 | 679,850 | **0** | 57 | `create:milling` |

**143 recipes + 1,197,305 bytes of JAR becomes 143 tracked pack files.** Both JARs
were SHA1-verified against the packwiz pins before inspection (7/7 byte-identical
across all three Tier 0 candidates), all 143 extracted files byte-compared
identical to the JARs, and every file parses as JSON.

### Why these two and not the third candidate

`simplyswords_create_lines` was the third candidate and looks similar on a class
count (1 class, 104 recipes), but it is **not** a data-only mod — it registers
104 items. See [Not datapackable](#not-datapackable-simply-swords-create-lines).

### Verified properties

- **Zero class files in both JARs.** Every `.json` in each archive sits under
  `data/create/recipe/milling/`; there is no other content except
  `META-INF/*` and `pack.mcmeta`.
- **Every recipe uses one serializer**, `create:milling` — 143/143. Create stays
  in the pack, so no serializer disappears with the JARs.
- **No cross-namespace collision.** This is the risk that the original seven did
  not have: both mods ship into the **`create` namespace**, not their own. Recipe
  IDs therefore stay `create:milling/<name>`, which is what makes the move
  behaviour-preserving. A full-path scan of all 480 installed JARs found **zero**
  collisions against the 143 paths. (A first pass that compared bare *filenames*
  appeared to show ~86 clashes with Create; those were false positives — Create's
  199 same-named files live under `data/create/recipe/milling/compat/`, a
  different path. Comparing full paths is the only correct test here.)
- **These two JARs also carried a latent distribution bug.** CurseForge reports
  `allowModDistribution = false` for both projects, which is the same condition
  that forced direct-URL pins for Simply More and Overgeared. They were pinned
  `mode = "metadata:curseforge"`, so `packwiz-installer` could refuse them with
  "excluded from the CurseForge API". Porting to a datapack removes the exposure.

### Licenses

Both JARs declare `license = "MIT"` in their own `neoforge.mods.toml`. The
CurseForge API returns a null `license` field for both projects, so the JAR
metadata is the authoritative source here. MIT requires attribution only; both
authors (Blizzor) are credited in `docs/mods/manifest.md`.

### Recipe-count caveat

`Loaded N recipes` is **noisy in this pack**. Five boots across three
configurations returned 47540, 47539, 47540, 47535 and 47540 — a ±5 band, from
mods that register recipes conditionally. The signal that matters is that the
count **never rose by 143**, which is what duplication by recipe ID would look
like, and that both post-removal boots matched the pre-change baseline of
47540. A canary boot with the JARs *still installed* confirmed the datapack
loads and wins by ID (`Found new data pack lead-leylines-compat-recipes`), with
**0** `Parsing error loading recipe` lines on every run. Do not treat a single
boot's count as authoritative.

## Not datapackable: Simply Swords Create Lines

`simplyswords_create_lines` (CurseForge 1595470) was the third Tier 0 candidate
and stays installed. **Two independent reasons, the structural one first.**

### 1. It registers items, so it is not a data-only mod

An earlier survey pass classified this as "1 dummy class, recipe-only" by
counting class files. That was wrong — the class count was read without
decompiling it. `javap` on the one class shows:

```
private static final DeferredRegister$Items ITEMS;
private static final String[] LINE_IDS;
public SimplySwordsCreateLines(IEventBus);
```

It registers **104 items** via `DeferredRegister`, and **all 104 recipes
reference those items** (`simplyswords_create_lines:*`). The JAR also ships 104
item models, 2 textures, and a lang file.

Minecraft 1.21.1 has **no data-driven item registry** — a datapack cannot create
items. Porting only the recipes would orphan every one of them and the Create
production lines would silently vanish from JEI. Removing this mod therefore
requires reimplementing it as pack-owned Java (104 item registrations + 104
models + 2 textures + 104 recipes), which is a content mod rather than a
consolidation. Not worth it to replace one working 92 KB JAR.

**Lesson for the next survey: a low class count is not evidence of a data-only
mod.** Read the class with `javap` before claiming a JAR is portable. The two
Create mods that were ported really did have **zero** class files, which is why
they moved cleanly.

### 2. The licence evidence conflicts

CurseForge's project page displays "MIT License", but the JAR's own
`neoforge.mods.toml` says `license="All-Rights-Reserved"`, and this repo already
records the parent project as **Timefall Development License / ARR** with an
explicit "do not embed the jars" note (`manifest.md`, Simply Swords rows). When
store metadata and the authored artefact disagree, the artefact and the parent
project's terms govern. The pack owner reviewed this and decided not to proceed,
which is why the item-registration work above was never started.

Had it been only a licence question, the DarkSleep precedent would apply:
reimplement rather than copy. It is not only a licence question, so this is
recorded as **not datapackable** rather than **not copied**.

## Layout decisions

**One new datapack for all 567 recipes**, `lead-leylines-compat-recipes/`, even
though they come from six mods. They are all the same shape (a recipe, one
vanilla-or-mod serializer, no behaviour), and splitting by origin would produce
six near-identical folders. The origin namespace (`fcbn`, `fctf`, `fcbe`,
`fcbwg`, `fcru`, `create_ru_compat`) is preserved inside each path, so
provenance is still obvious and a future re-sync is per-namespace.

The Tier 0 Create recipes went into the **same** datapack, under
`data/create/recipe/milling/`. Two consequences worth remembering:

1. **Recipe IDs do not move.** They stay `create:milling/<name>`, exactly as the
   JARs had them, so nothing that referenced them changes. This is why the
   `create` namespace was kept instead of being renamed to a pack namespace.
2. **Filename-level provenance is lost for these 143**, because the origin
   namespace genuinely is `create` for both mods. Git history plus the Tier 0
   table above are the record. If you ever re-add either mod, **delete these
   files first** or every recipe logs a duplicate-ID parse error — same rule as
   the Oritech Create compat noted in [configs.md](configs.md).

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
  Re-confirmed against NeoForge 21.1: the data-driven registry
  `data/<ns>/neoforge/loot_modifiers/global_loot_modifiers.json` does exist, but
  its codecs are item-level only (`add_item`, `remove_item`, `set_count`,
  `limit_count`, …) — there is no "roll another table and append" operation. A
  replacement therefore needs code, not data.
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

These eight upstream projects are ports of generated data and are close to
dormant, so a re-sync should be rare. When one is needed:

1. `packwiz` re-add the mod temporarily, or download the JAR from CurseForge.
2. Diff the JAR's `data/` tree against the matching namespace in
   `lead-leylines-compat-recipes/`.
3. Copy changed JSON, run `packwiz refresh`, then `scripts/smoke_test.py`.
4. Update the byte counts in the tables above.

For the two Tier 0 Create mods the diff is **not** per-namespace — they share
`data/create/recipe/milling/` — so compare against the file list recorded in the
Tier 0 table and expect both projects' recipes to be interleaved.

If a re-add ever ships a **new** recipe at a path already in the datapack, the
datapack wins and the JAR's version is silently ignored; the reverse is also
true. That is the intended precedence, not a bug — but it means a re-add must be
checked against the datapack contents, not just added.

Because the upstream repos are quiet, git history in this repo is the only
audit trail for what changed and when. Do not squash the migration commit.