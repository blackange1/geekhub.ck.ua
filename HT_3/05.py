"""
5. Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
-  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї), пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" і при нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.
-  Повиннi опрацювати такi умови:
-  x > y;       вiдповiдь - х бiльше нiж у на z
-  x < y;       вiдповiдь - у бiльше нiж х на z
-  x == y.      вiдповiдь - х дорiвнює z
"""
def comparison_of_numbersmy(x, y) -> str:
    x, y = map(float, (x, y))
    if x > y:
        return f'х бiльше нiж у на {abs(x - y)}'
    if x < y:
        return f'y бiльше нiж x на {abs(x - y)}'
    return f'вiдповiдь - х дорiвнює {x}'


print(comparison_of_numbersmy(1, 2))
print(comparison_of_numbersmy('1', -2))
print(comparison_of_numbersmy(0, '0'))