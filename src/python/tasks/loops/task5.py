"""Задача 5. Проценты по банковскому вкладу.

Рассчитайте сумму вклада с капитализацией процентов: для начальной суммы,
годовой ставки (в процентах) и срока в годах верните баланс на конец
каждого года.

Пример: principal=1000, rate=10%, years=3 -> [1100.0, 1210.0, 1331.0].

Закрепляет: пошаговое накопление в цикле, где результат шага становится
входом следующего.
Сложность: O(years) время и память.
"""


def deposit_growth(principal: float, rate_percent: float, years: int) -> list[float]:
    """Возвращает список балансов на конец каждого года при ежегодной капитализации.

    Длина списка равна `years`; отрицательный срок даёт пустой список.
    """
    balances: list[float] = []
    balance = principal
    for _ in range(years):
        balance *= 1 + rate_percent / 100
        balances.append(balance)
    return balances


if __name__ == "__main__":
    from labs.common.console import read_float, read_int

    principal = read_float("Начальная сумма: ")
    rate = read_float("Годовая ставка, %: ")
    years = read_int("Срок, лет: ")
    for year, balance in enumerate(deposit_growth(principal, rate, years), start=1):
        print(f"Год {year}: {balance:.2f}")
