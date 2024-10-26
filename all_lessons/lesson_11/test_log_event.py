import logging
import pytest

from all_lessons.lesson_11.log_event_function import log_event

@pytest.mark.log_event
@pytest.mark.parametrize('user_name, status, log_level', [
    ('Anton', 'success', 'INFO'),
    ('Tom', 'expired', 'WARNING'),
    ('Harry', 'failed', 'ERROR'),
    ('Ron', None, 'ERROR')
])

def test_log_event_different_status(user_name, status, log_level):

    log_event(user_name, status)

    with open('login_system.log') as log_file:
        log_lines = log_file.readlines()

    assert len(log_lines) > 0

    last_login = log_lines[-1].strip()

    expected_result = f'Login event - Username: {user_name}, Status: {status} - {log_level}'

    assert expected_result in last_login



