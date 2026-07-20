"""Render the complete Markdown index from palette.json."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path("..").resolve()
JSON_PATH = ROOT / "references" / "palette.json"
MARKDOWN_PATH = ROOT / "references" / "palette.md"


def render(records: list[dict]) -> str:
    lines = [
        "# 中国风颜色参考库",
        "",
        "`palette.json` 是完整的机器读取源，包含来自 10 张色卡图片的全部去重记录、HEX、RGB、来源和待复核状态。",
        "",
        "| 颜色 | HEX | RGB | 来源 | 状态 |",
        "|---|---|---|---|---|",
    ]
    for record in records:
        rgb = record["rgb"]
        source = record["source"]
        status = "待复核" if record["needs_review"] else "已校验"
        lines.append(
            f"| {record['name_zh']} | `{record['hex']}` | "
            f"`{rgb['r']}, {rgb['g']}, {rgb['b']}` | "
            f"`{source['file']}:{source['row']}` | {status} |"
        )
    lines.extend([
        "",
        "## 使用说明",
        "",
        "- 完整记录、别名和图片来源以 `palette.json` 为准。",
        "- `needs_review: true` 的记录只能作为候选，输出时要提示人工复核。",
        "- RGB 的顺序固定为 `R, G, B`。",
    ])
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    records = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    MARKDOWN_PATH.write_text(render(records), encoding="utf-8")
