/** Chunk helpers for store metadata batch APIs. Exported for unit tests. */

export const MODRINTH_CHUNK_SIZE = 100;
export const CURSEFORGE_CHUNK_SIZE = 1000;

export function chunkIds<T>(ids: T[], size: number): T[][] {
  if (size <= 0) {
    throw new Error("chunk size must be positive");
  }
  const chunks: T[][] = [];
  for (let i = 0; i < ids.length; i += size) {
    chunks.push(ids.slice(i, i + size));
  }
  return chunks;
}

/** Coerce CurseForge project IDs to integers. Strings are rejected by the API. */
export function toCurseForgeModIds(ids: Array<string | number>): number[] {
  const out: number[] = [];
  for (const id of ids) {
    const value = typeof id === "number" ? id : Number(id);
    if (!Number.isInteger(value) || value <= 0) {
      continue;
    }
    out.push(value);
  }
  return out;
}

export function curseforgeRequestBodies(ids: Array<string | number>): Array<{
  modIds: number[];
}> {
  return chunkIds(toCurseForgeModIds(ids), CURSEFORGE_CHUNK_SIZE).map((modIds) => ({
    modIds,
  }));
}

export function modrinthRequestUrls(ids: string[], base = "https://api.modrinth.com/v2"): string[] {
  return chunkIds(ids, MODRINTH_CHUNK_SIZE).map((chunk) => {
    const encoded = encodeURIComponent(JSON.stringify(chunk));
    return `${base}/projects?ids=${encoded}`;
  });
}
