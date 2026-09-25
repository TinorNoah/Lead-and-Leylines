#!/usr/bin/env python3
"""Generate docs/installed markdown and catalog.json from catalog.toml.

Default: rewrite docs/installed/README.md, each category page, and
docs/installed/catalog.json from docs/installed/catalog.toml plus pack/*.pw.toml.

--check: validate without writing; exit non-zero if the catalog is incomplete,
uses an undefined tag, or the committed markdown/json are out of sync.
"""

from __future__ import annotations

import argparse
import json
import sys
import tomllib
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "pack"
INSTALLED = ROOT / "docs" / "installed"
CATALOG_TOML = INSTALLED / "catalog.toml"
CATALOG_JSON = INSTALLED / "catalog.json"

FOLDER_KIND = {
    "mods": "mod",
    "resourcepacks": "resourcepack",
    "tacz": "tacz-pack",
    "pointblank": "pointblank-pack",
}


def load_pack_meta() -> dict[str, Any]:
    data = tomllib.loads((PACK / "pack.toml").read_text())
    versions = data.get("versions", {})
    return {
        "name": data.get("name", "Lead and Leylines"),
        "version": data.get("version", ""),
        "minecraft": versions.get("minecraft", ""),
        "loader": "neoforge" if "neoforge" in versions else next(iter(versions), ""),
        "loader_version": versions.get("neoforge") or next(iter(versions.values()), ""),
    }


def load_pw_entries() -> dict[str, dict[str, Any]]:
    found: dict[str, dict[str, Any]] = {}
    for folder, kind in FOLDER_KIND.items():
        directory = PACK / folder
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.pw.toml")):
            data = tomllib.loads(path.read_text())
            source = "unknown"
            project_id: str | int | None = None
            update = data.get("update", {})
            if "curseforge" in update:
                source = "curseforge"
                project_id = update["curseforge"].get("project-id")
            elif "modrinth" in update:
                source = "modrinth"
                project_id = update["modrinth"].get("mod-id") or update["modrinth"].get(
                    "project-id"
                )
            found[path.name] = {
                "file": path.name,
                "name": data.get("name", path.stem),
                "filename": data.get("filename", ""),
                "side": data.get("side", ""),
                "folder": folder,
                "kind": kind,
                "source": source,
                "project_id": project_id,
            }
    return found


def load_catalog() -> dict[str, Any]:
    return tomllib.loads(CATALOG_TOML.read_text())


def derived_tags(entry: dict[str, Any]) -> list[str]:
    tags = [entry["side"], entry["source"], entry["kind"]]
    return [tag for tag in tags if tag]


