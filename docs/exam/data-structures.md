# Структуры данных

Краткий справочник по основным структурам данных — от списков и словарей Python до связанных списков, стеков, очередей и двоичных деревьев. Примеры кода — на Python.

## 1. Списки и кортежи в Python

**Список (`list`)** — изменяемая упорядоченная коллекция.
**Кортеж (`tuple`)** — неизменяемая упорядоченная коллекция (можно использовать как ключ словаря, быстрее, защищён от изменений).

```python
lst = [1, 2, 3]
lst.append(4)        # [1, 2, 3, 4]
lst[0] = 10          # изменяемый

tup = (1, 2, 3)
# tup[0] = 10        # ошибка — неизменяемый
x, y, z = tup        # распаковка
```

## 2. Множества и словари в Python

**Множество (`set`)** — неупорядоченная коллекция уникальных элементов; быстрая проверка принадлежности O(1), операции объединения/пересечения.
**Словарь (`dict`)** — коллекция пар «ключ-значение», доступ по ключу O(1), ключи уникальны и хешируемы.

```python
s = {1, 2, 2, 3}     # {1, 2, 3}
s.add(4)
print(2 in s)        # True
a & b, a | b, a - b  # пересечение, объединение, разность

d = {"a": 1, "b": 2}
d["c"] = 3
print(d.get("a"))    # 1
```

## 3. Массив как структура данных

Набор элементов одного типа в **непрерывной области памяти**, доступ по индексу.

| Операция | Сложность |
|---|---|
| Доступ по индексу | O(1) |
| Поиск | O(n) |
| Вставка/удаление | O(n) (сдвиг элементов) |
| Вставка/удаление в конец (динам.) | O(1) амортизированно |

**Плюсы:** мгновенный доступ по индексу, компактность, кэш-локальность.
**Минусы:** фиксированный размер (для статических), дорогая вставка/удаление в середине.

## 4. Связанный список

Набор **узлов**, каждый хранит данные и ссылку на следующий узел. В памяти расположены произвольно.

| Операция | Сложность |
|---|---|
| Доступ по индексу | O(n) |
| Поиск | O(n) |
| Вставка/удаление (при известном узле) | O(1) |
| Вставка в начало | O(1) |

**Плюсы:** дешёвая вставка/удаление, динамический размер.
**Минусы:** нет доступа по индексу за O(1), доп. память на ссылки, плохая кэш-локальность.

## 5. Реализация связанного списка + доступ по индексу

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def get(self, index):
        cur = self.head
        i = 0
        while cur:
            if i == index:
                return cur.data
            cur = cur.next
            i += 1
        raise IndexError("index out of range")
```

## 6. Поиск в связанном списке

```python
def search(self, target):
    cur = self.head
    index = 0
    while cur:
        if cur.data == target:
            return index   # нашли — возвращаем позицию
        cur = cur.next
        index += 1
    return -1              # не найдено
```

## 7. Распечатка связанного списка

```python
def print_list(self):
    cur = self.head
    result = []
    while cur:
        result.append(str(cur.data))
        cur = cur.next
    print(" -> ".join(result))
```

## 8. Виды связанных списков

- **Односвязный** — узел ссылается только на следующий.
- **Двусвязный** — узел ссылается на следующий и предыдущий (обход в обе стороны).
- **Кольцевой (циклический)** — последний узел ссылается на первый.
- **Двусвязный кольцевой** — комбинация двух последних.

## 9. Стек (Stack)

Структура **LIFO** (Last In — First Out). Доступ только к вершине.

| Операция | Сложность |
|---|---|
| push / pop / peek | O(1) |

**Применение:** вызовы функций (call stack), отмена операций (undo), проверка скобок, обход в глубину (DFS), вычисление выражений.

## 10. Реализация стека на списке Python

```python
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self._items:
            raise IndexError("stack is empty")
        return self._items.pop()

    def peek(self):
        if not self._items:
            raise IndexError("stack is empty")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0
```

## 11. Очередь (Queue)

Структура **FIFO** (First In — First Out). Добавление в хвост, извлечение из головы.

| Операция | Сложность |
|---|---|
| enqueue / dequeue / peek | O(1) |

**Применение:** обработка задач, буферы, обход в ширину (BFS), планировщики, очереди сообщений.

## 12. Реализация очереди на связанном списке

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None   # откуда извлекаем
        self.tail = None   # куда добавляем

    def push(self, data):         # enqueue
        node = Node(data)
        if self.tail:
            self.tail.next = node
        self.tail = node
        if not self.head:
            self.head = node

    def pop(self):                # dequeue
        if not self.head:
            raise IndexError("queue is empty")
        node = self.head
        self.head = node.next
        if not self.head:
            self.tail = None
        return node.data

    def peek(self):
        if not self.head:
            raise IndexError("queue is empty")
        return self.head.data
```

## 13. Двоичное дерево

**Двоичное дерево** — иерархическая структура, где каждый узел имеет не более двух потомков (левый и правый).

Понятия: **корень** (верхний узел), **лист** (узел без потомков), **родитель/потомок**, **высота** (длина пути до самого глубокого листа), **глубина узла**, **поддерево**.

## 14. Реализация двоичного дерева на двусвязном узле

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None   # обратная ссылка (двусвязность)

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def add_left(self, node, value):
        node.left = TreeNode(value)
        node.left.parent = node
        return node.left

    def add_right(self, node, value):
        node.right = TreeNode(value)
        node.right.parent = node
        return node.right
```

## 15. Виды двоичных деревьев

- **Полное (full)** — каждый узел имеет 0 или 2 потомка.
- **Совершенное / идеальное (perfect)** — все внутренние узлы имеют 2 потомка, все листья на одном уровне.
- **Полностью заполненное (complete)** — все уровни заполнены, кроме, возможно, последнего, который заполняется слева направо.
- **Сбалансированное (balanced)** — высоты левого и правого поддеревьев любого узла отличаются не более чем на 1 (высота O(log n)).

> Терминология в русских курсах плавает: «идеальное» и «совершенное» часто означают perfect, «полное» — full. Уточните трактовку преподавателя.

## 16. Обход в ширину (BFS)

Уровень за уровнем, с помощью очереди.

```python
from collections import deque

def bfs(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
```

## 17. Обход в глубину (DFS)

Вглубь до листа, потом возврат. Три порядка: pre-/in-/post-order.

```python
def dfs_inorder(node, result=None):
    if result is None:
        result = []
    if node:
        dfs_inorder(node.left, result)    # левое
        result.append(node.value)         # корень
        dfs_inorder(node.right, result)   # правое
    return result

# pre-order: корень -> левое -> правое
# post-order: левое -> правое -> корень
```

## 18. Двоичное дерево поиска (BST). Построение

**BST** — двоичное дерево, где для любого узла: все значения в **левом** поддереве **меньше**, в **правом** — **больше** значения узла.

```python
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = BSTNode(value)
            return
        cur = self.root
        while True:
            if value < cur.value:
                if cur.left is None:
                    cur.left = BSTNode(value)
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = BSTNode(value)
                    return
                cur = cur.right
```

## 19. Поиск в BST

Сравниваем с узлом и идём влево или вправо.

```python
def search(node, target):
    while node:
        if target == node.value:
            return True
        elif target < node.value:
            node = node.left      # ищем слева
        else:
            node = node.right     # ищем справа
    return False
```

Сложность: **O(h)**, где h — высота дерева. Для сбалансированного — **O(log n)**, для вырожденного (в линию) — **O(n)**.

## См. также

- [Конспект DSA](../notes.md)
