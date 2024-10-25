import pytest

from all_lessons.functions_pytest import word_count


@pytest.mark.word_count
@pytest.mark.parametrize('input_value', [
    (16),
    (-25),
    (None),
    (['good', 'Harry Potter', 'UGLY']),
    ({}),
    ([]),
    #((''))
])

def test_word_counting_negative(input_value):
    with pytest.raises(AttributeError):
        word_count(input_value)
