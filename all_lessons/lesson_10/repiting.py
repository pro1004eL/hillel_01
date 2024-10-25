
# 1
def capitalize_text(str):
    return str.title()


# 2
def word_count(str):
    count_words_in_str = str.split()
    return len(count_words_in_str)

print('The words number:', word_count(str2))

# 3
def concatenate_strings(lst, separator):
    return separator.join(lst)

print(concatenate_strings(['1', '2', '3'], ', '))

# 4