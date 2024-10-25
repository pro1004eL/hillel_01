import pytest

from all_lessons.functions_pytest import string_methods


@pytest.mark.string_methods
@pytest.mark.parametrize('input_value, method', [
    (0, 'upper'),
    (None, 'upper'),
    (3, 'lower'),
    (None, 'lower')
])

def test_method_upper_negative(input_value, method):
    with pytest.raises(AttributeError):
        string_methods(input_value, method)

@pytest.mark.parametrize("input_value, prefix, expected_output", [
    ("Harry Potter", "Potter", False),
    ('Tom Riddle', 'Riddle', False)
])
def test_startswith(input_value, prefix, expected_output):
    result = string_methods(input_value, "startswith", prefix)
    assert result == expected_output

def test_endswith_negative():
    result = string_methods("Ron Weasley", "endswith", "Ron")
    assert result is False