import pytest

from tasks.interview.two_sum import two_sum


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3], 100, []),
    ],
)
def test_two_sum(nums, target, expected):
    assert two_sum(nums, target) == expected
