import pytest

from all_lessons.functions_pytest import concatenate_strings

@pytest.mark.concatinate_lst
@pytest.mark.parametrize('input_value, expected_result', [
    (['1', '2', '3'], '1 2 3'),
    (['World', 'wide', 'web!'], 'World wide web!'),
    ([''], '')
])

def test_concatinate_lst_positive_values(input_value, expected_result):
    assert concatenate_strings(input_value) == expected_result