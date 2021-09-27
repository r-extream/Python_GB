# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Python 3.9
# Windows 10 x64


import sys
import random


# для проверки
def show_size(x, level=0):
    print('\t' * level, f'type = {type(x)}, size = {sys.getsizeof(x)}, object = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)


def memory_size(logging=False):
    if logging:
        print('*' * 100)

    variables = globals().copy()
    size = 0

    for obj, val in variables.items():
        if obj.startswith('__'):
            continue
        elif hasattr(val, '__loader__'):
            continue
        elif hasattr(val, '__call__'):
            continue
        size += sys.getsizeof(val)
        if logging:
            print(f'Под переменную {obj} выделено: '
                  f'{sys.getsizeof(val)} байт (накопленный итог: {size} байт)')
        if hasattr(val, '__iter__'):
            if hasattr(val, 'items'):
                for key, value in val.items():
                    size += sys.getsizeof(key)
                    size += sys.getsizeof(value)
                    if logging:
                        print(f'Под ключ {key} выделено: '
                              f'{sys.getsizeof(key)} байт (накопленный итог: {size} байт)')
                        print(f'Под значение {value} выделено: '
                              f'{sys.getsizeof(value)} байт (накопленный итог: {size} байт)')
            elif not isinstance(val, str):
                for item in val:
                    size += sys.getsizeof(item)
                    if logging:
                        print(f'Под элемент {item} выделено: '
                              f'{sys.getsizeof(item)} байт (накопленный итог: {size} байт)')
    if logging:
        print('*' * 100)

    return size


# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = 598

a1 = a % 10
a2 = a % 100 // 10
a3 = a // 100

print(f'Под переменные выделено: {memory_size()} байт')
# Под переменные выделено: 112 байт

# проверка:
show_size(a)
show_size(a1)
show_size(a2)
show_size(a3)

# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ... Количество элементов (n) вводится с клавиатуры.

num = 6
total = 0
for i in range(num):
    total += 1 / (-2) ** i

print(f'Под переменные выделено: {memory_size()} байт')
# Под переменные выделено: 192 байта

# проверка:
show_size(num)
show_size(total)
show_size(i)

# 2. Во втором массиве сохранить индексы четных элементов первого массива. # Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 – если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

first = [random.randint(0, 100) for _ in range(10)]
second = [i for i, item in enumerate(first) if item % 2 == 0]

print(f'Под переменные выделено: {memory_size()} байт')
# Под переменные выделено: 996 байт

# проверка:
show_size(first)
show_size(_)
show_size(second)
show_size(i)
show_size(item)
