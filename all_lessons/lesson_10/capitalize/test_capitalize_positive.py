import pytest

from all_lessons.functions_pytest import capitalize_text

@pytest.mark.capitalize
@pytest.mark.parametrize('input_value, expected_result', [
    ('good Bad UGLY', 'Good Bad Ugly'),
    ('run< Forest, rUN', 'Run< Forest, Run'),
    ('123 tom & jerry', '123 Tom & Jerry'),
    ('$rr', '$Rr')
])

def test_capitalize_positive_text(input_value, expected_result):
    assert capitalize_text(input_value) == expected_result