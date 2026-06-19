import pytest

from tasks.interview.missing_number import missing_number


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 1, 2, 3, 5], 4),
        ([1, 2, 3, 4, 5], 0),
        ([0], 1),
        ([1], 0),
        ([0, 1], 2),
    ],
)
def test_missing_number(nums, expected):
    assert missing_number(nums) == expected
