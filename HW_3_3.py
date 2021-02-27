'''Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки, содержащие имена,
начинающиеся с соответствующей буквы. Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?
'''

my_list = ['Иван', 'Мария', 'Петр', 'Илья', 'Михаил', 'Андрей', 'Николай', 'Алексей', 'Иосиф', 'Денис', 'Дарья']


def thesaurus(some_list):
    my_dict = {}
    for i in my_list:
        name = filter(lambda f: f.startswith(i[0]), my_list)
        key = i[0]
        my_dict[key] = list(name)
    return my_dict


print(my_list)
print(thesaurus(my_list))

'''Пробовала сделать с пользовательским вводом списка, но не могу полностью распаковать список из списка'''
# my_list = []
# names = str(input('Введите имена сотрудников через пробел: ')).split(' ')
# my_list.append(names)


# def thesaurus(my_list):
#     my_dict = {}
#     for i in my_list:
#         name = filter(lambda f: f.capitalize().startswith(i[0]), my_list)
#         key = i[0]
#         my_dict[key] = list(name)
#     return my_dict
#
#
# print(*my_list)
# print(thesaurus(my_list))
