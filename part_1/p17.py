# Example 1: Simple Decorator

def my_decorator(func):

    def wrapper():
        print("Before function execution")

        func()

        print("After function execution")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()

def decorator(func):

    def wrapper(a, b):
        print("Adding numbers...")

        result = func(a, b)

        print("Result is:", result)

    return wrapper


@decorator
def add(a, b):
    return a + b


add(5, 3)

def method_decorator(func):
    def wrapper(self):
        print("Before method call")

        func(self)

        print("After method call")

    return wrapper


class Demo:
    @method_decorator
    def show(self):
        print("Inside method")


obj = Demo()
obj.show()