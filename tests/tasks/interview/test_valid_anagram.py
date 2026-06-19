import pytest

from tasks.interview.valid_anagram import is_anagram


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("ab", "a", False),
        ("", "", True),
    ],
)
def test_is_anagram(s, t, expected):
    assert is_anagram(s, t) == expected
