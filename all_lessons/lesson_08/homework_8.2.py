# Лише за допомогою функцій map, lambda, zip(необов'зково) створити та надрукувати словник квадратів цих чисел
# Очікуваний результат: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

square_up = dict(map(lambda item: (int(item), int(item)**2), str_list))

print(square_up)