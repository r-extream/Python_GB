# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

list = [random.randint(0, 100) for _ in range(10)]
print(*list)
min_el = list[0]
max_el = list[1]

for i, item in enumerate(list):
    if item <= min_el:
        min_el = item
        min_id = i
    if item >= max_el:
        max_el = item
        max_id = i

list[min_id] = max_el
list[max_id] = min_el

print('Переставим максимальный и минимальный элементы:\n', *list)
