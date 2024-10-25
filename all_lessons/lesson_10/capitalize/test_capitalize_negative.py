import pytest

from all_lessons.functions_pytest import capitalize_text

@pytest.mark.capitalize
@pytest.mark.parametrize('input_value', [
    (555, 456),
    (0),
    ([]),
    ({}),
    (None),
    ('')
])

def test_capitalize_negative_values(input_value):

    with pytest.raises(AttributeError):
        capitalize_text(input_value)