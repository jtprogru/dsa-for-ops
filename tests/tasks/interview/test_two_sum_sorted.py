import pytest

from tasks.interview.two_sum_sorted import two_sum_sorted


@pytest.mark.parametrize(
    "a, k, expected",
    [
        ([-1, 2, 5, 8], 7, [-1, 8]),
        ([1, 2, 3, 4], 100, []),
        ([1, 2, 3, 4], 7, [3, 4]),
        ([1, 2, 3, 10], 5, [2, 3]),  # сумма с краёв велика — двигаем правый указатель
        ([], 5, []),
    ],
)
def test_two_sum_sorted(a, k, expected):
    assert two_sum_sorted(a, k) == expected
