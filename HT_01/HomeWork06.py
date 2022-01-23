'''
6. Write a script to check whether a specified value is contained in a group of values.
        Test Data:
        3 -> [1, 5, 8, 3]: True
        -1 -> (1, 5, 8, 3): False
'''
n = int(input('example: 3'))
data = input('example: [1, 5, 8, 3]')[1:-1]

if ', ' in data:
        data = data.split(', ')
else:
        data = [data]

data = list(map(int, data))
print(f'{n} -> {data}: {n in data}')
