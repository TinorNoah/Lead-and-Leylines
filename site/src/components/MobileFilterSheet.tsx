"use client";

import { Drawer } from "vaul";

import { FilterSidebar } from "@/components/FilterSidebar";
import { Button } from "@/components/ui/button";
import type { CatalogCategory } from "@/lib/types";

type Props = {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  resultCount: number;
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
  onReset: () => void;
};

export function MobileFilterSheet(props: Props) {
  const { open, onOpenChange, resultCount, onReset, ...filterProps } = props;

  return (
    <Drawer.Root open={open} onOpenChange={onOpenChange}>
      <Drawer.Portal>
        <Drawer.Overlay className="fixed inset-0 z-50 bg-black/60" />
        <Drawer.Content className="fixed inset-x-0 bottom-0 z-50 flex max-h-[88vh] flex-col rounded-t-lg border border-card-border bg-card-elevated outline-none">
          <div className="mx-auto mt-3 h-1.5 w-12 rounded-full bg-card-border" />
          <div className="flex items-center justify-between px-4 pb-2 pt-3">
            <Drawer.Title className="font-display text-xl text-primary">
              Filter Ley-Vault
            </Drawer.Title>
            <button
              type="button"
              className="font-mono text-xs text-secondary underline"
              onClick={onReset}
            >
              Reset
            </button>
          </div>
          <div className="overflow-y-auto px-4 pb-4">
            <FilterSidebar {...filterProps} className="border-0 bg-transparent p-0" />
          </div>
          <div className="border-t border-card-border p-4">
            <Button className="w-full" onClick={() => onOpenChange(false)}>
              Show {resultCount} matching mods
            </Button>
          </div>
        </Drawer.Content>
      </Drawer.Portal>
    </Drawer.Root>
  );
}
