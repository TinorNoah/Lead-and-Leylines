"use client";

import { Input } from "@/components/ui/input";
import { ScrollArea } from "@/components/ui/scroll-area";
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group";
import { TagChip } from "@/components/TagChip";
import { cn } from "@/lib/utils";
import type { CatalogCategory } from "@/lib/types";

type Props = {
  categories: CatalogCategory[];
  categoryCounts: Map<string, number>;
  selectedCategory: string;
  selectedSide: string;
  selectedTags: string[];
  tagCounts: Array<[string, number]>;
  tagVocabulary: Record<string, string>;
  tagQuery: string;
  onTagQueryChange: (value: string) => void;
  onCategory: (slug: string) => void;
  onSide: (side: string) => void;
  onToggleTag: (tag: string) => void;
  onClearTags: () => void;
  className?: string;
};

export function FilterSidebar({
  categories,
  categoryCounts,
  selectedCategory,
  selectedSide,
  selectedTags,
  tagCounts,
  tagVocabulary,
  tagQuery,
  onTagQueryChange,
  onCategory,
  onSide,
  onToggleTag,
  onClearTags,
  className,
}: Props) {
  const filteredTags = tagCounts.filter(([tag]) =>
    tag.toLowerCase().includes(tagQuery.trim().toLowerCase()),
  );

  return (
    <aside
      className={cn(
        "flex h-fit flex-col gap-5 rounded border border-card-border bg-card/90 p-4",
        className,
      )}
    >
      <div>
        <div className="mb-2 font-mono text-[10px] uppercase tracking-[0.2em] text-muted">
          Categories
        </div>
        <ScrollArea className="max-h-64 pr-2">
          <div className="flex flex-col gap-1">
            <button
              type="button"
              onClick={() => onCategory("")}
              className={cn(
                "flex items-center justify-between rounded px-2 py-1.5 text-left text-sm",
                !selectedCategory
                  ? "bg-accent-soft text-primary"
                  : "text-foreground hover:bg-chip",
              )}
            >
              <span>All mods</span>
              <span className="font-mono text-[11px] text-muted">
                {[...categoryCounts.values()].reduce((sum, n) => sum + n, 0)}
              </span>
            </button>
            {categories.map((category) => (
              <button
                key={category.slug}
                type="button"
                onClick={() => onCategory(category.slug)}
                className={cn(
                  "flex items-center justify-between rounded px-2 py-1.5 text-left text-sm",
                  selectedCategory === category.slug
                    ? "bg-accent-soft text-primary"
                    : "text-foreground hover:bg-chip",
                )}
              >
                <span className="truncate pr-2">{category.title}</span>
                <span className="font-mono text-[11px] text-muted">
                  {categoryCounts.get(category.slug) ?? 0}
                </span>
              </button>
            ))}
          </div>
        </ScrollArea>
      </div>

      <div>
        <div className="mb-2 font-mono text-[10px] uppercase tracking-[0.2em] text-muted">
          Side
        </div>
        <ToggleGroup
          type="single"
          value={selectedSide || "any"}
          onValueChange={(value) => {
            if (!value || value === "any") onSide("");
            else onSide(value);
          }}
          className="grid grid-cols-4 gap-1 rounded border border-card-border bg-[#111a18] p-1"
        >
          {(["any", "both", "client", "server"] as const).map((side) => (
            <ToggleGroupItem key={side} value={side} className="capitalize">
              {side}
            </ToggleGroupItem>
          ))}
        </ToggleGroup>
      </div>

      <div>
        <div className="mb-2 flex items-center justify-between font-mono text-[10px] uppercase tracking-[0.2em] text-muted">
          <span>Tags</span>
          {selectedTags.length > 0 ? (
            <button
              type="button"
              className="normal-case tracking-normal text-secondary"
              onClick={onClearTags}
            >
              clear
            </button>
          ) : null}
        </div>
        <Input
          value={tagQuery}
          onChange={(event) => onTagQueryChange(event.target.value)}
          placeholder="Filter tag names…"
          className="mb-2 h-9"
        />
        <ScrollArea className="max-h-56">
          <div className="flex flex-wrap gap-2 pr-2">
            {filteredTags.slice(0, 40).map(([tag, count]) => (
              <TagChip
                key={tag}
                tag={tag}
                count={count}
                active={selectedTags.includes(tag)}
                title={tagVocabulary[tag]}
                onClick={() => onToggleTag(tag)}
              />
            ))}
          </div>
        </ScrollArea>
      </div>
    </aside>
  );
}
