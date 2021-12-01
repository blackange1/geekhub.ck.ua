"""
6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
"""

def my_range(start, end=None, step=1):
    if end is None:
        start, end = 0, start
    if step == 0:
        raise ValueError()
    if step > 0:
        while start < end:
            try:
                yield start
                start += step 
            except StopIteration:
                print('end iterator')
    else:
        while start > end:
            try:
                yield start
                start += step 
            except StopIteration:
                print('end iterator')


# test 
for i in my_range(2):
    print(i)

print(list(my_range(4)))
print(list(my_range(4, 10)))
print(list(my_range(4, 10, 2)))
print(list(my_range(10, 1, -2)))
print(list(my_range(10, 1, 0)))
