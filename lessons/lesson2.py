# родитель, суперкласс
class Car:
    # инициализатор объектов
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive(self, location):
        print(f"Car {self.model} is driving in {location}")

    def test(self):
        self.drive("Karakol")

# дочерний, подкласс, потомок
class Bus(Car):
    def __init__(self, color, model, seats):
        super().__init__(color, model)
        self.seats = seats

    def drive(self, location):
        # super().drive(location)
        print(f"Bus {self.model} is driving in {location}")

    def test_bus(self):
        print(f"Bus test {self.model}")

bus_1 = Bus("green", "Isuzu", 40)
print(bus_1.seats)
print(bus_1.color)
bus_1.drive("Bishkek")
# bus_1.test_bus()