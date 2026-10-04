# Known client asset issues (open)

Client resource-reload warnings that come from **other mods shipping missing or misnamespaced
assets**, not from this pack's configuration. Collected 2026-10-04 from a full client log of
pack 0.1.24 (ATLauncher instance, `latest crash.txt`).

Nothing here is a crash and nothing here is caused by the pack. The only reason to care is log
noise and reload time: a full client resource reload in this pack takes **3 min 27 s**
(18:53:39 → 18:57:06 measured), and each of these contributes a slice of it. Fixing them requires
either new art or upstream patches, so they are tracked here rather than in the pack.

Reproduce with: `packwiz serve` + a client boot, then read `logs/latest.log`. Every reload
repeats the whole list.

## How the counts were produced

Every path below was resolved against an index of all `assets/**/models/**/*.json` and
`assets/**/textures/**/*.png` entries in the 572 instance jars (116,486 model paths,
62,000 texture paths), so "exists elsewhere" is a fact, not a guess.

## Missing models — 232 warnings, ~130 distinct paths

`ModelBakery: Unable to load model: '<target>' referenced from: '<namespace>:<path>'`. Vanilla
falls back to its built-in `missing_model` placeholder, so the affected block or item renders as
the placeholder rather than disappearing.

| Referring mod | Refs / distinct | Target exists in another namespace? | Notes |
| --- | --- | --- | --- |
| `born_in_chaos_v1` | 82 / 41 | No | Every target is `minecraft:<item>` (e.g. `minecraft:item/frostbittenblade` from `born_in_chaos_v1:custom/frostbittenblade`) and exists in **no** namespace, vanilla included. 41 tombstone/scythe/blade items. Not fixable pack-side without authoring 41 models. |
| `cbc_at` | 30 / 15 | No | Rocket-pod rails, heavy-autocannon recoil springs, muzzle brakes and silencers. Create Big Cannons: Advanced Technology ships blockstates for blocks it never registers. |
| `unusualend` | 24 / 12 | No | 11 `minecraft:` refs (chorus cane, warped lantern, spirit mask, plush, …) plus `unusualend:block/cracked_small_eggs`. |
| `modern_industrialization` | 24 / 12 | No | `modern_industrialization:item/{lv,mv,hv,ev,superconductor,steel,bronze}_stress_input_hatch` and the chemical hatches. MI 2.5.8 references its own removed Ext. Integrations items. Same family as the 23 dead loot tables MIEI shipped. |
| `simplymore` | 14 / 7 | No | `item/{exedrill,mimicry,molten_flare,netherfused_carver,runefused_carver,scarab_roller,soul_foreseer}`. |
| `forbidden_arcanus` | 12 / 6 | No | `item/omega_arcoin` and the five `reinforced_deorum_*` tools. |
| `mekanism_extras` | 8 / 4 | **Yes** | `mekanism_extras:block/factory/front_led/active/{basic,advanced,elite,ultimate}` exists as `mekanism:block/factory/front_led/active/*`. **Fixable** with four `parent` alias models in a pack resource pack; the factory status LEDs currently render as the missing-model placeholder. |
| `aces_spell_utils` | 8 / 4 | No | `item/example_armor_{boots,chestplate,helmet,leggings}` — the library's own example items, harmless. |
| `armageddon_mod` | 6 / 3 | No | `minecraft:{elvenitehammer2,ironcolossusarm3,oathbreakerofchaos}`; also 319 `[RL FIX]` path lines caused by commas and spaces in its geo/animation filenames (see below). |
| singles | ~14 | No | `farmersdelight:block/shepherds_pie_block_leftover`, `tfmg:block_block`, `p1nero_bow:item/oblivionis`, `tacz_bandits:item/bandit_spawn_egg`, `fdbosses:item/no_entity_spawn_block`, `pointblank:item/ammodefault`, `fdlib:item/test_multiblock`, `dummmmmmy:item/target_dummy` (×2), `twilight_spellbooks` via `minecraft:knightmetal_staff`, `irons_spellbooks` (×2), `ars_nouveau` (×2), `createcasing:block/shaft/andesite`. Debug/spawn-egg items are harmless. |

## Missing textures — 65 distinct references, 128 log lines

`ModelManager: Missing textures in model <model>` → the surface renders with the
missing-texture checkerboard.

