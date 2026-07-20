"""Validate the machine-readable Chinese color palette."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


HEX_RE = re.compile(r"^#[0-9A-Fa-f]{6}$")
REQUIRED_FIELDS = ("name_zh", "hex", "rgb", "source", "needs_review", "aliases")


def _error(index: int, message: str) -> str:
    return f"record {index}: {message}"


def validate_palette(records: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(records, list):
        return ["palette must be a JSON array"]

    seen_hex: dict[str, int] = {}
    for index, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            errors.append(_error(index, "record must be an object"))
            continue

        missing = [field for field in REQUIRED_FIELDS if field not in record]
        if missing:
            errors.append(_error(index, f"missing fields: {', '.join(missing)}"))
            continue

        name = record["name_zh"]
        if not isinstance(name, str) or not name.strip():
            errors.append(_error(index, "name_zh must be a non-empty string"))

        hex_value = record["hex"]
        if not isinstance(hex_value, str) or not HEX_RE.fullmatch(hex_value):
            errors.append(_error(index, "hex must match #RRGGBB"))
            normalized_hex = None
        else:
            normalized_hex = hex_value.upper()
            if normalized_hex in seen_hex:
                errors.append(_error(index, f"duplicate HEX {normalized_hex}; first seen in record {seen_hex[normalized_hex]}"))
            else:
                seen_hex[normalized_hex] = index

        rgb = record["rgb"]
        if not isinstance(rgb, dict) or any(channel not in rgb for channel in ("r", "g", "b")):
            errors.append(_error(index, "rgb must contain r, g, and b"))
        else:
            for channel in ("r", "g", "b"):
                value = rgb[channel]
                if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= 255:
                    errors.append(_error(index, f"rgb.{channel} must be an integer from 0 to 255"))
            if normalized_hex and all(isinstance(rgb[channel], int) and not isinstance(rgb[channel], bool) for channel in ("r", "g", "b")):
                expected = tuple(int(normalized_hex[offset : offset + 2], 16) for offset in (1, 3, 5))
                actual = tuple(rgb[channel] for channel in ("r", "g", "b"))
                if actual != expected and not record["needs_review"]:
                    errors.append(_error(index, f"RGB {actual} does not match HEX {normalized_hex} (expected {expected})"))

        source = record["source"]
        if not isinstance(source, dict) or not isinstance(source.get("file"), str) or not source["file"].strip():
            errors.append(_error(index, "source.file must be a non-empty string"))
        if not isinstance(source, dict) or isinstance(source.get("row"), bool) or not isinstance(source.get("row"), int) or source["row"] < 1:
            errors.append(_error(index, "source.row must be a positive integer"))

        if not isinstance(record["needs_review"], bool):
            errors.append(_error(index, "needs_review must be boolean"))
        if not isinstance(record["aliases"], list) or any(not isinstance(alias, str) for alias in record["aliases"]):
            errors.append(_error(index, "aliases must be a list of strings"))

    return errors


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if len(args) != 1:
        print("Usage: validate_palette.py <palette.json>", file=sys.stderr)
        return 2
    path = Path(args[0])
    try:
        records = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"无法读取 JSON: {exc}", file=sys.stderr)
        return 2

    errors = validate_palette(records)
    if errors:
        print("颜色库校验失败：")
        print("\n".join(errors))
        return 1
    print(f"颜色库校验通过：{len(records)} 条记录")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
