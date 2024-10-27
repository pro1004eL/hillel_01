import logging
import pytest

from all_lessons.lesson_11.log_event_function import log_event

@pytest.mark.log_event
@pytest.mark.parametrize('user_name, status, log_level', [
    ('Joe', 'success', 'ERROR'),
    ('Inna', 'expired', 'INFO'),
    ('Ross', 'failed', 'WARNING'),
    ('Ira', None, 'INFO'),
    (123, 21312, 'WARNING')
])

def test_log_event_incorrect_log_level(user_name, status, log_level):


    log_event(user_name, status)

    with open('login_system.log') as log_file:
        log_lines = log_file.readlines()

    assert len(log_lines) > 0

    last_login = log_lines[-1].strip()

    expected_result = f'Login event - Username: {user_name}, Status: {status} - {log_level}'

    assert expected_result not in last_login


