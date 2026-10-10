# join-test

Mineflayer bot that logs into the local smoke-test server and times the join
phases (`loginMs`, `spawnMs`). This is the join-sync measurement that
`scripts/smoke_test.py` cannot do on its own — see `docs/TODO.md`.

Not part of the pack. Never add anything from here to `pack/mods/`.

## Setup (once)

```sh
cd scripts/join-test && npm install
```

## Use

1. Start the dedicated server manually (`smoke_test.py` stops its server when
   done, so for a join test run the work tree directly):
   ```sh
   cd dist/_smoke-test && bash run.sh
   ```
   Wait for `Done (...)!`, and note the `server-port` in
   `dist/_smoke-test/server.properties`.
2. Run the bot while the server is up:
   ```sh
   node scripts/join-test/join-test.mjs 127.0.0.1 <port>
   ```
   Prints one JSON line, e.g.
   `{"ok":true,...,"loginMs":1234,"spawnMs":5678}`. Exit 0 on spawn, 1 on
   kick/error/timeout (kick reason included — useful when the modded handshake
   rejects the vanilla-protocol bot).
3. Stop the server (`stop` in its console).

`JOIN_TEST_TIMEOUT_MS` overrides the 120 s spawn timeout.

## Verdict 2026-10-10: vanilla-protocol bots cannot join

Ran against the real pack server (NeoForge 21.1.252): the bot is rejected in
the configuration phase with
`neoforge.network.negotiation.failure.vanilla.client.not_supported` — the
server requires a NeoForge handshake the bot cannot speak, so no login, no
spawn, no join-sync timing. The old `node-minecraft-protocol-forge` plugin only
implements the pre-1.13 FML handshake and does not apply. The harness still
works as a connection-level check (it reports kick reasons cleanly), but real
join measurement needs a real client: HeadlessMc under Xvfb (Linux), or
in-world fake players (which skip the login sync itself).
