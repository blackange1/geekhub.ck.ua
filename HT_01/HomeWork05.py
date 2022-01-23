'''
5. Write a script to convert decimal to hexadecimal
        Sample decimal number: 30, 4
        Expected output: 1e, 04
'''

# v1 
# print(', '.join(map(lambda n: (n, f'0{n}')[len(n) < 2], sorted(
#     [hex(int(n))[2:] for n in input().split(', ')]))))

# v2 
data = input('example: 30, 4')

if ', ' in  data:
        data = data.split(', ')
else:
        data = [data]

for i in range(len(data)):
        tmp = hex(int(data[i]))[2:]
        if len(tmp) < 2:
                tmp = '0' + tmp
        data[i] = tmp

print(*data, sep=', ')