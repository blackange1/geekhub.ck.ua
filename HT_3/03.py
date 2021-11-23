# 3. Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12), яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)

months = {
    (12, 1, 2): 'зима',
    (3, 4, 5): 'весна',
    (6, 7, 8): 'лiто',
    (9, 10, 11): 'осiнь',
}

n = int(input('enter number month (1 - 12)\n'))
for key, month in months.items():
    if n in key:
        print(month)
        break