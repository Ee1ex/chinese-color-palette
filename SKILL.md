---
name: chinese-color-palette
description: Use when extracting color names and HEX/RGB values from color-table images, selecting Chinese traditional colors, creating Chinese-style palettes, or referencing Chinese-inspired colors for UI, branding, illustration, slides, and visual design.
---

# 中国风颜色识别与参考

## 核心原则

把色卡图片中的“每一行”当作一条颜色记录处理，不把整张图片的主色当作结果。颜色名保留图片原文；HEX 与 RGB 必须互相校验；无法确认的值必须明确标记待复核。

## 识别图片中的颜色

1. 先确认表头和列顺序，通常为 `颜色 / HEX格式 / R / G / B`。
2. 按行读取 `name_zh`、`hex`、`rgb`，忽略表头和装饰水印。
3. 记录来源图片文件名与从 1 开始的数据行号。
4. 规范化 HEX 为大写 `#RRGGBB`，把 RGB 保留为 0–255 整数。
5. 用 HEX 重新计算 RGB；不一致时保留图片显示值，并设置 `needs_review: true`，不得静默修正。
6. 输出记录时使用：

```json
{
  "name_zh": "牙色",
  "hex": "#EFDEB0",
  "rgb": {"r": 239, "g": 222, "b": 176},
  "source": {"file": "source.jpg", "row": 2},
  "needs_review": false,
  "aliases": []
}
```

新增或修改色库后，运行 `scripts/validate_palette.py references/palette.json`。只有已标记 `needs_review` 的截图矛盾记录可以保留不一致；其他记录必须通过 HEX↔RGB 校验。

## 选择中国风配色

需要中国风、国风、东方审美、传统色或古典配色时，先读取 `references/palette.json`，再按任务选择 3–6 个角色：主色、辅色、强调色、背景色、文字色。优先使用库内原始颜色名，并同时给出 HEX 和 RGB。

- 红、朱、胭脂、绯等暖色适合节庆、印章、强调和视觉焦点。
- 黛、玄青、墨、藏青等深色适合文字、边框、沉稳背景和高对比层级。
- 牙色、月白、缟、茶白、素等浅色适合纸张感背景和留白。
- 竹青、艾绿、铜绿、石青、松柏绿等青绿色适合自然、雅致和文人气质。
- 丁香色、青莲、雪青等紫色适合点缀，不要在没有理由时大面积使用。

检查文字与背景的明度差；品牌色或既有设计令牌优先于本库。库内没有直接匹配时，明确说明并给出最接近候选，不要伪造库内记录。

## 输出格式

识别任务输出：颜色名、HEX、RGB、来源和待复核状态。配色任务输出：颜色角色、颜色名、HEX、RGB、使用场景，以及待复核提示（如有）。

机器读取源：`references/palette.json`；人工浏览源：`references/palette.md`。
