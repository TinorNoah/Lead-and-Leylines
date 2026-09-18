# Config notes (necessary only)

Defaults are the pack unless a row below says otherwise. Do not dump every mod’s full config into git.

Minecraft, loader, and pack version: see [`pack/pack.toml`](../../pack/pack.toml).

| Mod | Touch? | Note |
|---|---|---|
| Java 21 JVM flags | Pack overlay | `pack/user_jvm_args.txt` (`-XX:+UseZGC`). `python scripts/update_prism.py` copies those flags into Prism `instance.cfg`. Dedicated NeoForge uses `server/run.sh`. Mrpack/CurseForge cannot auto-apply launcher JVM args. Do not add `-XX:+ZGenerational`. |
| Sodium Extra + More Culling | After first boot | Both can simplify/cull leaves. Disable Extra’s reduced-leaves option **or** More Culling’s leaf culling so they do not stack. Do not add Sodium Leaf Culling, OptiLeaves, or Chloride. |
| Create: Threaded Trains | Defaults | Offloads train calculation. Create addons that patch trains can freeze; test trains before adding those addons. |
| FTB Quests Optimizer | Defaults | File `3.2.0` is older than FTB Quests `2101.1.36`. If quest ticks misbehave, remove the optimizer first. |
| Bye?Pregen! | Defaults | Do not re-add Noisium or AntiXRay. Do not add FastNoise if RTF is later added. Chunk Pregenerator stays for operator pregen. |
| Lithostitched | Defaults | Regions Unexplored's eight `in_structure` placed features are overridden by `pack/global_packs/required_data/lead-leylines-ru-in-structure/`. Do not remove that datapack while RU and Lithostitched are both in. |
| Global Packs | `pack/config/global_packs.toml` | `config_version = 3` (jar default). `datapacks.required` includes `global_packs/required_data/`. `enable_system_global_packs` stays false. Unpacked datapack only; packwiz ignores `*.zip`. |
| Tectonic | Defaults | Dedicated NeoForge logs `Couldn't load fabric:overlays metadata` / unknown `tectonic:config`. The `tectonic` datapack still loads; that overlay path is Fabric resource-conditions noise. |
| Terralith | `pack/config/terralith.json` | `modules.terrain_slabs = false` so Terralith's overlay does not stack slabs with Countered's Terrain Slabs. Skylands stay on. Feature Recycler is the feature-order-cycle fix, not this toggle. |
| Feature Recycler | Defaults | Required while Terralith and Oh The Biomes We've Gone are both in. Server-logic, so packwiz `both`. |
| Cerulean | Defaults | Do not re-add Achievements Optimizer. |
