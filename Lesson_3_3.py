# Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_func(var_1, var_2, var_3):
    if var_1 >= var_2 >= var_3:
        return var_1 + var_2
    elif var_1 > var_2 < var_3:
        return var_1 + var_3
    elif var_1 <= var_2 <= var_3:
        return var_2 + var_3
    elif var_3 <= var_1 <= var_2:
        return var_2 + var_1


print(my_func(var_1=int(input('Введите число: ')), var_2=int(input('Введите число: ')),
              var_3=int(input('Введите число: '))))
