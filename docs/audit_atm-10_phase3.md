# Audit: Lead and Leylines vs ATM-10 — Phase 3 (config management)

- **Reference:** `AllTheMods/ATM-10`, shallow clone at `../_reference_pack`
- **This pack:** `Lead and Leylines` 0.1.24, `pack/pack.toml`
- **Scope:** `defaultconfigs`, server vs. client configs, config sync, datapacks and resource packs
- **Read-only.** This report is the only file created.

## 0. Evidence limits

Same as phases 1 and 2: ATM-10 has no mod manifest in git, so "ATM-10 ships mod X" means only "X has a committed config or script". Their **server build is not in git either** — CurseForge assembles it — so I cannot see what their server actually excludes.

Both packs are Minecraft 1.21.1, so config mechanisms transfer. Mod-specific keys do not.

## 1. Config surface

| | This pack | ATM-10 |
|---|---|---|
| Committed `config/` files | **20** | **206** (99 top-level + 107 in mod subdirs; quest/lang/sNBT content excluded) |
| `defaultconfigs/` | **absent** | 3 files |
| Files with a real non-default setting | 20 (all deliberate) | **21 of 206 — 185 only re-state mod defaults** |
| `-common.toml` committed | 1 | 38 |
| `-client.toml` committed | 0 | 20 |
| `-server.toml` committed | 0 | 19 |
| Plain (unsuffixed) committed | 19 | 22 |

## 2. Comparison table

| Area | ATM-10 does | My pack does | Gap or difference | Evidence | Confidence |
|---|---|---|---|---|---|
| `defaultconfigs/` | 3 files: `ftbultimine/ftbultimine-server.snbt`, `incontrol/spawn.json`, `justdirethings-common.toml`. These are **server-override** files that land in `world/serverconfig/`, letting a server admin tune per-world without touching mod defaults | **Absent.** No `defaultconfigs/` directory exists at all | The pack runs a dedicated server and generates **73 `-server.toml` files** at boot, none of them pack-overridable | `_reference_pack/defaultconfigs/` vs `ls pack/defaultconfigs` = missing; `find dist/_smoke-test/config -name '*-server.toml' \| wc -l` = 73 | VERIFIED |
| Config breadth | 20, and `docs/mods/configs.md` states the policy explicitly: *"Defaults are the pack unless a row below says otherwise. Do not dump every mod's full config into git."* | **~90% of ATM-10's surface is re-stated defaults, not content.** Of their 206 real config files, 185 carry no non-default value; only 21 change anything. The count was never the gap | `docs/mods/configs.md:3` vs diff-against-documented-default scan of `_reference_pack/config` | VERIFIED |
| Client-only configs on the server | Unknown — no server artifact in git | **5 client-only config files ship in the server zip**: `iris.properties`, `defaultoptions/keybindings.txt`, `entity_model_features.json`, `tooltipoverhaul/custom_frames.json`, `tooltipoverhaul/tooltipoverhaul.toml` | Dead weight on every dedicated server; none of the owning mods is present server-side | `zipfile` read of `dist/Lead-and-Leylines-0.1.24-server-mods.zip`; owners `irisshaders`/`defaultoptions`/`entity-model-features`/`tooltipoverhaul` are all `side = "client"` | VERIFIED |
| packwiz `side` on configs | n/a | **Not used.** All 20 config index entries have no `side` field; `side` appears only on `mods/*.pw.toml` | The index cannot express "this config is client-only", so every config goes to every install | `pack/index.toml` config entries vs `pack/mods/apotheosis.pw.toml:3` | VERIFIED |
| Server-vs-client config sync | `-server.toml`/`-client.toml`/`-common.toml` split respected across 77 committed files | Only 1 `-common.toml` (`tacz_tactical_breaching-common`) is committed; the other 19 are plain or mod-specific | The suffix convention is not used as a routing mechanism here | `ls pack/config` vs `ls _reference_pack/config` | VERIFIED |
| Datapacks | 1 committed zip (`sawmill.zip`), plus 7 `generateData` scripts that synthesise more at boot | **10 committed unpacked datapacks** under `pack/global_packs/required_data/`, no zips | **Advantage.** Unpacked files are git-diffable and reviewable in a PR; `pack/.packwizignore` also excludes loose `*.zip` | `ls pack/global_packs/required_data`; `pack/.packwizignore` | VERIFIED |
| Datapack loading mechanism | KubeJS `generateData` writes JSON at runtime | Global Packs force-enables `global_packs/required_data/` and `global_packs/required_resources/` | Both work. Global Packs is declarative and visible in a PR | `pack/config/global_packs.toml` `[datapacks].required` | VERIFIED |
| Datapack `pack_format` | not found | 48 on all three owned datapacks (`lead-leylines-load-fixes`, `lead-leylines-orphan-loot`, `darkloot`) | Correct for 1.21.1; consistent | `pack/global_packs/required_data/*/pack.mcmeta` | VERIFIED |
| Resource packs | 1 zip in repo; rest presumably as CurseForge metadata | **13 loose zips** in `pack/resourcepacks/` + 2 texture packs as CurseForge metadata in `mods/` + 1 unpacked required-resource folder | Mixed mechanism, deliberately — `global_packs.toml` comments explain why the zips stay loose | `pack/config/global_packs.toml` comment block above `[resourcepacks].required` | VERIFIED |
| Global Packs error noise | not applicable | 13 `FileAlreadyExistsException` per launch because `resourcepacks/` files are handed to a folder-creating API. Documented as cosmetic | Known and accepted; the file comments explain the alternative (pointing at `required_resources/`) breaks the CurseForge export | `pack/config/global_packs.toml` comment | VERIFIED |
| Pack-side server tuning surface | 3 `defaultconfigs/` entries covering Ultimine permissions, spawn rules, and JDT tick speed | **None** | This pack has 73 generated `-server.toml` files with no pack override for any of them | `_reference_pack/defaultconfigs/` vs `dist/_smoke-test/config/*-server.toml` | VERIFIED |

