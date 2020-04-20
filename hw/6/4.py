class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} wroom-wroom! with {self.speed} m/h")

    def stop(self):
        print(f"{self.name} Stop!")

    def turn(self):
        dir = input('Direction? (left / right)')
        print(f"{self.name} turned {dir}")

    def show_speed(self):
        speed_now = input('Enter speed')
        print(f"{self.name}`s speed is {speed_now} m/h")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def go(self):
        print(f"{self.name} wroom-wroom! with {self.speed} m/h")

    def stop(self):
        print(f"{self.name} Stop!")

    def turn(self):
        dir = input('Direction? (left / right)')
        print(f"{self.name} turned {dir}")

    def show_speed(self):
        speed_now = int(input('Enter speed'))
        if speed_now > 60:
            print(f"OVER SPEED!!! {self.name}`s speed is {speed_now} m/h")
        else:
            print(f"{self.name}`s speed is {speed_now} m/h")

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def go(self):
        print(f"{self.name} wroom-wroom! with {self.speed} m/h")

    def stop(self):
        print(f"{self.name} Stop!")

    def turn(self):
        dir = input('Direction? (left / right)')
        print(f"{self.name} turned {dir}")

    def show_speed(self):
        speed_now = int(input('Enter speed'))
        print(f"{self.name}`s speed is {speed_now} m/h")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def go(self):
        print(f"{self.name} wroom-wroom! with {self.speed} m/h")

    def stop(self):
        print(f"{self.name} Stop!")

    def turn(self):
        dir = input('Direction? (left / right)')
        print(f"{self.name} turned {dir}")

    def show_speed(self):
        speed_now = int(input('Enter speed'))
        if speed_now > 40:
            print(f"OVER SPEED!!! {self.name}`s speed is {speed_now} m/h")
        else:
            print(f"{self.name}`s speed is {speed_now} m/h")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def go(self):
        print(f"{self.name} wroom-wroom! with {self.speed} m/h")

    def stop(self):
        print(f"{self.name} Stop!")

    def turn(self):
        dir = input('Direction? (left / right)')
        print(f"{self.name} turned {dir}")

    def show_speed(self):
        speed_now = int(input('Enter speed'))
        print(f"{self.name}`s speed is {speed_now} m/h")


a = TownCar(80, "red", "BMW", False)

a.go()
a.turn()
a.show_speed()
a.stop()
print()

b = WorkCar(80, "red", "Audi", False)
b.go()
b.turn()
b.show_speed()
b.stop()
print()

c = SportCar(80, "red", "Lada", False)
c.go()
c.turn()
c.show_speed()
c.stop()