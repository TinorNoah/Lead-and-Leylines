# CurseForge-first distribution

"No third-party distribution" is a CurseForge author setting. It means **this pack must not ship the author's jar inside our zip**. CurseForge will still give players that jar when the pack lists the project and file IDs, because CurseForge itself fetches the file and the author's setting is respected.

`packwiz curseforge export` only references a mod that way when the `.pw.toml` has an `[update.curseforge]` block with a real `project-id` and `file-id`. CurseForge then fetches the file. That block is written by `packwiz curseforge install` (alias `packwiz cf install`).

A mod installed with `packwiz modrinth install` (or a bare `[download]` URL) does **not** get `[update.curseforge]`. At CurseForge-export time packwiz embeds that jar under `overrides/mods/` in the zip. **That embed is the actual violation** of "no third-party distribution", not merely "the mod is also on Modrinth."

That is why every install tries CurseForge first, even if you found the mod on Modrinth. A slug miss is not proof it is absent: retry with `--addon-id` / `--file-id` before falling back.

It is fine and expected to use Modrinth as a **mod source** when the mod is genuinely not on CurseForge. That has nothing to do with whether this pack is published to the Modrinth store.

Do not assume a `.pw.toml` exported cleanly. Verify and fix with:

- `python scripts/check_exports.py <client.zip> <pack.mrpack>` after an export
- `python scripts/detect_curseforge.py` as a manual pass over mods that were added without CurseForge metadata
