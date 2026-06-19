"""Задача 4. Длины слов.

По списку слов постройте второй список с длиной каждого слова.

Например: ['yes', 'no', 'maybe', 'ok', 'what'] -> [3, 2, 5, 2, 4].

Закрепляет: формирование нового списка из исходного в цикле.
Сложность: O(n) время (n — число слов), O(n) память под результат.
"""


def word_lengths(words: list[str]) -> list[int]:
    """Возвращает список длин для каждого слова из words (порядок сохраняется)."""
    lengths: list[int] = []
    for word in words:
        lengths.append(len(word))
    return lengths


if __name__ == "__main__":
    words = [input(f"Введите слово {i + 1}: ").strip() for i in range(5)]
    print(words)
    print(word_lengths(words))
