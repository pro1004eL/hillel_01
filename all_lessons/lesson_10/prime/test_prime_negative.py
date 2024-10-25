import pytest
import logging

from all_lessons.functions_pytest import find_primes

@pytest.mark.prime
@pytest.mark.negative
@pytest.mark.parametrize('number, expected_result', [
    ('0', TypeError),
    (None, TypeError)
], ids=['string value', 'None value'])
def test_prime_negative(number, expected_result):

    with pytest.raises(expected_result):
        find_primes(number)

