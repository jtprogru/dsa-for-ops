"""Задача 2. range → list.

Если объект range (диапазон) передать встроенной функции list(),
она преобразует его к списку. Создайте таким образом список с элементами
от 0 до 100 и шагом 17. Выведите результат на экран.

Закрепляет: понимание полуинтервала range — верхняя граница не входит,
поэтому для «включительно до 100» берём stop = 101.
Подсказка: https://github.com/kolei/OAP/blob/master/articles/t3l1.md#list
"""


def range_to_list(start: int, stop: int, step: int) -> list[int]:
    """Возвращает list(range(start, stop, step)).

    Как и у range, верхняя граница stop не включается.
    """
    return list(range(start, stop, step))


if __name__ == "__main__":
    # stop = 101, чтобы значение 100 при необходимости попало в полуинтервал.
    print(range_to_list(0, 101, 17))
