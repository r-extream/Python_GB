# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл. Иф элиф, метод реплэйс или словарь

my_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
new_file = []
with open('Lesson_5_4.txt', encoding='utf-8') as my_file:
    for line in my_file:
        line = line.split(' ', 1)
        new_file.append(my_dict[line[0]] + ' ' + line[1])
        # print(new_file)

with open('Lesson_5_4_new.txt', 'x', encoding='utf-8') as my_file_new:
    my_file_new.writelines(new_file)
