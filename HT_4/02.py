# 2. Написати функцію < bank > , яка працює за наступною логікою: користувач робить вклад у розмірі < a > одиниць строком на < years > років під < percents > відсотків 
# (кожен рік сума вкладу збільшується на цей відсоток, ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки).
#  Параметр < percents > є необов'язковим і має значення по замовчуванню < 10 > (10%). Функція повинна принтануть і вернуть суму, яка буде на рахунку.

def bank(a, years, percents=10):
    for _ in range(years):
        a += a * percents * 0.01
    
    print(a)
    return a


# test
bank(100, 2)