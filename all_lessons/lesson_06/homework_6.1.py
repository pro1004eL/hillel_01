
characters = str(input('Please enter the text: '))

characters_uniq = set(characters) # set automatically removes duplicates
characters_lens = len(characters_uniq)

# Check if the number of unique characters is greater than 10
if characters_lens > 10:
    result = True
else:
    result = False

print(result)