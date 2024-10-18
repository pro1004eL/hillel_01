import unittest
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent.parent))

from all_lessons.lesson_09.homeworks_functions import convert_to_24_hour

class TestConvertHoursPositive(unittest.TestCase):

    def test_convert_hours_12_00pm(self):
        actual_result = convert_to_24_hour('12:00 pm')
        expected_result = '12:00'

        self.assertEqual(actual_result, expected_result)

    def test_convert_hours_12_00am(self):
        actual_result = convert_to_24_hour('12:00 am')
        expected_result = '00:00'

        self.assertEqual(actual_result, expected_result)



if __name__ == '__main__':
    unittest.main(verbosity=2)


