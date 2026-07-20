import json
import unittest
from pathlib import Path

from validate_palette import validate_palette


ROOT = Path(__file__).parents[1]


class PaletteDataTests(unittest.TestCase):
    def test_reference_library_is_valid_and_nonempty(self):
        records = json.loads((ROOT / "references" / "palette.json").read_text(encoding="utf-8"))
        self.assertGreater(len(records), 0)
        self.assertEqual(validate_palette(records), [])


if __name__ == "__main__":
    unittest.main()
