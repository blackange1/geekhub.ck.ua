# 7. Write a script to concatenate all elements in a list into a string and print it.

# v1
my_list = [1, 2, 3, 'text', [4, 5], {'name': 'Bender'}]

for item in my_list:
    print(item, end='')
print()

# v2 
my_list = [1, 2, 3, 'text', [4, 5], {'name': 'Bender'}]

res = ''
for item in my_list:
    if isinstance(item, str):
        res += item
    else:
        res += str(item)

print(res)
