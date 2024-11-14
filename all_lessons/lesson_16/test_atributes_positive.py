import pytest

from lesson_16.homework_16_1 import TeamLead

@pytest.mark.parametrize("name, salary, department, programming_language, team_size", [
    ('Dima', 12000, 'Development', 'Jawa', 4),
    ('Denis', 26500, 'AQA', 'Python', 20)
])
def test_teamlead_valid_department_and_prog_programming_attributes(
        name, salary, department, programming_language, team_size):

    team_lead = TeamLead(name, salary, department, programming_language, team_size)

    assert team_lead.department == department
    assert team_lead.programming_language == programming_language


