# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

# def int_func():
#     word = input('Введите любое слово: ')
#     print(word.title())
#     return
#
#
# int_func()


def int_func(*args):
    word = input('Введите любые слова, разделенные пробелом: ')
    print(word.title())
    return


int_func()
