import pytest

from all_lessons.functions_pytest import mens_avr_height, person_data

@pytest.mark.avr_height
def test_avr_male_height_gender_mixed():
    result = mens_avr_height(person_data)
    assert result == 178.0

@pytest.mark.avr_height
def test_avr_male_height_only_males():
    person_data = {
        'person1': {'gender': 'Male', 'height': 180},
        'person2': {'gender': 'Male', 'height': 190},
    }
    result = mens_avr_height(person_data)
    assert result == 185.0

@pytest.mark.avr_height
def test_avr_male_height_no_males():
    person_data = {
        'person1': {'gender': 'Female', 'height': 170},
        'person2': {'gender': 'Female', 'height': 165}
    }
    result = mens_avr_height(person_data)
    assert result == 0  # No males, so average should be 0

