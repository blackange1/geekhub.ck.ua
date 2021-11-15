'''
5. Write a script to convert decimal to hexadecimal
        Sample decimal number: 30, 4
        Expected output: 1e, 04
'''
print(', '.join(map(lambda n: (n, f'0{n}')[len(n) < 2], sorted(
    [hex(int(n))[2:] for n in input().split(', ')]))))
