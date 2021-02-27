'''Написать функцию, переводящую числительные от 0 до 10 c английского на русский язык'''


def num_translate(number):
    numb_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    return numb_dict.get(number)


print(num_translate(number=input('Введите числительное от 0 до 10 на английском языке: ')))
