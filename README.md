# Chinese Color Palette

一个用于识别中国风色卡、整理传统色参数，并为设计任务提供中国风配色参考的 Codex skill。

## 主要作用

- 从色卡图片中逐行识别中文颜色名。
- 提取对应的 `HEX` 和 `RGB` 参数。
- 校验 `HEX` 与 `RGB` 是否一致。
- 保存颜色来源图片和行号，便于复核。
- 在中国风、国风、东方审美、传统色、古典配色等任务中提供可直接使用的色板。
- 对无法确认或图片数据矛盾的记录标记 `needs_review: true`。

## 适用场景

可以用于：

- 中国风网页、App 和品牌视觉设计。
- 国风海报、插画、封面和社交媒体图片。
- 古典建筑、节气、节庆和传统文化主题配色。
- 从已有色卡图片建立结构化颜色库。
- 为 AI 图像生成提供准确的中国风颜色参考。

## 使用方式

将此目录放入 Codex 可发现的 skills 目录，然后直接提出相关请求。例如：

```text
请从这张色卡图片中识别所有颜色名、HEX 和 RGB。
```

```text
请使用中国风颜色库，为清明节湖边亭子设计一组绿色配色。
```

```text
请用中国传统色为春节团圆饭场景生成配色方案，并列出每个颜色的 HEX 和 RGB。
```

当请求涉及图片取色、中国传统色、中国风 UI、国风品牌或东方审美配色时，Codex 可以自动参考本 skill 的颜色库。

## 输出示例

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

配色建议通常包含：

| 角色 | 内容 |
|---|---|
| 主色 | 画面或界面的主要视觉色 |
| 辅色 | 补充氛围和层次的颜色 |
| 强调色 | 按钮、印章、节庆元素或视觉焦点 |
| 背景色 | 纸张感、留白或空间基底 |
| 文字色 | 保证清晰度和对比度的深色 |

## 文件结构

```text
chinese-color-palette/
├─ SKILL.md
├─ README.md
├─ agents/openai.yaml
├─ references/
│  ├─ palette.json
│  └─ palette.md
└─ scripts/
   ├─ validate_palette.py
   └─ render_palette.py
```

### `references/palette.json`

完整的机器可读颜色库，包含颜色名、HEX、RGB、来源、别名和复核状态。

### `references/palette.md`

完整的人工浏览版颜色索引。

### `scripts/validate_palette.py`

检查颜色记录的字段、HEX 格式、RGB 范围以及 HEX 与 RGB 的一致性：

```powershell
python scripts/validate_palette.py references/palette.json
```

### `scripts/render_palette.py`

根据 `palette.json` 重新生成 `references/palette.md`：

```powershell
python scripts/render_palette.py
```

## 数据说明

- 颜色名默认保留图片中的原始中文名称。
- `HEX` 统一使用大写 `#RRGGBB` 格式。
- `RGB` 顺序固定为 `R, G, B`。
- `needs_review: true` 表示图片内容存在低清、歧义或 HEX/RGB 矛盾，使用时应提示人工复核。
- 当前色库来自提供的色卡图片，不等同于完整的中国传统色标准库。

## License

本项目中的 skill、脚本和整理后的颜色数据用于个人与项目内的设计辅助。图片及原始色卡内容的权利归其相应权利人所有。
