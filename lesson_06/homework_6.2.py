

while True:
    user_word = str(input('Please enter a word with letter H or h: '))
    if 'H' in user_word.upper(): # converts the word to uppercase using, so that both 'h' and 'H' are handled
        print('Text is correct')
        break