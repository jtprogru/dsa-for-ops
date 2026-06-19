import pytest

from tasks.interview.remove_duplicates import remove_duplicates


@pytest.mark.parametrize(
    "nums, expected_len, expected_head",
    [
        ([0, 1, 2, 3, 3, 5], 5, [0, 1, 2, 3, 5]),
        ([1, 1, 2], 2, [1, 2]),
        ([], 0, []),
        ([7], 1, [7]),
        ([2, 2, 2], 1, [2]),
    ],
)
def test_remove_duplicates(nums, expected_len, expected_head):
    assert remove_duplicates(nums) == expected_len
    assert nums == expected_head
