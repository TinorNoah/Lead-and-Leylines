"""Minimal RCON client (stdlib only) for driving the local smoke-test server.

Usage: python3 rcon.py <host> <port> <password> <command...>
Prints the command response. Exit 0 on success, 1 on auth/connection failure.
"""

from __future__ import annotations

import socket
import struct
import sys


def _packet(req_id: int, ptype: int, body: str) -> bytes:
    payload = struct.pack("<ii", req_id, ptype) + body.encode("utf-8") + b"\x00\x00"
    return struct.pack("<i", len(payload)) + payload


def _read_packet(sock: socket.socket) -> tuple[int, int, str]:
    (length,) = struct.unpack("<i", sock.recv(4))
    data = b""
    while len(data) < length:
        chunk = sock.recv(length - len(data))
        if not chunk:
            raise ConnectionError("rcon closed mid-packet")
        data += chunk
    req_id, ptype = struct.unpack("<ii", data[:8])
    return req_id, ptype, data[8:-2].decode("utf-8", "replace")


def run(host: str, port: int, password: str, command: str, timeout: float = 30.0) -> str:
    out: list[str] = []
    with socket.create_connection((host, port), timeout=timeout) as sock:
        sock.settimeout(timeout)
        sock.sendall(_packet(1, 3, password))
        req_id, _, _ = _read_packet(sock)
        if req_id == -1:
            raise PermissionError("rcon auth failed")
        sock.sendall(_packet(2, 2, command))
        while True:
            req_id, _, body = _read_packet(sock)
            out.append(body)
            if len(body) < 4096:
                break
    return "".join(out)


if __name__ == "__main__":
    host, port, password, *cmd = sys.argv[1:]
    try:
        print(run(host, int(port), password, " ".join(cmd)))
    except Exception as e:  # noqa: BLE001 - CLI surface, message is the result
        print(f"RCON FAILED: {e}")
        sys.exit(1)
