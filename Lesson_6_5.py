# Реализовать класс Stationery (канцелярская принадлежность).
# ●	определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки» (print);
# ●	создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ●	в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# ●	создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = 'Название'

    def draw(self):
        draw = 'Запуск отрисовки'
        print(draw)


class Pen(Stationery):
    def draw(self):
        draw = 'Запуск отрисовки ручкой'
        print(draw)


class Pencil(Pen):
    def draw(self):
        draw = 'Запуск отрисовки карандашом'
        print(draw)


class Handle(Pencil):
    def draw(self):
        draw = 'Запуск отрисовки вручную'
        print(draw)


st = Stationery()
st.draw()
p = Pen()
p.draw()
pn = Pencil()
pn.draw()
h = Handle()
h.draw()
