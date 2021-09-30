# Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

import hashlib


def subcount(input_str):
    input_str = str(input_str).lower()

    length = len(input_str)

    hash_set = set()

    for i in range(length + 1):
        for j in range(i + 1, length + 1):
            h = hashlib.sha1(input_str[i:j].encode('utf-8')).hexdigest()
            hash_set.add(h)

    return len(hash_set)


some_string = input('Введите строку, состоящую только из маленьких латинских букв: ')

print(f'Количество различных подстрок в строке {some_string}: {subcount(some_string)}')
