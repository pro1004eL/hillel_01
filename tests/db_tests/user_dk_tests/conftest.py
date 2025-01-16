import os
import pytest
import psycopg2


@pytest.fixture()
def connector():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )
    yield conn
    conn.close()


@pytest.fixture()
def cursor(connector):
    cursor = connector.cursor()
    yield cursor
    connector.commit()
    cursor.close()

