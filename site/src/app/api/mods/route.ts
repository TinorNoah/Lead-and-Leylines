import { NextResponse } from "next/server";

import { loadBrowserData } from "@/lib/catalog";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function GET() {
  try {
    const data = await loadBrowserData();
    return NextResponse.json({
      pack: data.snapshot.catalog.pack,
      mod_count: data.mods.length,
      tags: data.tags,
      categories: data.snapshot.catalog.categories.map((category) => ({
        slug: category.slug,
        title: category.title,
        intro: category.intro,
      })),
      mods: data.mods,
      commit: data.snapshot.commit,
      source: data.snapshot.source,
      fetchedAt: data.snapshot.fetchedAt,
    });
  } catch (error) {
    console.error(error);
    return NextResponse.json({ error: "catalog unavailable" }, { status: 503 });
  }
}
