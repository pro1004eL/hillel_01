import unittest

def sum_2_numbers(a, b):
    return a + b


class MyTest(unittest.TestCase):

    def test_sum_1_2(self):
        actual_result = sum_2_numbers(2, 2)
        expected_result = 4

        self.assertEqual(actual_result, expected_result)

    def test_sum_3_4(self):
        actual_result = sum_2_numbers(3, 4)
        expected_result = 7

        assert actual_result == expected_result

    def test_compare_2_lists_with_dicts(self):
        expected_list = [
            {
                'Name': 'Anton',
                'Age': 33,
                'Position': 'QA'
            },
            {
                'Name': 'Tom',
                'Age': 23,
                'Position': 'QA'
            },
            {
                'Name': 'Den',
                'Age': 24,
                'Position': 'QA'
            }
        ]
        actual_list = [
            {
                'Name': 'Anton',
                'Age': 33,
                'Position': 'QA'
            },
            {
                'Name': 'Den',
                'Age': 34,
                'Position': 'AQA'
            },
            {
                'Name': 'Ivan',
                'Age': 34,
                'Position': 'QA'
            },
        ]

        self.assertNotEqual(actual_list, expected_list)

    def test_almost_equal(self):

        self.assertAlmostEqual(4, 6, delta=3) # 6 between 4-3 and 4+3

if __name__ == '__main__':
    unittest.main()
