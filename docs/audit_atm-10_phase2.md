# Audit: Lead and Leylines vs ATM-10 — Phase 2 (mod conflicts and bug fixes)

- **Reference:** `AllTheMods/ATM-10`, shallow clone at `../_reference_pack`
- **This pack:** `Lead and Leylines` 0.1.24, `pack/pack.toml`
- **Scope:** KubeJS/CraftTweaker scripts, mixin or config overrides, fix/patch mods, removed or replaced mods, known-issue workarounds
- **Read-only.** Nothing in this pack was modified by this audit. This report is the only file created.

## 0. Evidence limits

**The ATM-10 repo still has no mod list.** VERIFIED: no `manifest.json`, no `.mrpack`, no `mods/` directory. Its mod set is only knowable from a CurseForge manifest (project 925200, confirmed at `_reference_pack/config/bcc-common.toml:4`) which was not fetched. So "ATM-10 ships mod X" below means "X has a committed config or script in their repo", never "X is installed".

**ATM-10's scripts are All Rights Reserved and not reusable.** Every file carries: *"As all AllTheMods packs are licensed under All Rights Reserved, this file is not allowed to be used in any public packs not released by the AllTheMods Team, without explicit permission."* This pack is MIT-licensed and public. **No ATM-10 script may be copied into it.** Only the *mechanisms* are transferable, and only if reimplemented from scratch.

Both packs are Minecraft 1.21.1, so loader-level findings transfer. Mod-version findings do not.

## 1. Pack details

| Property | This pack | ATM-10 | Confidence |
|---|---|---|---|
| Minecraft / loader | 1.21.1, NeoForge 21.1.252 | 1.21.1, NeoForge (version not in repo) | VERIFIED / UNKNOWN |
| Mods | 570 (`ls pack/mods/*.pw.toml \| wc -l`) | not found | VERIFIED / UNKNOWN |
| KubeJS | **installed** (`kubejs-neoforge-2101.7.2-build.377.jar`, `both`) + 5 addons | installed, 208 `.js` files | VERIFIED both |
| KubeJS scripts in pack | **0 files** | 208 (19 startup, 174 server, 15 client) | VERIFIED both |
| `defaultconfigs/` | **absent** | 3 files (`ftbultimine`, `incontrol`, `justdirethings-common`) | VERIFIED both |
| Committed datapacks | 10 under `pack/global_packs/required_data/` | 1 (`datapacks/sawmill.zip`) | VERIFIED both |
| Load-fix ledger | `docs/mods/load-fixes-inventory.md`, 103 rows | none in repo | VERIFIED |

## 2. Comparison table

