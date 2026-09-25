import { siteConfig } from "./env";
import type { ReleaseChannel, ReleaseChannels, ReleaseInfo } from "./types";

const FETCH_TIMEOUT_MS = 8_000;

type GitHubReleaseBody = {
  tag_name?: string;
  name?: string;
  html_url?: string;
  prerelease?: boolean;
  draft?: boolean;
};

function authHeaders(): HeadersInit {
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

function versionFromTag(tag: string): string {
  return tag.replace(/^v/i, "");
}

function channelLabel(channel: ReleaseChannel): string {
  switch (channel) {
    case "release":
      return "Release";
    case "prerelease":
      return "Pre-release";
    default: {
      const _exhaustive: never = channel;
      return _exhaustive;
    }
  }
}

export { channelLabel };

function toReleaseInfo(body: GitHubReleaseBody, channel: ReleaseChannel): ReleaseInfo | null {
  const tag = body.tag_name?.trim();
  if (!tag || !body.html_url) {
    return null;
  }
  const version = versionFromTag(tag);
  return {
    tag,
    version,
    name: body.name?.trim() || `Lead and Leylines ${version}`,
    url: body.html_url,
    channel,
  };
}

export function releaseFromPackVersion(
  version: string,
  channel: ReleaseChannel = "prerelease",
): ReleaseInfo {
  const { githubRepo } = siteConfig();
  const tag = `v${version}`;
  return {
    tag,
    version,
    name: `Lead and Leylines ${version}`,
    url: `https://github.com/${githubRepo}/releases/tag/${tag}`,
    channel,
  };
}

async function fetchJson(url: string, signal: AbortSignal): Promise<unknown | null> {
  const response = await fetch(url, {
    headers: authHeaders(),
    signal,
    cache: "no-store",
  });
  if (!response.ok) {
    console.warn("github release fetch", url, response.status);
    return null;
  }
  return response.json();
}

/**
 * Official = GitHub "Latest" (non-prerelease).
 * Pre-release = newest published prerelease that is not the same tag as official.
 */
export async function fetchReleaseChannels(
  fallbackVersion?: string,
): Promise<ReleaseChannels> {
  const { githubRepo } = siteConfig();
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), FETCH_TIMEOUT_MS);
  try {
    const [latestBody, listBody] = await Promise.all([
      fetchJson(`https://api.github.com/repos/${githubRepo}/releases/latest`, controller.signal),
      fetchJson(
        `https://api.github.com/repos/${githubRepo}/releases?per_page=20`,
        controller.signal,
      ),
    ]);

    const official =
      latestBody && typeof latestBody === "object"
        ? toReleaseInfo(latestBody as GitHubReleaseBody, "release")
        : null;

    let prerelease: ReleaseInfo | null = null;
    if (Array.isArray(listBody)) {
      for (const entry of listBody) {
        if (!entry || typeof entry !== "object") {
          continue;
        }
        const body = entry as GitHubReleaseBody;
        if (body.draft || !body.prerelease) {
          continue;
        }
        const info = toReleaseInfo(body, "prerelease");
        if (!info) {
          continue;
        }
        if (official && info.tag === official.tag) {
          continue;
        }
        prerelease = info;
        break;
      }
    }

    if (!prerelease && fallbackVersion) {
      const fallbackTag = `v${fallbackVersion}`;
      if (!official || official.tag !== fallbackTag) {
        prerelease = releaseFromPackVersion(fallbackVersion, "prerelease");
      }
    }

    if (!official && !prerelease && fallbackVersion) {
      return {
        official: releaseFromPackVersion(fallbackVersion, "release"),
        prerelease: null,
      };
    }

    return { official, prerelease };
  } catch (error) {
    console.warn("github releases failed", error);
    if (fallbackVersion) {
      return {
        official: null,
        prerelease: releaseFromPackVersion(fallbackVersion, "prerelease"),
      };
    }
    return { official: null, prerelease: null };
  } finally {
    clearTimeout(timer);
  }
}
