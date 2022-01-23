# 7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.

def get_count_repeat(items:list) -> list:
    res = []
    for el in set(items):
        count = items.count(el)
        message = 'раз'
        if (count in (3, 4)) or (count % 10 == 2 and count != 12):
            message = 'раза'
        res.append(f'{el} - {count} {message}')
    return res


# test
print(get_count_repeat([1, 3, 3, 1, 1, 1, 1, "g", (1, "a", 2), (1, "a", 2)]))
# ['1 - 5 раз', 'g - 1 раз', '3 - 2 раза', "(1, 'a', 2) - 2 раза"]