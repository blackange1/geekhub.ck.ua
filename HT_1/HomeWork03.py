# 3. Write a script to sum of the first n positive integers.
sum_el = 0
while True:
    n = int(input())
    if n <= 0:
        break
    sum_el += n

print(sum_el)
