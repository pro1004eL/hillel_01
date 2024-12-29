import pytest
import logging
import json


@pytest.mark.parametrize("sort_by, limit, expected_status", [
    ('brand', 10, 200),
    ('year', 3, 200),
    ('engine_volume', 7, 200),
    ('price', 5, 200)
], ids=['brand,10', 'year,3', 'engine_volume,7', 'price,5'])
def test_sort_cars_positive(car_search_request, sort_by, limit, expected_status):

    response = car_search_request(sort_by=sort_by, limit=limit)
    assert response.status_code == expected_status

    #
    formatted_response = '[\n' + ',\n'.join(
        json.dumps(car, separators=(', ', ': '), ensure_ascii=False) for car in response.json()) + '\n]'

    logging.info(f'Positive test passed: sort_by={sort_by}, limit={limit}: \n{formatted_response}')