## 2b. What ATM-10's 21 non-default configs actually do

**Correction:** this audit first reported 123 files (it counted subdirectories as single files). The real number is **206** real config files — and 185 of them only re-state the mod's own documented defaults. Only 21 change anything:

**Difficulty / economy rebalancing — 17 files.** Boss cooldowns cut hard in `cataclysm-common.toml` (128: incinerator 400→100, maelstrom 180→45, bulwark 80→20); `oritech-common.toml` (35: energy/tick 32→64→128→256→512); `modular_machinery_reborn*` (41: size 2048→10280, transfer 128→1028); `extremereactors/common.toml` (4: power ×4, fuel ×0.8); `ironfurnaces-common.toml` (5, tier 1→2); `create_enchantment_industry-server.toml` (2: max enchant 30→50); `modern_industrialization-server.toml` (1: FE/EU 10→16); `refinedstorage-common.toml` (1: energy 1000→50000); `actuallyadditions-common.toml` (1: laser rate → Integer.MAX); `solcarrot-server.toml` (2: hearts 2→3); `pylons-server.toml` (1: harvester delay 60→20); `justdirethings-server.toml` (1: time-wand cost 100→750); `industrialforegoingsouls` (6: damage 4→12); `apotheosis/enchantments.cfg` (2: one enchantment 5→1).

**Client cosmetics — 4 files.** `packmenu.cfg` (13: title/splash/panorama off), `cosmeticarmorreworked-client.toml` (4: buttons nudged 1–2px), `curios-client.toml` (2), `invtweaks-client.toml` (1).

This strengthens R2: most of that 17-file group is server-operator balance policy, but ATM-10 ships it in `config/` to every client, where clients ignore it. It belongs in `defaultconfigs/` (`world/serverconfig/`), editable per-world.

## 3. Recommendations

Ranked by impact ÷ risk. **Nothing applied.**

### R1 — Stop shipping 5 client-only configs to dedicated servers (impact: med, risk: low)

The server zip carries `iris.properties`, `defaultoptions/keybindings.txt`, `entity_model_features.json`, and two `tooltipoverhaul` files. Their owning mods are all `side = "client"`, so a dedicated server reads none of them. Five dead files per server install, and it misleads anyone auditing what the server actually gets.

Two ways to fix, and the choice matters:

- **Set packwiz `side = "client"` on those config entries.** Cleanest if packwiz honours `side` outside `mods/`. **Unverified — I did not test whether packwiz 1.1.0 applies `side` to arbitrary index entries.** Needs a scratch-pack test before relying on it.
- **Filter them in `scripts/pack_artifacts.py`** when building the server zip. Guaranteed to work, touches one function, but is pack-logic rather than manifest-logic.

Try (1) first, fall back to (2). Test: build the server zip and confirm `config/iris.properties` is absent while `config/terrablender.toml` remains.

### R2 — Decide whether `defaultconfigs/` is wanted (impact: med, risk: low)

This is the one structural gap. `defaultconfigs/` is NeoForge's server-override mechanism: a file there is copied into `world/serverconfig/`, so a server admin can change it per-world without editing mod defaults. This pack has **73** generated `-server.toml` files and overrides none of them.

ATM-10 uses it for exactly three things: FTB Ultimine permissions, InControl spawn rules, and Just Direct Things tick speed. All three are **server-operator policy** decisions — how much players may optimise mining, what spawns, how fast machines tick — which is precisely what a `defaultconfigs/` entry is for.

Recommendation: **add it, with a small number of deliberate entries.** Start with the two this pack actually has a reason to set:
- `ftbultimine-server.snbt` if FTB Ultimine is installed and player mining permissions should be bounded
- `incontrol/spawn.json` if the pack wants a spawn policy

Do **not** bulk-copy 73 files. The value of `defaultconfigs/` is that each entry expresses an operator decision; a full dump has the same problem as a full `config/` dump.

