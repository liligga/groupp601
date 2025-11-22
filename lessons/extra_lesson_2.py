def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("function working")
        func(*args, **kwargs)
    return wrapper


@my_decorator
def print_text(name):
    print(f'Hello {name}')

@my_decorator
def test_function(text):
    print(f"Test function {text}")

# print_text = my_decorator(print_text)
print_text("Artur")

# test_function = my_decorator(test_function)
test_function(text="Artur")