"""
5. Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити). Словник для
   роботи захардкодити свій.
                Приклад словника (не використовувати):
                {'a': 1, 'b': 3, 'c': 1, 'd': 5}
                Очікуваний результат:
                {'a': 1, 'b': 3, 'd': 5}
"""
student_data = {
    'id1':
    {
        'name': 'Volodymyr',
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id2':
    {
        'name': 'David',
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id3':
    {
        'name': 'Volodymyr',
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id4':
    {
        'name': 'Artem',
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
}

res = {}

for key, value in student_data.items():
    if value not in res.values():
        res[key] = value

print(res)