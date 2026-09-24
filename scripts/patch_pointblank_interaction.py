#!/usr/bin/env python3
"""Let Vic's Point Blank Interaction load on a dedicated server.

InteractionManager is marked @OnlyIn(Dist.CLIENT), and its client methods
reference LocalPlayer. The dedicated server calls the same class while loading
config and while blocking gun interactions, so NeoForge refuses the load and
the server never finishes starting. The client jar from CurseForge is
unchanged. The server-mods zip drops that class-level marker and replaces the
client-only method bodies with empty stubs. The shared block and entity checks
stay.
"""

from __future__ import annotations

import struct
import sys
import zipfile
from pathlib import Path

CLASS_PATH = "com/vics/pointblank/passthrough/core/InteractionManager.class"
ONLY_IN = b"Lnet/neoforged/api/distmarker/OnlyIn;"
ANNOTATIONS_ATTR = b"RuntimeVisibleAnnotations"


def patch_jar(path: Path) -> bool:
    """Return True when the dedicated-server class bytes changed."""
    with zipfile.ZipFile(path, "r") as archive:
        original = archive.read(CLASS_PATH)
        patched = stub_client_methods(strip_class_only_in(original))
        if patched == original:
            return False
        entries = [(info, archive.read(info.filename)) for info in archive.infolist()]

    with zipfile.ZipFile(path, "w") as archive:
        for info, data in entries:
            next_info = zipfile.ZipInfo(filename=info.filename, date_time=info.date_time)
            next_info.compress_type = info.compress_type
            next_info.external_attr = info.external_attr
            next_info.flag_bits = info.flag_bits
            if info.filename == CLASS_PATH:
                data = patched
            archive.writestr(next_info, data)
    return True


def strip_class_only_in(data: bytes) -> bytes:
    """Drop a class-level @OnlyIn annotation. Leave method annotations alone."""
    if data[:4] != b"\xca\xfe\xba\xbe":
        raise SystemExit(f"{CLASS_PATH} is not a class file")
    pool, offset = _constant_pool(data, 8)
    offset += 6  # access flags, this class, super class
    interface_count = struct.unpack_from(">H", data, offset)[0]
    offset += 2 + interface_count * 2
    offset = _skip_members(data, offset)
    offset = _skip_members(data, offset)
    attr_count = struct.unpack_from(">H", data, offset)[0]
    cursor = offset + 2
    kept: list[bytes] = []
    removed = False
    for _ in range(attr_count):
        name_index, length = struct.unpack_from(">HI", data, cursor)
        blob = data[cursor : cursor + 6 + length]
        cursor += 6 + length
        name = pool[name_index]
        if name == ANNOTATIONS_ATTR and _only_annotation_is_only_in(blob[6:], pool):
            removed = True
            continue
        kept.append(blob)
    if cursor != len(data):
        raise SystemExit(f"{CLASS_PATH} class attributes did not end at the file end")
    if not removed:
        return data
    return data[:offset] + struct.pack(">H", len(kept)) + b"".join(kept)


def _only_annotation_is_only_in(info: bytes, pool: list[bytes | None]) -> bool:
    count = struct.unpack_from(">H", info, 0)[0]
    if count != 1:
        return False
    type_index = struct.unpack_from(">H", info, 2)[0]
    return pool[type_index] == ONLY_IN


def _constant_pool(data: bytes, offset: int) -> tuple[list[bytes | None], int]:
    count = struct.unpack_from(">H", data, offset)[0]
    offset += 2
    pool: list[bytes | None] = [None]
    index = 1
    while index < count:
        tag = data[offset]
        offset += 1
        if tag == 1:
            length = struct.unpack_from(">H", data, offset)[0]
            offset += 2
            pool.append(data[offset : offset + length])
            offset += length
        elif tag in (7, 8, 16, 19, 20):
            pool.append(None)
            offset += 2
        elif tag in (3, 4, 9, 10, 11, 12, 17, 18):
            pool.append(None)
            offset += 4
        elif tag == 15:
            pool.append(None)
            offset += 3
        elif tag in (5, 6):
            pool.append(None)
            pool.append(None)
            offset += 8
            index += 1
        else:
            raise SystemExit(f"unknown constant-pool tag {tag} in {CLASS_PATH}")
        index += 1
    return pool, offset


def _skip_members(data: bytes, offset: int) -> int:
    count = struct.unpack_from(">H", data, offset)[0]
    offset += 2
    for _ in range(count):
        offset += 6  # access, name, descriptor
        attr_count = struct.unpack_from(">H", data, offset)[0]
        offset += 2
        for _attr in range(attr_count):
            length = struct.unpack_from(">I", data, offset + 2)[0]
            offset += 6 + length
    return offset