def validate(catalog: dict[str, Any], pw: dict[str, dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    tag_vocab = catalog.get("tags", {})
    if not tag_vocab:
        errors.append("catalog.toml has no [tags] vocabulary")

    used: list[str] = []
    categories = catalog.get("category", [])
    for category in categories:
        slug = category.get("slug", "?")
        for group in category.get("group", []):
            for mod in group.get("mods", []):
                stem = mod.get("file", "")
                used.append(stem)
                if stem not in pw:
                    errors.append(f"{slug}: catalog lists missing pack file {stem}")
                for tag in mod.get("tags", []):
                    if tag not in tag_vocab:
                        errors.append(f"{stem}: undefined tag {tag!r}")

    dupes = sorted({stem for stem in used if used.count(stem) > 1})
    for stem in dupes:
        errors.append(f"listed more than once: {stem}")

    extra = sorted(set(pw) - set(used))
    for stem in extra:
        errors.append(f"pack entry not in catalog: {stem}")

    return errors


def build_payload(
    catalog: dict[str, Any], pw: dict[str, dict[str, Any]], pack: dict[str, Any]
) -> dict[str, Any]:
    tag_vocab = dict(sorted(catalog.get("tags", {}).items()))
    categories_out: list[dict[str, Any]] = []
    mods_out: list[dict[str, Any]] = []

    for category in catalog.get("category", []):
        groups_out: list[dict[str, Any]] = []
        for group in category.get("group", []):
            group_mods: list[dict[str, Any]] = []
            for mod in group.get("mods", []):
                stem = mod["file"]
                entry = pw[stem]
                manual = list(mod.get("tags", []))
                auto = derived_tags(entry)
                tags = []
                for tag in manual + auto:
                    if tag not in tags:
                        tags.append(tag)
                record = {
                    "file": stem,
                    "name": entry["name"],
                    "filename": entry["filename"],
                    "side": entry["side"],
                    "folder": entry["folder"],
                    "kind": entry["kind"],
                    "source": entry["source"],
                    "project_id": entry["project_id"],
                    "blurb": mod.get("blurb", ""),
                    "tags": tags,
                    "manual_tags": manual,
                    "category": category["slug"],
                    "category_title": category["title"],
                    "group": group["name"],
                }
                group_mods.append(
                    {
                        "file": stem,
                        "blurb": record["blurb"],
                        "tags": tags,
                        "name": record["name"],
                        "filename": record["filename"],
                        "side": record["side"],
                        "source": record["source"],
                        "project_id": record["project_id"],
                        "kind": record["kind"],
                    }
                )
                mods_out.append(record)
            groups_out.append({"name": group["name"], "mods": group_mods})
        categories_out.append(
            {
                "slug": category["slug"],
                "title": category["title"],
                "intro": category.get("intro", ""),
                "groups": groups_out,
            }
        )

    mods_out.sort(key=lambda item: (item["category"], item["group"], item["name"].lower()))
    return {
        "pack": pack,
        "tags": tag_vocab,
        "categories": categories_out,
        "mods": mods_out,
        "mod_count": len(mods_out),
    }


def render_category_markdown(category: dict[str, Any], pw: dict[str, dict[str, Any]]) -> str:
    lines = [
        f"# {category['title']}",
        "",
        category.get("intro", "").strip(),
        "",
        "Each mod is listed once. Decision notes stay in [`docs/mods/`](../mods/manifest.md).",
        "",
    ]
    for group in category.get("group", []):
        lines.append(f"## {group['name']}")
        lines.append("")
        lines.append("| Mod | File | Side | Tags | What it adds |")
        lines.append("|---|---|---|---|---|")
        for mod in group.get("mods", []):
            entry = pw[mod["file"]]
            name = entry["name"].replace("|", "\\|")
            filename = entry["filename"].replace("|", "\\|")
            blurb = mod.get("blurb", "").replace("|", "\\|")
            tags = ", ".join(f"`{tag}`" for tag in mod.get("tags", []))
            lines.append(
                f"| {name} | `{filename}` | {entry['side']} | {tags} | {blurb} |"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_readme(categories: list[dict[str, Any]], mod_count: int) -> str:
    lines = [
        "# Installed mods",
        "",
        "Browse the mods in the pack by what they add. Compat addons sit in the same table as the mod they extend.",
        "",
        "Why a mod was kept or held is in [`docs/mods/`](../mods/manifest.md). This folder is only the current install.",
        "",
        "Edit [`catalog.toml`](catalog.toml), then run `python3 scripts/installed_catalog.py` to regenerate these pages and [`catalog.json`](catalog.json). Who updates what: [`MAINTENANCE.md`](MAINTENANCE.md).",
        "",
        "The searchable browser UI lives in [`site/`](../../site/README.md) (Docker / Dokploy).",
        "",
        "| Category | Mods | What you'll find |",
        "|---|---:|---|",
    ]
    for category in categories:
        count = sum(len(group.get("mods", [])) for group in category.get("group", []))
        intro = category.get("intro", "").strip()
        sentence = intro.split(".")[0].strip() + "." if intro else ""
        lines.append(f"| [{category['title']}]({category['slug']}.md) | {count} | {sentence} |")
    lines.append("")
    lines.append(f"{mod_count} entries, each listed once.")
    lines.append("")
    return "\n".join(lines)


def expected_files(
    catalog: dict[str, Any], pw: dict[str, dict[str, Any]], pack: dict[str, Any]
) -> dict[Path, str]:
    payload = build_payload(catalog, pw, pack)
    files: dict[Path, str] = {
        CATALOG_JSON: json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n",
        INSTALLED / "README.md": render_readme(catalog.get("category", []), payload["mod_count"]),
    }
    for category in catalog.get("category", []):
        files[INSTALLED / f"{category['slug']}.md"] = render_category_markdown(category, pw)
    return files


def write_files(files: dict[Path, str]) -> None:
    for path, content in files.items():
        path.write_text(content)


def check_files(files: dict[Path, str]) -> list[str]:
    errors: list[str] = []
    for path, expected in files.items():
        if not path.exists():
            errors.append(f"missing generated file: {path.relative_to(ROOT)}")
            continue
        actual = path.read_text()
        if actual != expected:
            errors.append(f"out of sync: {path.relative_to(ROOT)}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate catalog and generated outputs without writing.",
    )
    args = parser.parse_args(argv)

    if not CATALOG_TOML.exists():
        print(f"missing {CATALOG_TOML}", file=sys.stderr)
        return 1

    catalog = load_catalog()
    pw = load_pw_entries()
    pack = load_pack_meta()
    errors = validate(catalog, pw)
    if errors:
        print("catalog validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1

    files = expected_files(catalog, pw, pack)
    if args.check:
        sync_errors = check_files(files)
        if sync_errors:
            print("generated outputs out of sync:", file=sys.stderr)
            for error in sync_errors:
                print(f"  {error}", file=sys.stderr)
            print("Run: python3 scripts/installed_catalog.py", file=sys.stderr)
            return 1
        print(f"ok: {len(pw)} mods, {len(catalog.get('category', []))} categories")
        return 0

    write_files(files)
    print(f"wrote {len(files)} files ({len(pw)} mods)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
