'''
Напишіть декоратор, який логує аргументи та результати викликаної функції.
'''

def log_arguments_and_results(func):

    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")

        return result

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__

    return wrapper

@log_arguments_and_results
def multiply(a, b):
    return a * b

@log_arguments_and_results
def add(a, b):
    return a + b

@log_arguments_and_results
def greet(name, greeting="Hi"):
    return f"{greeting}, {name}!"


# Testing the decorator
multiply(777, 777)
add(133, 1235)
greet("Harry", greeting="Welcome")