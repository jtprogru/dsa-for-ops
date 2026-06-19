import pytest

from tasks.loops.task2 import range_to_list


@pytest.mark.parametrize(
    "start, stop, step, expected",
    [
        (0, 101, 17, [0, 17, 34, 51, 68, 85]),
        (0, 5, 1, [0, 1, 2, 3, 4]),
        (0, 10, 3, [0, 3, 6, 9]),
        (5, 5, 1, []),  # пустой полуинтервал
        (10, 0, -2, [10, 8, 6, 4, 2]),
    ],
)
def test_range_to_list(start, stop, step, expected):
    assert range_to_list(start, stop, step) == expected
