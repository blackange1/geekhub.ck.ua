# 7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.

def get_count_repeat(items:list) -> int:
    res = 0
    for el in set(items):
        count = items.count(el)
        if count > 1:
            res += count
    return res


# test
print(get_count_repeat([1, 2, 3, 4, 5, 6]))
print(get_count_repeat([1, 2, 2, 3, 3, 4])) # 2 2 3 3 -> 4
print(get_count_repeat([1, 2, 2, 2, 3, 4])) # 2 2 2 -> 3