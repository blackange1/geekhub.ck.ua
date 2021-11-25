# 5. Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.

def fibonacci(number):
    a, b = 1, 1
    print(a)
    while number > b:
        b, a = a + b, b
        print(a)
    return None


# test
fibonacci(100)