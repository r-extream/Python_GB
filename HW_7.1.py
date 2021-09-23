# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random


def sort(arr, reverse=False):
    if reverse:
        left = 1
        right = 0
    else:
        left = 0
        right = 1
    n = 1
    length = len(arr)
    while n < length:
        count = True
        for i in range(n - 1, length - n):
            if arr[i + left] > arr[i + right]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                count = False
        if count:
            break
        for j in range(length - n, n - 1, -1):
            if arr[j - left] < arr[j - right]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
        n += 1


lst = [random.randint(-100, 99) for _ in range(10)]
random.shuffle(lst)
print(f'Список до:\n{lst}')
sort(lst, reverse=True)
print(f'Список после:\n{lst}')
