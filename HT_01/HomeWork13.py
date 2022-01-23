'''
13. Write a script to get the maximum and minimum value in a dictionary.
'''
d = {
    'key 1': 8,
    'key 2': 1,
    'key 3': 5,
    'key 4': 4,
    'key 5': 9,
    'key 6': 0,
    'key 7': 3,
}

values = d.values()
print(f'max = {max(values)}, min = {min(values)}')
