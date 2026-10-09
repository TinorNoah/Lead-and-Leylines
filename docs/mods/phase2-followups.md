# Phase 2 follow-ups: KubeJS classification, suppression mechanisms, revalidation, bug triage, join sync

Worked through the six items from `docs/audit_atm-10_phase2.md`. Everything below is measured or read from files; nothing is inferred without saying so.

## 1. KubeJS and its five addons

Evidence: every `mods.toml` in `dist/_smoke-test/mods/` scanned for a `kubejs` dependency entry.

**KubeJS itself: REQUIRED.** Eight other installed mods declare it, and none mark it optional:

| Consumer | declaration |
|---|---|
| PonderJS | `modId = "kubejs"`, **`mandatory = true`** |
| Create Ore Excavation | `modId="kubejs"`, type unspecified → defaults mandatory |
| Modern Industrialization | `ordering = "AFTER"`, unspecified → mandatory |
| InControl | `ordering = "AFTER"` → mandatory |
| LootJS | `modId = "kubejs"` → mandatory |
| FTB XMod Compat | `ordering = "AFTER"` → mandatory |
| Create Encased | `ordering = "AFTER"` → mandatory |
| Create: Aquatic Ambitions | `modId="kubejs"` → mandatory |

PonderJS is the hard one — it is explicitly `mandatory = true`, and Ponder is a Create dependency. Removing KubeJS breaks Create, MI, InControl, LootJS and more.

**The five addons: PLANNED-FOR-USE.** None is required by anything:

