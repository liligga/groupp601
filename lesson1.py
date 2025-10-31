class Car:
    # инициализатор объектов
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive(self, location):
        print(f"Car {self.model} is driving in {location}")

    def test(self):
        self.drive("Karakol")

class MySuperBigCar:
    pass

color = "red"
car_honda = Car(color="red", model="Honda")
car_subaru = Car(color="silver", model="Subaru")

car_honda.drive("Bishkek")
car_honda.test()
print(car_honda)
print(car_subaru)
print(car_honda.color)
print(car_subaru.color)
print(car_honda.model == car_subaru.model)

print(type(123), type("aaaaaaaa"))
print(type(car_subaru))