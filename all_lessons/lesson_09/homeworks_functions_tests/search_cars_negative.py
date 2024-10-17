import unittest
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.parent))

from all_lessons.lesson_09.homeworks_functions import matching_cars



class SearchCarsNegativeTest(unittest.TestCase):

    def test_negative_price_value(self):
        actual_result = matching_cars(2021, 3, -50000)
        expected_result = 'No matching cars'

        self.assertEqual(actual_result, expected_result)

    def test_negative_values(self):
        actual_result = matching_cars(-2019, -1.6, -35000)
        expected_result = 'No matching cars'

        self.assertEqual(actual_result, expected_result)

    def test_string_year_matching_type(self):

        with self.assertRaises(TypeError):
            matching_cars(2019, 1.6, '35000')

    def test_str_matching_types(self):

        with self.assertRaises(TypeError):
            matching_cars('2017', '2.5', '40000')

    def test_zero_matching_values(self):
        actual_result = matching_cars(0, 0, 0)
        expected_result = 'No matching cars'

        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main(verbosity=3)