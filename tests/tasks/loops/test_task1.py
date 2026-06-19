import pytest

from tasks.loops.task1 import min_adjacent_pair


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([10, 3, 8, 1, 9, 4], (2, 9)),
        ([1, 2], (0, 3)),
        ([5, 5, 5], (0, 10)),  # при равенстве берём самую левую пару
        ([4, 1, 1, 4], (1, 2)),
        ([-3, -4, 10, 10], (0, -7)),
    ],
)
def test_min_adjacent_pair(nums, expected):
    assert min_adjacent_pair(nums) == expected


@pytest.mark.parametrize("nums", [[], [42]])
def test_min_adjacent_pair_requires_two_elements(nums):
    with pytest.raises(ValueError):
        min_adjacent_pair(nums)
