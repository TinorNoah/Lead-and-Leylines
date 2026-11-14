# To do

The single list of open work. Details live in the linked docs — this file is the index, not a duplicate.

## Needs your input (blocking)

- [ ] **Balance-tuning values + placement** — 7 mods from the phase 3 follow-up (Oritech energy ~2–4×, MI FE:EU 10→16, RS energy 1000→50000, Create Enchantment Industry 30→50/60→100, Apotheosis `miners_fervor` 5→1, Just Dire Things time-wand 100→750 RF, Curios offset skipped). Oritech and MI interact through FE, so decide those two together. Placement is part of the same decision: server-balance items belong in `defaultconfigs/`, which does not exist yet.
- [ ] **R2: want server-operator policy in the pack at all?** (Ultimine permissions, spawn rules, machine tick speeds.) If no, document *why* there is no `defaultconfigs/` so the absence reads as a decision. Overlaps the placement question above — answer once.
- [ ] **R1: permission for a scratch packwiz test** — does `side` work on non-mod index entries? Decides whether the 5 client-only configs in the server zip get a manifest fix or a `pack_artifacts.py` filter.

## Audits remaining

- [ ] **Phase 4** (startup, load time, memory)
- [ ] **Phase 5** (maintenance)

## Parked (deferred, not blocking any release)

- [ ] **Verify the 2026-10-25 mod wave in game** — Animal Pens accepting entities it should not (Ice and Fire dragons, bosses) and Tool Belt's belt bar beside Curios both need a real client session; a dedicated boot cannot show either. Also confirm the starting-kit iron backpack arrives on a fresh join.
- [ ] **Verify the 2026-10-25 tech wave in game** — the second wave of that day needs a client session for things a boot cannot show: Superb Warfare's gun and vehicle keys against TaCZ and Vic's Point Blank (three firearm systems now share the keyboard), SKY ACES' aircraft controls, whether Grim Storage's network and Smartstock's terminals read AE2/Refined Storage inventories correctly, and whether the Grim trio plus Voltex/Singulo/HBM overlap enough in recipes to confuse players. Balance between those tech trees is unmeasured.
- [ ] **One-off client startup crash, 2026-10-25 06:32** — `Failed to wait for future Common setup` from `ExceptionInInitializerError: ClosedWatchServiceException` at `fzzy_config ThreadingUtils.register`, triggered by `simplyswords config.LootConfig.<clinit>`. Fzzy Config 0.7.7 is the newest 1.21.1 build, so there is no update path; the immediate relaunch booted clean. If it recurs, it is a race between Fzzy's shared config watcher being closed and a late config class-init, and needs an upstream report rather than a pack change.
- [ ] **Epitaphs graves in existing worlds** — the Epitaphs→Graveless swap (2026-10-25) orphans Epitaphs grave blocks. Any grave still holding items in the test world is item loss; clear or empty them before updating that world, or accept it.
- [ ] **Override revalidation boot tests** — `scripts/audit_overrides.py --inventory --items` reports **0** re-enable candidates, so the rest needs boots batched per namespace. Plan and batches: `docs/mods/load-fixes-inventory.md` ("TODO — deferred, not started").
- [x] **TaCZ Tactical Breaching 1.0.7 startup crash** — still unguarded in `1.0.7` bytecode (`ClientWeaponHeatHandler.tick` calls `ENABLE_WEAPON_HEAT.get()` before `SPEC.isLoaded()`, and `DistantGunshotHandler.handleGunEvent` hardcodes 6 `LOGGER.info` lines per shot regardless of `debugDistantGunshots`). Candidate fix remains a 2-method guard mixin in `leylines_patches` if a `1.0.8` build does not ship. (Kept open as a known `leylines_patches` candidate below.)
- [ ] **`leylines_patches` candidate: TaCZ Tactical Breaching 1.0.7** — guard `ClientWeaponHeatHandler.tick` on `BallisticBlockConfig.SPEC.isLoaded()` and gate `DistantGunshotHandler` `LOGGER.info` spam behind `debugEnabled()` if upstream stays on 1.0.7.
- [x] **JEI Stuff's server-side join sync** — measured 2026-11-13 (`JeiStuff$Events` bytecode + Prism log): **6.22 s** once per server boot on first player login (walks 2,335 loot tables, caches in memory for subsequent joins, sends 2.0 MB across 3 packets). Kept (`side = "both"`) for live server datapack/GLM loot (`darkloot`, `Loot Integrations`) and Fluid Interaction/Bartering/Fishing JEI tabs.
- [ ] **`smoke_test.py` join measurement** — harness added (`scripts/join-test/`, Mineflayer bot; see `local-smoke-test` skill), but the 2026-10-10 spike proved vanilla-protocol bots are rejected at NeoForge negotiation (`vanilla.client.not_supported`), so no login timing. Remaining paths: HeadlessMc real client (Linux+Xvfb, not set up) or fake-player mods (skip login sync itself).
- [x] **`dynamic_resources` boot-time proof** — confirmed active and healthy across 2026-11-13/14 client boots (`206.8 s` total boot to menu, 4,076 permanent baked models, `24.38 s` `ModifyBakingResult`).
- [x] **Inventory Essentials re-decision** — resolved 2026-11-14: kept (`side = "client"`) specifically for unique hotbar tool/stack auto-refill (`enableToolRefill`, `enableStackRefill`) and `Space+Click` armor swap, with colliding `enableShiftDrag`, `enableBulkTransfer`, and `Middle-Click` sort disabled in `pack/config/inventoryessentials-common.toml` + `defaultoptions/keybindings.txt`.

## Upstream (waiting on others)

- [ ] **Ice and Fire CE × Epic Fight Armor Compat** — removed 2026-11-14; only file wants `iceandfire` below 2.2. Recheck CurseForge project `1634414` around **2026-11-21** for a NeoForge 1.21.1 build that accepts CE 2.2 ([deferred.md](mods/deferred.md)).
- [x] **Tonywww2/JEI-Optimize#12** — JET 0.14.9 restores 19.57 ABI (pack bumped 2026-11-13). Prism client re-measure still needed.
