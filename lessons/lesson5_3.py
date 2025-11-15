def repeat_decorator(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator


@repeat_decorator(5)
def hello_world():
    return print("Hello World")

# hello_world()


def class_decorator(cls):
    class NewClass(cls):
        def new_method(self):
            return print("I am a new method!!")
    return NewClass

@class_decorator
class OldClass:
    def old_method(self):
        return print("I am old method!!")

obj_1 = OldClass()

print(type(obj_1))

class I:
    def t(self):
        pass

class J(I):
    def t2(self):
        pass