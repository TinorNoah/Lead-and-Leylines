import { promises as fs } from "node:fs";
import path from "node:path";

import { siteConfig } from "./env";
import type { CatalogPayload, CatalogSnapshot, CommitInfo } from "./types";

const MIN_REFRESH_GAP_MS = 30_000;
const FETCH_TIMEOUT_MS = 10_000;

type MemoryState = {
  snapshot: CatalogSnapshot | null;
  commitEtag: string | null;
  inFlight: Promise<CatalogSnapshot> | null;
  lastRefreshAttemptAt: number;
};

const globalState = globalThis as typeof globalThis & {
  __llCatalogState?: MemoryState;
};

function state(): MemoryState {
  if (!globalState.__llCatalogState) {
    globalState.__llCatalogState = {
      snapshot: null,
      commitEtag: null,
      inFlight: null,
      lastRefreshAttemptAt: 0,
    };
  }
  return globalState.__llCatalogState;
}

function isCatalogPayload(value: unknown): value is CatalogPayload {
  if (!value || typeof value !== "object") return false;
  const candidate = value as CatalogPayload;
  return (
    Array.isArray(candidate.mods) &&
    Array.isArray(candidate.categories) &&
    typeof candidate.mod_count === "number" &&
    candidate.pack != null
  );
}

async function readJsonFile(filePath: string): Promise<CatalogPayload | null> {
  try {
    const raw = await fs.readFile(filePath, "utf8");
    const parsed = JSON.parse(raw) as unknown;
    return isCatalogPayload(parsed) ? parsed : null;
  } catch {
    return null;
  }
}

async function writeThrough(catalog: CatalogPayload): Promise<void> {
  const { dataDir } = siteConfig();
  try {
    await fs.mkdir(dataDir, { recursive: true });
    const target = path.join(dataDir, "catalog.json");
    const temp = `${target}.tmp`;
    await fs.writeFile(temp, JSON.stringify(catalog));
    await fs.rename(temp, target);
  } catch (error) {
    console.warn("catalog write-through failed", error);
  }
}

async function loadLocalFallback(): Promise<CatalogSnapshot | null> {
  const { dataDir, seedPath } = siteConfig();
  const dataPath = path.join(dataDir, "catalog.json");
  const fromData = await readJsonFile(dataPath);
  if (fromData) {
    return {
      catalog: fromData,
      commit: null,
      source: "data",
      fetchedAt: new Date().toISOString(),
    };
  }
  const fromSeed = await readJsonFile(seedPath);
  if (fromSeed) {
    return {
      catalog: fromSeed,
      commit: null,
      source: "seed",
      fetchedAt: new Date().toISOString(),
    };
  }
  // Dev fallback: repo-relative seed when running outside Docker.
  const localSeed = path.join(process.cwd(), "seed", "catalog.json");
  const fromLocal = await readJsonFile(localSeed);
  if (fromLocal) {
    return {
      catalog: fromLocal,
      commit: null,
      source: "seed",
      fetchedAt: new Date().toISOString(),
    };
  }
  const repoSeed = path.join(process.cwd(), "..", "docs", "installed", "catalog.json");
  const fromRepo = await readJsonFile(repoSeed);
  if (fromRepo) {
    return {
      catalog: fromRepo,
      commit: null,
      source: "seed",
      fetchedAt: new Date().toISOString(),
    };
  }
  return null;
}