| Addon | Provides | Required by |
|---|---|---|
| `kubejs_create` | `CreateEvents`, `BoilerHeaterHandlerEvent`, `SpecialFluidHandlerEvent`, `SpecialSpoutHandlerEvent` | Create Ore Excavation, but **`type="optional"`** — VERIFIED |
| `kubejsadditions` | `AdditionalEvents`, `JadeEvents`, `JEIEvents` | nothing |
| `irons_spells_js` | `IronsSpellsJSEvents` | nothing (Iron's Spells itself does not require it) |
| `kjsbotanypots` | Botany Pots KubeJS bindings | nothing |
| `kubejs_mekanism` | Mekanism KubeJS bindings | nothing |

With zero scripts shipped, every one of these event buses is currently idle. They are held, not required.

**Conclusion:** KubeJS is load-bearing and stays. The five addons are held for planned use — the bindings exist so a future script can use them without a mod round-trip. Keep them; document that they are unused today.

Also: delete the empty `pack/kubejs/`. It is not in the packwiz index and implies scripts that do not exist.

## 2. Why recipe suppression and loot-table suppression use different mechanisms

**Both mechanisms work, and both are in active use.** The divergence is not an oversight in effect, but it is undocumented, which is the actual risk.

- Recipes — 63 files, `neoforge:conditions: [{type: neoforge:false}]`. Example: `lead-leylines-load-fixes/data/cbc_at/recipe/munition/rocket/rocket_fuzing.json`
- Loot tables — 120 files, `{"type":"minecraft:empty"}`. Example: `lead-leylines-orphan-loot/data/arsdelight/loot_table/blocks/dawnberry_jelly.json`

**Why they differ.** A recipe id is referenced by nothing at runtime — it is an entry the recipe book and JEI read. A block's loot table id *is* referenced, implicitly, by the block itself: break the block and Minecraft looks up `data/<ns>/loot_table/blocks/<block_id>`. `neoforge:false` makes that lookup fail, which produces `Couldn't parse element` or a missing-table warning — trading one error for another. `minecraft:empty` resolves cleanly and yields no drops.

**What would break if you changed either mechanism:**

Changing loot tables to `neoforge:false` — the 118 `blocks/` tables would become dangling references for blocks that still exist. `spawn` (3 tables) has its mod installed, and `mekmm` (80) is a JarJar inside `mekanism_extras-1.21.1-1.4.1.jar`, which IS installed. Those 83 belong to live blocks, so `neoforge:false` would reintroduce exactly the parse errors the override exists to remove.

Changing recipes to `minecraft:empty` — `minecraft:empty` is a loot-table type, not a recipe type. This is not a valid substitution; it would fail to parse rather than disable.

**The safety finding.** I swept all 831 non-orphan datapack JSON files (475 KB) for references to the 120 orphan ids: **zero referrers.** That means every one of the 120 could be deleted without a dangling reference *within our datapacks*. But it does **not** mean they are safe to delete — the reference is the block itself, at runtime, not a file in our datapacks. That is precisely why `minecraft:empty` was chosen over deletion.

**Correction — all 120 belong to mods that ARE installed.**

An earlier version of this document claimed ~37 of the 120 belonged to removed mods. That was wrong, and the error is worth recording because it is easy to repeat: it came from matching namespaces against **jar filenames** in `pack/mods/`. `arsdelight` looked absent because there is no `arsdelight.pw.toml` — the mod is **Ars Nouveau's Flavors & Delight**, whose jar is `arsdelight-2.2.2.jar` with `modId = "arsdelight"`.

Matching on the `modId` declared inside each jar's `mods.toml`, all ten namespaces are installed:

| Namespace | Mod |
|---|---|
| `mekmm` (80) | JarJar inside Mekanism Extras |
| `create_connected` (16) | Create: Connected |
| `createcasing` (8) | Create: Casings |
| `arsdelight` (6) | Ars Nouveau's Flavors & Delight |
| `mekanism_extras` (4) | Mekanism Extras |
| `spawn` (3) | Spawn |
| `unusualend` (2) | Unusual End |
| `createdieselgenerators`, `extendedae`, `farmers_spell` (1 each) | installed |

So **every** one of the 120 empties is still load-bearing: the block exists and needs *a* table. That is why `scripts/audit_overrides.py` reports 0 unnecessary out of 120, and it kills the "batch 1, highest yield" idea from the revalidation plan — there is no free win there.

## 3. Revalidation plan for the 63 disabled recipes and 120 empty loot tables

Both sets date from `2026-09-27`. Some may be fixed upstream. `docs/mods/load-fixes-inventory.md` already records a per-row undo path, so this is mechanical — but it must be batched, because a boot with a re-enabled broken recipe tells you nothing about which of ten caused it.

**Rules for every batch:**
1. One namespace per batch. Never mix.
2. Max 10 overrides per recipe batch, max 20 per loot batch.
3. Before each batch: `git stash` is not used — instead branch, so the batch is one revertable commit.
4. After each batch: `packwiz refresh` from `pack/`, then `python scripts/smoke_test.py --skip-bench --memory 8192`.
5. Pass condition: no new `Parsing error loading recipe`, `Couldn't parse element`, `loot_table`, or `Failed to load` in `latest.log`. Grep explicitly:
   ```
   grep -E 'Parsing error loading recipe|Couldn.t parse element|Failed to load|Unknown recipe' dist/_smoke-test/logs/latest.log
   ```
6. Any failure: `git revert` the batch commit. Not a partial revert — the batch is the unit.
7. Record every outcome in `docs/mods/load-fixes-inventory.md` with the date and the smoke-run path, including "still broken".

**Order — cheapest and highest-yield first:**

| Batch | Contents | Why first |
|---|---|---|
| 1 | The 6 namespaces whose mod is **gone** (~37 loot tables) | Highest chance of being obsolete — the mod was removed, so its tables can no longer parse-fail. |
| 2 | `unusualend` recipes (13) + `unusualend` loot (2) | Largest single recipe group |
| 3 | `tf_dnv` (6), `netherexp` (6), `eclipticseasons` (6) | Three whole namespaces, recipe-only |
| 4 | `spectrum` (4), `regions_unexplored` (4), `create_shimmer` (4), `cbc_at` (4) | Small even groups |
| 5 | `mekmm` (80) + `spawn` (3) loot | **Last.** Blocks still exist, so a re-enabled broken table re-breaks. Lowest expected yield, highest blast radius. |

**Time:** batches 1–4 are boot-only checks, roughly 2 min each, so ~40 min total. Batch 5 needs a fuller run.

**Expected yield, honestly:** low. These overrides were correct 8 days ago and the mods have not been updated since. Batch 1 is the only one where I'd bet on real deletions.

## 4. NaN-health and biome-alias bugs

**Both are ATM-10-specific. Neither applies to this pack.** Investigated rather than assumed:

**NaN health on login** — ATM-10's `fix_death_bug.js` fires on `PlayerEvents.loggedIn` when `getHealth()` or `getAbsorptionAmount()` is NaN. Evidence this pack is unaffected:
- No NaN in any of the 20 smoke-run reports. The only hit across all of them is an unrelated Vulkan float-control log line (`preserveZeroInfNan32=true`) in `2026-09-26T063821Z.md:304`
- No symptom has ever been reported in `CHANGELOG.md` or the ledgers

This mod pack has Apotheosis, Epic Fight, ParCool and Point Blank, all of which touch attributes and health, so the *mechanism* is plausible here — but absence of evidence is not evidence of absence, and the honest position is: **no evidence the bug exists, no basis for a workaround.** Adding a `loggedIn` handler that mutates player health on a guess is a change with real risk and no demonstrated problem behind it.

**Biome alias** — ATM-10's `registry_fix.js` aliases `biomeswevegone:skyrise_vale` → `:skyris_vale`. Evidence:
- `biomeswevegone` is **NOT in this pack.** VERIFIED: no match in `pack/mods/`
- Both spellings ship in `Oh-The-Biomes-Weve-Gone-NeoForge-2.6.0.jar`, which IS installed — so the typo source exists, but the alias is not needed unless something references the wrong spelling
- `grep -riE 'skyrise|skyris' pack/ docs/` finds nothing

**No fix warranted for either.** If a NaN death ever appears, the reproduction is a login with the affected player state, and the fix is then justified.

## 5. Server-side join synchronization

**I could not measure this, and I want to be explicit about why rather than produce a number that looks like data.**

The blocker: `scripts/smoke_test.py` **never logs a player in.** No `PlayerLoggedIn`, no join command, no second connection — it boots, generates, samples `/tick query`, and stops. So join sync has no harness. Every number I could produce today would be a boot-time proxy, not join sync, and labelling it "join sync" would be misleading.

What I did establish:

- **JEI and JEI Stuff cannot be the cause.** Both are `side = "BOTH"`, but their expensive phase is client-side ingredient/recipe indexing — `Registering recipes: jeistuff:jeistuff took 4.541 s` runs on the client. Item 6 re-confirms this figure from `latest.log`.
- The pack's actual join-handling mods are `Login Protection` (`logprot-1.21.1-3.6.jar`, `both`) and `NeoAuth` (`client` only). Login Protection is the only server-side join hook.

**To measure it properly, the harness needs a join.** That is a real code change to `scripts/smoke_test.py`: start the server, connect a client, and time `PlayerLoggedIn` → first chunk sent. That needs a real client — either a headless Minecraft bot (e.g. `mineflayer`, Node) or the existing Prism instance driven manually. It is not something I can fake with a console command, and `/tick query` on an empty server measures an idle server, not a join.

**Recommendation:** treat this as a tooling task, not an audit finding. Either (a) add join measurement to `smoke_test.py` as a separate opt-in `--join-test` mode, or (b) measure once by hand in Prism with Spark running and read the join-time breakdown. Option (b) is faster and answers the question; option (a) makes it repeatable. Given that Spark is deliberately not a pack mod, (b) means injecting it the way `smoke_test.py --profile` already does.

## 6. JEI Stuff

**Leaving it alone.** No new evidence contradicts the measurement.

- Item 2's sweep touched 831 datapack JSON files and found no JEI Stuff artifact.
- The server-side join sync concern remains **unmeasured**, not disproven — item 5 explains why. So the original open question is unchanged, and per instruction it stays open rather than being quietly closed.
- Client cost re-verified from today's log: **4.541 s** of an 11.9 min index (0.6%), matching the 4.6 s already recorded.

`AGENTS.md` and `docs/mods/manifest.md` already say "still shipped pending an explicit remove decision" and name the server-side sync as the unquantified part. That remains accurate; nothing needs changing.
