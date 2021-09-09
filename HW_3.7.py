# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

list = [random.randint(1, 100) for _ in range(10)]
min_el = list[1]
min_el_2 = list[0]

for num in list:
    if num <= min_el:
        min_el_2 = min_el
        min_el = num
    elif num <= min_el_2:
        min_el_2 = num

print(f'В массиве: \n{list} \nминимальные элементы: {min_el} и {min_el_2}')
