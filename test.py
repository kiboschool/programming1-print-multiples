from unittest.mock import patch
from unittest import TestCase
import unittest
import sys
import io

class Test(TestCase):
    def test_first_ten_lines(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            import main

            expected_lines = """1
2
3 is a multiple of 3
4
5 is a multiple of 5
6 is a multiple of 3
7
8
9 is a multiple of 3
10 is a multiple of 5""".split("\n")

            actual_lines = mock_stdout.getvalue().split("\n")
            for i, expected in enumerate(expected_lines):
                self.assertEqual(expected, actual_lines[i])

            sys.modules.pop('main')

if __name__ == '__main__':
    unittest.main()
