"use client";

type Props = {
  tag: string;
  count?: number;
  active?: boolean;
  title?: string;
  onClick?: () => void;
};

export function TagChip({ tag, count, active, title, onClick }: Props) {
  return (
    <button
      type="button"
      title={title}
      onClick={onClick}
      className={`rounded-full border px-2.5 py-1 text-xs transition ${
        active
          ? "border-accent bg-accent-soft text-accent"
          : "border-card-border bg-chip text-muted hover:text-foreground"
      }`}
    >
      {tag}
      {typeof count === "number" && <span className="ml-1 opacity-70">{count}</span>}
    </button>
  );
}
