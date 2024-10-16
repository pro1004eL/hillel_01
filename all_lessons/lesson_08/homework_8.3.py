# Напишіть інтерактивний калькулятор. Передбачається, що користувач вводить формулу,
# що складається з числа, оператора (як мінімум * і /) та іншого числа, розділених пробілом (наприклад, 2 * 5).
# Якщо вхідні дані не складаються з трьох елементів, генеруйте та спіймайте власний ексепшн FormulaError.
# Якщо другий елемент не є «*» або «/», генеруйте та спіймайте власний ексепшн WrongOperatorError
# Якщо введені числа не int або float спіймайте ValueError
# Також ловіть помилку при діленні на 0
# В кожній спійманій помилці друкуйте пояснення, що пішло не так
# Надайте три спроби скористуватись калькулятором, якщо введені не вірні дані, якщо не вийшло - прінтайте що закінчились спроби
# Результат виконання формули - float число з двома знаками після крапки

class WrongOperatorError(Exception):
    def __init__(self):
        super().__init__('Error: Wrong Operator')

class FormulaError(Exception):
    def __init__(self):
        super().__init__('Error: Not enough elements')



def interactivity_calculator():

    attempts = 3

    while attempts > 0:

        formula = input('Please, enter your formula (e.g. 6 / 3): ')

        try:

            elements = formula.split()

            if len(elements) != 3: # Raise an error if there are not exactly 3 elements
                raise FormulaError

            num1, operator, num2 = elements
            num1 = float(num1)
            num2 = float(num2)

            if operator == '/':
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 / num2
            elif operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            else:
                result = num1 * num2

            if operator not in ('/', '*', '+', '-'):
                raise WrongOperatorError

            print(f"Result: {result:.2f}")
            return  # Exit the function after successful calculation

        except FormulaError as fe:
            print(fe)
        except WrongOperatorError as oe:
            print(oe)
        except ZeroDivisionError as zde:
            print('Error: Division by zero is not allowed')
        except ValueError as ve:
            print(f'Error: Entered values are not numbers: {ve}')

        attempts -= 1

    print('Attempts are over.')

interactivity_calculator()