CLIENT_PREFIX = b"net/minecraft/client/"
_CP_INDEX_OPS = {
    18: "u1",
    19: "u2",
    20: "u2",
    178: "u2",
    179: "u2",
    180: "u2",
    181: "u2",
    182: "u2",
    183: "u2",
    184: "u2",
    185: "u2",
    186: "u2",
    187: "u2",
    189: "u2",
    192: "u2",
    193: "u2",
    197: "u2",
}
_EXTRA = {
    16: 1, 17: 2, 18: 1, 19: 2, 20: 2,
    21: 1, 22: 1, 23: 1, 24: 1, 25: 1,
    54: 1, 55: 1, 56: 1, 57: 1, 58: 1,
    132: 2, 153: 2, 154: 2, 155: 2, 156: 2, 157: 2, 158: 2,
    159: 2, 160: 2, 161: 2, 162: 2, 163: 2, 164: 2, 165: 2, 166: 2, 167: 2, 168: 2,
    169: 1, 178: 2, 179: 2, 180: 2, 181: 2, 182: 2, 183: 2, 184: 2,
    185: 4, 186: 4, 187: 2, 188: 1, 189: 2, 192: 2, 193: 2, 197: 3,
    198: 2, 199: 2, 200: 4, 201: 4,
}


def stub_client_methods(data: bytes) -> bytes:
    """Replace method bodies that touch client classes. Leave the shared checks."""
    pool, offset = _rich_pool(data, 8)
    client_ids = _client_constant_ids(pool)
    offset += 6
    interface_count = struct.unpack_from(">H", data, offset)[0]
    offset += 2 + interface_count * 2
    offset = _skip_members(data, offset)
    method_count = struct.unpack_from(">H", data, offset)[0]
    cursor = offset + 2
    methods: list[bytes] = []
    changed = False
    for _ in range(method_count):
        start = cursor
        access, _name, desc = struct.unpack_from(">HHH", data, cursor)
        cursor += 6
        attr_count = struct.unpack_from(">H", data, cursor)[0]
        cursor += 2
        attrs: list[bytes] = []
        for _attr in range(attr_count):
            attr_start = cursor
            name_index, length = struct.unpack_from(">HI", data, cursor)
            cursor += 6 + length
            blob = data[attr_start:cursor]
            if pool[name_index][1] == b"Code" and _code_uses_client(blob[6:], pool, client_ids):
                blob = _stub_code_attribute(name_index, access, pool[desc][1])
                changed = True
            attrs.append(blob)
        if not changed and cursor != start:
            methods.append(data[start:cursor])
        else:
            methods.append(data[start : start + 8] + b"".join(attrs))
    if not changed:
        return data
    return data[: offset + 2] + b"".join(methods) + data[cursor:]


def _client_constant_ids(pool: list[tuple[str, bytes | int]]) -> set[int]:
    ids: set[int] = set()
    for index, entry in enumerate(pool):
        if entry is None:
            continue
        kind, value = entry
        if kind == "class" and isinstance(value, int):
            name = pool[value][1]
            if isinstance(name, bytes) and name.startswith(CLIENT_PREFIX):
                ids.add(index)
        elif kind == "ref" and isinstance(value, int) and _class_is_client(pool, value):
            ids.add(index)
    return ids


def _class_is_client(pool: list[tuple[str, bytes | int]], class_index: int) -> bool:
    entry = pool[class_index]
    if entry is None or entry[0] != "class" or not isinstance(entry[1], int):
        return False
    name = pool[entry[1]][1]
    return isinstance(name, bytes) and name.startswith(CLIENT_PREFIX)


def _code_uses_client(
    info: bytes,
    pool: list[tuple[str, bytes | int]],
    client_ids: set[int],
) -> bool:
    code_length = struct.unpack_from(">I", info, 4)[0]
    code = info[8 : 8 + code_length]
    for index in _bytecode_constant_ids(code):
        if index in client_ids:
            return True
    cursor = 8 + code_length
    exception_count = struct.unpack_from(">H", info, cursor)[0]
    cursor += 2 + exception_count * 8
    attr_count = struct.unpack_from(">H", info, cursor)[0]
    cursor += 2
    for _ in range(attr_count):
        name_index, length = struct.unpack_from(">HI", info, cursor)
        body = info[cursor + 6 : cursor + 6 + length]
        cursor += 6 + length
        if pool[name_index][1] == b"StackMapTable" and _stack_map_uses_client(body, client_ids):
            return True
    return False


def _bytecode_constant_ids(code: bytes) -> list[int]:
    ids: list[int] = []
    ip = 0
    while ip < len(code):
        op = code[ip]
        if op == 0xC4:  # wide
            wide_op = code[ip + 1]
            ip += 6 if wide_op == 0x84 else 4
            continue
        if op == 0xAA:  # tableswitch
            ip = _tableswitch_end(code, ip)
            continue
        if op == 0xAB:  # lookupswitch
            ip = _lookupswitch_end(code, ip)
            continue
        kind = _CP_INDEX_OPS.get(op)
        if kind == "u1":
            ids.append(code[ip + 1])
        elif kind == "u2":
            ids.append(struct.unpack_from(">H", code, ip + 1)[0])
        ip += 1 + _EXTRA.get(op, 0)
    return ids


def _tableswitch_end(code: bytes, ip: int) -> int:
    aligned = (ip + 4) & ~3
    low, high = struct.unpack_from(">ii", code, aligned + 4)
    return aligned + 12 + (high - low + 1) * 4


