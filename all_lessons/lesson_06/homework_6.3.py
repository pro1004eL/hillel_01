

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

# Create a new list that contains only the string variables from lst1
lst2 = [item for item in lst1 if type(item) == type('str')]

print(lst2)