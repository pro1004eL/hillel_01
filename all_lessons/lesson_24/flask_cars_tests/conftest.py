import pytest
import time
import requests
from requests.auth import HTTPBasicAuth
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True,
    handlers=[
        logging.FileHandler("test_search.log"),
        logging.StreamHandler()
    ]
)


@pytest.fixture(scope="session")
def base_url():
    print('SetUp of base_url fixture')
    yield 'http://127.0.0.1:8080'
    print('Teardown of base_url fixture')


@pytest.fixture(scope='session')
def auth_headers(base_url):
    token = requests.post(url=f'{base_url}/auth',
                          auth=requests.auth.HTTPBasicAuth(username='test_user', password='test_pass'))

    return token.json()['access_token']


@pytest.fixture(scope='session')
def car_search_request(auth_headers, base_url):
    def car_search(sort_by=None, limit=None):

        params = {}

        if sort_by is not None:
            params['sort_by'] = sort_by
        if limit is not None:
            params['limit'] = limit

        response = requests.get(url=f'{base_url}/cars',
                                headers={'Authorization': f'Bearer {auth_headers}'}, params=params)
        return response

    return car_search


@pytest.fixture(scope='session', autouse=True)
def timing_of_all_tests():
    start_time = time.time()
    yield
    print(f"Time of all tests is {time.time() - start_time}")




