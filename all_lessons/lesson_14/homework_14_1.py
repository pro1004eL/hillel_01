
class Student:
    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_score = 0

    def set_average_score(self, average_score):

        self.average_score = average_score



anton = Student(first_name='Anton', last_name='Kolomiiets', age=33)



print(f'First name: {anton.first_name}\nLast name: {anton.last_name}\n'
      f'Age: {anton.age}\nAverage score: {anton.average_score}\n')

anton.set_average_score(99.9)

print(f'First name: {anton.first_name}\nLast name: {anton.last_name}\n'
      f'Age: {anton.age}\nAverage score: {anton.average_score}\n')

