import pytest

from all_lessons.functions_pytest import is_palindrome

@pytest.mark.palindrome
@pytest.mark.parametrize('input_value', [
    (2024),
    (None),
    ([])
])

def test_is_palindrome_negative(input_value):
    with pytest.raises(TypeError):
        is_palindrome(input_value)