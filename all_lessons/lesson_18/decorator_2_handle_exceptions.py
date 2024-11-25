'''
Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
'''

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return f"Result in {func.__name__}: {result}"
        except ZeroDivisionError as e:
            return f"ZeroDivisionError in {func.__name__}: {e}"
        except IndexError as e:
            return f"IndexError in {func.__name__}: {e}"
        except ValueError as e:
            return f"ValueError in {func.__name__}: {e}"
    return wrapper

@handle_exceptions
def divide(a, b):
    return a / b

@handle_exceptions
def access_list_element(lst, index):
    return lst[index]

@handle_exceptions
def parse_int(value):
    return int(value)


# Testing the decorator
print(divide(65, 2))
print(divide(44, 0))

print(access_list_element(['Chandler', 'Monica', 'Ross', 'Joye'], 3))
print(access_list_element(['Chandler', 'Monica', 'Ross', 'Joye'], 5))

print(parse_int("62"))
print(parse_int("not a number"))

