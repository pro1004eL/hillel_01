# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the appropriate variable
        multiplier += 1

print('Task_1')
multiplication_table(6)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_num(num1, num2):
    return num1 + num2

print('Task_2')
print('The sum of two numbers:', sum_two_num(26.5, -1))


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_mean(numbers):
    return sum(numbers) / len(numbers)

numbers = [1,2,4,5,6,5,5,5,5,5,5,10, -12]

print('Task 3')
print(f'The arithmetic mean of a list of numbers: {average_mean(numbers)}')

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_list(txt):
    return txt[::-1]

any_text = 'some string'

print('Task 4')
print(f'Text in reverse order: {reverse_list(any_text)}')

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(lst):
    lgst_word = max(lst, key=len)
    return lgst_word

words = ['Write', 'function', 'function', 'function', 'that', 'takes', 'a', 'list', 'of', 'words']

print('Task 5')
print(f'The longest word in the list: {longest_word(words)}')


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

print('Task 6')
str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7-10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7
# create a function to the homework 6.3
# сформує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
def take_what_you_need(lst):
    # Create a new list that contains only the string variables from lst1
    lst2 = [item for item in lst1 if type(item) is str]
    return lst2

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

print('Task 7')
print(f'Only "str" type: {take_what_you_need(lst1)}')

# task 8
# create a function to the homework 6.4
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
def summ_even_number(numbers):
    # Create a new list that contains only even numbers from numbers_lst and sum it
    sum_even_lst = sum(item for item in numbers_lst if item % 2 == 0)
    return sum_even_lst

numbers_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print('Task 8')
print(f'Сума усіх парних чисел: {summ_even_number(numbers_lst)}')

# task 9
# create a function to the homework 5.2[3]
# 3 - check that all people in modified list with records indexes 6, 10, 13 have age >= 30.

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

def indexes_to_check_age(index1, index2, index3):
    all_above_30 = all(people_records[index][2] >= 30 for index in [index1, index2, index3])

    if all_above_30:
        return 'All people at the specified indexes have age >= 30'
    else:
        return 'Not all people at the specified indexes have age >= 30'

print('Task 9')
print(indexes_to_check_age(6, 10, 13))

# task 10
# create a function to the homework 5.1
# get cars that satisfy search criteria
# Cars should be sorted by price ascending.
# We should print up to five (5) first found elements

car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
  'Kia': ('white', 2020, 2.0, 'sedan', 28000),
  'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
  'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
  'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
  'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
  'Jeep': ('green', 2021, 3.0, 'suv', 50000),
  'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
  'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
  'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
  'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
  'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
  'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
  'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
  'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
  'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
  'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
  'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
  'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
  'Acura': ('white', 2017, 2.4, 'suv', 40000),
  'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
  'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
  'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
  'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
  'Ram': ('black', 2019, 5.7, 'pickup', 40000),
  'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
  'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
  'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
  'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}
def suitable_cars(min_year, min_engine_volume, max_price):

    suitable_cars_list = [
        (car, *data)
        for car, data in car_data.items()
        if data[1] >= min_year and data[2] >= min_engine_volume and data[4] <= max_price
    ]

    # sorted 'suitable_cars_list' by price ascending
    sorted_by_price = sorted(suitable_cars_list, key=lambda x: x[5])

    if not sorted_by_price:  # if list is empty print 'No matching cars' text
        print( 'No matching cars')
    else:  # if matches exist - print up to five first found elements
        for car, color, year, engine_volume, car_type, price in sorted_by_price[:5]:
            print (f"{car}: {color}, {year}, {engine_volume}, {car_type}, {price}")

print('Task 10')
suitable_cars(2017, 1.6, 35000)

