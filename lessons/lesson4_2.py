from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def test(self):
        pass

class Dog(Animal):
    def test(self):
        print("Dog test")

    def make_sound(self):
        print("Гав гав")


class Cat(Animal):
    # def test(self):
    #     print("Cat test")

    def make_sound(self):
        print("мяяяяу")

puppy = Dog()
puppy.make_sound()
kitten = Cat()