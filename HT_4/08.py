"""
8. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку. Тобто, функція приймає два аргументи: 
   список і величину зсуву (якщо ця величина додатня - пересуваємо з кінця на початок, якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
   Наприклад:
       fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
       fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]
"""

print(-1 % 5)

def fnc(arr:list, shift):
    res = []
    for i in range(len(arr)):
        index = (-shift + i) % len(arr)
        res.append(arr[index])
    print(res)
    return res


# text
fnc([1, 2, 3, 4, 5], shift=1)
fnc([1, 2, 3, 4, 5], shift=-2)