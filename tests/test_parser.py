import unittest
import os
import sys

# Add scripts/ to path to import lib
sys.path.append(os.path.join(os.path.dirname(__file__), "../scripts"))

from lib.parser import parse_file, GlossaryError, SectionMissingError, FormatError

class TestParser(unittest.TestCase):
    def setUp(self):
        self.fixtures_dir = os.path.join(os.path.dirname(__file__), "fixtures")

    def test_valid_file(self):
        filepath = os.path.join(self.fixtures_dir, "valid/simple-term.md")
        data = parse_file(filepath)
        self.assertEqual(data["title"], "Simple Term")
        self.assertEqual(data["Meta"]["Category"], "Test")
        self.assertEqual(data["English (EN)"]["Status"], "Draft")

    def test_invalid_status(self):
        filepath = os.path.join(self.fixtures_dir, "invalid/bad-status.md")
        with self.assertRaises(FormatError) as cm:
            parse_file(filepath)
        self.assertIn("Invalid Status 'InProgress'", str(cm.exception))

    def test_missing_meta(self):
        filepath = os.path.join(self.fixtures_dir, "invalid/missing-meta.md")
        with self.assertRaises(SectionMissingError) as cm:
            parse_file(filepath)
        self.assertIn("Missing section: '## Meta'", str(cm.exception))

if __name__ == '__main__':
    unittest.main()
