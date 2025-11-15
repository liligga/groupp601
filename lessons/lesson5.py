class Swimm:
    def move(self):
        return f"Плавает"
    pass
class Flyable:
    def move(self):
        return f"Летает"
    pass
class Animal:
    def move(self):
        return f"Двигается"
    pass

class Duck(Animal, Swimm, Flyable):
    # def move(self):
    #     return "Может плавать летать и ходить"
    pass

donald_duck = Duck()
print(donald_duck.move())
print(Duck.__mro__)


class A:
    def action(self):
        return print("A")

class B(A):
    def action(self):
        super().action()
        return print("B")

class C(A):
    def action(self):
        # super().action()
        return print("C")

class D(B, C):
    # def action(self):
    #     return "D"
    pass

obj_d = D()
obj_d.action()
print(D.__mro__)


