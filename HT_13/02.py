"""
Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів, які зберігатиме в відповідні змінні.
Методи, які повинні бути в класі Person 
    - show_age, print_name, show_all_information.
    - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.
"""

class Person(object):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def show_age(self) -> None:
        print(self.age)

    def print_name(self) -> None:
        print(self.name)
    
    def show_all_information(self) -> None:
        print(f'name: {self.name}, age: {self.age}')


p1 = Person('Gregor', 55)
p1.profession = 'Teacher'

p2 = Person('Peta', 25)
p2.profession = 'Cook'