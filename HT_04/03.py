# 3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000, и яка вертатиме True, якщо це число просте, и False - якщо ні.

def is_prime(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


# test
test = [1, 2, 3, 4, 8, 11, 17, 21, 29, 121]

for n in test:
    print(f'is_prime({n}) = {is_prime(n)}')