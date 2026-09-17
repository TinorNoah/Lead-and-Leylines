# Config notes (necessary only)

Defaults are the pack unless a row below says otherwise. Do not dump every mod’s full config into git.

Minecraft, loader, and pack version: see [`pack/pack.toml`](../../pack/pack.toml).

| Mod | Touch? | Note |
|---|---|---|
| Java 21 JVM flags | Pack overlay | `pack/user_jvm_args.txt` (`-XX:+UseZGC`). `python scripts/update_prism.py` copies those flags into Prism `instance.cfg`. Dedicated NeoForge uses `server/run.sh`. Mrpack/CurseForge cannot auto-apply launcher JVM args. Do not add `-XX:+ZGenerational`. |
