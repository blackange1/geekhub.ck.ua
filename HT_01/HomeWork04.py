# 4. Write a script to concatenate N strings.

# v1
print(''.join([input() for _ in range(int(input()))]))

# v2
# print(*[input() for _ in range(int(input()))], sep='')