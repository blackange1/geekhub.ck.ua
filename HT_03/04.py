# 4. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат. Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат та також повертає результат. Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3
def abs_vector(x, y) -> float:
    return (x ** 2 + y ** 2) ** 0.5


def what_plane(x, y) -> str:
    if 0 in (x, y):
        return 'x or y = 0'
    if x * y < 0:
        if x < 0:
            return 'plane II'
        return 'plane IV'
    if x > 0:
        return 'plane I'
    return 'plane III'


def normal_v(x, y) -> tuple:
    k_vector = abs_vector(x, y)
    return x / k_vector, y / k_vector


def info_vector(x, y) -> tuple:
    info = []
    for f in (abs_vector, what_plane, normal_v):
        info.append(f(x, y))
        print(f'{f.__name__}({x}, {y}) = {info[-1]}')
    return tuple(info)
        

data = info_vector(3, 4)
print('info_vector =', data)