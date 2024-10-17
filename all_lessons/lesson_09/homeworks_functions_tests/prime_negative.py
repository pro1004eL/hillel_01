import unittest
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.parent))

from all_lessons.lesson_09.homeworks_functions import find_primes

class TestFindPrimeNegative(unittest.TestCase):

    def test_prime_minus_10(self):
        actual_result = find_primes(-10)
        expected_result = []

        self.assertEqual(actual_result, expected_result)

    def test_prime_put_str_type(self):

        with self.assertRaises(TypeError):
            actual_result = find_primes('20')

    def test_prime_put_float_type(self):

        with self.assertRaises(TypeError):
            find_primes(10.5)


if __name__ == '__main__':
    unittest.main(verbosity=2)


