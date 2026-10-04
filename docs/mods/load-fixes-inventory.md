# Load-fix inventory (2026-09-27)

Pack-side overrides from the [2026-09-27T063607Z smoke audit](../smoke-runs/2026-09-27T063607Z-audit.md). Use this when you want to **re-enable** content instead of leaving it silenced.

## How these overrides work

| Kind | Datapack | Override shape | Undo |
| --- | --- | --- | --- |
| Disable recipe | `pack/global_packs/required_data/lead-leylines-load-fixes/` | Same path as the mod recipe under `data/<ns>/recipe/<path>.json`, with `"neoforge:conditions": [{"type": "neoforge:false"}]` | Delete that override file, then `packwiz refresh` from `pack/` |
| Empty loot table | `pack/global_packs/required_data/lead-leylines-orphan-loot/` | `data/<ns>/loot_table/<path>.json` → `{"type": "minecraft:empty"}` | Same: delete override, `packwiz refresh` |
| Recipe rewrite | load-fixes | Full corrected JSON at the mod’s recipe path | Replace with upstream when fixed, or delete if upstream ships the fix |

Recipe id `namespace:path/with/slashes` maps to:

`data/namespace/recipe/path/with/slashes.json`

After any add/remove of these files: from `pack/`, run `packwiz refresh`. Smoke with `python scripts/smoke_test.py --skip-bench --memory 8192` and grep `latest.log` for `Parsing error loading recipe` / `Couldn't parse element` / `loot_table`.

Generator used once (not a release tool): `dist/_gen_smoke_load_fixes.py` (under gitignored `dist/`). Prefer editing this inventory + the JSON files by hand going forward.

---

## Disabled recipes (45) — load-fixes

Each row: **delete the override** only after the “Fix later” condition is true (or after you ship a corrected recipe JSON in the same path).

### Soft-dep / missing items

| Recipe id | Why it failed | Pack override | Fix later |
| --- | --- | --- | --- |
| `ae_universal_press:overloadprocessorpress` | Unknown item `ae2lt:overload_inscriber_press` | `…/ae_universal_press/recipe/overloadprocessorpress.json` | Add AE2LT (and matching Universal Press version), **or** drop AE Universal Press soft recipes upstream |
| `ae_universal_press:printedcompatprocessor` | Unknown item `extendedterminal:printed_compat_processor` | `…/printedcompatprocessor.json` | Add Extended Terminal, or remove that soft recipe |
| `ae_universal_press:unoverloaded_circuit_board_print` | Unknown item `ae2lt:unoverloaded_circuit_board` | `…/unoverloaded_circuit_board_print.json` | Same as AE2LT above |
| `jadensnetherexpansiondelight:blue_scale_fungus_roll` | Unknown item `netherexp:blue_scale_fungus` | `…/jadensnetherexpansiondelight/recipe/blue_scale_fungus_roll.json` | Wait for Jaden’s Nether Expansion to register those fungi, or rewrite roll recipes to real items |
| `jadensnetherexpansiondelight:red_scale_fungus_roll` | Unknown item `netherexp:red_scale_fungus` | `…/red_scale_fungus_roll.json` | Same |
| `cbc_at:munition/rocket/rocket_fuzing` | Unknown recipe serializer `cbc_at:rocket_munition_fuzing` | `…/cbc_at/recipe/munition/rocket/rocket_fuzing.json` | CBC Advanced Technologies update that registers the serializer, or remove the recipe from that mod |
| `spectrum:mod_integration/gobber/anvil_crushing/globette_nether_from_buds` | Gobber soft-dep JSON missing `levels` / broken shape | `…/spectrum/recipe/mod_integration/gobber/anvil_crushing/globette_nether_from_buds.json` | Add Gobber **and** a Spectrum build that ships a valid recipe, or leave disabled (Gobber not in pack) |

The seven `twilightdelight` Neapolitan-bridge recipes (`neapolitan/{aurora,glacier,phytochemical,torchberry}_cake_slice`, `rainbow_ice_cream`, `refreshing_ice_cream`, `twilight_ice_cream`) used to be listed here as unknown-item failures. **Resolved 2026-10-04 by installing Neapolitan 6.0.1** (CurseForge 382016 / 7119475); the overrides are deleted and the recipes are live again. Root cause was upstream: Twilight's Flavors & Delight 3.2.3 registers those items only behind `isLoaded("neapolitan")` but ships its recipes, tags, and loot tables unconditionally. See the manifest wave note.

