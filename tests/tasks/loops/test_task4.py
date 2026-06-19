import pytest

from tasks.loops.task4 import word_lengths


@pytest.mark.parametrize(
    "words, expected",
    [
        (["yes", "no", "maybe", "ok", "what"], [3, 2, 5, 2, 4]),
        ([], []),
        (["", "a", "ab"], [0, 1, 2]),
        (["привет"], [6]),  # длина в кодовых точках, не в байтах
    ],
)
def test_word_lengths(words, expected):
    assert word_lengths(words) == expected
