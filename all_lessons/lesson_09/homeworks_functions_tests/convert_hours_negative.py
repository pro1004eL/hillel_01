import unittest
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.parent))

from all_lessons.lesson_09.homeworks_functions import convert_to_24_hour

class TestConvertHoursNegative(unittest.TestCase):

    def test_convert_hours_12_00_without_period(self):

        with self.assertRaises(ValueError):
            convert_to_24_hour('12:00')

    def test_convert_hours_incorrect_format(self):

        with self.assertRaises(ValueError):
            convert_to_24_hour('07-15 pm')

    def test_convert_put_357_hours(self):

        with self.assertRaises(ValueError):
            convert_to_24_hour('357:15 pm')

    def test_convert_put_1555_minutes(self):

        with self.assertRaises(ValueError):
            convert_to_24_hour('07:1555 pm')

    def test_convert_put_negativ_hours_minutes(self):

        with self.assertRaises(ValueError):
            convert_to_24_hour('-07:-15 pm')

    def test_convert_put_pmm_period(self):

        with self.assertRaises(ValueError):
            convert_to_24_hour('07:15 pmm')



if __name__ == '__main__':
    unittest.main(verbosity=2)