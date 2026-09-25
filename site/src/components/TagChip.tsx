"use client";

import { cn } from "@/lib/utils";

type Props = {
  tag: string;
  count?: number;
  active?: boolean;
  title?: string;
  onClick: () => void;
};

export function TagChip({ tag, count, active, title, onClick }: Props) {
  return (
    <button
      type="button"
      title={title}
      onClick={onClick}
      className={cn(
        "rounded border px-2 py-1 font-mono text-[11px] transition",
        active
          ? "border-primary bg-accent-soft text-primary"
          : "border-card-border bg-chip text-muted hover:border-card-border-active hover:text-foreground",
      )}
    >
      #{tag}
      {typeof count === "number" ? <span className="ml-1 opacity-70">{count}</span> : null}
    </button>
  );
}
