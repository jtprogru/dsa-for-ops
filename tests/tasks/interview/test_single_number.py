import pytest

from tasks.interview.single_number import single_number


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
        ([7, 3, 3, 7, 9], 9),
    ],
)
def test_single_number(nums, expected):
    assert single_number(nums) == expected
