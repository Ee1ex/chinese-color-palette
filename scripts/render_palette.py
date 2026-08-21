"""Render the complete Markdown index from palette.json."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "references" / "palette.json"
MARKDOWN_PATH = ROOT / "references" / "palette.md"


def render(records: list[dict]) -> str:
    image_count = len({record["source"]["file"] for record in records})
    review_count = sum(1 for record in records if record.get("needs_review"))
    lines = [
        "# 中国风颜色参考库",
        "",
        f"`palette.json` 是完整的机器读取源，包含来自 {image_count} 张色卡图片的 "
        f"{len(records)} 条去重记录、HEX、RGB、色系、来源和待复核状态（其中 {review_count} 条待复核）。",
        "",
        "| 颜色 | 拼音 | 色系 | HEX | RGB | 来源 | 别名 / 备注 | 状态 |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for record in records:
        rgb = record["rgb"]
        source = record["source"]
        status = "待复核" if record.get("needs_review") else "已校验"
        pinyin = record.get("pinyin") or "—"
        aliases = "、".join(record.get("aliases", [])) or "—"
        lines.append(
            f"| {record['name_zh']} | {pinyin} | {record.get('category', '—')} | `{record['hex']}` | "
            f"`{rgb['r']}, {rgb['g']}, {rgb['b']}` | "
            f"`{source['file']}:{source['row']}` | {aliases} | {status} |"
        )
    lines.extend([
        "",
        "## 使用说明",
        "",
        "- 完整记录、别名和图片来源以 `palette.json` 为准。",
        "- `pinyin` 为颜色名拼音（离线静态生成，便于检索），`category` 由 HEX 色相自动推导，仅用于按色系筛选。",
        "- `needs_review: true` 的记录只能作为候选，输出时要提示人工复核。",
        "- RGB 的顺序固定为 `R, G, B`。",
    ])
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    records = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    MARKDOWN_PATH.write_text(render(records), encoding="utf-8")
    print(f"已重新生成 {MARKDOWN_PATH.name}（{len(records)} 条记录）")
