class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        print(f"Итоговый доход: {self._income['w'] + self._income['b'] - self._income['f']}")


a = Position("S", "P", "d", {"w": 500, "b": 100, "f": 50})
a.get_full_name()
a.get_total_income()

