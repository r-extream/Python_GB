'''2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
a.	Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
b.	К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
c.	* Решить задачу под пунктом b, не создавая новый список'''

N = 1000
odd_numbers = []
number = 0
summ_number_list = 0
while number < N:
    if number % 2:
        odd_numbers.append(number ** 3)
    number += 1
for idx in odd_numbers:
    _sum = 0
    num = idx
    while (num != 0):
        _sum = _sum + num % 10
        num = num // 10
    if not _sum % 7:
        summ_number_list += idx
print('Сумма чисел = ', summ_number_list)
summ_number_list = 0
for idx in range(len(odd_numbers)):
    odd_numbers[idx] += 17
    _sum = 0
    num = odd_numbers[idx]
    while (num != 0):
        _sum = _sum + num % 10
        num = num // 10
    if not _sum % 7:
        summ_number_list += odd_numbers[idx]
print('Сумма чисел новая = ', summ_number_list)