### Malformed 1.21 ingredient JSON (`item` vs `id` / cutting format)

These are **upstream recipe format bugs** on NeoForge 1.21.1. Fix by rewriting the recipe JSON (pack override with a valid recipe) or waiting for the mod author.

| Recipe id | Failure symptom | Pack override |
| --- | --- | --- |
| `unusualend:blob_stew_farmer_delight` | `No key id` on bowl ingredient | `…/unusualend/recipe/blob_stew_farmer_delight.json` |
| `unusualend:carved_squash_farmer_delight` | Result not a JSON object (`warped_squash_wedge`) | `…/carved_squash_farmer_delight.json` |
| `unusualend:chorus_juice_farming_delight` | `No key id` on glass bottle | `…/chorus_juice_farming_delight.json` |
| `unusualend:chorus_petals_via_cutting` | Cutting result not a JSON object | `…/chorus_petals_via_cutting.json` |
| `unusualend:chorus_planks_via_cutting` | Cutting sound/result/straw not objects | `…/chorus_planks_via_cutting.json` |
| `unusualend:chorus_slab_via_cutting` | Same cutting format | `…/chorus_slab_via_cutting.json` |
| `unusualend:chorus_stairs_via_cutting` | Same | `…/chorus_stairs_via_cutting.json` |
| `unusualend:chorus_tea_farming_delight` | `No key id` on glass bottle | `…/chorus_tea_farming_delight.json` |
| `unusualend:ender_stew_farming_delight` | `No key id` on bowl | `…/ender_stew_farming_delight.json` |
| `unusualend:small_squash_farmer_delight` | Result not a JSON object | `…/small_squash_farmer_delight.json` |
| `unusualend:stripped_chorus_cane_block_compa` | Cutting format | `…/stripped_chorus_cane_block_compa.json` |
| `unusualend:warped_squash_farmer_delight` | Result not a JSON object | `…/warped_squash_farmer_delight.json` |
| `unusualend:warped_stew_farming_delight` | `No key id` on bowl | `…/warped_stew_farming_delight.json` |
| `tf_dnv:alchemy_table` | `No key id` on result stack | `…/tf_dnv/recipe/alchemy_table.json` |
| `tf_dnv:butcher_table` | Same | `…/butcher_table.json` |
| `tf_dnv:composter` | Same | `…/composter.json` |
| `tf_dnv:lumber_table` | Same | `…/lumber_table.json` |
| `tf_dnv:mushgloom_torch` | Same | `…/mushgloom_torch.json` |
| `tf_dnv:mycologist_table` | Same | `…/mycologist_table.json` |
| `createdeco:placard` | Dye ingredient `id`/`tag` shape mismatch | `…/createdeco/recipe/placard.json` |
| `create_shimmer:coloring/blue_castle_door` | Mixing/coloring ingredient `amount`/`id` vs `item`/`count` | `…/create_shimmer/recipe/coloring/blue_castle_door.json` |
| `create_shimmer:coloring/pink_castle_door` | Same | `…/pink_castle_door.json` |
| `create_shimmer:coloring/violet_castle_door` | Same | `…/violet_castle_door.json` |
| `create_shimmer:coloring/yellow_castle_door` | Same | `…/yellow_castle_door.json` |
| `cbc_at:cutting/rocket_pod_breech_cast_mould` | Cutting output `amount`/`id` vs `item` | `…/cbc_at/recipe/cutting/rocket_pod_breech_cast_mould.json` |
| `cbc_at:cutting/rocket_pod_rail_cast_mould` | Same | `…/rocket_pod_rail_cast_mould.json` |
| `cbc_at:cutting/twin_autocannon_barrel_cast_mould` | Same | `…/twin_autocannon_barrel_cast_mould.json` |

### Tag / fluid parse

