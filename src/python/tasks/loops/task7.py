"""Задача 7. Методы словаря setdefault и update.

Две обёртки показывают поведение методов словаря, не мутируя вход:

- `insert_if_absent` — обёртка над dict.setdefault: возвращает значение
  ключа (существующее или только что вставленное по умолчанию) вместе с
  получившимся словарём;
- `merge` — обёртка над dict.update: обновляет копию словаря из другого
  словаря, из списка пар и из именованных аргументов.

Закрепляет: разницу между «вставить, если нет» и «слить/перезаписать».
"""


def insert_if_absent(d: dict, key, default) -> tuple[object, dict]:
    """Возвращает (значение ключа, новый словарь) по семантике dict.setdefault.

    Если ключ уже есть — возвращается его значение, словарь не меняется.
    Если ключа нет — вставляется default и возвращается он же.
    Исходный словарь не мутируется.
    """
    result = dict(d)
    value = result.setdefault(key, default)
    return value, result


def merge(
    base: dict,
    other: dict | None = None,
    pairs: list[tuple] | None = None,
    **kwargs,
) -> dict:
    """Возвращает копию base, последовательно обновлённую из other, pairs и kwargs.

    Источники применяются по порядку, поэтому более поздний перекрывает ранний.
    Исходный словарь не мутируется.
    """
    result = dict(base)
    if other:
        result.update(other)
    if pairs:
        result.update(pairs)
    result.update(kwargs)
    return result


if __name__ == "__main__":
    print(insert_if_absent({"x": 2}, "x", 99))  # ключ есть -> (2, {'x': 2})
    print(insert_if_absent({"x": 2}, "y", 99))  # ключа нет -> (99, {'x': 2, 'y': 99})
    print(merge({"x": 2}, other={"y": 3}, pairs=[("z", 4)], w=5))
