import { promises as fs } from "node:fs";
import path from "node:path";

import { curseforgeRequestBodies, modrinthRequestUrls } from "./chunks";
import { siteConfig } from "./env";
import type { CatalogMod, ModMetadata } from "./types";

const META_TTL_MS = 24 * 60 * 60 * 1000;
const FETCH_TIMEOUT_MS = 15_000;

type MetaCacheFile = {
  updatedAt: string;
  entries: Record<string, ModMetadata>;
};

type MetaState = {
  cache: MetaCacheFile | null;
  inFlight: Promise<Record<string, ModMetadata>> | null;
};

const globalState = globalThis as typeof globalThis & {
  __llMetaState?: MetaState;
};

function state(): MetaState {
  if (!globalState.__llMetaState) {
    globalState.__llMetaState = { cache: null, inFlight: null };
  }
  return globalState.__llMetaState;
}

function cacheKey(source: string, projectId: string | number): string {
  return `${source}:${projectId}`;
}

async function loadCache(): Promise<MetaCacheFile> {
  const memory = state();
  if (memory.cache) return memory.cache;
  const { dataDir } = siteConfig();
  const filePath = path.join(dataDir, "meta-cache.json");
  try {
    const raw = await fs.readFile(filePath, "utf8");
    const parsed = JSON.parse(raw) as MetaCacheFile;
    memory.cache = {
      updatedAt: parsed.updatedAt || "",
      entries: parsed.entries || {},
    };
    return memory.cache;
  } catch {
    memory.cache = { updatedAt: "", entries: {} };
    return memory.cache;
  }
}

async function saveCache(cache: MetaCacheFile): Promise<void> {
  const { dataDir } = siteConfig();
  try {
    await fs.mkdir(dataDir, { recursive: true });
    const target = path.join(dataDir, "meta-cache.json");
    const temp = `${target}.tmp`;
    await fs.writeFile(temp, JSON.stringify(cache));
    await fs.rename(temp, target);
  } catch (error) {
    console.warn("meta cache write failed", error);
  }
  state().cache = cache;
}

async function fetchWithTimeout(url: string, init: RequestInit = {}): Promise<Response> {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), FETCH_TIMEOUT_MS);
  try {
    return await fetch(url, { ...init, signal: controller.signal, cache: "no-store" });
  } finally {
    clearTimeout(timer);
  }
}

async function fetchCurseForge(
  ids: Array<string | number>,
  apiKey: string,
): Promise<Record<string, ModMetadata>> {
  const out: Record<string, ModMetadata> = {};
  for (const body of curseforgeRequestBodies(ids)) {
    try {
      const response = await fetchWithTimeout("https://api.curseforge.com/v1/mods", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
          "x-api-key": apiKey,
        },
        body: JSON.stringify(body),
      });
      if (!response.ok) {
        console.warn("curseforge batch failed", response.status);
        continue;
      }
      const json = (await response.json()) as {
        data?: Array<{
          id: number;
          summary?: string;
          links?: { websiteUrl?: string };
          logo?: { thumbnailUrl?: string; url?: string };
        }>;
      };
      for (const mod of json.data || []) {
        out[cacheKey("curseforge", mod.id)] = {
          iconUrl: mod.logo?.thumbnailUrl || mod.logo?.url || null,
          summary: mod.summary || null,
          url: mod.links?.websiteUrl || `https://www.curseforge.com/minecraft/mc-mods/${mod.id}`,
        };
      }
    } catch (error) {
      console.warn("curseforge chunk error", error);
    }
  }
  return out;
}

async function fetchModrinth(ids: string[]): Promise<Record<string, ModMetadata>> {
  const out: Record<string, ModMetadata> = {};
  for (const url of modrinthRequestUrls(ids)) {
    try {
      const response = await fetchWithTimeout(url, {
        headers: { "User-Agent": "lead-and-leylines-mod-browser" },
      });
      if (!response.ok) {
        console.warn("modrinth batch failed", response.status);
        continue;
      }
      const projects = (await response.json()) as Array<{
        id: string;
        slug?: string;
        description?: string;
        icon_url?: string | null;
      }>;
      for (const project of projects) {
        out[cacheKey("modrinth", project.id)] = {
          iconUrl: project.icon_url || null,
          summary: project.description || null,
          url: `https://modrinth.com/mod/${project.slug || project.id}`,
        };
      }
    } catch (error) {
      console.warn("modrinth chunk error", error);
    }
  }
  return out;
}

function fallbackUrl(mod: CatalogMod): string | null {
  if (mod.project_id == null) return null;
  if (mod.source === "curseforge") {
    return `https://www.curseforge.com/minecraft/mc-mods/${mod.project_id}`;
  }
  if (mod.source === "modrinth") {
    return `https://modrinth.com/mod/${mod.project_id}`;
  }
  return null;
}

export async function getModMetadataMap(
  mods: CatalogMod[],
): Promise<Record<string, ModMetadata>> {
  const memory = state();
  if (memory.inFlight) {
    return memory.inFlight;
  }

  memory.inFlight = (async () => {
    const cache = await loadCache();
    const needed = mods.filter((mod) => mod.project_id != null && mod.source !== "unknown");
    const missing = needed.filter((mod) => {
      const key = cacheKey(mod.source, mod.project_id as string | number);
      return !cache.entries[key];
    });
    const age = cache.updatedAt ? Date.now() - Date.parse(cache.updatedAt) : Number.POSITIVE_INFINITY;
    const stale = !Number.isFinite(age) || age > META_TTL_MS;

    if (missing.length === 0 && !stale) {
      return cache.entries;
    }

    const curseIds = needed
      .filter((mod) => mod.source === "curseforge")
      .map((mod) => mod.project_id as string | number);
    const modrinthIds = needed
      .filter((mod) => mod.source === "modrinth")
      .map((mod) => String(mod.project_id));

    const { curseforgeApiKey } = siteConfig();
    const fresh: Record<string, ModMetadata> = {};
    if (curseforgeApiKey && curseIds.length > 0) {
      Object.assign(fresh, await fetchCurseForge(curseIds, curseforgeApiKey));
    }
    if (modrinthIds.length > 0) {
      Object.assign(fresh, await fetchModrinth(modrinthIds));
    }

    const next: MetaCacheFile = {
      updatedAt: new Date().toISOString(),
      entries: { ...cache.entries, ...fresh },
    };
    await saveCache(next);
    return next.entries;
  })();

  try {
    return await memory.inFlight;
  } finally {
    memory.inFlight = null;
  }
}

export function enrichMod(
  mod: CatalogMod,
  metaMap: Record<string, ModMetadata>,
): CatalogMod & { iconUrl: string | null; summary: string | null; storeUrl: string | null } {
  const key =
    mod.project_id != null ? cacheKey(mod.source, mod.project_id) : "";
  const meta = key ? metaMap[key] : undefined;
  return {
    ...mod,
    iconUrl: meta?.iconUrl ?? null,
    summary: meta?.summary ?? null,
    storeUrl: meta?.url ?? fallbackUrl(mod),
  };
}
