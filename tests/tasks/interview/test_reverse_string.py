import pytest

from tasks.interview.reverse_string import reverse_string


@pytest.mark.parametrize(
    "chars, expected",
    [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
        (["x"], ["x"]),
        ([], []),
    ],
)
def test_reverse_string(chars, expected):
    reverse_string(chars)
    assert chars == expected
