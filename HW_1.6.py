# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

num = int(input('Введите номер буквы в алфавите от 1 до 26 или от 33 до 58: '))
char = chr(num + 64)
print(f'Это буква "{char}"')
