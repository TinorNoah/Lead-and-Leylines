export function monogram(name: string): string {
  const cleaned = name.replace(/[\[\]\|]/g, " ").trim();
  const parts = cleaned.split(/\s+/).filter(Boolean);
  if (parts.length === 0) return "?";
  if (parts.length === 1) return parts[0]!.slice(0, 2).toUpperCase();
  return `${parts[0]![0] ?? ""}${parts[1]![0] ?? ""}`.toUpperCase();
}

export function sideLabel(side: string): string {
  if (side === "client") return "client";
  if (side === "server") return "server";
  return "both";
}
