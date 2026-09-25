"use client";

import Fuse from "fuse.js";
import { useMemo, useState } from "react";
import { usePathname, useRouter, useSearchParams } from "next/navigation";

import type { CatalogCategory, EnrichedMod } from "@/lib/types";
import { ModCard } from "@/components/ModCard";
import { ModTable } from "@/components/ModTable";
import { TagChip } from "@/components/TagChip";

type Props = {
  mods: EnrichedMod[];
  categories: CatalogCategory[];
  tagVocabulary: Record<string, string>;
};

type ViewMode = "cards" | "grouped";

function parseList(value: string | null): string[] {
  if (!value) return [];
  return value
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);
}

export function CatalogBrowser({ mods, categories, tagVocabulary }: Props) {
  const router = useRouter();
  const pathname = usePathname();
  const searchParams = useSearchParams();

  const query = searchParams.get("q") ?? "";
  const selectedTags = parseList(searchParams.get("tags"));
  const selectedCategory = searchParams.get("category") ?? "";
  const selectedSide = searchParams.get("side") ?? "";
  const view = (searchParams.get("view") as ViewMode) || "cards";

  const [draftQuery, setDraftQuery] = useState(query);

  const fuse = useMemo(
    () =>
      new Fuse(mods, {
        keys: [
          { name: "name", weight: 0.45 },
          { name: "blurb", weight: 0.25 },
          { name: "tags", weight: 0.2 },
          { name: "filename", weight: 0.1 },
        ],
        threshold: 0.35,
        ignoreLocation: true,
      }),
    [mods],
  );

  const filtered = useMemo(() => {
    let list = mods;
    if (query.trim()) {
      list = fuse.search(query.trim()).map((result) => result.item);
    }
    if (selectedCategory) {
      list = list.filter((mod) => mod.category === selectedCategory);
    }
    if (selectedSide) {
      list = list.filter((mod) => mod.side === selectedSide);
    }
    if (selectedTags.length > 0) {
      list = list.filter((mod) => selectedTags.every((tag) => mod.tags.includes(tag)));
    }
    return list;
  }, [mods, fuse, query, selectedCategory, selectedSide, selectedTags]);

  const tagCounts = useMemo(() => {
    const counts = new Map<string, number>();
    for (const mod of mods) {
      for (const tag of mod.tags) {
        counts.set(tag, (counts.get(tag) || 0) + 1);
      }
    }
    return [...counts.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));
  }, [mods]);

  function updateParams(mutate: (params: URLSearchParams) => void) {
    const params = new URLSearchParams(searchParams.toString());
    mutate(params);
    const next = params.toString();
    router.replace(next ? `${pathname}?${next}` : pathname, { scroll: false });
  }

  function toggleTag(tag: string) {
    updateParams((params) => {
      const current = parseList(params.get("tags"));
      const next = current.includes(tag)
        ? current.filter((item) => item !== tag)
        : [...current, tag];
      if (next.length === 0) params.delete("tags");
      else params.set("tags", next.join(","));
    });
  }

  const grouped = useMemo(() => {
    const byCategory = new Map<string, Map<string, EnrichedMod[]>>();
    for (const mod of filtered) {
      if (!byCategory.has(mod.category)) byCategory.set(mod.category, new Map());
      const groups = byCategory.get(mod.category)!;
      if (!groups.has(mod.group)) groups.set(mod.group, []);
      groups.get(mod.group)!.push(mod);
    }
    return categories
      .filter((category) => byCategory.has(category.slug))
      .map((category) => ({
        category,
        groups: [...(byCategory.get(category.slug)?.entries() || [])].map(([name, items]) => ({
          name,
          mods: items,
        })),
      }));
  }, [filtered, categories]);

  return (
    <div className="mx-auto grid w-full max-w-7xl gap-6 px-4 pb-16 pt-6 lg:grid-cols-[260px_minmax(0,1fr)]">
      <aside className="space-y-5 rounded-2xl border border-card-border bg-card/80 p-4 backdrop-blur">
        <div>
          <label className="mb-2 block text-xs uppercase tracking-[0.2em] text-muted">
            Search
          </label>
          <form
            onSubmit={(event) => {
              event.preventDefault();
              updateParams((params) => {
                if (draftQuery.trim()) params.set("q", draftQuery.trim());
                else params.delete("q");
              });
            }}
          >
            <input
              value={draftQuery}
              onChange={(event) => setDraftQuery(event.target.value)}
              placeholder="tacz, boss, create…"
              className="w-full rounded-xl border border-card-border bg-background px-3 py-2 text-sm outline-none ring-accent focus:ring-2"
            />
          </form>
        </div>

        <div>
          <div className="mb-2 text-xs uppercase tracking-[0.2em] text-muted">Category</div>
          <div className="flex max-h-56 flex-col gap-1 overflow-auto pr-1">
            <button
              type="button"
              onClick={() =>
                updateParams((params) => {
                  params.delete("category");
                })
              }
              className={`rounded-lg px-2 py-1.5 text-left text-sm ${
                !selectedCategory ? "bg-accent-soft text-accent" : "hover:bg-chip"
              }`}
            >
              All categories
            </button>
            {categories.map((category) => (
              <button
                key={category.slug}
                type="button"
                onClick={() =>
                  updateParams((params) => {
                    params.set("category", category.slug);
                  })
                }
                className={`rounded-lg px-2 py-1.5 text-left text-sm ${
                  selectedCategory === category.slug
                    ? "bg-accent-soft text-accent"
                    : "hover:bg-chip"
                }`}
              >
                {category.title}
              </button>
            ))}
          </div>
        </div>

        <div>
          <div className="mb-2 text-xs uppercase tracking-[0.2em] text-muted">Side</div>
          <div className="flex flex-wrap gap-2">
            {["", "both", "client", "server"].map((side) => (
              <button
                key={side || "any"}
                type="button"
                onClick={() =>
                  updateParams((params) => {
                    if (!side) params.delete("side");
                    else params.set("side", side);
                  })
                }
                className={`rounded-full px-3 py-1 text-xs ${
                  selectedSide === side
                    ? "bg-accent text-background"
                    : "bg-chip text-muted hover:text-foreground"
                }`}
              >
                {side || "any"}
              </button>
            ))}
          </div>
        </div>

        <div>
          <div className="mb-2 flex items-center justify-between text-xs uppercase tracking-[0.2em] text-muted">
            <span>Tags</span>
            {selectedTags.length > 0 && (
              <button
                type="button"
                className="normal-case tracking-normal text-accent"
                onClick={() =>
                  updateParams((params) => {
                    params.delete("tags");
                  })
                }
              >
                clear
              </button>
            )}
          </div>
          <div className="flex max-h-72 flex-wrap gap-2 overflow-auto">
            {tagCounts.slice(0, 60).map(([tag, count]) => (
              <TagChip
                key={tag}
                tag={tag}
                count={count}
                active={selectedTags.includes(tag)}
                title={tagVocabulary[tag]}
                onClick={() => toggleTag(tag)}
              />
            ))}
          </div>
        </div>
      </aside>

      <section className="space-y-4">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div className="text-sm text-muted">
            Showing <span className="text-foreground">{filtered.length}</span> of {mods.length}{" "}
            mods
            {selectedTags.length > 0 && (
              <span> · tags: {selectedTags.join(", ")}</span>
            )}
          </div>
          <div className="flex gap-2">
            {(["cards", "grouped"] as ViewMode[]).map((mode) => (
              <button
                key={mode}
                type="button"
                onClick={() =>
                  updateParams((params) => {
                    params.set("view", mode);
                  })
                }
                className={`rounded-full px-3 py-1 text-xs capitalize ${
                  view === mode ? "bg-accent text-background" : "bg-chip text-muted"
                }`}
              >
                {mode}
              </button>
            ))}
          </div>
        </div>

        {view === "cards" ? (
          <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-3">
            {filtered.map((mod) => (
              <ModCard key={mod.file} mod={mod} />
            ))}
          </div>
        ) : (
          <div className="space-y-8">
            {grouped.map(({ category, groups }) => (
              <div key={category.slug} className="space-y-4">
                <div>
                  <h2 className="text-xl font-semibold text-foreground">{category.title}</h2>
                  <p className="mt-1 text-sm text-muted">{category.intro}</p>
                </div>
                {groups.map((group) => (
                  <ModTable key={`${category.slug}-${group.name}`} title={group.name} mods={group.mods} />
                ))}
              </div>
            ))}
          </div>
        )}

        {filtered.length === 0 && (
          <div className="rounded-2xl border border-dashed border-card-border p-10 text-center text-muted">
            No mods match these filters.
          </div>
        )}
      </section>
    </div>
  );
}