| Mod | Refs | Target exists elsewhere? | Notes |
| --- | --- | --- | --- |
| `cbc_at` | 52 | No | `cbc_at:block/{bronze,cast_iron}_rocket_pod` (~20 each), `cbc_at:block/built_up_nethersteel_barrel_side`, `minecraft:{bronze_cannon_barrel_side,cast_mould,0}`. Same root cause as its missing models: the addon references textures it never ships. |
| `corn_delight` | 4 | **Yes** | `farmersdelight:block/tray_top` exists as `arsdelight:block/tray_top`. **Fixable** by repointing the nachos block model — no art copying needed, since the fix is a JSON reference, not a duplicated texture. |
| `simplymore` | 1 | No | `simplymore:item/uniques/timekeeper/sun_14`. |
| `twilight_spellbooks` | 1 | No | `twilight_spellbooks:item/ultimate_scepter`. |
| `pointblank` | 1 | No | `minecraft:item/cp2077_e305_prospecta` (misnamespaced). |

## GeckoLib — 252 warnings

| Warning | Count | Notes |
| --- | --- | --- |
| `Found animation file with improper file name format` | 108 | Ars Nouveau (43), Ars Technica (5), Ars Creo, Ars Additions, Iron's Spellbooks (6), Farmer's Spell. Files are named `*_animations.json` instead of `*.animation.json`, so they are not picked up as animations. Affects entities that animate from those files. |
| `Unable to parse animation` | 98 | 18 distinct names, including `animation.gobelinlord.*`, `animation.soldatarion.death`, `animation.vaedricthefallenwanderer.*` (mod-provided), and vanilla names like `sit`, `sit2`, `idle`, `attack`, `supernova`, `adjust_size` — those come from **resource packs**: Fresh Animations rewrites vanilla entity animations with Molang expressions GeckoLib cannot evaluate (e.g. `Failed to parse expression '5-math.cos(-40+query.anim_time*180)*2+nan'`). |
| `Unsupported geometry json version for model` | 46 | `pointblank`, `twilight_spellbooks`, `farmers_spell`, `block_factorys_bosses` ship geo files newer than GeckoLib 4.9.3 supports. Those models do not load. |

## Other

- **407** `BlockStateModelLoader: Exception loading blockstate definition` lines. Dominated by
  `modern_industrialization:*` and `ars_nouveau:*` / `ars_additions:*` blockstates that
  enumerate variants their blocks do not register (same class of bug as the MI hatches above),
  plus `dungeonnowloading:blockstates/ballista_golem_statue_part.json`, which uses
  `ballista_golem_statue_state=bottom_c`, a value outside the mod's own declared property set.
- **319** `[RL FIX]` lines: mods whose asset filenames contain characters `ResourceLocation`
  rejects (commas, spaces, `.psd`, `.txt`). Armageddon is the worst offender and is already
  worked around by `pack/global_packs/required_resources/lead-leylines-armageddon-models/`, which
  republishes its geo/animation files under sanitized names.
- **2** `BlockModel: Found 'parent' loop` — `aces_spell_utils:item/example_gun` points at itself.
  Library example item.

## Open item, not an asset issue

`AlmostUnified` logs two ERRORs per load:
`forbidden_arcanus:stella_arcanum is bound to multiple stone variant tags: c:ores_in_ground/stone
and c:ores_in_ground/deepslate`. Root cause is Forbidden & Arcanus 2.6.1 itself, which lists the
ore in **both** `c:tags/item/ores_in_ground/stone.json` and `.../deepslate.json` (and the block
equivalents). `StoneVariantsImpl.mapEntriesToStoneVariantTags` does `map.put(...)` **before** it
logs, so no ore is skipped; the deepslate tag is written last and wins, and the ore is treated as
a deepslate ore.

Not fixed, because 1.21.1 tag files have no per-entry removal (`TagFile` is only `entries` +
`replace`) and no installed mod depends on this. The only pack-side lever is a `"replace": true`
override of `c:ores_in_ground/stone` for both registries, re-listing every ore from all 19
contributing mods including nested `#c:ores/...` includes. A mistake there silently deletes other
mods' ores from stone generation, and the boot smoke test cannot detect that. Options, in order of
preference:

1. Report it upstream to Forbidden & Arcanus (one ore in one tag file).
2. Accept the two ERROR lines.
3. Do the `replace: true` override, verified by diffing the merged tag before and after on a
   dedicated-server boot — still a maintenance trap, since any future mod that adds an ore to
   `c:ores_in_ground/stone` would be silently dropped until the override is updated.
