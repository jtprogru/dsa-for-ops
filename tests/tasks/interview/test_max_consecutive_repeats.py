import pytest

from tasks.interview.max_consecutive_repeats import max_consecutive_repeats


@pytest.mark.parametrize(
    "s, expected",
    [
        ("aafbaaaaffc", {"a": 4, "f": 2, "b": 1, "c": 1}),
        ("", {}),
        ("aaaa", {"a": 4}),
        ("abc", {"a": 1, "b": 1, "c": 1}),
    ],
)
def test_max_consecutive_repeats(s, expected):
    assert max_consecutive_repeats(s) == expected
