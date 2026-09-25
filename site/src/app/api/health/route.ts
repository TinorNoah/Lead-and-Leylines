import { NextResponse } from "next/server";

import { getCatalogSnapshot } from "@/lib/source";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function GET() {
  try {
    const snapshot = await getCatalogSnapshot();
    return NextResponse.json({
      ok: true,
      mod_count: snapshot.catalog.mod_count,
      source: snapshot.source,
      commit: snapshot.commit?.sha ?? null,
      fetchedAt: snapshot.fetchedAt,
    });
  } catch (error) {
    console.error(error);
    return NextResponse.json({ ok: false }, { status: 503 });
  }
}
