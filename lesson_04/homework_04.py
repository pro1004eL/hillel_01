import re

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while 
the late steamer 
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

# перезаписали зміст змінної adwentures_of_tom_sawer замінивши кінець абзацу на пробіл
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

# task 02 ==
""" Замініть .... на пробіл
"""
# перезаписали зміст змінної adwentures_of_tom_sawer замінивши "...." на пробіл
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
# розділяємо рядок на частини
words = adwentures_of_tom_sawer.split()
# обʼєднуємо рядки в змінній "text" за допомогою "пробіла" як роздільник
adwentures_of_tom_sawer = ' '.join(words)



# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
chracter_h = adwentures_of_tom_sawer.count('h')
print('Task 04')
print(f'У тексті літера "h" зустрічається: {chracter_h} разів.')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
# Варіант 1: використав регулярне вираження
condition1 = r'[A-Z]+'
match_list = re.findall(condition1, adwentures_of_tom_sawer)
print('Task 05')
print(f'У тексті {len(match_list)} слів починається з Великої літери.') # Використовуючи рег. вираження кількість слів: 14


# Варіант 2: використав цикл 'for'
words = adwentures_of_tom_sawer.split() # розділяємо рядок на частини
capitalized_words = []
for word in words:
    if word[0].isupper():
        capitalized_words.append(word)
print(f'У тексті {len(capitalized_words)} слів починається з Великої літери.') # Виводить 13 слів з великої букви
# пропускає слово "Big, так як індекс 0 це лапки... запитати Дениса

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
tom_position2 = adwentures_of_tom_sawer.index('Tom', 1)
print('Task 06')
print(f'Позиція в тексті на якій слово "Tom" зустрічається вдруге: {tom_position2}')


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
# розділяємо текст по кінцю речення:
sentences = adwentures_of_tom_sawer.split('.')
# створюємо пустий список для збереження результату:
adwentures_of_tom_sawer_sentences = []
# ітеруємо рядки за допомогою циклу for:
for sentence in sentences:
    # видаляємо зайві пробіли з початку та кінця кожного рядка:
    cleaned_sentence = sentence.strip()
    if cleaned_sentence:
        # добавляємо рядки до кінцевого списку
        adwentures_of_tom_sawer_sentences.append(cleaned_sentence)


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
sentence_four = adwentures_of_tom_sawer_sentences[3].lower()
print('Task 08')
print(sentence_four) # вивели четверте речення з adwentures_of_tom_sawer_sentences в нижньому регістрі

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
#

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
