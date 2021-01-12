#  4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#  Для решения используйте цикл while и арифметические операции.
#  Целочисленное на 10 + остаток от деления на 10 (остаток от деления 0)

user_number = int(input('Введите целое положительное число '))

min_number = -1
while user_number > min_number:
    max_number = user_number % 10
    user_number //= 10
    if max_number > min_number:
        min_number = max_number
print(min_number)

# print(max([int(i) for i in str(user_number)]))


