# Реализовать класс Road (дорога).
# ●	определить атрибуты: length (длина), width (ширина);
# ●	значения атрибутов должны передаваться при создании экземпляра класса;
# ●	атрибуты сделать защищёнными;
# ●	определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# ●	использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# ●	проверить работу метода.

class Road:
    def __init__(self, __length, __width):
        self.__length = __length
        self.__width = __width

    def mass(self):
        return self.__width * self.__length * self.volume * self.thickness


class MassRoad(Road):
    def __init__(self, __length, __width, volume, thickness):
        super().__init__(__length, __width)
        self.volume = volume
        self.thickness = thickness


road = MassRoad(20, 5000, 25, 5)
print(road.mass())
