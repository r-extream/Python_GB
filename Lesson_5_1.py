# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

my_file = open('input.txt', 'w')

while True:
    line = input('Введите произвольную строку\n')
    my_file.writelines(line)
    if not line:
        break

my_file.close()

with open('input.txt') as f_obj:
    for line in f_obj:
        print(line)

# my_file = open('input.txt', 'r')
# cont = my_file.readlines()
# print(cont)
# my_file.close()
