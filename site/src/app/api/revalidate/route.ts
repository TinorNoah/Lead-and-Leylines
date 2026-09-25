import { NextResponse } from "next/server";

import { getCatalogSnapshot } from "@/lib/source";
import { siteConfig } from "@/lib/env";
import { extractPushSha, verifyGitHubSignature } from "@/lib/webhook";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function POST(request: Request) {
  const { revalidateSecret, githubBranch } = siteConfig();
  if (!revalidateSecret) {
    return NextResponse.json({ error: "revalidate disabled" }, { status: 503 });
  }

  const rawBody = await request.text();
  const signature = request.headers.get("x-hub-signature-256");
  if (!verifyGitHubSignature(rawBody, signature, revalidateSecret)) {
    return NextResponse.json({ error: "invalid signature" }, { status: 401 });
  }

  const event = request.headers.get("x-github-event") || "";
  if (event === "ping") {
    return NextResponse.json({ ok: true, event: "ping" });
  }
  if (event !== "push") {
    return NextResponse.json({ ok: true, ignored: event }, { status: 202 });
  }

  let payload: unknown;
  try {
    payload = JSON.parse(rawBody);
  } catch {
    return NextResponse.json({ error: "invalid json" }, { status: 400 });
  }

  const sha = extractPushSha(payload, githubBranch);
  if (!sha) {
    return NextResponse.json({ ok: true, ignored: "branch or sha" }, { status: 202 });
  }

  const snapshot = await getCatalogSnapshot({ force: true, sha });
  return NextResponse.json({
    ok: true,
    sha: snapshot.commit?.sha ?? sha,
    source: snapshot.source,
    mod_count: snapshot.catalog.mod_count,
  });
}
