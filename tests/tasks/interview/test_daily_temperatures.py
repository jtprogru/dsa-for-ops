import pytest

from tasks.interview.daily_temperatures import daily_temperatures


@pytest.mark.parametrize(
    "temps, expected",
    [
        ([13, 12, 15, 11, 9, 12, 16], [2, 1, 4, 2, 1, 1, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 20, 10], [0, 0, 0]),
        ([], []),
    ],
)
def test_daily_temperatures(temps, expected):
    assert daily_temperatures(temps) == expected
