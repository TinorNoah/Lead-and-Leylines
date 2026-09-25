"use client";

import Fuse from "fuse.js";
import { LayoutGrid, List, Rows3, Search, SlidersHorizontal } from "lucide-react";
import { useEffect, useMemo, useRef, useState } from "react";
import { usePathname, useRouter, useSearchParams } from "next/navigation";

import type { CatalogCategory, EnrichedMod } from "@/lib/types";
import { FilterSidebar } from "@/components/FilterSidebar";
import { MobileFilterSheet } from "@/components/MobileFilterSheet";
import { ModCard } from "@/components/ModCard";
import { ModDetailDrawer } from "@/components/ModDetailDrawer";
import { ModList } from "@/components/ModList";
import { ModTable } from "@/components/ModTable";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { cn } from "@/lib/utils";

type Props = {
  mods: EnrichedMod[];
  categories: CatalogCategory[];
  tagVocabulary: Record<string, string>;
};

type ViewMode = "cards" | "list" | "grouped";

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
  const selectedModFile = searchParams.get("mod") ?? "";

  const [draftQuery, setDraftQuery] = useState(query);
  const [tagQuery, setTagQuery] = useState("");
  const [mobileFiltersOpen, setMobileFiltersOpen] = useState(false);
  const searchRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    setDraftQuery(query);
  }, [query]);

  useEffect(() => {
    function onKeyDown(event: KeyboardEvent) {
      if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") {
        event.preventDefault();
        searchRef.current?.focus();
      }
    }
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, []);

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

  const categoryCounts = useMemo(() => {
    const counts = new Map<string, number>();
    for (const mod of mods) {
      counts.set(mod.category, (counts.get(mod.category) || 0) + 1);
    }
    return counts;
  }, [mods]);

  const selectedMod = useMemo(
    () => mods.find((mod) => mod.file === selectedModFile) ?? null,
    [mods, selectedModFile],
  );

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

  function updateParams(mutate: (params: URLSearchParams) => void) {
    const params = new URLSearchParams(searchParams.toString());
    mutate(params);
    const next = params.toString();
    router.replace(next ? `${pathname}?${next}` : pathname, { scroll: false });
  }

  function setSearch(value: string) {
    updateParams((params) => {
      if (value.trim()) params.set("q", value.trim());
      else params.delete("q");
    });
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

  function openMod(mod: EnrichedMod) {
    updateParams((params) => {
      params.set("mod", mod.file);
    });
  }

  function resetFilters() {
    updateParams((params) => {
      params.delete("category");
      params.delete("side");
      params.delete("tags");
      params.delete("q");
    });
    setDraftQuery("");
    setTagQuery("");
  }

  const filterProps = {
    categories,
    categoryCounts,
    selectedCategory,
    selectedSide,
    selectedTags,
    tagCounts,
    tagVocabulary,
    tagQuery,
    onTagQueryChange: setTagQuery,
    onCategory: (slug: string) =>
      updateParams((params) => {
        if (!slug) params.delete("category");
        else params.set("category", slug);
      }),
    onSide: (side: string) =>
      updateParams((params) => {
        if (!side) params.delete("side");
        else params.set("side", side);
      }),
    onToggleTag: toggleTag,
    onClearTags: () =>
      updateParams((params) => {
        params.delete("tags");
      }),
  };

  const hasFilters = Boolean(selectedCategory || selectedSide || selectedTags.length || query);

  return (
    <div className="mx-auto w-full max-w-[1560px] px-4 pb-16 pt-4 sm:px-6 lg:px-8">
      <form
        className="sticky top-0 z-20 -mx-4 mb-5 border-b border-card-border/60 bg-background px-4 py-3 sm:-mx-6 sm:px-6 lg:-mx-8 lg:px-8"
        onSubmit={(event) => {
          event.preventDefault();
          setSearch(draftQuery);
        }}
      >
        <div className="relative">
          <Search className="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted" />
          <Input
            ref={searchRef}
            value={draftQuery}
            onChange={(event) => setDraftQuery(event.target.value)}
            placeholder="Search mods, tags, bosses…"
            className="h-12 pl-10 pr-24 text-base"
          />
          <kbd className="pointer-events-none absolute right-3 top-1/2 hidden -translate-y-1/2 rounded border border-card-border bg-chip px-2 py-0.5 font-mono text-[10px] text-muted sm:inline">
            ⌘K
          </kbd>
        </div>
      </form>

      <div className="grid gap-6 lg:grid-cols-[280px_minmax(0,1fr)]">
        <div className="hidden lg:block">
          <FilterSidebar {...filterProps} />
        </div>

        <section className="space-y-4">
          <div className="flex flex-wrap items-center justify-between gap-3">
            <div className="text-sm text-muted">
              Showing <span className="font-mono text-foreground">{filtered.length}</span> of{" "}
              <span className="font-mono text-foreground">{mods.length}</span> mods
              {hasFilters ? (
                <button
                  type="button"
                  className="ml-3 text-secondary hover:underline"
                  onClick={resetFilters}
                >
                  Clear filters
                </button>
              ) : null}
            </div>
            <div className="flex items-center gap-2">
              <Button
                type="button"
                variant="outline"
                size="sm"
                className="lg:hidden"
                onClick={() => setMobileFiltersOpen(true)}
              >
                <SlidersHorizontal className="h-4 w-4" />
                Filters
              </Button>
              <div className="flex rounded border border-card-border bg-[#111a18] p-0.5">
                {(
                  [
                    ["cards", LayoutGrid, "Cards"],
                    ["list", List, "List"],
                    ["grouped", Rows3, "Grouped"],
                  ] as const
                ).map(([mode, Icon, label]) => (
                  <button
                    key={mode}
                    type="button"
                    title={label}
                    onClick={() =>
                      updateParams((params) => {
                        params.set("view", mode);
                      })
                    }
                    className={cn(
                      "inline-flex items-center gap-1.5 rounded px-2.5 py-1.5 text-xs font-semibold",
                      view === mode
                        ? "bg-primary text-primary-foreground"
                        : "text-muted hover:text-foreground",
                    )}
                  >
                    <Icon className="h-3.5 w-3.5" />
                    <span className="hidden sm:inline">{label}</span>
                  </button>
                ))}
              </div>
            </div>
          </div>

          {view === "cards" ? (
            <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-3">
              {filtered.map((mod) => (
                <ModCard
                  key={mod.file}
                  mod={mod}
                  selected={selectedModFile === mod.file}
                  onOpen={openMod}
                />
              ))}
            </div>
          ) : null}

          {view === "list" ? (
            <ModList mods={filtered} selectedFile={selectedModFile} onOpen={openMod} />
          ) : null}

          {view === "grouped" ? (
            <div className="space-y-10">
              {grouped.map(({ category, groups }) => (
                <div key={category.slug} className="space-y-6">
                  <div>
                    <h2 className="font-display text-2xl font-semibold text-primary">
                      {category.title}
                    </h2>
                    <p className="mt-1 text-sm text-muted">{category.intro}</p>
                  </div>
                  {groups.map((group) => (
                    <ModTable
                      key={`${category.slug}-${group.name}`}
                      title={group.name}
                      mods={group.mods}
                      selectedFile={selectedModFile}
                      onOpen={openMod}
                    />
                  ))}
                </div>
              ))}
            </div>
          ) : null}

          {filtered.length === 0 ? (
            <div className="rounded border border-dashed border-card-border p-10 text-center text-muted">
              No mods match these filters.
            </div>
          ) : null}
        </section>
      </div>

      <ModDetailDrawer
        mod={selectedMod}
        open={Boolean(selectedMod)}
        onOpenChange={(open) => {
          if (!open) {
            updateParams((params) => {
              params.delete("mod");
            });
          }
        }}
        tagVocabulary={tagVocabulary}
        onTagClick={(tag) => {
          toggleTag(tag);
          updateParams((params) => {
            params.delete("mod");
          });
        }}
      />

      <MobileFilterSheet
        open={mobileFiltersOpen}
        onOpenChange={setMobileFiltersOpen}
        resultCount={filtered.length}
        onReset={resetFilters}
        {...filterProps}
      />
    </div>
  );
}
