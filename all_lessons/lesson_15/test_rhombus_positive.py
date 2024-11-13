import pytest

from all_lessons.lesson_15.homework_15_1 import Rhombus


@pytest.mark.parametrize("side_a, angle_a, expected_angle_b", [
    (1, 1, 179),
    (10, 90, 90),
    (3, 45, 135)
])

def test_rhombus_positive_values(side_a, angle_a, expected_angle_b):
    rhombus = Rhombus(side_a, angle_a)
    assert rhombus.side_a == side_a
    assert rhombus.angle_a == angle_a
    assert rhombus.angle_b == expected_angle_b



