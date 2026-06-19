import pytest

from tasks.loops.task3 import count_negatives


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, -1, -7, 0, 5, -2], 3),
        ([1, 2, 3], 0),
        ([-1, -2, -3], 3),
        ([], 0),
        ([0, 0, 0], 0),  # ноль не отрицательный
    ],
)
def test_count_negatives(nums, expected):
    assert count_negatives(nums) == expected
