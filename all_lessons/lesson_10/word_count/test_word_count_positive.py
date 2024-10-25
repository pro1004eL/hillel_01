import pytest

from all_lessons.functions_pytest import word_count


@pytest.mark.word_count
@pytest.mark.parametrize('input_value, expected_result', [
    ('good bad ugly', 3),
    ('22 good good NEW Com-Service', 5),
    ('% - @ $', 4),
    ('', 0)
])

def test_word_counting_positive(input_value, expected_result):
    assert word_count(input_value) == expected_result


