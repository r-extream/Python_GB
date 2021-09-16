# Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.

# Определить, какое число в массиве встречается чаще всего
# 1 вариант
import cProfile
from random import randint


def get_number_freq(items_cnt):
    array = [randint(0, items_cnt // 2) for _ in range(items_cnt)]

    size = len(array)
    max_cnt = 1
    item = array[0]

    for i in range(size - 1):
        cnt = 1
        for j in range(i + 1, size):
            if array[i] == array[j]:
                cnt += 1

        if cnt > max_cnt:
            max_cnt = cnt
            item = array[i]

    return item, items_cnt


cProfile.run('get_number_freq(1000)')


# 2 вариант
def get_number_freq(items_cnt):
    array = [randint(0, items_cnt // 2) for _ in range(items_cnt)]

    return sorted(((i, array.count(i)) for i in set(array)))[-1]


cProfile.run('get_number_freq(1000)')


# 3 вариант
def get_number_freq(items_cnt):
    array = [randint(0, items_cnt // 2) for _ in range(items_cnt)]

    scores = {}

    for i in array:
        try:
            scores[i] += 1
        except KeyError:
            scores[i] = 1

    return sorted((count, item) for item, count in scores.items())[-1]


cProfile.run('get_number_freq(1000)')

# 3-й вариант оказался самым быстрым
