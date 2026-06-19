import pytest

from tasks.interview.second_max import second_max


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([-2, 3, 0, 1, 5], 3),
        ([1, 1], None),
        ([5, 5, 4], 4),
        ([5, 4, 3], 4),
        ([1], None),
        ([], None),
        ([2, 2, 2], None),
        ([10, 9, 10], 9),
    ],
)
def test_second_max(arr, expected):
    assert second_max(arr) == expected
