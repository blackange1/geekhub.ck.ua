# 2. Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).

start_year, end_year = map(int, input('введівть інтервал років. Наприклад: 1200 2021\n').split())

for year in range(start_year, end_year + 1):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(year)
