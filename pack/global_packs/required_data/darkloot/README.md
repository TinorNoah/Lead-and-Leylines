# DarkLoot

Vendored from CurseForge datapack [DarkLoot - Change mob loot drops](https://www.curseforge.com/minecraft/data-packs/darkloot-datapack) (`1446380`), file `darkloot_datapack_1.21.x.zip`.

Edit loot under `data/minecraft/loot_table/entities/*.json` (item id, weight, count). Defaults are generous (guaranteed heads; buffed drops).

Pack fixes vs upstream zip:
- `pack_format` 48 for Minecraft 1.21.1 (upstream still said 15)
- `magma_cube.json` uses `minecraft:enchanted_count_increase` (upstream still had removed `looting_enchant`)
