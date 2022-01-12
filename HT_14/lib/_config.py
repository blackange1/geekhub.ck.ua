import pathlib

ADMIN = 'Панель адміністратора системи GOLD LAMP'
HELLO = 'Вітаємо вас в GOOLD LAMP'
CREATE_USER = 'Створення нового користувача GOLD LAMP | для виходу введіть EXIT'
NOMINAL = (1000, 500, 200, 100, 50, 20, 10)
EXIT = '____ для виходу натисніть ENTER\n'
LOGIN = 'Авторизація в системі GOLD LAMP'
USERS_DB = pathlib.Path(__file__).parent.parent.joinpath('db').joinpath('users.db')
