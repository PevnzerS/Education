class Road:
    def __init__(self, lenght, width, a, m):
        self._lenght = lenght
        self._width = width
        self.a = 5 # толщина асфальта
        self.m = 25 # масса асфальта для покрытия 1 кв.м

    def calc(self):
        print(f"{(self._lenght * self._width * self.a * self.m) / 1000}т")

total = Road(5000, 20, 5, 25)
total.calc()