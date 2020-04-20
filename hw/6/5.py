class Stationery:
    def draw(self):
        print('Запуск отсортировки!')


class Pen(Stationery):
    def draw(self):
        print('Ручка')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш')


class Handle(Stationery):
    def draw(self):
        print('Маркер')


a = Stationery()
a.draw()
print()
b = Pen()
b.draw()
print()
c = Handle()
c.draw()