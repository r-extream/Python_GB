# 2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию input().

my_list = ['John', 50, 'male', True, 2.5, 'None']
my_list.insert(0, my_list[1])
my_list.pop(2)
my_list.insert(2, my_list[3])
my_list.pop(4)
my_list.insert(4, my_list[5])
my_list.pop(6)
print(my_list)

# var_1 = my_list[0]
# var_2 = my_list[1]
# var_3 = my_list[2]
# var_4 = my_list[3]
# var_5 = my_list[4]
# var_6 = my_list[5]
# var_1, var_2 = var_2, var_1
# var_3, var_4 = var_4, var_3
# var_5, var_6 = var_6, var_5
# print(var_1, var_2, var_3, var_4, var_5, var_6)
