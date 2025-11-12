# родитель, суперкласс
class Car:
    # инициализатор объектов
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self._max_speed = 0
        self.__fined = False

    def drive(self, location):
        print(f"Car {self.model} is driving in {location}, max speed: {self._max_speed}, fine: {self.__fined}")

    def _test(self):
        self.drive("Karakol")

    def get_fined(self):
        # геттер
        return self.__fined

    def set_fined(self, value):
        # сеттер
        self.__fined = value

    def set_max_speed(self, value):
        if value <= 0:
            print("Max speed must be positive")
            return
        self._max_speed = value

# дочерний, подкласс, потомок
class Bus(Car):
    def __init__(self, color, model, seats):
        super().__init__(color, model)
        self.seats = seats

    def drive(self, location):
        # super().drive(location)
        print(f"Bus {self.model} is driving in {location}, max speed: {self._max_speed}, fine: {self.get_fined()}")

    def test_bus(self):
        print(f"Bus test {self.model}")




bus_1 = Bus("green", "Isuzu", 40)
print(bus_1.seats)
print(bus_1.color)
bus_1.drive("Bishkek")
# print(bus_1.__fined)
bus_1._test()
car1 = Car("red", "Isuzu")
car1.drive("Karakol")
print(car1.get_fined())
car1.set_fined(True)
# car1.__fined = True
print(car1.get_fined())
