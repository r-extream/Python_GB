# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста. Дампом и лодом проверить

import json

firms = {}
profit = []

with open('Lesson_5_7.txt.txt') as my_file:
    lines = my_file.readlines()

for line in lines:
    name, form, income, losses = line.split()
    diff = float(income) - float(losses)
    firms[name] = diff
    if diff > 0:
        profit.append(diff)

profit = sum(profit) / len(profit)
result = [firms, {'Средняя прибыль': profit}]

with open('Lesson_5_7.json', 'w') as my_json:
    json.dump(result, my_json)

with open('Lesson_5_7.json') as my_json:
    print(json.load(my_json))
