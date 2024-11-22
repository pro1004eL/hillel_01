'''
Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
'''

def fibonacci_generator(num):
    a, b = 0, 1
    while a <= num:
        yield a
        a, b = b, a + b


list_fibo = list(fibonacci_generator(60))
print(list_fibo)