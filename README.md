# 🎨 elx-cncolor

> 中国风色卡识别与国风配色参考 skill —— 从色卡图抽取传统色名与 HEX/RGB，按色系智能选配中国风配色。

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Colors](https://img.shields.io/badge/colors-111-BC1A1A)](references/palette.json)
[![License](https://img.shields.io/badge/license-Custom-2EA44F)](LICENSE)
[![Updated](https://img.shields.io/badge/updated-2026--08-brightgreen)](https://github.com/Ee1ex/elx-cncolor)
[![Made with ❤️](https://img.shields.io/badge/made%20with-%E2%9D%A4%EF%B8%8F-ff69b4)](https://github.com/Ee1ex/elx-cncolor)

一个用于识别中国风色卡、整理传统色参数，并为设计任务提供中国风配色参考的 Agent / Codex skill。

---

## ✨ 特性

- 🖼️ **逐行识别色卡**：把色卡图片的每一行当作一条记录，识别中文颜色名 + HEX + RGB
- ✅ **程序化校验**：自动校验 HEX↔RGB 一致性，矛盾项标记 `needs_review`，绝不静默乱改
- 📚 **结构化色库**：111 条国风色，每条含 `category` 色系、`pinyin` 拼音、来源图片与行号、别名
- 🎨 **智能选色**：按「主色 / 辅色 / 强调色 / 背景 / 文字」角色，先用 `category` 锁定色系候选再挑选
- 🔧 **可维护**：内置校验、渲染、单测，一条 `make all` 守住数据质量

## 📊 色库概览

当前收录 **111** 种颜色，按色系分布如下：

| 色系 | 数量 | 色系 | 数量 |
|------|:----:|------|:----:|
| 🟢 绿 | 25 | 🔵 蓝 | 14 |
| 🔴 红 | 19 | 🟡 黄 | 9 |
| ⚪ 白 | 8 | 🟣 紫 | 7 |
| 🟠 橙 | 6 | 🟤 棕 | 4 |
| 🔘 青 | 14 | ⚫ 灰 | 3 |
| ⬛ 黑 | 2 | | |

### 🎴 部分代表色

| 颜色 | 色系 | HEX | 预览 |
|------|:----:|-----|:----:|
| 胭脂 | 红 | `#9D2932` | 🟥 |
| 竹青 | 绿 | `#789262` | 🟩 |
| 艾绿 | 绿 | `#A3E2C5` | 🟩 |
| 黛 | 蓝 | `#484163` | 🟦 |
| 月白 | 青 | `#D7ECF1` | 🟦 |
| 牙色 | 橙 | `#EFDEB0` | 🟧 |
| 青莲 | 紫 | `#7F1CAD` | 🟪 |
| 海棠红 | 红 | `#DB5A6B` | 🟥 |
| 苍色 | 青 | `#75878B` | 🟦 |
| 靛青 | 蓝 | `#177CB0` | 🟦 |

> 预览为 emoji 近似色，精确值请以 `HEX` 为准；完整 111 色见 [`references/palette.md`](references/palette.md)。

## 🚀 使用方式

将此目录作为 skill 放入 Agent / Codex 可发现的 skills 目录，然后直接提出相关请求：

```text
请从这张色卡图片中识别所有颜色名、HEX 和 RGB。
请使用中国风颜色库，为清明节湖边亭子设计一组绿色配色。
请用中国传统色为春节团圆饭场景生成配色方案，并列出每个颜色的 HEX 和 RGB。
```

当请求涉及图片取色、中国传统色、中国风 UI、国风品牌或东方审美配色时，Agent 会自动参考本库。

### 输出示例

```json
{
  "name_zh": "牙色",
  "hex": "#EFDEB0",
  "rgb": {"r": 239, "g": 222, "b": 176},
  "category": "黄",
  "pinyin": "yase",
  "source": {"file": "source.jpg", "row": 2},
  "needs_review": false,
  "aliases": []
}
```

配色建议通常包含：

| 角色 | 内容 |
|------|------|
| 主色 | 画面或界面的主要视觉色 |
| 辅色 | 补充氛围和层次的颜色 |
| 强调色 | 按钮、印章、节庆元素或视觉焦点 |
| 背景色 | 纸张感、留白或空间基底 |
| 文字色 | 保证清晰度和对比度的深色 |

## 📦 文件结构

```text
elx-cncolor/
├─ Makefile                      # 本地维护入口（validate / render / test / all）
├─ SKILL.md
├─ README.md
├─ agents/openai.yaml            # Codex 专属 UI 元数据（其他运行时忽略）
├─ references/
│  ├─ palette.json               # 机器可读色库（111 条）
│  └─ palette.md                 # 人工浏览版（含色系 + 拼音 + 别名）
└─ scripts/
   ├─ validate_palette.py        # 校验字段 / HEX / RGB / category、去重
   ├─ render_palette.py          # 由 palette.json 重新生成 palette.md
   ├─ test_validate_palette.py   # 校验逻辑单测
   ├─ test_palette_data.py       # 数据完整性单测
   └─ test_palette_markdown.py   # Markdown 与 JSON 一致性单测
```

## 🛠️ 本地维护

```bash
make validate    # 校验 palette.json 的字段 / HEX / RGB / 分类 / 重名
make render      # 重新生成 palette.md
make test        # 运行 scripts/ 下的单元测试
make all         # 依次执行 validate -> render -> test
```

也可单独运行 Python 脚本：

```bash
python scripts/validate_palette.py references/palette.json
python scripts/render_palette.py
python -m unittest discover -s scripts -p "test_*.py"
```

## 📖 数据字段说明

- 颜色名默认保留图片中的原始中文名称。
- `category` 由 HEX 色相自动推导，用于按色系筛选，不代表文化考据分类。
- `pinyin` 为颜色名拼音（离线静态生成），用于拼音检索，不影响原始色名。
- `HEX` 统一使用大写 `#RRGGBB` 格式。
- `RGB` 顺序固定为 `R, G, B`。
- `needs_review: true` 表示图片内容存在低清、歧义或 HEX/RGB 矛盾，使用时应提示人工复核。
- 同名异色（如两个来源都叫「黛」但 HEX 不同）属正常情况，校验会给出提醒但不报错；必要时可在 `aliases` 中标注区分。
- 当前色库来自提供的色卡图片，不等同于完整的中国传统色标准库。

## 🤝 许可证

本项目中的 skill、脚本和整理后的颜色数据用于个人与项目内的设计辅助。图片及原始色卡内容的权利归其相应权利人所有。

---

<p align="center">Made with ❤️ for 中国风设计 · <a href="https://github.com/Ee1ex/elx-cncolor">elx-cncolor</a></p>
