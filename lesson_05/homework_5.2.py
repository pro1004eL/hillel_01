# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

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

# task 01
# use function 'insert' for add new record to the beginning of the list
people_records.insert(0, ('Anton', 'Kolomiiets', 33, 'QA Engineer', 'Zhytomyr'))

# task 2
# In modified list swap elements with indexes 1 and 5 (1<->5)
people_records[1], people_records[5] = people_records[5], people_records[1]

# print result
print('Task 02')
for item in people_records:
    print(item)

# task 3
# indexes to check age
indexes_to_check_age = [6, 10, 13]

# Check if all people at the specified indexes have age >= 30
all_above_30 = True # Assume all ages are >= 30

# Iterate over the list of indexes to check
for index in indexes_to_check_age:
    # Check if the age at the current index is less than 30
    if people_records[index][2] < 30:
        all_above_30 = False

# Print the condition check result
print('Task 3')

if not all_above_30: # print if not all people have age >= 30
    print('Not all people at the specified indexes have age >= 30')
else: # if all people have age >= 30
    print('All people at the specified indexes have age >= 30')



