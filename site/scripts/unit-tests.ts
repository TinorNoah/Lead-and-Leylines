import assert from "node:assert/strict";
import { createHmac } from "node:crypto";

import {
  CURSEFORGE_CHUNK_SIZE,
  MODRINTH_CHUNK_SIZE,
  chunkIds,
  curseforgeRequestBodies,
  modrinthRequestUrls,
  toCurseForgeModIds,
} from "../src/lib/chunks.ts";
import { extractPushSha, verifyGitHubSignature } from "../src/lib/webhook.ts";

function testChunks() {
  const modrinth = Array.from({ length: 250 }, (_, i) => `id-${i}`);
  const modrinthChunks = chunkIds(modrinth, MODRINTH_CHUNK_SIZE);
  assert.equal(modrinthChunks.length, 3);
  assert.equal(modrinthChunks[0]?.length, 100);
  assert.equal(modrinthChunks[2]?.length, 50);
  assert.equal(modrinthRequestUrls(modrinth).length, 3);

  const curseIds = Array.from({ length: 1500 }, (_, i) => i + 1);
  const bodies = curseforgeRequestBodies(curseIds);
  assert.equal(bodies.length, 2);
  assert.equal(bodies[0]?.modIds.length, CURSEFORGE_CHUNK_SIZE);
  assert.equal(bodies[1]?.modIds.length, 500);
  assert.ok(bodies.every((body) => body.modIds.every((id) => typeof id === "number")));

  assert.deepEqual(toCurseForgeModIds(["12", 34, "nope", 0, -1, 56.7]), [12, 34]);
}

function testWebhook() {
  const secret = "test-secret";
  const body = JSON.stringify({
    ref: "refs/heads/main",
    after: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  });
  const signature = `sha256=${createHmac("sha256", secret).update(body).digest("hex")}`;
  assert.equal(verifyGitHubSignature(body, signature, secret), true);
  assert.equal(verifyGitHubSignature(body, "sha256=deadbeef", secret), false);
  assert.equal(verifyGitHubSignature(body, "sha256=ab", secret), false);
  assert.equal(verifyGitHubSignature(body, null, secret), false);
  assert.equal(
    extractPushSha(JSON.parse(body), "main"),
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  );
  assert.equal(extractPushSha(JSON.parse(body), "develop"), null);
  assert.equal(
    extractPushSha(
      { ref: "refs/heads/main", after: "0000000000000000000000000000000000000000" },
      "main",
    ),
    null,
  );
}

testChunks();
testWebhook();
console.log("unit tests passed");
