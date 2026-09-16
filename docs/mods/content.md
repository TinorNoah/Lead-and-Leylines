# Magic, tech, dimension, and QoL — considered, chosen, dropped

Research snapshot: 2026-09-16. Target is whatever Minecraft + Forge are in [`pack/pack.toml`](../../pack/pack.toml). Re-check store pages before a file bump.

**Status:** combat/magic cut **installed** (2026-09-16). Distant Horizons is **off** until the player enables it. No extra EMI addon jar — AE2 15.4.10 has native EMI; Ars, Supplementaries, Waystones, Twilight Forest, and Lootr ship their plugins in-jar. Polymorph stays on 0.49.10 because 0.49.11 fails next to TMRV's JEI stub. EMI Loot was not added; Fzzy Config is in only as Simply Swords’ library. Ice and Fire is **Community Edition**, not the original AlexThe666 jar.

## Side (packwiz)

| `side` | Meaning |
|---|---|
| `client` | Prism / player instance only. Dedicated server must not require it. |
| `both` | Must run in singleplayer’s integrated server **and** on the dedicated server. |

## Decision rules

1. Distant Horizons stays **client** and **renderer off** (`rendererMode = "DISABLED"`, no distant generation). Floor quality is only a safety net if someone turns it on. Do not put DH on the dedicated server. Launcher Java 17 uses `-XX:+UseZGC` from `pack/user_jvm_args.txt` (DH's G1 warning). Prism sync writes it into `instance.cfg`; other launchers still need that flag in Java settings.
2. One recipe browser (EMI). Do not add JEI for AE2. Do not add EMI Loot unless loot-table pages are requested.
3. Official Twilight Forest CurseForge file only. Do not add the Modrinth “Unofficial” port.
4. FancyMenu + Drippy is the menu/loading stack. No custom title art unless chosen on purpose. FancyMenu must not customize Create / AE2 / Xaero / Supplementaries / Twilight Forest screens (upstream blocks those packages). When we start custom layouts, use [FancyMenu docs (en-US home)](https://docs.fancymenu.net/docs/en-US/home).
5. Default Options is how the pack unbinds FTB Chunks **Open Map**. Ship `keybindings.txt` only. Do not ship a full `options.txt`.
6. Ice and Fire is [Community Edition](https://www.curseforge.com/minecraft/mc-mods/iceandfire-ce). Do not also install the original [Ice and Fire](https://modrinth.com/mod/ice-and-fire-dragons) jar — they share a mod id and CE warns that swapping on an existing save corrupts it. New worlds can start on CE.

## Chosen

| Mod | Project | `side` | Why add |
|---|---|---|---|
| Distant Horizons | [modrinth.com/mod/distanthorizons](https://modrinth.com/mod/distanthorizons) `3.2.0-b` (`FWGxbEM3`) | client | Optional LOD view. **Beta.** Off by default. Oculus 1.8.0 already claims DH 2.2+ shader support. Java 17: `pack/user_jvm_args.txt` (`-XX:+UseZGC`). |
| Ars Nouveau | [modrinth.com/mod/ars-nouveau](https://modrinth.com/mod/ars-nouveau) `4.12.7` (`Hw2aD01e`) | both | Spellcraft. Planned magic line. |
| Patchouli | [modrinth.com/mod/patchouli](https://modrinth.com/mod/patchouli) `1.20.1-85` (`94dtOLgZ`) | both | Ars (and other) books |
| Applied Energistics 2 | [modrinth.com/mod/ae2](https://modrinth.com/mod/ae2) `15.4.10` (`7KVs6HMQ`) | both | Storage network. Native EMI in this file. |
| GuideME | [modrinth.com/mod/guideme](https://modrinth.com/mod/guideme) `20.1.15` (`i7Tp1AHw`) | both | Required by AE2 15.4 |
| Twilight Forest | CurseForge file `5468648` (`4.3.2508`) | both | Adventure dimension. Official jar. |
| Supplementaries | [modrinth.com/mod/supplementaries](https://modrinth.com/mod/supplementaries) `3.1.43` (`S0TIJ1hU`) | both | Vanilla-plus blocks/items |
| Moonlight Lib | [modrinth.com/mod/moonlight](https://modrinth.com/mod/moonlight) `2.16.35` (`W0ZWjZib`) | both | Supplementaries + Target Dummy |
| Waystones | [modrinth.com/mod/waystones](https://modrinth.com/mod/waystones) `14.1.21` (`Y0IgdaoP`) | both | Public warps. Homes stay FTB Essentials. |
| Lootr | [modrinth.com/mod/lootr](https://modrinth.com/mod/lootr) `0.7.35.94` (`mWTXC1ZX`) | both | Per-player dungeon loot. Does not replace Sophisticated Storage. |
| MmmMmmMmmMmm | [modrinth.com/mod/mmmmmmmmmmmm](https://modrinth.com/mod/mmmmmmmmmmmm) `1.20-2.0.12-forge` (`c1HMqDvI`) | both | Target dummy for combat testing |
| Polymorph | [modrinth.com/mod/polymorph](https://modrinth.com/mod/polymorph) `0.49.10` (`UZBKtFyR`) | both | Overlapping recipes (FD / Create / AE2 / Ars). Do not bump to 0.49.11 while TMRV stubs JEI 15.20.0.132. |
| Crafting Tweaks | [modrinth.com/mod/crafting-tweaks](https://modrinth.com/mod/crafting-tweaks) `18.2.9` (`KOqT9kSZ`) | both | Crafting-grid buttons |
| Nether Portal Fix | [modrinth.com/mod/netherportalfix](https://modrinth.com/mod/netherportalfix) `13.0.1` (`cWPAnu7u`) | both | Return-portal linking |
| TrashSlot | [modrinth.com/mod/trashslot](https://modrinth.com/mod/trashslot) `15.1.5` (`r0K8IYd7`) | both | Inventory trash. Different from FTB `/trashcan`. |
| Balm | [modrinth.com/mod/balm](https://modrinth.com/mod/balm) `7.3.43` (`1VlYVa3k`) | both | Blay library |
| Controlling | [modrinth.com/mod/controlling](https://modrinth.com/mod/controlling) `12.0.2` (`LH6Bi6Am`) | client | Searchable keybinds |
| Searchables | [modrinth.com/mod/searchables](https://modrinth.com/mod/searchables) `1.0.3` (`PM9yAW1G`) | client | Required by Controlling |
| Mouse Tweaks | [modrinth.com/mod/mouse-tweaks](https://modrinth.com/mod/mouse-tweaks) `2.25.1` (`7JVXOe3K`) | client | Inventory mouse drag |
| Better Advancements | [modrinth.com/mod/better-advancements](https://modrinth.com/mod/better-advancements) `0.6.0.73` (`zKOCnRdK`) | client | Advancement UI |
| FancyMenu | [modrinth.com/mod/fancymenu](https://modrinth.com/mod/fancymenu) `3.9.12` (`ucAaUjAE`) | client | Menu framework for Drippy. No custom title pack yet. |
| Drippy Loading Screen | [modrinth.com/mod/drippy-loading-screen](https://modrinth.com/mod/drippy-loading-screen) `3.1.5` (`Nof419YS`) | client | Loading overlay. Needs FancyMenu. |
| Konkrete | [modrinth.com/mod/konkrete](https://modrinth.com/mod/konkrete) `1.8.0` (`skYziQQL`) | client | FancyMenu / Drippy library |
| Melody | [modrinth.com/mod/melody](https://modrinth.com/mod/melody) `1.0.3` (`lJlW5r8R`) | client | FancyMenu 3.9 library |
| Default Options | [modrinth.com/mod/default-options](https://modrinth.com/mod/default-options) `18.0.5` (`AVz3mvZZ`) | client | Pack default keybind: FTB Open Map unbound |
| Amendments | [modrinth.com/mod/amendments](https://modrinth.com/mod/amendments) `1.20-2.2.6` (`nJORWvdh`) | both | Supplementaries 3.x moved wall lanterns, skull candles, ceiling pots/banners, skull piles here. Moonlight already in. |
| Trash Cans | [modrinth.com/mod/trash-cans](https://modrinth.com/mod/trash-cans) `1.1.0a` (`iiNJsz5q`) | both | Placeable item/fluid/energy voids. Not TrashSlot. Needs Core Lib + Config Lib. |
| SuperMartijn642's Core Lib | [modrinth.com/mod/supermartijn642s-core-lib](https://modrinth.com/mod/supermartijn642s-core-lib) `1.1.24a` (`Rty5QRB6`) | both | Required by Trash Cans |
| SuperMartijn642's Config Lib | [modrinth.com/mod/supermartijn642s-config-lib](https://modrinth.com/mod/supermartijn642s-config-lib) `1.1.8` (`ZKor79dR`) | both | Required by Trash Cans |
| IceAndFire Community Edition | CurseForge file `8757817` (`1.2.8`) | both | Dragons and mythical creatures. Needs Jupiter + Uranus (not Citadel). Citadel stays for Alex's Caves. |
| Jupiter | CurseForge file `7738299` (`2.3.7`) | both | CE config library |
| Uranus | CurseForge file `7745532` (`2.2.6-bugfix.2`) | both | CE animation/util library |
| [TaCZ] Timeless and Classics Zero | [modrinth.com/mod/timeless-and-classics-zero](https://modrinth.com/mod/timeless-and-classics-zero) `1.1.8-hotfix` (`yOVIzIJR`) | both | Official gun mod. Default pack is in this jar. |
| LesRaisins Tactical Equipements | [modrinth.com/mod/lr-tactical](https://modrinth.com/mod/lr-tactical) `0.4.3` (`eygQmqIl`) | both | TACZ throwables/melee support. Needs TACZ 1.1.8. |
| LesRaisins Append Pack | [modrinth.com/mod/lesraisins-weapon](https://modrinth.com/mod/lesraisins-weapon) `0.3.0` (`KbReepVU`) | both | Extra LesRaisins guns |
| Gucci & Vuitton Attachments | [modrinth.com/mod/tacz-gucci-vuitton-attachments](https://modrinth.com/mod/tacz-gucci-vuitton-attachments) `0.2.2` (`NnUWhMdw`) | both | Extra TACZ attachments |
| Daffa's Arsenal | [modrinth.com/mod/daffasarsenal](https://modrinth.com/mod/daffasarsenal) `3.7.1.1` (`1Q9ypxVQ`) | both | Large extra TACZ gun pack |
| AppleSkin | [modrinth.com/mod/appleskin](https://modrinth.com/mod/appleskin) `2.5.1+mc1.20.1` (`XdXDExVF`) | both | Hunger/saturation HUD. Official squeek502. `both` so saturation syncs. |
| NeoAuth | [modrinth.com/mod/neoauth](https://modrinth.com/mod/neoauth) `1.0.3` (`9xLXbEMY`) | client | Microsoft session re-login in the multiplayer screen. Auth Me’s Forge port. Not a cracked-server login mod. |
| Legendary Tooltips | [modrinth.com/mod/legendary-tooltips](https://modrinth.com/mod/legendary-tooltips) `1.4.5` (`JhxD2e6J`) | client | Rarity frames. Needs Iceberg + Prism lib. |
| Iceberg | [modrinth.com/mod/iceberg](https://modrinth.com/mod/iceberg) `1.1.25` (`BQ8rJPXV`) | client | Grend library for Legendary Tooltips / Equipment Compare |
| Prism | [modrinth.com/mod/prism-lib](https://modrinth.com/mod/prism-lib) `1.0.5` (`FFyss87M`) | client | Color helper for Legendary Tooltips (not the launcher) |
| Equipment Compare | [modrinth.com/mod/equipment-compare](https://modrinth.com/mod/equipment-compare) `1.3.7` (`x1lxEKIp`) | client | Shift-compare gear. Needs Iceberg. |
| Simply Swords | [modrinth.com/mod/simply-swords](https://modrinth.com/mod/simply-swords) `1.70.2` (`Na6e94J1`) | both | Extra weapon types. Lootr-safe loot inject in this file. |
| Fzzy Config | [modrinth.com/mod/fzzy-config](https://modrinth.com/mod/fzzy-config) `0.7.7` (`53kg5uoF`) | both | Required by Simply Swords 1.70. Kotlin for Forge already in. Not EMI Loot. |
| Simply Tooltips | [modrinth.com/mod/simply-tooltips](https://modrinth.com/mod/simply-tooltips) `0.1.5` (`s87jNabF`) | client | Required by Simply Swords 1.70 |
| Simply More | [modrinth.com/mod/simplymore](https://modrinth.com/mod/simplymore) `1.1.4` (`u4dfPRHB`) | both | Holdover so Simply More does not crash on Simply Swords 1.70 |
| Better Combat | [modrinth.com/mod/better-combat](https://modrinth.com/mod/better-combat) `1.9.0` (`rnhiaw3t`) | both | Melee animations. Guns stay TACZ. |
| playerAnimator | [modrinth.com/mod/playeranimator](https://modrinth.com/mod/playeranimator) `1.0.2-rc1` (`xe2EVE6q`) | both | Required by Better Combat |
| Ice and Fire Dragons X Better Combat | [modrinth.com/mod/ice-and-fire-dragons-x-better-combat](https://modrinth.com/mod/ice-and-fire-dragons-x-better-combat) `1.0` (`d5Vp1w6z`) | both | IAF weapons under Better Combat |
| Alex's Caves Better Combat | [modrinth.com/mod/alexs-caves-better-combat](https://modrinth.com/mod/alexs-caves-better-combat) `1.0` (`25y1lqsO`) | both | Alex's Caves weapons under Better Combat |
| Ars Elemental | CurseForge file `8399870` (`1.20.1-0.6.8.0`) | both | Elemental foci/glyphs for Ars Nouveau 4.12.7. CurseForge only. |

Geckolib and Curios were already in (Ars). Citadel stays for Alex's Caves.

## Dropped / skipped this cut

| Asked as | Outcome |
|---|---|
| EMI Loot | **Skipped.** Optional loot-table pages. Needs Fzzy Config. AE2/Ars/etc. already show recipes in EMI. |
| Extra Mod Integrations (EMI) | **Skipped.** No Forge 1.20.1 file. |
| Twilight Forest Unofficial (Modrinth) | **Dropped.** Official CurseForge `4.3.2508`. |
| JEI (for AE2) | **Skipped.** EMI is the viewer. AE2 15.4.10 has native EMI. |
| Polymorph `0.49.11` (`5lNATnbO`) | **Held.** Only change vs 0.49.10 is a JEI 15.57+ recipe-transfer API. TMRV 0.9.0 provides `jei` at 15.20.0.132, so Forge aborts. Revisit if TMRV bumps that stub on 1.20.1. |
| DH on the dedicated server | **Skipped.** LOD gen on the server is the same class of hitch as `/rtp`. |
| FancyMenu custom title art | **Held.** Framework only until a layout is chosen. Docs: https://docs.fancymenu.net/docs/en-US/home |
| Ice and Fire (original `2.1.13-1.20.1-beta-5`) | **Dropped.** Community Edition replaces it. Do not install both. |
| Maxstuff / Elite X Quality Guns / more random TACZ packs | **Held.** LesRaisins + Gucci + Daffa is the extra-pack set. More packs overlap IDs and quality. |
| Better Combat Particle / Better Mob Combat | **Skipped.** Not requested. Player Better Combat is in. |
| Auth Me / AuthAgain | **Skipped.** Auth Me is Fabric-only; AuthAgain duplicates NeoAuth. |

## Configs worth documenting

| Mod | Why a pack note |
|---|---|
| Distant Horizons | `pack/config/DistantHorizons.toml`: renderer off, distant gen off. Options → DH to enable. |
| Default Options | `pack/config/defaultoptions/keybindings.txt` unbinds `key.ftbchunks.map`. Existing instances that already saved **M** keep that bind — unbind once in Controls if it still fights Xaero. |
| AE2 / Ars / Twilight Forest / Supplementaries / Waystones | Worldgen and blocks. New chunks for meteors, Archwood, TF overworld portals, village waystones. TF dimension still works on the current world. |
| Lootr | Converts loot-table chests. Player-placed Sophisticated Storage is unchanged. |
| IceAndFire CE / TACZ / Simply Swords / Ars Elemental / Amendments / Trash Cans | World data. New chunks for dragon roosts and IAF structures. Guns, weapons, elemental blocks, and trash cans stay in the save if removed. Existing Supplementaries worlds keep wall lanterns only with Amendments. |
| Legendary Tooltips / Equipment Compare / AppleSkin | If hover frames or the hunger overlay glitch, disable ImmediatelyFast `hud_batching`. |