| Area | ATM-10 does | My pack does | Gap or difference | Evidence | Confidence |
|---|---|---|---|---|---|
| Conflict-guard script | `startup_scripts/incompatible_versions.js` asserts 5 version pins + 2 "mod loaded" hazard warnings | **nothing** — no KubeJS scripts at all | No automated guard against a known-bad mod version entering the pack | `_reference_pack/kubejs/startup_scripts/incompatible_versions.js` vs `find pack/kubejs -type f` = 0 | VERIFIED |
| Broken-recipe suppression | 63 scripts call `event.remove(...)`; `remove_recipes_from_banlist.js` reads a **config list** (`config.remove_recipes_by`) so removals are data, not code | 63 committed JSON overrides under `lead-leylines-load-fixes`, each with `neoforge:conditions: false`. Deleting a file is the undo | Same outcome, different mechanism. Mine is declarative and diffable; theirs is data-driven at runtime | `pack/global_packs/required_data/lead-leylines-load-fixes/` (63 files) vs `_reference_pack/kubejs/server_scripts/` | VERIFIED |
| Orphan loot tables | **962 ids** in one 74 KB JSON, applied by `disable_loot_table.js` via `ServerEvents.generateData` writing `neoforge:false` at runtime. No committed datapack | **120 committed JSON files**, each `{"type":"minecraft:empty"}` | **Mine is 8× smaller and more surgical; theirs is 8× broader.** 928 of theirs are Bibliocraft | `disable_loot_table_ids.json` vs `find pack/global_packs/required_data/lead-leylines-orphan-loot -name '*.json' \| wc -l` = 120 | VERIFIED |
| Disable mechanism | `neoforge:conditions: [{type: neoforge:false}]` for **both** recipes and loot tables | Recipes: `neoforge:false`. **Loot tables: `minecraft:empty` instead** | Inconsistent mechanism inside my own pack. `empty` still satisfies a referencing table; `neoforge:false` makes it not exist | `lead-leylines-orphan-loot/*.json` vs `lead-leylines-load-fixes/data/cbc_at/recipe/.../rocket_fuzing.json` | VERIFIED |
| Registry / alias repair | `registry_fix.js` adds a biome alias at runtime (`biomeswevegone:skyrise_vale` → `:skyris_vale`) via `Java.loadClass` | No equivalent. Not needed — no `skyrise`/`skyris` reference anywhere in my pack | Not applicable | `_reference_pack/kubejs/server_scripts/Tweaks/registry_fix.js`; `grep -riE 'skyrise\|skyris' pack/` = no match | VERIFIED |
| Runtime player-state patch | `fix_death_bug.js` — on login, heals `NaN` health and zeroes `NaN` absorption | No equivalent | Would be needed if this pack had the same NaN-health bug. **Untested and unproven here** | `_reference_pack/kubejs/server_scripts/Tweaks/fix_death_bug.js` | VERIFIED (theirs) / NOT APPLICABLE (mine) |
| Fix-shaped mods | Ships `allthetweaks`, `utilitarian`, `integrateddynamicscompat`, `amendments`, `euphoria_patcher` | Has `amendments` only; lacks the other four | Not directly comparable without their mod list. `utilitarian` is a general fix library ATM-10 configures | `ls _reference_pack/config \| grep -E 'allthetweaks\|utilitarian\|integrateddynamicscompat\|amendments\|euphoria_patcher'` vs `ls pack/mods` | VERIFIED |
| Biome-modifier suppression | `disable_biome_modifier.js` + a 1-entry id list (`create:neoforge/biome_modifier/zinc_ore`) | Suppresses vanilla stone blobs via a **datapack** that strips placed features from biome lists (`lead-leylines-no-vanilla-stone`) | Different lever, same goal class. Mine is larger in scope and declarative | `_reference_pack/kubejs/server_scripts/Tweaks/disable_biome_modifier*.{js,json}` vs `pack/global_packs/required_data/lead-leylines-no-vanilla-stone/` | VERIFIED |
| Fix inventory as documentation | none — the id lists are the documentation | `docs/mods/load-fixes-inventory.md`, 103 rows, with the undo path and the "Fix later" condition per row | **Clear advantage.** Their 962-id JSON says what is broken but not when it can be re-enabled | `docs/mods/load-fixes-inventory.md` | VERIFIED |
| Fix provenance | none recorded | Every override names the upstream bug; the ledger cites the smoke audit it came from (`2026-09-27T063607Z`) | Advantage | `docs/mods/load-fixes-inventory.md:1-25` | VERIFIED |
| Tooltip/config crash workarounds | `utilitarian-common.toml` configured; `lmft.json` disables in-game error | `apothic_enchanting.cfg`, `bclib/client.json`, `wover/client.json` disable first-run welcome screens | Comparable in spirit, different mods | `_reference_pack/config/{utilitarian-common.toml,lmft.json}` vs `pack/config/{apotheosis,bclib,wover}` | VERIFIED |
| Stray script directory | none | **Empty `pack/kubejs/` exists but is not in the packwiz index** | Harmless, but confusing: KubeJS is installed and the directory implies scripts that do not exist | `find pack/kubejs -type f` = 0; `pack/index.toml` has no `kubejs/` entries | VERIFIED |

## 3. Recommendations

Ranked by impact ÷ risk. All are proposals; **nothing was applied.**

### R1 — Note the KubeJS licensing boundary so nobody copies ATM-10 scripts (impact: high, risk: low)

This is the one finding that could cause real legal harm. ATM-10 stamps **every** script with an explicit All Rights Reserved notice forbidding use in public packs without permission. This pack is MIT and public. A future agent comparing the two repos could plausibly copy `disable_loot_table.js` or `incompatible_versions.js` and not notice the header.

Cheapest durable fix: a line in `AGENTS.md` and in the audit report that ATM-10 scripts are ARR and must never be copied — only their mechanisms may be reimplemented. No code change.

### R2 — Make the suppression mechanism consistent (impact: med, risk: low)

My pack uses `neoforge:false` for recipes but `minecraft:empty` for loot tables. These are not equivalent: `empty` satisfies anything referencing the table, whereas `neoforge:false` means the loot table does not exist at all.

That inconsistency is currently *load-bearing but undocumented* — an empty table is required where something still references the path, and `neoforge:false` would produce a dangling reference. That is a plausible source of future `Couldn't parse element` errors when someone "tidies" one set into the other.

Recommendation: document in `docs/mods/load-fixes-inventory.md` which overrides need `empty` because a reference survives, and which are free to be `neoforge:false`. Do **not** bulk-convert. Low risk, purely explanatory, and it stops a plausible future breakage.

### R3 — Reconsider `KubeJS` itself, or wire it up (impact: med, risk: med)

KubeJS 6 mods are installed (`kubejs`, `kubejs-additions`, `kubejs-botany-pots`, `kubejs-create`, `kubejs-irons-spells`, `kubejs-mekanism`) and **not one script is shipped**, yet an empty `pack/kubejs/` sits in the tree. That is a standing invitation to add scripts casually, in a pack that currently gets all its overrides from declarative datapacks instead.

