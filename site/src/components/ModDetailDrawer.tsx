"use client";

import { ExternalLink } from "lucide-react";

import { monogram, sideLabel } from "@/lib/format";
import type { EnrichedMod } from "@/lib/types";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";
import { ScrollArea } from "@/components/ui/scroll-area";

type Props = {
  mod: EnrichedMod | null;
  open: boolean;
  onOpenChange: (open: boolean) => void;
  tagVocabulary: Record<string, string>;
  onTagClick?: (tag: string) => void;
};

export function ModDetailDrawer({
  mod,
  open,
  onOpenChange,
  tagVocabulary,
  onTagClick,
}: Props) {
  return (
    <Sheet open={open} onOpenChange={onOpenChange}>
      <SheetContent side="right" className="p-0">
        {mod ? (
          <>
            <SheetHeader>
              <p className="font-mono text-[10px] uppercase tracking-[0.2em] text-muted">
                Artifact field inspection
              </p>
              <SheetTitle className="text-2xl text-primary-bright">{mod.name}</SheetTitle>
              <SheetDescription>{mod.blurb || mod.summary || "No description."}</SheetDescription>
            </SheetHeader>
            <ScrollArea className="flex-1 px-4 py-4">
              <div className="flex items-start gap-4">
                {mod.iconUrl ? (
                  // eslint-disable-next-line @next/next/no-img-element
                  <img
                    src={mod.iconUrl}
                    alt=""
                    className="h-16 w-16 rounded border border-card-border object-cover"
                  />
                ) : (
                  <div className="flex h-16 w-16 items-center justify-center rounded border border-card-border bg-accent-soft font-display text-lg font-semibold text-primary">
                    {monogram(mod.name)}
                  </div>
                )}
                <div className="space-y-2">
                  <div className="flex flex-wrap gap-2">
                    <Badge variant={mod.side === "both" ? "moss" : "muted"}>
                      {sideLabel(mod.side)}
                    </Badge>
                    <Badge variant="outline">{mod.category_title}</Badge>
                    <Badge variant="default">{mod.source}</Badge>
                  </div>
                  <p className="text-sm text-muted">
                    Group: <span className="text-foreground">{mod.group}</span>
                  </p>
                </div>
              </div>

              <div className="mt-6">
                <h3 className="font-mono text-[11px] uppercase tracking-wider text-muted">
                  Overview
                </h3>
                <p className="mt-2 text-sm leading-relaxed text-foreground/90">
                  {mod.summary || mod.blurb || "No longer description available."}
                </p>
              </div>

              <div className="mt-6">
                <h3 className="font-mono text-[11px] uppercase tracking-wider text-muted">Tags</h3>
                <div className="mt-2 flex flex-wrap gap-2">
                  {mod.tags.map((tag) => (
                    <button
                      key={tag}
                      type="button"
                      title={tagVocabulary[tag]}
                      onClick={() => onTagClick?.(tag)}
                      className="rounded border border-card-border bg-chip px-2 py-1 font-mono text-[11px] text-secondary hover:border-secondary"
                    >
                      #{tag}
                    </button>
                  ))}
                </div>
              </div>

              <div className="mt-8 space-y-2 border-t border-card-border pt-4 font-mono text-xs text-muted">
                <div>
                  Filename: <span className="text-foreground">{mod.filename}</span>
                </div>
                <div>
                  Pack file: <span className="text-foreground">{mod.file}</span>
                </div>
                <div>
                  Kind: <span className="text-foreground">{mod.kind}</span> · Folder:{" "}
                  <span className="text-foreground">{mod.folder}</span>
                </div>
              </div>

              {mod.storeUrl ? (
                <div className="mt-6 pb-6">
                  <Button asChild className="w-full">
                    <a href={mod.storeUrl} target="_blank" rel="noreferrer">
                      View on store
                      <ExternalLink className="h-4 w-4" />
                    </a>
                  </Button>
                </div>
              ) : null}
            </ScrollArea>
          </>
        ) : null}
      </SheetContent>
    </Sheet>
  );
}
