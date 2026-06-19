import pytest

from tasks.loops.task5 import deposit_growth


@pytest.mark.parametrize(
    "principal, rate, years, expected",
    [
        (1000, 10, 3, [1100.0, 1210.0, 1331.0]),
        (1000, 0, 2, [1000.0, 1000.0]),  # нулевая ставка не меняет баланс
        (500, 100, 1, [1000.0]),
        (1000, 10, 0, []),  # нулевой срок — пустой список
        (1000, 10, -5, []),  # отрицательный срок — тоже пустой
    ],
)
def test_deposit_growth(principal, rate, years, expected):
    result = deposit_growth(principal, rate, years)
    assert result == pytest.approx(expected)


def test_deposit_growth_length_matches_years():
    assert len(deposit_growth(1000, 7, 12)) == 12
