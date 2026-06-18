# common — общие утилиты

Базовые helper'ы, которые повторяются из лабораторной в лабораторную, вынесены в локальный пакет `labs/common` — чтобы не дублировать один и тот же код. Лабы импортируют их напрямую:

```python
from labs.common import array_length, generate_array, print_array, custom_range
```

Импортировать можно как из пакета (`from labs.common import array_length`), так и из конкретного модуля (`from labs.common.arrays import array_length`). Встроенные функции (`len`, `range`, …) внутри этих helper'ов **намеренно не используются** — это часть учебного задания.

Пакет разложен на два модуля:

| Модуль | Что внутри |
|--------|------------|
| `labs.common.arrays` | `array_length`, `generate_array`, `print_array` |
| `labs.common.ranges` | `custom_range` |

## `arrays` — операции над массивом

### `array_length(arr)` — длина без `len()`

Проходим по всем элементам и считаем их — «ручная» замена `len()`.

```python
def array_length(arr: list) -> int:
    count = 0
    for _ in arr:      # перебираем элементы, само значение не нужно
        count += 1
    return count
```

- **Сложность:** O(n) — один проход.
- В реальном коде так писать не нужно: есть `len()` за O(1). Здесь — учебная цель.

### `generate_array(size)` — заполнение случайными числами

```python
def generate_array(size: int) -> list[int]:
    result = []
    i = 0
    while i < size:
        result.append(random.randint(1, 100))  # случайное число 1..100 включительно
        i += 1
    return result
```

- `random.randint(a, b)` возвращает целое в диапазоне **[a, b]** (обе границы включены).
- Цикл `while` с ручным счётчиком вместо `for i in range(size)` — снова из-за запрета встроенных функций.

### `print_array(arr)` — вывод по индексу

Задание требует обращаться к элементам **по индексу**, а не перебором значений.

```python
def print_array(arr: list[int]) -> None:
    i = 0
    while i < array_length(arr):
        print(f"[{i}] = {arr[i]}")   # arr[i] — доступ по индексу
        i += 1
```

Вывод:
```
[0] = 42
[1] = 7
[2] = 99
```

## `ranges` — самописный `range`

### `custom_range(start, stop=None, step=1)` — аналог `range`

Самописная замена встроенной `range`: возвращает **список** целых чисел. Поддерживает обе формы вызова — `custom_range(stop)` и `custom_range(start, stop[, step])` — и отрицательный шаг.

```python
def custom_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start      # форма custom_range(stop)
    if step == 0:
        raise ValueError("step не может быть равен нулю.")
    result = []
    current = start
    if step > 0:
        while current < stop:
            result.append(current)
            current += step
    else:                           # отрицательный шаг — идём вниз
        while current > stop:
            result.append(current)
            current += step
    return result
```

- При `stop is None` единственный аргумент трактуется как верхняя граница, а старт сдвигается на 0 — ровно как у встроенной `range`.
- `step == 0` запрещён (иначе бесконечный цикл) — поднимается `ValueError`.
- В отличие от настоящей `range` (ленивый итератор), здесь сразу материализуется список — для учебных размеров это несущественно.

Используется в [lab02](lab02.md) и [lab02_random](lab02_random.md) при построении «холста» для визуализации дерева (`for _ in custom_range(rows)`).
