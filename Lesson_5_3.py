# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.

with open('Lesson_5_3.txt', encoding='utf-8') as my_file:
    salary = []
    find = []
    content = my_file.read().split('\n')
for line in content:
    line = line.split()
    if float(line[1]) < 20000.00:
        find.append(line[0])
    salary.append(line[1])
print(f'Оклад меньше 20000.00 {find}, средний оклад {sum(map(float, salary)) / len(salary)}')
