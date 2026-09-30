# CurseForge-first distribution

"No third-party distribution" is a CurseForge author setting. It means **this pack must not ship the author's jar inside our zip**. CurseForge will still give players that jar when the pack lists the project and file IDs, because CurseForge itself fetches the file and the author's setting is respected.

`packwiz curseforge export` only references a mod that way when the `.pw.toml` has an `[update.curseforge]` block with a real `project-id` and `file-id`. CurseForge then fetches the file. That block is written by `packwiz curseforge install` (alias `packwiz cf install`).

A mod installed with `packwiz modrinth install` (or a bare `[download]` URL) does **not** get `[update.curseforge]`. At CurseForge-export time packwiz embeds that jar under `overrides/mods/` in the zip. **That embed is the actual violation** of "no third-party distribution", not merely "the mod is also on Modrinth."

That is why every install tries CurseForge first, even if you found the mod on Modrinth. A slug miss is not proof it is absent: retry with `--addon-id` / `--file-id` before falling back.

It is fine and expected to use Modrinth as a **mod source** when the mod is genuinely not on CurseForge. That has nothing to do with whether this pack is published to the Modrinth store.

## `allowModDistribution = false` — distribution is off, not "just embed it"

Some authors publish to CurseForge with **distribution disabled** (`allowModDistribution: false` in the CurseForge API). CurseForge then refuses to hand the file to third-party tools, and a `.pw.toml` that references `project-id` / `file-id` **breaks installs** for anyone using the pack. The packwiz installer says:

```
<Mod>: This mod is excluded from the CurseForge API and must be downloaded manually.
```

This is the opposite of the rule above. When `allowModDistribution = false`:

- Do **not** reference the project in the manifest. The client install fails.
- Ship the mod from Modrinth (or another direct URL) so packwiz embeds the jar under `overrides/mods/`. That is the only way the mod reaches players at all, and it is the author's own choice to keep the CurseForge listing non-distributable.
- Treat the resulting `overrides/mods/` jar as **expected**, not as a violation to clean up.

Check the flag before assuming a project is usable:

```bash
python3 scripts/lookup_mod.py <slug>   # prints allowModDistribution
```

Verified on 2026-09-30: `library-ferret-neoforge` (522351) and `awesome-dungeon-neoforge` (530465) are both `allowModDistribution = false`, so both are embedded from Modrinth. `aquamirae` (536254) and `mmr-moogs-mineshafts-reimagined` (1570795) are `true` and are manifest references.

Because a manifest reference is only as good as the flag, **an export is not proof that a client install works.** Run the installer against the local Prism instance (`python scripts/update_prism.py`) and confirm it reports "already up to date" instead of an exclusion error.

Do not assume a `.pw.toml` exported cleanly. Verify and fix with:

- `python scripts/check_exports.py <client.zip> <pack.mrpack>` after an export
- `python scripts/detect_curseforge.py` as a manual pass over mods that were added without CurseForge metadata
