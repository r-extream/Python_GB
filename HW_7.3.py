# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.

import random


def med(array, k):
    if len(array) == 1:
        return array[0]

    pivot = random.choice(array)

    left_el = [el for el in array if el < pivot]
    right_el = [el for el in array if el > pivot]
    pivots = [el for el in array if el == pivot]

    if k < len(left_el):
        return med(left_el, k)
    elif k < len(left_el) + len(pivots):
        return pivots[0]
    else:
        return med(right_el, k - len(left_el) - len(pivots))


M = 5
lst = [random.randint(0, 20) for _ in range(2 * M + 1)]
print(f'Исходный список:\n{lst}')
print(f'Медианой является:\n{med(lst, len(lst) / 2)}')
lst.sort()
print(f'Список после сортировки:\n{lst}')
print(f'Медианой является:\n{lst[len(lst) // 2]}')
