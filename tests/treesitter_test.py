import unittest

from pathlib2 import Path

from src.code_processing.treesitter import process_identifiers, setup_tree_sitter_parser


class TreeSitterTest(unittest.TestCase):
    def test_identifiers(self):
        setup_tree_sitter_parser()
        path_to_file = str(Path(f"{Path.cwd()}/test_files/qwerty.java"))
        print(path_to_file)
        code_info = process_identifiers(path_to_file, "java")
        print(code_info)
        self.assertEqual(code_info["classes"]["Employee"], 1, "Found one class")


if __name__ == '__main__':
    unittest.main()
