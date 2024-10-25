import pytest

from all_lessons.functions_pytest import mens_avr_height

@pytest.mark.avr_height
def test_average_male_height_empty_dict():
    person_data = {}
    result = mens_avr_height(person_data)
    assert result == 0

@pytest.mark.avr_height
def test_average_male_height_missing_keys():
    person_data = {
        'person1': {'gender': 'Male'},
        'person2': {'height': 180}
    }
    with pytest.raises(KeyError):
        mens_avr_height(person_data)

@pytest.mark.avr_height
def test_average_male_height_invalid_gender():
    person_data = {
        'person1': {'gender': 'Other', 'height': 180},
        'person2': {'gender': 'Unknown', 'height': 170}
    }
    result = mens_avr_height(person_data)
    assert result == 0  # No valid 'Male' gender, so average should be 0

@pytest.mark.avr_height
def test_average_male_height_none_height():
    person_data = {
        'person1': {'gender': 'Male', 'height': None}
    }
    with pytest.raises(TypeError):
        mens_avr_height(person_data)