**Both mods are installed**, so both entries are directly applicable. VERIFIED against the boot-generated config directory:

| `defaultconfigs/` path | Maps to | Status in this pack |
|---|---|---|
| `ftbultimine/ftbultimine-server.snbt` | `dist/_smoke-test/config/ftbultimine-server.snbt` | generated, unoverridden |
| `incontrol/spawn.json` | `dist/_smoke-test/config/incontrol/spawn.json` | generated as `[]` — no spawn policy at all |

InControl is the clearer case. Its twelve generated JSON files (`areas`, `breakevents`, `effects`, `events`, `experience`, `leftclicks`, `loot`, `phases`, `placeevents`, `rightclicks`, `spawn`, `spawner`) are **all empty arrays**, meaning this pack has no spawn policy whatsoever. That is a legitimate design choice — but it is currently an *unrecorded* one, and ATM-10's `spawn.json` shows the mechanism for expressing it.

### R3 — Keep the declarative-datapack policy (no action)

Worth stating because the phase-1 instinct is "ATM-10 has more, add more." ATM-10's `generateData` approach means its datapack contents **do not exist in git** — they are synthesised at boot, so a reviewer cannot see what a change does without running the game. This pack commits 10 unpacked datapacks, every override is diffable, and `docs/mods/load-fixes-inventory.md` records a cause and undo path per row. That is a genuine advantage and should not be traded for parity.

### R4 — Note the Global Packs error noise rather than "fix" it (no action)

13 `FileAlreadyExistsException` per launch is ugly but documented and cosmetic. The `global_packs.toml` comment already records that the obvious fix (pointing at `required_resources/`) breaks the CurseForge export because the launcher installs texture packs into `resourcepacks/` by its own rule. Leave it.

### R5 — The config count was never the gap (no action)

206 vs 20 sounds like a gap and is not one. 185 of their 206 only re-state documented defaults; 21 change anything (17 difficulty/economy, 4 cosmetics). This pack carries 20 deliberate overrides and a written policy. The right question is not "do we have as many files" but "is every override we have actually load-bearing" — and `scripts/audit_overrides.py` was built to answer that for overrides. **No change recommended.**

## 4. What this pack does better — do not "fix" these

- **Unpacked, committed, git-diffable datapacks.** 10 folders vs ATM-10's 1 zip plus 7 runtime generators. Every change shows in a PR.
- **A written policy about configs.** `docs/mods/configs.md:3` says outright: defaults are the pack, don't dump full configs into git, and every override needs a reason. ATM-10 has no equivalent statement.
- **Per-row provenance.** Each override traces to a dated smoke audit. ATM-10's `generateData` ids trace to nothing.
- **Documented export mechanics.** The `global_packs.toml` comments explain a *broken-looking* error and why the obvious fix is wrong. That is the kind of note that saves an hour next time.
- **Correct `pack_format`.** 48 on every owned datapack, matching 1.21.1.

## 5. Could not be verified

- **Whether packwiz applies `side` to non-mod index entries.** R1 depends on this. Needs a scratch-pack test.
- **What ATM-10's server actually excludes.** Their server artifact is built by CurseForge and is not in the repo, so their client-config-on-server situation is unknown.
- **Whether this pack wants `defaultconfigs/` at all.** That is a server-policy decision, not a technical one. R2 assumes yes because three ATM-10 uses look applicable. FTB Ultimine and InControl are both confirmed installed (`pack/mods/ftb-ultimine-forge.pw.toml`, `pack/mods/in-control.pw.toml`).

## Remaining phases / follow-up tasks

- **Phase 4 (startup, load time, memory)** is now the most valuable remaining. This pack has hard numbers ATM-10 has none of: 306 s client boot, 11.43 min JEI indexing with 166.1 s render-thread freeze, 85–129 s server boot, ~15.9–21.2 CPS. Their repo contains no measurable performance data at all.
- **Phase 5 (maintenance).** Their `CHANGELOG.md` + 59 per-version `changelogs/` files vs one `CHANGELOG.md` here.
- R1 needs a packwiz scratch test before implementation. R2 needs a server-policy decision first.
- Deferred and not started: override revalidation (see the TODO in `docs/mods/load-fixes-inventory.md`), JEI Stuff's server-side join sync, and `smoke_test.py` join measurement.

## Questions for me

1. **R1:** may I run a scratch packwiz test to find out whether `side` works on non-mod entries? If it does, that's a manifest fix; if not, I'll filter in `pack_artifacts.py`.
2. **R2:** do you want server-operator policy in the pack at all — Ultimine permissions, spawn rules, machine tick speeds? If the answer is no, the right action is to document *why* there is no `defaultconfigs/`, so the next person doesn't read the absence as an oversight.
3. ~~Are FTB Ultimine and InControl in the pack?~~ Answered during the audit: both are installed, and InControl currently has no spawn policy at all. So the remaining question is whether you *want* one.
4. Phase 4 next, or would you rather land R1 first since it is small and self-contained?