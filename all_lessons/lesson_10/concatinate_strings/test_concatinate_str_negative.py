import pytest

from all_lessons.functions_pytest import concatenate_strings


@pytest.mark.concatinate_lst
@pytest.mark.parametrize('input_value', [
    (['test', 5]),
    (['1', '2', ['1', '2']]),
    (-2),
    (None),
    ([{'word', 'word2'}])
])

def test_concotinate_str_with_negative_values(input_value):
    with pytest.raises(TypeError):
        concatenate_strings(input_value)
