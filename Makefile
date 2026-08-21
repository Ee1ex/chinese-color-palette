# 中国风颜色参考库 — 本地维护入口
# 用法（在 elx-cncolor/ 目录下）：
#   make validate   校验 palette.json 的字段 / HEX / RGB / 分类 / 重名
#   make render     由 palette.json 重新生成 palette.md
#   make test       运行 scripts/ 下的单元测试
#   make all        依次执行 validate -> render -> test

PY ?= python

.PHONY: validate render test all

validate:
	$(PY) scripts/validate_palette.py references/palette.json

render:
	$(PY) scripts/render_palette.py

test:
	$(PY) -m unittest discover -s scripts -p "test_*.py"

all: validate render test
