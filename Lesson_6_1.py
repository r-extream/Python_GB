# Создать класс TrafficLight (светофор).
# ●	определить у него один атрибут color (цвет) и метод running (запуск);
# ●	атрибут реализовать как приватный;
# ●	в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# ●	продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# ●	переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# ●	проверить работу примера, создав экземпляр и вызвав описанный метод.

# Сайкл, лист из цветов,  тайм слип, принт красный горит Х секунд…

from time import sleep


class TrafficLight:
    __color = ['красный', 'жёлтый', 'зелёный']

    def running(self):
        i = 0
        while i < 3:
            print(f'Переключение светофора\n'
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(10)
            i += 1


TrafficL = TrafficLight()
TrafficL.running()
