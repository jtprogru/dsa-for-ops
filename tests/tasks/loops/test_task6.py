import pytest

from tasks.loops.task6 import decrypt, encrypt


@pytest.mark.parametrize(
    "text, shift, expected",
    [
        ("abc", 3, "def"),
        ("xyz", 3, "abc"),  # перенос через конец алфавита
        ("Hello, World!", 3, "Khoor, Zruog!"),  # регистр и пунктуация сохранены
        ("Привет 123", 3, "Привет 123"),  # не-латиница не меняется
    ],
)
def test_encrypt(text, shift, expected):
    assert encrypt(text, shift) == expected


@pytest.mark.parametrize(
    "text",
    ["", "abc", "Hello, World!", "Mixed CASE 42!", "Привет, мир"],
)
@pytest.mark.parametrize("shift", [1, 3, 13, 25, 26, 100])
def test_decrypt_is_inverse_of_encrypt(text, shift):
    assert decrypt(encrypt(text, shift), shift) == text


def test_default_shift_round_trip():
    assert decrypt(encrypt("secret message")) == "secret message"
