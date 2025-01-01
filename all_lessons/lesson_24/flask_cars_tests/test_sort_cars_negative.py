import pytest
import logging


@pytest.mark.parametrize("sort_by, limit, expected_status", [
    ('pricqwe', 5, 400),
    ('price', -1, 400),
    ('price', '', 400),
    ("", 5, 400),
    ('brand', None, 400),
    (None, None, 400)
], ids=('pricqwe,5', 'price,-1', 'price,""', '"", 5', 'brand,None', 'None, None'))
def test_sort_cars_negative(car_search_request, sort_by, limit, expected_status):

    response = car_search_request(sort_by=sort_by, limit=limit)
    assert response.status_code == expected_status

    logging.info(f'Negative test passed: sort_by={sort_by}, limit={limit}: {response.json()}')


