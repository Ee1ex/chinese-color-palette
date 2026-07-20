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
        }
        self.assertTrue(any("RGB" in error for error in validate_palette([record])))


if __name__ == "__main__":
    unittest.main()