Two honest options, and this is a judgement call, not a measurement:
- **Keep KubeJS but declare its role.** It is a dependency magnet — 5 addons need it — and removing it means removing those. Document in `docs/mods/configs.md` that recipe work goes in datapacks under `global_packs/required_data/`, and KubeJS is dependency-only.
- **Remove KubeJS and the 5 addons**, dropping 6 mods.

I lean toward the first: the addons pull in behaviour other mods expect, and the declarative approach is working (103 documented overrides, zero script-maintenance burden). But the empty directory should go either way, since it implies scripts that do not exist.

### R4 — Add a version-hazard guard only if a real hazard exists (impact: low, risk: low)

ATM-10's `incompatible_versions.js` pins 5 versions and warns on 2 mods. **None of those transfers.** Their list is `jei`, `uranus`, `octolib`, `utilitarian`, `amendments` plus `accessories_compat_layer` and `letmedespawn` hazards; my pack has only `amendments` in common, and `letmedespawn` is present but has never been reported as a problem here.

Adding a guard script now would be speculative. It becomes worth doing the moment this pack hits a mod version that visibly breaks something — which is exactly what happened on 2026-09-30 with JET 0.14.1, and that history is already in `docs/mods/manifest.md`.

### R5 — Do **not** adopt ATM-10's loot-table breadth (impact: none, risk: high)

Tempting to conclude "they disable 962 broken tables and we disable 120, so we have 842 more errors." That would be wrong. Their list is 928 Bibliocraft entries — one mod with a large broken surface — and this pack does not have Bibliocraft's equivalent problem. The count measures their pack's mod mix, not their diligence.

No action. Recorded here so the next audit does not re-derive it.

## 4. What this pack does better — do not "fix" these

- **A load-fix ledger with undo instructions.** `docs/mods/load-fixes-inventory.md` gives 103 rows, each with the override path, the shape, the undo step, and a "Fix later" condition. ATM-10's equivalent is a bare id list — you can see what is broken but not when it can come back.
- **Declarative over imperative.** 63 JSON overrides are diffable, reviewable in a PR, and removable by deleting a file. ATM-10's removals live in JavaScript that runs at boot.
- **Provenance.** Every override traces to a dated smoke audit (`2026-09-27T063607Z`). ATM-10 records no source for its fixes.
- **Recipe-only-jar porting.** Two mods whose only content was recipes were converted to a datapack rather than shipped as jars (`lead-leylines-compat-recipes`, `lead-leylines-oritech-create-compat`), avoiding CurseForge's `allowModDistribution = false` install failure documented in `docs/mods/configs.md`.

## 5. Could not be verified

- **Whether ATM-10's fixes are still needed.** Their scripts disable ids with no conditions and no re-check. Some may be long-fixed upstream. Their repo has no issue tracker or fix ledger, so there is no way to tell from the repo.
- **Whether my 63 disabled recipes and 120 empty tables are all still necessary.** Some may be fixed upstream since 2026-09-27. Re-enabling one at a time is the only way to know, and `docs/mods/load-fixes-inventory.md` already records the undo path per row.
- **Whether my pack has an unfixed ATM-10-style bug.** `fix_death_bug.js` (NaN health/absorption on login) and `registry_fix.js` (biome alias) are both absent from my pack, and neither absence is evidence of being unaffected — only that no symptom has been reported.
- ATM-10's mod list, and therefore whether any of their fix-mods (`utilitarian`, `allthetweaks`, `integrateddynamicscompat`) duplicate something of mine.

## Remaining phases / follow-up tasks

- **Phase 3 (config management)** is the natural next pass and the numbers are stark: **19 committed config entries vs their 123**, and **no `defaultconfigs/` directory at all** vs their 3. `defaultconfigs` is also the server/client config mechanism, which is where the JEI client stall and the Smooth Chunk Save decision actually live.
- **Phase 4 (startup, load time, memory).** This pack now has the harder data: 306 s client boot, 11.43 min JEI indexing with 166 s render-thread freeze, 85–129 s server boot. ATM-10 has nothing measurable in git.
- **Phase 5 (maintenance).** Their `CHANGELOG.md` plus 59 per-version `changelogs/` files; this pack has one `CHANGELOG.md` and no split.
- R1–R5 need approval, then `minecraft-modding`/`add-mod` for any jar change and `local-smoke-test` to verify. R2 and R3's first half are documentation-only and need neither.
- `../_reference_pack` can be deleted; it is outside the pack and outside git.

## Questions for me

1. **R3:** keep KubeJS as a dependency magnet and document that recipes go in datapacks, or remove all 6 KubeJS mods? I lean keep-and-document, but the empty `pack/kubejs/` should go either way.
2. **R2:** want me to write up which of the 120 empty loot tables need `minecraft:empty` specifically (because a reference survives) versus which could safely become `neoforge:false`? That is a real audit of 120 files, not a bulk edit.
3. Is re-testing the 2026-09-27 recipe disables worth doing now, or is that a pre-release pass? Some may be fixed upstream and could come back.
4. Should phase 3 run next, or would you rather I finish the phase-2 items you pick from the recommendations above first?
