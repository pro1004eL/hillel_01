'''
Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
'''

class EvenNumbersIterator:

    def __init__(self, number):

        self.number = number
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.current > self.number:
            raise StopIteration

        even_number = self.current
        self.current += 2
        return even_number

list_of_even_numbers = list(EvenNumbersIterator(26))
print(list_of_even_numbers)