| Recipe id | Why | Fix later |
| --- | --- | --- |
| `spectrum:titration_barrel/bristle_mead_fluid` | `#c:honey` / fluid ingredient shape invalid for this recipe type | Spectrum update, or rewrite fluid ingredient to a registered honey fluid that exists in-pack |
| `spectrum:titration_barrel/infused_beverages/lager_fluid` | Same `#c:honey` | Same |
| `spectrum:titration_barrel/infused_beverages/mead_fluid` | Same | Same |

### Stack-size / other

| Recipe id | Why | Fix later |
| --- | --- | --- |
| `armageddon_mod:bsotlh_duplication_recipe` | Result stack size 2 > max stack 1 for that item | Upstream Armageddon fix, **or** pack override with `count: 1` (changes balance) |

### Older load-fixes (pre–2026-09-27 audit)

Still disabled the same way (Jaden’s Nether Expansion items never registered):

| Recipe id | Notes |
| --- | --- |
| `netherexp:warphopper_fur_paper` | Unregistered `warphopper_fur` |
| `netherexp:cooking/iron_nugget_from_iron_scrap` | Unregistered `iron_scrap` |
| `netherexp:cooking/iron_nugget_from_iron_scrap_blasting` | Same |
| `netherexp:igneous_reeds_orange_dye` | Unregistered `igneous_reeds` |
| `netherexp:stonecutting/from_pale_soul_slate/indented` | Unregistered `indented_soul_slate_tiles` |

Plus advancement stub: `netherexp/advancement/recipes/misc/warphopper_fur_paper.json`.

---

## Recipe rewrites (not disabled) — keep these

| Recipe id | What we did | When you can delete the override |
| --- | --- | --- |
| `agritechevolved:planter/crop/biomeswevegone/pale_pumkin_seeds` | Typo fix: `pale_pumkin` → `pale_pumpkin` / `pale_pumpkin_seeds` | When Agritech Evolved ships corrected ids (then delete our file) |
| `agritechevolved:planter/crop/biomeswevegone/japanses_orchid` | Typo fix: `japanses_orchid` → `japanese_orchid` | Same |

Files:

- `lead-leylines-load-fixes/data/agritechevolved/recipe/planter/crop/biomeswevegone/pale_pumkin_seeds.json`
- `lead-leylines-load-fixes/data/agritechevolved/recipe/planter/crop/biomeswevegone/japanses_orchid.json`

---

## Emptied loot tables (39 from audit + older Mek/ExtendedAE set)

Path prefix: `pack/global_packs/required_data/lead-leylines-orphan-loot/data/`.

### 2026-09-27 audit batch

| Loot table id | Missing / bad item (from log) | Fix later |
| --- | --- | --- |
| `arsdelight:blocks/dawnberry_crate` | `arsdelight:dawnberry_crate` | Ars Delight build that registers dawnberry/lightchee blocks, **or** add whatever soft-dep those items need |
| `arsdelight:blocks/dawnberry_jelly` | `arsdelight:dawnberry_jelly` | Same |
| `arsdelight:blocks/dawnberry_pie` | `arsdelight:dawnberry_pie_slice` (table refs slice) | Same |
| `arsdelight:blocks/lightchee_crate` | `arsdelight:lightchee_crate` | Same |
| `arsdelight:blocks/lightchee_jelly` | `arsdelight:lightchee_jelly` | Same |
| `arsdelight:blocks/lightchee_pie` | `arsdelight:lightchee_pie_slice` | Same |
| `create_connected:blocks/dye_depot_*_fan_dyeing_catalyst` (16 colors: amber, aqua, beige, coral, forest, ginger, indigo, maroon, mint, navy, olive, rose, slate, tan, teal, verdant) | Matching `create_connected:dye_depot_*` items | Install **Dye Depot**, **or** remove Create Connected’s Dye Depot soft content |
| `createcasing:blocks/brass_slicer` | `createcasing:brass_slicer` | Soft-dep metal / Create: Enchanted / etc. that registers those slicers — only re-enable if the block exists |
| `createcasing:blocks/copper_slicer` | `createcasing:copper_slicer` | Same |
| `createcasing:blocks/creative_slicer` | `createcasing:creative_slicer` | Same |
| `createcasing:blocks/industrial_iron_slicer` | `createcasing:industrial_iron_slicer` | Same |
| `createcasing:blocks/railway_slicer` | `createcasing:railway_slicer` | Same |
| `createcasing:blocks/refined_radiance_slicer` | `createcasing:refined_radiance_slicer` | Same (often Create: Steam ’n’ Rails / CC&A radiance) |
| `createcasing:blocks/shadow_steel_slicer` | `createcasing:shadow_steel_slicer` | Same |
| `createcasing:blocks/weathered_iron_slicer` | `createcasing:weathered_iron_slicer` | Same |
| `createdieselgenerators:blocks/andesite_girder_strut` | `createdieselgenerators:andesite_girder_strut` | CDG update that registers the block |
| `farmers_spell:rewards/foodgeist_satisfied` | `irons_spellbooks:ink_epic` | Iron’s Spellbooks id rename / Farmers Spell update |
| `spawn:archaeology/anthill` | `spawn:roly_poly` | Spawn update that registers roly poly |
| `unusualend:blocks/celestial_fluid` | `unusualend:celestial_fluid` | Unusual End update |
| `unusualend:blocks/warped_endstone_sprouts` | `unusualend:warped_endstone_sprouts` | Unusual End update |

