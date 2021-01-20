# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def summ():
    summ_result = 0
    exit = False
    while exit == False:
        ask_number = input('Введите строку чисел, разделенных пробелом, либо * для выхода: ').split()
        res = 0
        for i in range(len(ask_number)):
            if ask_number[i] == '*':
                exit = True
                break
            else:
                res = res + int(ask_number[i])
        summ_result = summ_result + res
        print(f'Текущая сумма введенных чисел равна {summ_result}')
    print(f'Итоговая сумма введенных чисел равна {summ_result}')


summ()
