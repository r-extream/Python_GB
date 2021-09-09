# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]

for i, row in enumerate(matrix):

    if i == 0:
        min_row = row.copy()
        for item in row:
            print(f'{item:>5}', end='')
        print()
        continue

    for id, item in enumerate(row):
        if item < min_row[id]:
            min_row[id] = item
        print(f'{item:>5}', end='')
    print()

print('-' * len(min_row) * 5)

max_min = min_row[0]
for item in min_row:
    print(f'{item:>5}', end='')
    if item > max_min:
        max_min = item

print()
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы = {max_min}')
