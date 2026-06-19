"""Задача 6. Модуль шифрации/дешифрации.

Две функции — encrypt(text) и decrypt(text) — реализуют шифр Цезаря:
циклический сдвиг латинских букв на `shift` позиций. Регистр сохраняется,
все остальные символы (цифры, пробелы, кириллица, пунктуация) остаются
как есть. Гарантия: decrypt(encrypt(s)) == s для любой строки s.

Закрепляет: проход по символам строки и сборку результата; обратимость
обеспечивается сдвигом по модулю длины алфавита.
Сложность: O(n) время, O(n) память под результат.
"""

ALPHABET_SIZE = 26
DEFAULT_SHIFT = 3


def _shift_char(char: str, shift: int) -> str:
    """Сдвигает одну латинскую букву на `shift` по модулю 26, прочее — без изменений."""
    if "a" <= char <= "z":
        base = ord("a")
    elif "A" <= char <= "Z":
        base = ord("A")
    else:
        return char
    return chr(base + (ord(char) - base + shift) % ALPHABET_SIZE)


def encrypt(text: str, shift: int = DEFAULT_SHIFT) -> str:
    """Шифрует строку сдвигом латинских букв на `shift` позиций вперёд."""
    return "".join(_shift_char(char, shift) for char in text)


def decrypt(text: str, shift: int = DEFAULT_SHIFT) -> str:
    """Расшифровывает строку, сдвигая латинские буквы на `shift` позиций назад."""
    return "".join(_shift_char(char, -shift) for char in text)


if __name__ == "__main__":
    message = input("Текст для шифрования: ")
    encrypted = encrypt(message)
    print(f"Зашифровано:   {encrypted}")
    print(f"Расшифровано:  {decrypt(encrypted)}")
