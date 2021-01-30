# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

with open('Lesson_5_2.txt', encoding='utf-8') as f_obj:
    lines = f_obj.readlines()
print(f'Количество строк в файле {len(lines)}')
for i in range(len(lines)):
    print(f'Количество символов {i + 1}-ой строки {len(lines[i])}')
