import pytest
import logging

from all_lessons.functions_pytest import convert_to_24_hour

@pytest.mark.convert
class TestConvertHorsPositive:

    @pytest.mark.parametrize('input_value,expected_result', [
        ('12:00 pm', '12:00'),
        ('12:00 am', '00:00'),
        pytest.param('00:01 am', '00:01', marks = pytest.mark.xfail (reason = 'know issue xfail'))
    ])
    def test_convert_am_hours(self, input_value, expected_result):
        actual_r = convert_to_24_hour(input_value)
        logging.info(f'actual {input_value}, expected {expected_result}')
        assert actual_r == expected_result

