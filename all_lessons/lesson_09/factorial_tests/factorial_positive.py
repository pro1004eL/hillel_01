import unittest

import sys
import pathlib

# шлях до файлу test_function
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.parent))

from test_functions import factorial


class FactorialPositiveTest(unittest.TestCase):

    def test_factorial_5(self):
        actual_result = factorial(5)
        expected_result = 120

        self.assertEqual(actual_result, expected_result)

    def test_factorial_0(self):
        actual_result = factorial(0)
        expected_result = 1

        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
