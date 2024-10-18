import unittest
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.parent))

from all_lessons.lesson_09.homeworks_functions import matching_cars

class SearchCarsPositiveTest(unittest.TestCase):

    def test_matching_cars(self):
        actual_result = matching_cars(2021, 3, 50000)
        expected_result = [
            ('Jeep', 'green', 2021, 3.0, 'suv', 50000),
            ('Ford F-Series', 'gray', 2021, 3.5, 'pickup', 50000)
        ]

        self.assertListEqual(actual_result, expected_result)

    def test_no_matching_cars(self):
        actual_result = matching_cars(2022, 4.5, 25000)
        expected_result = 'No matching cars'

        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)


