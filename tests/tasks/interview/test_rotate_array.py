import pytest

from tasks.interview.rotate_array import rotate


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([1, 2], 0, [1, 2]),
        ([1, 2, 3], 3, [1, 2, 3]),
        ([1, 2, 3], 4, [3, 1, 2]),
        ([], 2, []),
    ],
)
def test_rotate(nums, k, expected):
    rotate(nums, k)
    assert nums == expected
