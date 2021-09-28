# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

import collections

while True:
    try:
        n = int(input('Введите количество предприятий: '))
    except ValueError:
        print('Вы ввели недопустимое значение')
        continue
    break

companies = collections.defaultdict()
profit_high = collections.deque()
profit_low = collections.deque()
total_profit = 0
quat = 4

for i in range(n):
    name = input(f'\nВведите название {i + 1}й компании: ')
    profit = 0
    q = 1
    while q <= quat:
        try:
            profit += float(input(f'Введите прибыль за {q}й квартал: '))
        except ValueError:
            print('Вы ввели недопустимое значение')
            continue
        q += 1
    companies[name] = profit
    total_profit += profit

mid_profit = total_profit / n
for i, item in companies.items():
    if item >= mid_profit:
        profit_high.append(i)
    else:
        profit_low.append(i)
print(f'Средняя прибыль для всех компаний: {mid_profit}')
print(f'Прибыль выше среднего у {len(profit_high)} компаний:')
for name in profit_high:
    print(name)
print(f'Прибыль ниже среднего у {len(profit_low)} компаний:')
for name in profit_low:
    print(name)
