# Реализуйте базовый класс Car.
# ●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# ●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# ●	для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_r(self):
        return f'{self.name} повернула направо'

    def turn_l(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f' Скорость {self.name} равна {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городской машины {self.name} равна {self.speed}')
        if self.speed > 40:
            return f'{self.name} превысила скорость'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городской машины {self.name} равна {self.speed}')
        if self.speed > 60:
            return f'{self.name} превысила скорость'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - машина полиции'
        else:
            return f'{self.name} не принадлежит полиции'


vw = WorkCar(65, 'white', 'VW Golf', False)
bmw = PoliceCar(50, 'blue', 'BMW X5', True)
kia = TownCar(60, 'red', 'Kia Ceed', False)
nissan = SportCar(250, 'black', 'Nissan GT', False)

print(f'{vw.go()}, {kia.go()}')
print(f'{vw.stop()}, {kia.turn_l()}, {bmw.police()}')
print(f'{nissan.go()}, {nissan.turn_r()}, {bmw.go()}')
print(f'{vw.show_speed()}')
print(f'{kia.show_speed()}, {nissan.stop()}')
