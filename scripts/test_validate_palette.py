import unittest

from validate_palette import validate_palette


class PaletteValidationTests(unittest.TestCase):
    def test_accepts_matching_hex_and_rgb(self):
        record = {
            "name_zh": "牙色",
            "hex": "#EFDEB0",
            "rgb": {"r": 239, "g": 222, "b": 176},
            "source": {"file": "sample.jpg", "row": 2},
            "needs_review": False,
            "aliases": [],
            "category": "黄",
        }
        self.assertEqual(validate_palette([record]), [])

    def test_rejects_mismatched_rgb(self):
        record = {
            "name_zh": "牙色",
            "hex": "#EFDEB0",
            "rgb": {"r": 0, "g": 0, "b": 0},
            "source": {"file": "sample.jpg", "row": 2},
            "needs_review": False,
            "aliases": [],
            "category": "黄",
        }
        self.assertTrue(any("RGB" in error for error in validate_palette([record])))

    def test_rejects_invalid_category(self):
        record = {
            "name_zh": "牙色",
            "hex": "#EFDEB0",
            "rgb": {"r": 239, "g": 222, "b": 176},
            "source": {"file": "sample.jpg", "row": 2},
            "needs_review": False,
            "aliases": [],
            "category": "彩虹",
        }
        self.assertTrue(any("category" in error for error in validate_palette([record])))

    def test_warns_on_same_name_different_hex(self):
        from validate_palette import find_duplicate_names

        records = [
            {"name_zh": "黛", "hex": "#494166", "rgb": {"r": 73, "g": 65, "b": 102},
             "source": {"file": "a.jpg", "row": 1}, "needs_review": False, "aliases": [], "category": "紫"},
            {"name_zh": "黛", "hex": "#484163", "rgb": {"r": 72, "g": 65, "b": 99},
             "source": {"file": "b.jpg", "row": 1}, "needs_review": False, "aliases": [], "category": "紫"},
        ]
        warnings = find_duplicate_names(records)
        self.assertTrue(any("同名异色" in w for w in warnings))


if __name__ == "__main__":
    unittest.main()
