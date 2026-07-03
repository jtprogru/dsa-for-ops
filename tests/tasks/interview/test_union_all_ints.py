import pytest

from tasks.interview.union_all_ints import union_all_ints


@pytest.mark.parametrize(
    "arrays, expected",
    [
        (([1, 2, 3], [3, 4], [2, 5]), [1, 2, 3, 4, 5]),
        ((), []),
        ((None, [1, 1, 2]), [1, 2]),
        (([], []), []),
        (([7],), [7]),
        (([3, -1], [0, 3], [-1]), [-1, 0, 3]),
    ],
)
def test_union_all_ints(arrays, expected):
    assert union_all_ints(*arrays) == expected
