"""
1. Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран. Список можна "захардкодити".
   Елементами списку повинні бути як рядки, так і числа.
"""
# v1-------------------------------|
#----------------------------------|
list_1 = [1, 2, 3, '45', '678', 90]

print(''.join(map(str, list_1)))


# v2-------------------------------|
#----------------------------------|
# list_1 = [1, 2, 3, '45', '678', 90]

# res = ''
# for elem in list_1:
#    res += str(elem)

# print(res)
