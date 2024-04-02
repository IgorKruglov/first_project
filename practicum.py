from math import sqrt
from typing import Optional


def add_numbers(xray: int, yray: int) -> int:
    return xray + yray


def calculate_square_root(number: float) -> float:
    return sqrt(number)


def calc(your_number: int) -> Optional[str]:
    if your_number <= 0:
        return
    root = calculate_square_root(your_number)
    return (f"""
    Мы вычислили квадратный корень из введённого вами числа. Это будет:
    {root}""")


xray = 10
yray = 5

print('Сумма чисел: ', add_numbers(xray, yray))
print(calc(25.5))