def _lookupswitch_end(code: bytes, ip: int) -> int:
    aligned = (ip + 4) & ~3
    npairs = struct.unpack_from(">i", code, aligned + 4)[0]
    return aligned + 8 + npairs * 8


def _stack_map_uses_client(body: bytes, client_ids: set[int]) -> bool:
    count = struct.unpack_from(">H", body, 0)[0]
    cursor = 2
    for _ in range(count):
        frame = body[cursor]
        cursor += 1
        if frame <= 63:
            continue
        if frame <= 127:
            cursor = _skip_verification(body, cursor, client_ids)
            if cursor < 0:
                return True
            continue
        if frame == 247:
            cursor += 2
            cursor = _skip_verification(body, cursor, client_ids)
            if cursor < 0:
                return True
            continue
        if frame <= 251:
            cursor += 2
            continue
        if frame <= 254:
            cursor += 2
            for _local in range(frame - 251):
                cursor = _skip_verification(body, cursor, client_ids)
                if cursor < 0:
                    return True
            continue
        cursor += 2
        locals_count = struct.unpack_from(">H", body, cursor)[0]
        cursor += 2
        for _local in range(locals_count):
            cursor = _skip_verification(body, cursor, client_ids)
            if cursor < 0:
                return True
        stack_count = struct.unpack_from(">H", body, cursor)[0]
        cursor += 2
        for _stack in range(stack_count):
            cursor = _skip_verification(body, cursor, client_ids)
            if cursor < 0:
                return True
    return False


def _skip_verification(body: bytes, cursor: int, client_ids: set[int]) -> int:
    tag = body[cursor]
    cursor += 1
    if tag < 7:
        return cursor
    index = struct.unpack_from(">H", body, cursor)[0]
    if tag == 7 and index in client_ids:
        return -1
    return cursor + 2


def _stub_code_attribute(name_index: int, access: int, descriptor: bytes) -> bytes:
    return_type = descriptor.rsplit(b")", 1)[1]
    if return_type == b"V":
        code = b"\xb1"
        max_stack = 0
    elif return_type[:1] in b"ZBCSI":
        code = b"\x03\xac"
        max_stack = 1
    elif return_type[:1] == b"J":
        code = b"\x09\xad"
        max_stack = 2
    elif return_type[:1] == b"F":
        code = b"\x0b\xae"
        max_stack = 1
    elif return_type[:1] == b"D":
        code = b"\x0e\xaf"
        max_stack = 2
    else:
        code = b"\x01\xb0"
        max_stack = 1
    max_locals = _argument_slots(descriptor)
    if access & 0x0008 == 0:
        max_locals += 1
    info = struct.pack(">HHI", max_stack, max_locals, len(code)) + code + struct.pack(">HH", 0, 0)
    return struct.pack(">HI", name_index, len(info)) + info


def _argument_slots(descriptor: bytes) -> int:
    slots = 0
    index = 1  # skip '('
    while descriptor[index : index + 1] != b")":
        char = descriptor[index]
        if char in b"JD":
            slots += 2
            index += 1
        elif char == ord("L"):
            slots += 1
            index = descriptor.index(b";", index) + 1
        elif char == ord("["):
            slots += 1
            index += 1
            while descriptor[index] == ord("["):
                index += 1
            if descriptor[index] == ord("L"):
                index = descriptor.index(b";", index) + 1
            else:
                index += 1
        else:
            slots += 1
            index += 1
    return slots


def _rich_pool(data: bytes, offset: int) -> tuple[list[tuple[str, bytes | int] | None], int]:
    count = struct.unpack_from(">H", data, offset)[0]
    offset += 2
    pool: list[tuple[str, bytes | int] | None] = [None]
    index = 1
    while index < count:
        tag = data[offset]
        offset += 1
        if tag == 1:
            length = struct.unpack_from(">H", data, offset)[0]
            offset += 2
            pool.append(("utf8", data[offset : offset + length]))
            offset += length
        elif tag == 7:
            pool.append(("class", struct.unpack_from(">H", data, offset)[0]))
            offset += 2
        elif tag in (9, 10, 11):
            pool.append(("ref", struct.unpack_from(">H", data, offset)[0]))
            offset += 4
        elif tag in (8, 16, 19, 20):
            pool.append(("other", b""))
            offset += 2
        elif tag in (3, 4, 12, 17, 18):
            pool.append(("other", b""))
            offset += 4
        elif tag == 15:
            pool.append(("other", b""))
            offset += 3
        elif tag in (5, 6):
            pool.append(("other", b""))
            pool.append(None)
            offset += 8
            index += 1
        else:
            raise SystemExit(f"unknown constant-pool tag {tag} in {CLASS_PATH}")
        index += 1
    return pool, offset


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {Path(sys.argv[0]).name} <jar>")
    path = Path(sys.argv[1])
    changed = patch_jar(path)
    print(f"{'patched' if changed else 'already server-safe'}: {path}")


if __name__ == "__main__":
    main()
