# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

matrix = [[] for _ in range(4)]

for row in matrix:
    line_sum = 0
    for i in range(4):
        num = int(input('Введите значение: '))
        row.append(num)
        line_sum += num
    row.append(line_sum)

for row in matrix:
    for num in row:
        print(f'\t{num:>5}', end='')
    print()
