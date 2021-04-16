'''Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах'''

duration = int(input('Введите время в секундах - '))

seconds = duration % 60
minutes = (duration // 60) % 60
hours = (duration // 3600) % 24
days = duration // 86400

if 0 < duration < 60:
    print(f'Ваше время - {seconds} сек.')
elif 60 <= duration < 3600:
    print(f'Ваше время - {minutes} мин. {seconds} сек.')
elif 86400 > duration >= 3600:
    print(f'Ваше время - {hours} ч. {minutes} мин. {seconds} сек.')
elif duration >= 86400:
    print(f'Ваше время - {days} дн. {hours} ч. {minutes} мин. {seconds} сек.')
else:
    print('Время не может быть отрицательным')
