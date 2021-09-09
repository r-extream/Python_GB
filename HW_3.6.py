# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random

list = [random.randint(0, 10) for _ in range(10)]
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

print(f'Минимальный элемент = {min_el}(индекс {min_id})\nМаксимальный элемент = {max_el} (индекс {max_id})')
if max_id < min_id:
    max_id, min_id = min_id, max_id

print(f'Между минимальным и максимальным элементами: {list[min_id + 1:max_id]}')

summa = 0
for i in range(min_id + 1, max_id):
    summa += list[i]

print(f'Сумма элементов, находящихся между минимальным и максимальным элементами = {summa}')