Four `twilightdelight:blocks/{aurora,glacier,phytochemical,torchberry}_cake` tables were also emptied in this batch because the matching `twilightdelight:*_cake_slice` items never registered. **Removed 2026-10-04** — Neapolitan 6.0.1 makes them register, so the `minecraft:empty` overrides are deleted and the cakes drop their slices again.

### Older orphan-loot (still present)

Do not delete these unless you add the soft-dep mods:

- `mekmm` dense/overclocked/quantum/multiversal/creative factory block loot (Evolved Mekanism tiers)
- `mekanism_extras` absolute/cosmic/infinite/supreme chemical-infusing factory loot
- `extendedae:blocks/ex_emc_interface` (ProjectE)

See short summary in [configs.md](configs.md) “Orphan loot tables”.

---

## Other pack changes in the same pass

### Removed: Apothic Category Compat

| | |
| --- | --- |
| Was | `pack/mods/apothic-category-compat.pw.toml` → `apothic_compat-2.0.2.jar` (CurseForge 1516278) |
| Why | `data/apotheosis/data_maps/item/loot_category_overrides.json` hard-coded absent `alexscaves:*`, `cataclysm:*`, `undergarden:slingshot` → DataMapLoader ERROR every boot |
| Kept in datapack | `lead-leylines-load-fixes/data/apotheosis/data_maps/item/loot_category_overrides.json` with only in-pack bows: `born_in_chaos_v1:pumpkinhandgun`, `twilightforest:block_and_chain`, `twilightforest:cube_of_annihilation`. The two `alexsmobs:*` entries were dropped on 2026-10-04 when Alex's Mobs left the pack; they were the same class of dead reference this row exists to prevent, and NeoForge's `DataMapLoader` logged an ERROR for each one every boot. |
| Lost with jar | Affix blacklist config (`apothic_compat-common.toml` / `/ac reload`) — use Apotheosis datapacks if you need that again |
| Deferred note | [deferred.md](deferred.md) |
| Re-add? | Only if upstream drops soft-dep rows **or** those mods join the pack |

### Blueprint `modid:example`

| | |
| --- | --- |
| Attempt | `lead-leylines-load-fixes/data/blueprint/data_maps/dimension/modded_biome_slice_sizes.json` with `"values": {}` + `"remove": ["modid:example"]` |
| Result | Jar still logs one DataMapLoader ERROR when Blueprint attaches the placeholder; datapack cannot silence that without editing/removing Blueprint |
| Fix later | Blueprint upstream removes the example entry |

### Docs / catalog touched

- `CHANGELOG.md` `[Unreleased]` Fixed bullets
- `docs/mods/configs.md`, `manifest.md`, `deferred.md`
- `docs/installed/catalog.toml` (+ regenerated markdown/json)
- `pack/index.toml` via `packwiz refresh`
- Smoke audit follow-ups: [2026-09-27T063607Z-audit.md](../smoke-runs/2026-09-27T063607Z-audit.md)

### Still open (not overridden)

From the same audit — not silenced by datapack:

