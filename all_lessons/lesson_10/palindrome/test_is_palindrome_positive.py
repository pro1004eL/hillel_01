import pytest

from all_lessons.functions_pytest import is_palindrome

@pytest.mark.palindrome
@pytest.mark.parametrize('input_value, expected_result', [
    ('SOS', True),
    ('11-11', True),
    ('Tom Felton', False),
    ('', True),
    ('####-####', True),
    ('$-#', False)
])

def test_is_palindrome_positive(input_value, expected_result):
    assert is_palindrome(input_value) == expected_result
