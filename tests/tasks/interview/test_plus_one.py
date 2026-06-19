import pytest

from tasks.interview.plus_one import plus_one


@pytest.mark.parametrize(
    "digits, expected",
    [
        ([1, 2, 3], [1, 2, 4]),
        ([1, 2, 9], [1, 3, 0]),
        ([9, 9], [1, 0, 0]),
        ([0], [1]),
        ([9], [1, 0]),
    ],
)
def test_plus_one(digits, expected):
    assert plus_one(digits) == expected


def test_plus_one_does_not_mutate_input():
    digits = [1, 2, 3]
    plus_one(digits)
    assert digits == [1, 2, 3]
