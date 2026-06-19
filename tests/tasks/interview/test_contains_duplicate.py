import pytest

from tasks.interview.contains_duplicate import contains_duplicate


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 1, 2, 3, 3, 5], True),
        ([0, 1, 2, 3], False),
        ([1, 1], True),
        ([], False),
        ([42], False),
    ],
)
def test_contains_duplicate(nums, expected):
    assert contains_duplicate(nums) == expected
