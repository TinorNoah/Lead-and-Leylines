---
name: minecraft-modding
description: Use this skill whenever the user wants to add, remove, update, or troubleshoot Minecraft mods, mod packs, or a modded instance (Forge, Fabric, NeoForge, or Quilt). Trigger it any time a mod name, a modpack, a launcher instance, or terms like "mod loader", "crash log", "mods folder", or "modrinth/curseforge" come up — even if the user just says "add X mod" without asking for a full workflow. Make sure to use this skill before installing, downloading, or recommending any Minecraft mod, since skipping the compatibility and dependency checks here is the single biggest cause of broken modded instances.
---

# Minecraft Modding

A workflow for safely adding mods to a Minecraft instance — covering necessity, compatibility, conflicts, dependencies, documentation, and rollback. The goal is a modded instance that boots cleanly and stays reproducible, not just a mod that got downloaded.

## Core principle

**Never just download and drop a jar in.** Every mod addition is a small change to a fragile, interdependent system (loader version + Minecraft version + every other mod's dependencies). Treat it like a dependency-managed install, not a file copy.

**Optimize for a stable, coherent modpack, not for mod count.** Every installed mod should have a clear purpose and a documented justification. When in doubt, defer rather than install.

**Optimize for reproducibility.** Pin exact mod versions and exact download sources, record the exact loader version, and keep the manifest synchronized with what's actually in the `mods/` folder. If someone can't look at the manifest six months from now and reconstruct the exact working combination, the documentation has failed at its job.

**Never upgrade the ecosystem to accommodate a mod, without separate approval.** If a candidate mod needs a newer Minecraft version, loader version, or a newer build of a shared dependency (e.g. Fabric API) than what's installed, do not silently perform that upgrade as part of adding the mod. Present the ecosystem upgrade as its own proposed change, with its own compatibility assessment, and get it approved separately — a one-mod request can otherwise cascade into a 20-mod compatibility problem.

**The decision chain is four distinct gates, not two:** need confirmation → technical assessment → recommendation → installation approval. Don't collapse "does the user want this" into the same moment as "does the user approve installing this specific researched, vetted mod" — they're different questions asked at different points with different information available.

## Step 0 — Establish the instance context (do this before anything else)

Before evaluating any mod, confirm or infer:
- **Minecraft version** (e.g. 1.20.1, 1.21.4)
- **Mod loader** (Forge, NeoForge, Fabric, or Quilt) and its loader version
- **Launcher** (CurseForge app, Modrinth App, Prism, MultiMC, vanilla launcher) — affects where files live and how updates are tracked
- Whether this is a **client**, a **dedicated server**, or both need to match

If any of this is unknown, ask the user rather than guessing — a mod that's correct for 1.20.1 Fabric will crash on 1.21 Forge. If the user has an existing `mods/` folder or modpack manifest, read it first to infer the above instead of asking.

## Step 1 — Confirm the mod is actually needed

Don't add a mod just because it was named. Check with the user:
- What problem/feature are they trying to solve? Sometimes the answer is "that's vanilla behavior" or "a config change/datapack does this without a mod."
- Is there already a mod in the instance that covers this (avoid redundant/overlapping mods, e.g. two ore-doubling mods)?
- Is this a hard requirement or a "nice to have"? This affects how much conflict risk is acceptable.

If the fit is unclear or marginal, that's a signal for **Step 7 (defer to a "future mods" list)** rather than installing now.

## Step 2 — Research the mod itself

For each candidate mod, gather:
1. **Source legitimacy**: verify the official project page, a known/identifiable author, an explicit build for the target Minecraft version and loader, and recent maintenance activity, from a reputable distribution source (Modrinth, CurseForge, or the author's own official channel). Download count alone is not a quality or security signal — don't rely on it. Avoid random jar links or unofficial mirrors, which are the main malware vector in modding.
2. **Maintenance status**: when was it last updated? Is there a build for the target Minecraft version and loader? An abandoned mod on an old MC version is a common source of silent breakage or exploits.
3. **Side (client/server/both)**: check the mod page's environment tag. This determines whether it goes in the client's `mods/` folder only, the server's only, or both. Getting this wrong causes join errors ("mod X is present on client but not server" or vice versa).
4. **Role/category**: what does it actually do? (e.g. optimization, tech, magic, QoL, world-gen, library). Useful for the doc and for spotting redundancy.
5. **Dependencies — split by necessity, not lumped together**:
   - **Required**: the mod will not load without these. Every one of these must be identified and installed alongside it.
   - **Optional**: the mod loads fine without them but a feature is disabled/degraded (e.g. an optional integration with another mod for cross-mod compatibility).
   - **Recommended**: not dependencies in the technical sense, but companion mods the author suggests for the intended experience (e.g. a config-GUI mod, a performance companion).
   Treating an optional dependency as required bloats the install; missing a genuinely required one causes crash-on-launch — so get the category right, not just the list.
6. **Ecosystem compatibility**: does this mod require a newer Minecraft version, loader version, or newer build of a shared dependency (e.g. Fabric API, Forge) than what's currently installed? If so, this is not a config detail — flag it explicitly as a separate proposed ecosystem upgrade (see Core Principle above) rather than folding it into this mod's install.
7. **Config requirements**: check whether the mod needs any config changes to work correctly or to avoid conflicts:
   - Does it generate a config file on first launch that needs editing (e.g. to disable a feature that overlaps with another installed mod, adjust spawn rates, toggle a recipe)?
   - Does it require changes to an *existing* mod's config to resolve a conflict (e.g. disabling one mod's ore-gen so it doesn't fight another's)?
   - Is there a server-side config that must match (or intentionally differ from) the client config?
   - Are there recommended non-default settings the community/author calls out (e.g. "set X to false or it'll lag on large servers")?
   If config changes are needed, note the exact file and setting — don't just say "may need configuring."
8. **Performance implications**: does the mod add significant tick load, memory use, or rendering cost? Is it known to cause lag at scale (large servers, many players, big builds)? Note this especially for mods that touch entities, particle effects, lighting, or run per-tick logic.
9. **World-data and persistent-state impact**: does the mod add or remove blocks, items, entities, or dimensions, or otherwise write persistent data into the world save? Mods in this category are the hardest to safely remove later (removing a block-adding mod can corrupt chunks that used its blocks), so flag this explicitly as a factor in the recommendation, not just a backup trigger.
10. **Removability**: if this mod is added and later needs to come out, can it be cleanly uninstalled? Note anything that would make removal risky (world-gen mods, mods that convert vanilla data, mods with no clean uninstall path) so this is a known trade-off before installing, not a surprise afterward.
11. **License and attribution requirements**: check the mod's license (e.g. MIT, LGPL, "All Rights Reserved," a custom CurseForge/Modrinth license). Note whether it requires: crediting the author by name if the modpack is shared/distributed, linking back to the original mod page, or explicit permission from the author before including it in a distributed modpack at all (common for "All Rights Reserved" mods). If the instance is private/personal-use only, attribution is still good practice to document; if the modpack will be shared or published, treat unmet license requirements as a blocker, not an afterthought.

## Step 3 — Check for conflicts

Cross-reference the candidate mod against the current mod list for:
- **Known incompatibilities** stated on the mod's page (many authors explicitly list these).
- **Overlapping functionality** with an installed mod (e.g. two mods that both modify the same recipe system, or two optimization mods that touch the same rendering pipeline — like Sodium/Rubidium or Optifine).
- **Loader/version mismatches** among dependencies (a dependency that only supports an older loader version than what's installed).
- **Mixin conflicts** — if crash logs are available from a past attempt, check for mixin injection errors, which usually mean two mods patch the same code location.

If a real conflict is found, tell the user clearly: what conflicts, why, and the options (skip it, find an alternative mod, or accept the risk knowingly). If the only real "conflict" is that the mod needs a newer ecosystem version, treat that per the Core Principle above — a separate proposed upgrade, not an automatic side effect of this install. Log it in the manifest's "Deferred Ecosystem Upgrades" section if it isn't approved right away.

## Step 4 — Present the recommendation and get approval

Before installing anything, present each proposed mod as a clear recommendation covering:
- What it does, and why it's needed
- Why this mod specifically was selected (vs. alternatives, if any were considered)
- Client / server / both
- Its role in the modpack
- Dependencies
- Known conflicts
- Configuration requirements
- Performance implications
- World-compatibility / persistent-data implications
- Removability trade-offs
- License and attribution requirements (and whether they're already satisfied)

**Do not install until the user approves this recommendation** — unless the user has already given explicit standing authorization to auto-install mods matching defined criteria (e.g. "any Modrinth-listed optimization mod compatible with our loader, no approval needed"). If no such standing authorization exists, treat approval as a required checkpoint, not a formality to rush past.

## Step 5 — Back up before installing

Before touching the instance:
- Back up the `mods/` folder (or note the exact modpack version if using a manager).
- Back up the world save if the mod touches world generation, save data, or is otherwise not safely removable later (see Step 2's removability assessment).
- Note the current working state so there's a known-good point to roll back to.

## Step 6 — Install and verify

1. **Re-verify the exact version before downloading.** Confirm the specific mod version/build number that matches the researched and approved Minecraft version + loader combination — don't grab "latest" by default, since a newer build may have shipped between research and install that targets a different Minecraft/loader version or pulls in an ecosystem upgrade. Record the exact version and download source used.
2. Add the mod (and all its **required** dependencies — see Step 2's required/optional/recommended split) to the correct location(s) per the client/server determination in Step 2. Make only the changes required for this mod — don't bundle in unrelated upgrades, unrequested mod updates, or other modifications while you're in there, since that makes it harder to isolate what caused a problem later.
3. Launch once to let the mod generate its default config file(s), then apply any config changes identified in Step 2 (both to the new mod's config and to any existing mod's config that needs adjusting to avoid conflicts) — and only those changes.
4. Launch the instance again (or have the user do so) and check the outcome:
   - Clean boot → good.
   - Crash → read the crash report/log, identify the failing mod, and diagnose (usually: missing dependency, version mismatch, missing config change, or genuine conflict).
5. If this is a client/server setup, verify the client can actually connect to the server after the change, not just that each launches independently.
6. Verify the dependencies loaded correctly (visible in the mod list in-game or in the log) and test the specific functionality that motivated the install in the first place (Step 1) — don't just confirm it boots.
7. Pay particular attention to mods that modify world generation or add/remove blocks, items, entities, or dimensions: check that existing chunks/saves still load correctly and nothing already placed is missing or broken.
8. Don't declare success until there's an actual clean launch confirmation, working connectivity (if applicable), and confirmed functionality with the intended config applied — "I added the file" is not the same as "it works as intended."

## Step 7 — Update the mod list documentation

Maintain a running, structured mod manifest (see `references/mod-manifest-template.md`) rather than an informal list. For every mod actually installed, record:
- Name, **exact pinned version/build**, Minecraft version, loader, and **exact download source** (URL/page) used — enough to redownload the identical file later, not just "latest as of install."
- Side: client / server / both
- Category/role (e.g. "optimization", "tech mod", "QoL")
- Why it was chosen (1–2 lines) — especially useful if there was a runner-up considered and rejected
- **Dependencies, split into Required / Optional / Recommended** (see Step 2) — not a flat list
- **Config changes required** — exact file + setting(s) changed, and why (e.g. "config/modname.toml: disable_worldgen=true — avoids conflict with X's ore-gen"). If no config changes were needed, note that explicitly so it's not re-checked later.
- Date added

After updating, **confirm the manifest matches what's actually in the `mods/` folder** — a manifest that's drifted from reality (missing an entry, or listing a mod that got removed without updating the doc) defeats the point of keeping one. This sync check matters more the longer the instance has been running.

Also maintain a **Credits / Attribution** section (see the manifest template) crediting every mod author per that mod's license terms — required reading before sharing or publishing the modpack anywhere, not just a courtesy.

For mods that came up but weren't a fit right now, add them to a **"Future / Deferred Mods"** section in the same doc with a short note on why (e.g. "not compatible with current loader version yet," "overlaps with X until X is replaced," "nice-to-have, revisit if performance allows") and what would change that (e.g. "revisit once we drop mod X" or "revisit if a NeoForge port ships"). This avoids re-litigating the same mod later and gives the user a running wishlist.

## Step 8 — Communicate back to the user

Summarize plainly:
- What was added and why
- Client/server/both
- What it depends on
- Any conflicts found and how they were handled (or avoided by choosing an alternative)
- What got deferred to the future list and why

## Rollback

If a mod causes problems after being accepted as "working" (discovered later, e.g. a world corruption or performance regression):
1. Remove the mod. **Before removing any of its dependencies, check the manifest's Required/Optional/Recommended records for every other installed mod** — a dependency only comes out if no other installed mod still requires it. Removing a shared dependency out from under another mod just trades one crash for another.
2. Refer back to the removability assessment from Step 2 — mods flagged there as hard to cleanly remove may need a save restore rather than a simple uninstall.
3. Restore the pre-install backup if the issue is save-related.
4. Update the manifest to reflect the removal (and any dependency removals) and note why, so it isn't re-added blindly later.

## Reference files

- `references/mod-manifest-template.md` — the structured doc template used in Step 7, including the "Future/Deferred" section format.
- `references/this-pack.md` — Lead and Leylines packwiz mapping. Read after Step 0.
