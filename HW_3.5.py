# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве

import random

list = [random.randint(-10, 10) for _ in range(10)]
min_el = -float('inf')

for i, item in enumerate(list):
    if min_el < item < 0:
        min_el = item
        min_id = i

print(f'В массиве: \n{list} \nминимальный отрицательный элемент = {min_el} \nего индекс = {min_id}')
