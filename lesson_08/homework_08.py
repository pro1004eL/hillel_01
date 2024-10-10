
def summ_item(list):

    try:
        # Split the string by commas to get a list of strings, then convert to integers
        for item in list:
            numbers = [int(num) for num in item.split(',')]
            # Calculate the sum of the list of integers
            total = sum(numbers)
            print(f'Sum of {item}: {total}')

    except ValueError as val_er:
        print("Can't sum it up!")

lst = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']

summ_item(lst)