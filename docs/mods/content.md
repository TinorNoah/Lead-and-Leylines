# Magic, tech, dimension, and QoL — considered, chosen, dropped

Research snapshot: 2026-09-16. Target is whatever Minecraft + Forge are in [`pack/pack.toml`](../../pack/pack.toml). Re-check store pages before a file bump.

**Status:** this cut **installed** (2026-09-16). Distant Horizons is **off** until the player enables it. No extra EMI addon jar — AE2 15.4.10 has native EMI; Ars, Polymorph, Supplementaries, Waystones, Twilight Forest, and Lootr ship their plugins in-jar. EMI Loot (needs Fzzy Config) was not added.

## Side (packwiz)

| `side` | Meaning |
|---|---|
| `client` | Prism / player instance only. Dedicated server must not require it. |
| `both` | Must run in singleplayer’s integrated server **and** on the dedicated server. |

## Decision rules

1. Distant Horizons stays **client** and **renderer off** (`rendererMode = "DISABLED"`, no distant generation). Floor quality is only a safety net if someone turns it on. Do not put DH on the dedicated server.
2. One recipe browser (EMI). Do not add JEI for AE2. Do not add EMI Loot unless loot-table pages are requested.
3. Official Twilight Forest CurseForge file only. Do not add the Modrinth “Unofficial” port.
4. FancyMenu + Drippy is the menu/loading stack. No custom title art unless chosen on purpose. FancyMenu must not customize Create / AE2 / Xaero / Supplementaries / Twilight Forest screens (upstream blocks those packages).
5. Default Options is how the pack unbinds FTB Chunks **Open Map**. Ship `keybindings.txt` only. Do not ship a full `options.txt`.

## Chosen

| Mod | Project | `side` | Why add |
|---|---|---|---|
| Distant Horizons | [modrinth.com/mod/distanthorizons](https://modrinth.com/mod/distanthorizons) `3.2.0-b` (`FWGxbEM3`) | client | Optional LOD view. **Beta.** Off by default. Oculus 1.8.0 already claims DH 2.2+ shader support. |
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
| Polymorph | [modrinth.com/mod/polymorph](https://modrinth.com/mod/polymorph) `0.49.11` (`5lNATnbO`) | both | Overlapping recipes (FD / Create / AE2 / Ars). EMI plugin in-jar. |
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

Geckolib and Curios were already in (Ars).

## Dropped / skipped this cut

| Asked as | Outcome |
|---|---|
| EMI Loot | **Skipped.** Optional loot-table pages. Needs Fzzy Config. AE2/Ars/etc. already show recipes in EMI. |
| Extra Mod Integrations (EMI) | **Skipped.** No Forge 1.20.1 file. |
| Twilight Forest Unofficial (Modrinth) | **Dropped.** Official CurseForge `4.3.2508`. |
| JEI (for AE2) | **Skipped.** EMI is the viewer. AE2 15.4.10 has native EMI. |
| DH on the dedicated server | **Skipped.** LOD gen on the server is the same class of hitch as `/rtp`. |
| FancyMenu custom title art | **Held.** Framework only until a layout is chosen. |

## Configs worth documenting

| Mod | Why a pack note |
|---|---|
| Distant Horizons | `pack/config/DistantHorizons.toml`: renderer off, distant gen off. Options → DH to enable. |
| Default Options | `pack/config/defaultoptions/keybindings.txt` unbinds `key.ftbchunks.map`. Existing instances that already saved **M** keep that bind — unbind once in Controls if it still fights Xaero. |
| AE2 / Ars / Twilight Forest / Supplementaries / Waystones | Worldgen and blocks. New chunks for meteors, Archwood, TF overworld portals, village waystones. TF dimension still works on the current world. |
| Lootr | Converts loot-table chests. Player-placed Sophisticated Storage is unchanged. |
