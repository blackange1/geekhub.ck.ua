# 7. Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!

def calculation(x, y, oper='sum'):
    d = {
        'sum': lambda x, y: x + y,
        'sub': lambda x, y: x - y,
        'mul': lambda x, y: x * y,
        'pow': lambda x, y: x ** y,
        'div': lambda x, y: x // y,
        'mod': lambda x, y: x % y,
        'dil': lambda x, y: x / y if y != 0 else 'ділити на нуль не можна',
    }

    if oper in d:
        return d[oper](x, y)
    return None


print(calculation(2, 5))
print(calculation(2, 5, 'sub'))
print(calculation(2, 5, 'pow'))
print(calculation(2, 5, 'dil'))
print(calculation(2, 0, 'dil'))