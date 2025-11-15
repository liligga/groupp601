from lessons.lesson1 import Car

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"Money object, amount={self.amount}"

    # eq: equal
    def __eq__(self, other):
        print(f"other: {other}")
        if self.amount == other.amount:
            return True
        return False

    # lt: less than: <
    # lte: less than or equal <=
    # gt: greater than >
    # gte: greater than or equal >=
    def __lt__(self, other):
        print(f"other: {other}")
        if self.amount < other.amount:
            return True
        return False

    def __add__(self, other):
        new_amount = self.amount + other.amount
        return Money(new_amount)

    # sub: subtract
    def __sub__(self, other):
        new_amount = self.amount - other.amount
        return Money(new_amount)

car_1 = Car("red", "honda civic")
print(car_1)
print(car_1.model)
money1 = Money(100)
print(money1)
money2 = Money(200)
print(money2 == money1)
print(money1 < money2)
# print(money1 <= money2) # error no lte in class Money
print(id(money1), id(money2))
money3 = money1 + money2
print(money3, id(money3))
money4 = money3
print(id(money4), id(money3))