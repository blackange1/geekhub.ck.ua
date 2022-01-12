def sum(a, b):
    return (int(a) * 100 + int(b) * 100) / 100


def isfloat(s):
    return s.replace('.', '', 1).isdigit()


def number_of_bills(n, args):
    if len(args) != 7:
        return None
    
    n1000, n500, n200, n100, n50, n20, n10 = args

    for k1000 in range(min(n // 1000, n1000), -1, -1):
        for k500 in range(min(n // 500, n500), -1, -1):
            for k200 in range(min(n // 200, n200), -1, -1):
                for k100 in range(min(n // 100, n100), -1, -1):
                    for k50 in range(min(n // 50, n50), -1, -1):
                        for k20 in range(min(n // 20, n20), -1, -1):
                            for k10 in range(min(n // 10, n10), -1, -1):
                                if 1000 * k1000 + 500 * k500 + 200 * k200 + 100 * k100 + 50 * k50 + 20 * k20 + 10 * k10 == n:
                                    return (k1000, k500, k200, k100, k50, k20, k10)

modul = 'calculate'
if __name__ == '__main__':
    print(f'You run lib {modul}')