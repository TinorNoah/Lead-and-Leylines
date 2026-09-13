#!/usr/bin/env python3
"""Build multipart/form-data bodies without third-party packages."""

from __future__ import annotations

import secrets


def encode(
    fields: list[tuple[str, bytes, str | None, str | None]],
) -> tuple[bytes, str]:
    """Return (body, content_type).

    Each field is (name, content, filename or None, content_type or None).
    """
    boundary = "----LeadAndLeylines" + secrets.token_hex(16)
    chunks: list[bytes] = []
    for name, content, filename, content_type in fields:
        chunks.append(f"--{boundary}\r\n".encode("ascii"))
        disposition = f'Content-Disposition: form-data; name="{name}"'
        if filename:
            disposition += f'; filename="{filename}"'
        chunks.append(f"{disposition}\r\n".encode("utf-8"))
        if content_type:
            chunks.append(f"Content-Type: {content_type}\r\n".encode("ascii"))
        chunks.append(b"\r\n")
        chunks.append(content)
        chunks.append(b"\r\n")
    chunks.append(f"--{boundary}--\r\n".encode("ascii"))
    return b"".join(chunks), f"multipart/form-data; boundary={boundary}"
