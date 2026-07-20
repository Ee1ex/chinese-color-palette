import json
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]


class PaletteMarkdownTests(unittest.TestCase):
    def test_markdown_contains_every_json_record(self):
        records = json.loads((ROOT / "references" / "palette.json").read_text(encoding="utf-8"))
        markdown = (ROOT / "references" / "palette.md").read_text(encoding="utf-8")
        missing = [record["name_zh"] for record in records if f"| {record['name_zh']} |" not in markdown]
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
