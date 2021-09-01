# Написать программу, которая генерирует в указанных пользователем границах
# ●	случайное целое число,
# ●	случайное вещественное число,
# ●	случайный символ.

import random

data_type = input('Введите тип данных i(целое число)|f(вещественное число)|c(символ): ')
start = input('Введите нижнюю границу: ')
end = input('Введите верхнюю границу: ')

if data_type == 'i':
    r = random.randint(int(start), int(end))
elif data_type == 'f':
    r = random.uniform(float(start), float(end))
elif data_type == 'c':
    r = chr(random.randint(ord(start), ord(end)))
else:
    r = f"Неизвестный тип данных '{data_type}'"

print(f'Случайное значение в диапазоне от {start} до {end} = {r}')
