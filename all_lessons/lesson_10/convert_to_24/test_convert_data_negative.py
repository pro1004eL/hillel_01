import pytest

from all_lessons.functions_pytest import convert_to_24_hour

@pytest.mark.convert
class TestConvertHorsNegative:

    @pytest.mark.parametrize('input_value', [
        ('12:05'),
        ('110:31 pm'),
        ('-07:-15 pm'),
        ('07:1555 pm'),
        ('07-15 pm'),
        ('07:15 pmm')
    ])
    def test_convert_negative_hours(self, input_value):

        with pytest.raises(ValueError):
            convert_to_24_hour(input_value)

