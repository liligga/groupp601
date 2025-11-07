class Car:
    cars_total = 0

    def __init__(self, color, model, speed):
        self.color = color
        self.model = model
        self.speed = speed
        Car.cars_total += 1

    @staticmethod
    def validate_speed(speed):
        # статический метод для проверки скорости
        if speed < 0:
            raise ValueError(f"Speed cannot be negative: {speed}")
        return True

    @classmethod
    def create(cls, color, model, speed):
        # метод класса для создания объекта
        if cls.validate_speed(speed):
            new_car = cls(color, model, speed)
            return new_car

    @classmethod
    def get_cars_total(cls):
        return cls.cars_total

car_mazda = Car.create("red", "Mazda", 100)
car_1 = Car.create("red", "Mazda", -10)
print(car_mazda.color)
print(Car.cars_total)
print(Car.get_cars_total())