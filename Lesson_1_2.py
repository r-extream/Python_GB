# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате
# чч:мм:сс. Используйте форматирование строк.

user_time = int(input('Введите время в секундах '))

seconds = user_time % 60
minutes = (user_time // 60) % 60
hours = user_time // 3600

print(f'Ваше время в формате чч:мм:сс - {hours}:{minutes}:{seconds}')
