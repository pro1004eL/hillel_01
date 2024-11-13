import pytest
from lesson_16.homework_16_1 import TeamLead


@pytest.mark.parametrize("name, salary, department, programming_language, team_size", [
    ('Dima', 12000, "", "Jawa", 4),
    ('Denis', 26500, None, "Python", 20),
    ('Aleks', 3, +100500, "JS", 34),
    ('Obelix', 10500, None, 123, 12),
    ('Petro', 1000, -2, "Python", 2),
    ('Galya', 1000, 'QA', '', 1),
])
def test_teamlead_invalid_department_and_prog_programming_attributes(
        name, salary, department, programming_language, team_size):

    with pytest.raises(AssertionError):
        TeamLead(name, salary, department, programming_language, team_size)

