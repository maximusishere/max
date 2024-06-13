from typing import List


def transport_robots(weights: List[int], limit: int) -> int:
    weights.sort()  # Сортируем массив весов роботов по возрастанию
    count = 0
    left = 0
    right = len(weights) - 1

    while left <= right:
        if weights[left] + weights[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        count += 1

    return count


# Пример использования функции
weights = [3, 5, 3, 7, 4]
limit = 5

print(transport_robots(weights, limit))