function authHeaders(): Record<string, string> {
  const { githubToken } = siteConfig();
  const headers: Record<string, string> = {
    Accept: "application/vnd.github+json",
    "User-Agent": "lead-and-leylines-mod-browser",
  };
  if (githubToken) {
    headers.Authorization = `Bearer ${githubToken}`;
  }
  return headers;
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

async function fetchCommit(sha?: string): Promise<{ commit: CommitInfo; etag: string | null }> {
  const { githubRepo, githubBranch } = siteConfig();
  const memory = state();
  const ref = sha && /^[0-9a-f]{40}$/i.test(sha) ? sha : githubBranch;
  const url = `https://api.github.com/repos/${githubRepo}/commits/${ref}`;
  const headers: Record<string, string> = { ...authHeaders() };
  if (!sha && memory.commitEtag) {
    headers["If-None-Match"] = memory.commitEtag;
  }
  const response = await fetchWithTimeout(url, { headers });
  if (response.status === 304 && memory.snapshot?.commit) {
    return { commit: memory.snapshot.commit, etag: memory.commitEtag };
  }
  if (!response.ok) {
    throw new Error(`github commit ${response.status}`);
  }
  const body = (await response.json()) as {
    sha: string;
    html_url: string;
    commit: { message: string; committer?: { date?: string }; author?: { date?: string } };
  };
  const commit: CommitInfo = {
    sha: body.sha,
    message: (body.commit.message || "").split("\n")[0] ?? "",
    date: body.commit.committer?.date || body.commit.author?.date || "",
    url: body.html_url,
  };
  return { commit, etag: response.headers.get("etag") };
}

async function fetchCatalogAtSha(sha: string): Promise<CatalogPayload> {
  const { githubRepo } = siteConfig();
  const url = `https://raw.githubusercontent.com/${githubRepo}/${sha}/docs/installed/catalog.json`;
  const response = await fetchWithTimeout(url, {
    headers: { "User-Agent": "lead-and-leylines-mod-browser" },
  });
  if (!response.ok) {
    throw new Error(`raw catalog ${response.status}`);
  }
  const parsed = (await response.json()) as unknown;
  if (!isCatalogPayload(parsed)) {
    throw new Error("raw catalog payload invalid");
  }
  return parsed;
}

async function refreshFromGitHub(forcedSha?: string): Promise<CatalogSnapshot> {
  const memory = state();
  const { commit, etag } = await fetchCommit(forcedSha);
  if (
    !forcedSha &&
    memory.snapshot?.commit?.sha === commit.sha &&
    memory.snapshot.source === "github"
  ) {
    memory.commitEtag = etag;
    memory.snapshot = { ...memory.snapshot, fetchedAt: new Date().toISOString() };
    return memory.snapshot;
  }
  const catalog = await fetchCatalogAtSha(commit.sha);
  await writeThrough(catalog);
  const snapshot: CatalogSnapshot = {
    catalog,
    commit,
    source: "github",
    fetchedAt: new Date().toISOString(),
  };
  memory.snapshot = snapshot;
  memory.commitEtag = etag;
  return snapshot;
}

export async function getCatalogSnapshot(options?: {
  force?: boolean;
  sha?: string;
}): Promise<CatalogSnapshot> {
  const memory = state();
  const { cacheTtlSeconds } = siteConfig();
  const now = Date.now();
  const forceRefresh = Boolean(options?.force || options?.sha);

  // Coalesce before any await so concurrent callers share one refresh.
  if (memory.inFlight) {
    return memory.inFlight;
  }

  if (!memory.snapshot) {
    // Synchronously claim the in-flight slot, then load local + optional GitHub.
    memory.lastRefreshAttemptAt = now;
    memory.inFlight = (async () => {
      try {
        const local = await loadLocalFallback();
        if (local) {
          memory.snapshot = local;
        }
        try {
          return await refreshFromGitHub(options?.sha);
        } catch (error) {
          console.error("catalog refresh failed", error);
          if (memory.snapshot) {
            return memory.snapshot;
          }
          if (local) {
            return local;
          }
          throw error;
        }
      } finally {
        memory.inFlight = null;
      }
    })();
    return memory.inFlight;
  }

  const parsedFetchedAt = Date.parse(memory.snapshot.fetchedAt || "");
  const ageMs = Number.isFinite(parsedFetchedAt)
    ? now - parsedFetchedAt
    : Number.POSITIVE_INFINITY;
  const freshEnough =
    !forceRefresh &&
    memory.snapshot.source === "github" &&
    ageMs < cacheTtlSeconds * 1000;

  if (freshEnough) {
    return memory.snapshot;
  }

  if (
    !forceRefresh &&
    now - memory.lastRefreshAttemptAt < MIN_REFRESH_GAP_MS
  ) {
    return memory.snapshot;
  }

  memory.lastRefreshAttemptAt = now;
  memory.inFlight = (async () => {
    try {
      return await refreshFromGitHub(options?.sha);
    } catch (error) {
      console.error("catalog refresh failed", error);
      return memory.snapshot!;
    } finally {
      memory.inFlight = null;
    }
  })();

  return memory.inFlight;
}

/** Test helper: clear in-memory state between unit tests. */
export function resetCatalogStateForTests(): void {
  globalState.__llCatalogState = {
    snapshot: null,
    commitEtag: null,
    inFlight: null,
    lastRefreshAttemptAt: 0,
  };
}
