# 4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.

def prime_list(start, end) -> list:
    res = []

    def is_prime(number):
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False
        return True

    for n in range(start, end + 1):
        if is_prime(n):
            res.append(n)
    return res


# test
print(prime_list(3, 100))
