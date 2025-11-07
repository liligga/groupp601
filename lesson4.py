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

    # def get_fined(self):
    #     # геттер
    #     return self.__fined
    #
    # def set_fined(self, value):
    #     # сеттер
    #     self.__fined = value

    @property
    def fined(self):
        # геттер работающий как атрибут
        return self.__fined

    @fined.setter
    def fined(self, val):
        # сеттер работающий как атрибут
        if type(val) != bool:
            raise TypeError("fined must be a boolean")
        self.__fined = val

    def set_max_speed(self, value):
        if value <= 0:
            # print("Max speed must be positive")
            raise ValueError("max_speed must be positive")
        self._max_speed = value


car1 = Car("red", "Isuzu")
# car1.set_max_speed(0) # error raised
print(car1.fined)
car1.fined = True
print(car1.fined)
