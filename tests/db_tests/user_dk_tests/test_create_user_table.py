import pytest
import allure


@allure.feature('DB tests')
@pytest.mark.user_dk
def test_create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS "user" (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INTEGER
        );
    """)
    cursor.execute("""
        SELECT table_name FROM information_schema.tables
        WHERE table_name='user';
    """)

    result = cursor.fetchone()
    assert result is not None
