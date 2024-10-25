import pytest

from all_lessons.functions_pytest import string_methods


@pytest.mark.string_methods
@pytest.mark.parametrize('input_value, expected_result', [
    ('tom', 'TOM'),
    ('ToM', 'TOM'),
    ('333', '333'),
    ('$3', '$3'),
    ('', '')
])

def test_method_upper_positive(input_value, expected_result):
    actual_result = string_methods(input_value,'upper')
    assert actual_result == expected_result

@pytest.mark.parametrize('input_value, expected_result', [
    ('ToM', 'tom'),
    ('555Tom', '555tom'),
    ('$3', '$3'),
    ('', '')
])

def test_method_lower_positive(input_value, expected_result):
    actual_result = string_methods(input_value,'lower')
    assert actual_result == expected_result


def test_method_startswith_positive():
    actual_result = string_methods('Tom Riddle', 'startswith', 'Tom')
    assert actual_result is True

def test_method_endswith_positive():
    actual_result = string_methods('Tom Riddle', 'endswith', 'Riddle')
    assert actual_result is True