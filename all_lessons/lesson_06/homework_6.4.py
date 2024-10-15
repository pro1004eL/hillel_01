

numbers_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# Create a new list that contains only even numbers from numbers_lst and sum it
sum_even_lst = sum(item for item in numbers_lst if item % 2 == 0)

print(f'Сума усіх парних чисел: {sum_even_lst}')