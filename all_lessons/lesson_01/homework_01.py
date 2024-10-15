#todo Home work 1:  Anton Kolomiiets

# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!") #таб не потрібен

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!") #потрібно добавити таб

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
storona_1 = 1 #Ім’я змінної не може починатися із числа
storona_2 = 2 #Ім’я змінної не може починатися із спец.сиволів
storona_3 = 3 #Як я зрозумів то можна використовувати українську мову для створення іменні змінної,
# але рекомендується використовувати англійську мову, особливо якщо код може бути використаний іншими розробниками.
storona_4 = 4 #Ім’я змінної не може починатися із спец.сиволів

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
#variant 1
trees = 4 + (4 + 5) + (4 - 2)
print('Всього посадили дерев:', trees)

#variant 2
apples = 4
pears = apples + 5
plum = apples - 2
trees = apples + pears + plum
print('Всього посадили дерев:', trees)


# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
#variant 1
temperature = 5 - 10 + 4
print(f'Tемпература надвечір була: {temperature} градус')

#variant 2
temperature_before_dinner = 5
temperature_after_dinner = -10
temperature_evening = 4
temperature = temperature_before_dinner + temperature_after_dinner + temperature_evening
print(f'Tемпература надвечір була: {temperature} градус')

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
#variant 1
all_kids = 24 + (24 / 2) - 1 - 2
print(f'Сьогодні дітей у театральному гуртку: {int(all_kids)}')

#variant 2
boys = 24
girls = boys / 2
sick_boy = 1
away_girls = 2
all_kids = boys + girls - sick_boy - away_girls
print(f'Сьогодні дітей у театральному гуртку: {int(all_kids)}')

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
#variant 1
books_price = 8 + 10 + (8 + 10) / 2
print(f'Усі книжки будуть коштувати: {books_price}')

#variant 2
first_book = 8
second_book = 10
third_book = (first_book + second_book) / 2
books_price = first_book + second_book + third_book
print(f'Усі книжки будуть коштувати: {books_price}')
