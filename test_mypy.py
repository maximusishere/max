from math import sqrt
from typing import Optional, Union


def add_numbers(xi: int, yi: int) -> int:
    return xi + yi


def calculate_square_root(number: int) -> float:
    return sqrt(number)


def calc(your_number: Union[int, float]) -> Optional[str]:
    if not your_number <= 0:
        result = calculate_square_root(your_number)
        print(f'Мы вычислили квадратный корень из введённого вами числа.'
              f' Это будет: {result}')


xi: int = 10
yi = 5

print('Сумма чисел: ', add_numbers(xi, yi))

print(calc(25.5))
