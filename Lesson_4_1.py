# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

name, working_time, rate, bonus = argv
try:
    working_time = int(working_time)
    rate = int(rate)
    bonus = int(bonus)

    salary = working_time * rate + bonus
    print(f'Заработная плата сотрудника составляет {salary}')
except ValueError:
    print('Необходимо вводить число')
