# @abstractmethod
# @staticmethod
# @classmethod
# @property

# Декоратор
def simple_decorator(func):
    def wrapper():
        print('До выполнения!!!')
        func()
        print('после выполнения!!')
    return wrapper


@simple_decorator
def say_hello():
    return print("hello!!")

@simple_decorator
def test():
    return print("test")

say_hello()
test()


def greeting_decorator(func):
    def wrapper(name):
        print(f'Hello !!')
        func(name)
    return wrapper

@greeting_decorator
def greet(name):
    return print(f"Как дела {name}?")


greet("Ardager")