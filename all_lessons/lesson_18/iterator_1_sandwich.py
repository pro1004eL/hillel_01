
'''
Реалізуйте ітератор для зворотного виведення елементів списку.
'''
class ReverceSandwichIterator:

    def __init__(self, items):

        self.items = items
        self.index = len(items) - 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.index >= 0:
            item = self.items[self.index]
            self.index -= 1
            return item
        else:
            raise StopIteration

myList = ['bread', 'butter', 'cheese', 'jam']

for item in ReverceSandwichIterator(myList):
    print(item)



