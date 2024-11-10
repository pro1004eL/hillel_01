import pytest

from all_lessons.lesson_15.homework_15_1 import Rhombus

@pytest.mark.parametrize("side_a, expected_error", [
    ('0', TypeError),
    (-1, ValueError),
    (0, ValueError),
    (None, TypeError)
], ids=['string_value','negative_value', '0', 'None'])

def test_rhombus_invalid_side_a(side_a, expected_error):
    with pytest.raises(expected_error):
        Rhombus(side_a, 10)

@pytest.mark.parametrize("angle_a, expected_error", [
    (0, ValueError),
    (180, ValueError),
    ('10', TypeError),
    (-10, ValueError),
    (None, TypeError)
], ids=['0', '180', 'string value', 'negative value', 'None'])

def test_rhombus_invalid_angle_a(angle_a, expected_error):
    with pytest.raises(expected_error):
        Rhombus(5, angle_a)

def test_rhombus_cannot_set_corner_b():
    rhombus = Rhombus(5, 60)
    with pytest.raises(AttributeError):
        rhombus.angle_b = 40

