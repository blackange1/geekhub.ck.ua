# 6. Вводиться число. Якщо це число додатне, знайти його квадрат, якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.

def get_super_number(number):
    if number > 0:
        return number ** 0.5
    if number < 0:
        return number * 100
    return number


print(get_super_number(int(input())))