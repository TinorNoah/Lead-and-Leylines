import { createHmac, timingSafeEqual } from "node:crypto";

export function verifyGitHubSignature(
  rawBody: string,
  signatureHeader: string | null,
  secret: string,
): boolean {
  if (!secret || !signatureHeader) {
    return false;
  }
  const expected = `sha256=${createHmac("sha256", secret).update(rawBody).digest("hex")}`;
  const left = Buffer.from(expected);
  const right = Buffer.from(signatureHeader);
  if (left.length !== right.length) {
    return false;
  }
  return timingSafeEqual(left, right);
}

export function extractPushSha(payload: unknown, branch: string): string | null {
  if (!payload || typeof payload !== "object") {
    return null;
  }
  const body = payload as {
    ref?: string;
    after?: string;
  };
  if (body.ref !== `refs/heads/${branch}`) {
    return null;
  }
  const after = body.after || "";
  if (!/^[0-9a-f]{40}$/i.test(after)) {
    return null;
  }
  // GitHub uses all-zeros for branch deletes.
  if (/^0+$/.test(after)) {
    return null;
  }
  return after.toLowerCase();
}
