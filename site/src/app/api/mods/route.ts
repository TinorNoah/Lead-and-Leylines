import { connection } from "next/server";
import { NextResponse } from "next/server";

import { loadCachedBrowserData } from "@/lib/catalog";

export const runtime = "nodejs";
/** Runtime ISR window; connection() prevents baking empty icons at docker build. */
export const revalidate = 600;

const CACHE_CONTROL = "public, s-maxage=600, stale-while-revalidate=86400";

export async function GET() {
  await connection();
  try {
    const data = await loadCachedBrowserData();
    return NextResponse.json(
      {
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
      },
      {
        headers: {
          "Cache-Control": CACHE_CONTROL,
        },
      },
    );
  } catch (error) {
    console.error(error);
    return NextResponse.json(
      { error: "catalog unavailable" },
      {
        status: 503,
        headers: {
          "Cache-Control": "no-store",
        },
      },
    );
  }
}
