"""Pack Java 17 JVM flags. Source of truth: pack/user_jvm_args.txt."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
USER_JVM_ARGS = ROOT / "pack" / "user_jvm_args.txt"

CONFLICTING_FLAGS = (
    "-XX:+UseG1GC",
    "-XX:+UseShenandoahGC",
    "-XX:+ZGenerational",
    "-XX:+UseParallelGC",
    "-XX:+UseSerialGC",
    "-XX:+UseConcMarkSweepGC",
)


def pack_jvm_flags() -> list[str]:
    if not USER_JVM_ARGS.is_file():
        raise SystemExit(f"missing {USER_JVM_ARGS}")
    flags: list[str] = []
    for line in USER_JVM_ARGS.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        flags.extend(stripped.split())
    if not flags:
        raise SystemExit(f"{USER_JVM_ARGS} has no JVM flags")
    return flags


def merge_jvm_args(existing: str) -> str:
    drop = {flag.lower() for flag in CONFLICTING_FLAGS}
    wanted = pack_jvm_flags()
    wanted_lower = {flag.lower() for flag in wanted}
    kept = [
        token
        for token in existing.split()
        if token.lower() not in drop and token.lower() not in wanted_lower
    ]
    return " ".join(kept + wanted)


def _unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def _set_ini_key(text: str, key: str, value: str) -> str:
    newline = "\r\n" if "\r\n" in text else "\n"
    line = f"{key}={value}"
    pattern = re.compile(rf"^{re.escape(key)}=.*$", re.MULTILINE)
    if pattern.search(text):
        return pattern.sub(line, text, count=1)
    after = re.compile(r"^OverrideJavaArgs=.*$", re.MULTILINE)
    if key != "OverrideJavaArgs" and after.search(text):
        return after.sub(lambda match: match.group(0) + newline + line, text, count=1)
    if text and not text.endswith(("\n", "\r\n")):
        text += newline
    return text + line + newline


def apply_to_prism_instance(instance_dir: Path) -> str:
    cfg_path = instance_dir / "instance.cfg"
    if not cfg_path.is_file():
        raise SystemExit(f"no instance.cfg in {instance_dir}")
    text = cfg_path.read_text(encoding="utf-8")
    current = ""
    match = re.search(r"^JvmArgs=(.*)$", text, flags=re.MULTILINE)
    if match:
        current = _unquote(match.group(1).strip())
    merged = merge_jvm_args(current)
    text = _set_ini_key(text, "OverrideJavaArgs", "true")
    text = _set_ini_key(text, "JvmArgs", merged)
    cfg_path.write_text(text, encoding="utf-8")
    return merged
