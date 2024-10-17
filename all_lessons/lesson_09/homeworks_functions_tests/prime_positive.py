import unittest
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.parent))

from all_lessons.lesson_09.homeworks_functions import find_primes

class TestFindPrimePositive(unittest.TestCase):

    def test_prime_10(self):
        actual_result = find_primes(25)
        expected_result = [2, 3, 5, 7, 11, 13, 17, 19, 23]

        self.assertListEqual(actual_result, expected_result)

    def test_prime_0(self):
        actual_result = find_primes(0)
        expected_result = []

        self.assertListEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)


