# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. (enumerate) Если слово длинное, выводить только первые 10 букв в слове. (срез до 10)

some_str = input('Введите строку из нескольких слов, разделённых пробелами: ').split(' ')

for i, el in enumerate(some_str):
    print(i, el[:10])
