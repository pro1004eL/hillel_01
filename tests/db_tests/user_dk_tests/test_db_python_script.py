import pytest
import allure


@allure.feature('DB tests')
@pytest.mark.user_dk
def test_database_connection(connector):

    print("Connected to the database!")
    assert connector is not None


@allure.feature('DB tests')
@pytest.mark.user_dk
def test_add_new_user(cursor):

    cursor.execute("""INSERT INTO "user" (name, age) VALUES (%s, %s) RETURNING id;""", ("Anton", 20))
    user_id = cursor.fetchone()[0]

    assert user_id is not None, "Failed to insert the user"

    cursor.execute("SELECT name, age FROM \"user\" WHERE id = %s;", (user_id,))
    result = cursor.fetchone()

    assert result == ("Anton", 20), f"Expected ('Anton', 20), but got {result}"


@allure.feature('DB tests')
@pytest.mark.user_dk
def test_update_user(cursor):

    cursor.execute("""UPDATE "user" SET age = %s WHERE name = %s RETURNING id;""", (33, "Anton"))

    user_id = cursor.fetchone()[0]
    assert user_id is not None


@allure.feature('DB tests')
@pytest.mark.user_dk
def test_delete_user(cursor):
    cursor.execute("""
        DELETE FROM "user" WHERE name = %s RETURNING id;
    """, ("Anton",))

    deleted_id = cursor.fetchone()[0]
    assert deleted_id is not None


@allure.feature('DB tests')
@pytest.mark.user_dk
def test_get_sample_data(cursor):

    with allure.step("Execute query to fetch sample data"):
        cursor.execute("SELECT * FROM \"user\" LIMIT 1;")

    with allure.step("Retrieve the first record from the result"):
        student = cursor.fetchone()

    with allure.step("Validate that fetching data works"):
        if student is not None:
            print(f"Student data retrieved: {student}")
        else:
            print("The 'user' table is empty.")


