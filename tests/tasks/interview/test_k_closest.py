import pytest

from tasks.interview.k_closest import k_closest


@pytest.mark.parametrize(
    "a, idx, k, expected",
    [
        ([10, 15, 20, 50, 55, 78, 91], 2, 3, [10, 15, 50]),
        ([1, 2, 3, 4, 5], 0, 2, [2, 3]),
        ([1, 2, 3, 4, 5], 4, 2, [3, 4]),
        ([1, 2, 3, 4, 5], 2, 4, [1, 2, 4, 5]),
    ],
)
def test_k_closest(a, idx, k, expected):
    assert k_closest(a, idx, k) == expected
