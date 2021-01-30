# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open('Lesson_5_5.txt', 'w', encoding='utf-8') as my_file:
    numbers = input('Введите набор чисел, разделенных пробелами ')
    my_file.write('Вы ввели ' + numbers + '\n')
    numbers_summ = sum(map(int, numbers.split()))
    my_file.write('Сумма введенных чисел равна ' + str(numbers_summ))
print('Сумма чисел', numbers_summ)
