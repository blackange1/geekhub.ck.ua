"""
Створити пустий клас, який називається Thing. Потім створіть об'єкт example цього класу. 
Виведіть типи зазначених об'єктів.
"""

class Thing(object):
    pass


example = Thing()

print(*example.__dir__(), sep='\n')