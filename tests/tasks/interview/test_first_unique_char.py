import pytest

from tasks.interview.first_unique_char import first_unique_char


@pytest.mark.parametrize(
    "s, expected",
    [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1),
        ("", -1),
        ("z", 0),
    ],
)
def test_first_unique_char(s, expected):
    assert first_unique_char(s) == expected
