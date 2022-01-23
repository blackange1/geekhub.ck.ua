"""
1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
   Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
   Логіка наступна:
       якщо введено коректну пару ім'я/пароль - вертається <True>;
       якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, інакше (<silent> == <False>) - породжується виключення LoginException
"""
class LoginException(Exception):
    pass


def login_user(username, password, silent=False):

    data = [
        {
            'name': 'Trinity',
            'password': 'blablabla',
        },
        {
            'name': 'Esteban',
            'password': 'password',
        },
        {
            'name': 'Claude',
            'password': '1234',
        },
        {
            'name': 'Kennedy',
            'password': 'aracadabra',
        },
        {
            'name': 'Elsie',
            'password': 'iambatman',
        },
    ]

    for d in data:
        name, pw = d.get('name'), d.get('password')
        if username == name and password == pw:
            return True

    if silent:
        return False

    raise LoginException("Ups...") 


# test
print(login_user('Kennedy', 'aracadabra'))
print(login_user('Kennedy', '**********', silent=True))
print(login_user('Kennedy', '**********'))
