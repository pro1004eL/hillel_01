'''
Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
'''

def generator_even_number(N):
    for i in range(0, N+1, 2):
        yield i

even_list = list(generator_even_number(16))
print(even_list)