- Patchouli BetterEnd / BetterNether books (`use_resource_pack` false)
- KubeJS `mbtool` plugin ClassNotFound
- My Nether’s Delight `minersdelight:cup_variant` WARN (Miner's Delight not installed)
- Mass `Entity … has no attributes` log noise (now includes `neapolitan:chimpanzee` and `neapolitan:plantain_spider`; this is the normal pack-wide pattern, roughly 470 lines, not a Neapolitan defect)
- Optional mixin soft-deps (Copycats+, Scorched Guns, FramedBlocks, AE2LT, …)

### Broken tags still logging (2026-10-04)

LMFT 1.1.1+1.21.9 mixes into `TagLoader.tryBuildTag`, so it logs entries that fail to resolve and then reports `It seems that some tags are a bit cooked` instead of letting the tag throw. Installing Neapolitan cleared three of the seven. Four remain, in descending order of value:

| Tag (as LMFT prints it) | Real file | Bad entries | Fix |
| --- | --- | --- | --- |
| `blueprint:generates_overrides` | `data/blueprint/tags/trim_material/generates_overrides.json` (Unusual End 2.3.1b) | `prismalite_gem`, `shiny_crystal`, `citrine_chunk`, `pearlescent_ingot` | **Real fix available, not yet applied.** Blueprint 8.2.0 declares this a `TagKey<TrimMaterial>` — the 1.21.9 *registry* tag — but Unusual End writes plain item IDs. Unusual End does ship the correct registry entries: `unusualend:citrine_material`, `pearlescent_material`, `prismatic_material`, `shiny_material`. A 4-line datapack file with `"replace": true` and those IDs is the whole fix; single contributor, so the snapshot risk is nil. |
| `farmersdelight:pies` | `data/farmersdelight/tags/block/pies.json` (Ars Delight 2.2.2) | `arsdelight:dawnberry_pie`, `arsdelight:lightchee_pie` | Same root cause as the emptied `arsdelight:blocks/dawnberry_pie` loot table above — those two blocks never register. Needs an Ars Delight build that registers them. A `"replace": true` restating the 9 valid entries (4 Farmer's Delight + 5 Ars Delight) would silence it at the cost of a 2-contributor snapshot. |
| `minecraft:rabbit_food` | `data/minecraft/tags/item/rabbit_food.json` (Pam's Harvest Crops 1.0.9) | `pamhc2crops:_blackberryitem` | **Upstream typo, leave it.** The jar literally contains `"pamhc2crops: blackberryitem"` — a space where the `:` belongs. Not worth a 58-entry snapshot of a vanilla tag to add one berry to rabbit food. |
| `apothic_pointblank:gun/small_arms` | `data/apothic_pointblank/tags/item/gun/small_arms.json` | `pointblank:mk23` | Stale tag: Point Blank 2.2.0 has no `mk23` id at all. Harmless; a 46-entry snapshot to drop one line is not worth it. |

Also worth knowing: LMFT's in-game error can be silenced without touching any of this, either with `-Dlmft.disable_error_output=true` in `pack/user_jvm_args.txt` or `"disableIngameError": true` in its generated config. That only hides the chat message and the summary ERROR — the WARN lines stay in `latest.log`.

---

## Suggested restore order

1. **Safe content adds:** ~~Neapolitan~~ **done 2026-10-04** (CurseForge 382016 / 7119475). Still open: Dye Depot (Create Connected fan catalysts), AE2LT / Extended Terminal (Universal Press recipes) — each needs a normal mod research + install approval.
2. **Upstream waits:** Unusual End Delight/cutting recipes, TF DNV tables, Create Shimmer castle doors, Create Deco placard, CBC-AT moulds/fuzing, Spectrum honey titration, Armageddon stack-2, Jaden fungus rolls, CDG girder strut, Spawn roly poly, Unusual End block loot.
3. **Do not re-add casually:** Apothic Category Compat, Evolved Mekanism / ProjectE just to clear old orphan loot.
4. **Cheap real fix, not yet applied:** the `blueprint:trim_material/generates_overrides` override in the table above. It is a genuine Blueprint/Unusual End wiring bug, it is 4 lines, and it has no snapshot downside — unlike the other three.
