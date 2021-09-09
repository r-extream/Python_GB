# Определить, какое число в массиве встречается чаще всего.

import random

list = [random.randint(1, 5) for _ in range(10)]
d = dict.fromkeys(list, 0)

for num in list:
    d[num] += 1

max_num = 0
for key in d:
    if d[key] > max_num:
        max_key = key
        max_num = d[key]

print(f'В списке \n{list} \nчаще всего встречается число: {max_key} ({max_num} раз)')
