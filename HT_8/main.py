import csv
from pathlib import Path
from time import sleep
from user import User, print_message, print_warning


MAIN_PATH = Path(__file__).parent.joinpath('db')
USERS_DB = MAIN_PATH.joinpath('users.data')

ADMIN = 'Панель адміністратора системи GOLD LAMP'
HELLO = 'Вітаємо вас в GOOLD LAMP'
CREATE_USER = 'Створення нового користувача GOLD LAMP | для виходу введіть EXIT'
LOGIN = 'Авторизація в системі GOLD LAMP'
NOMINAL = (1000, 500, 200, 100, 50, 20, 10)


def login():
    print_message(LOGIN)
    name = input("Введіть ім'я користувача | username\n")

    data = None
    with open(USERS_DB) as file:
        reader = csv.DictReader(file)

        for row in reader:
            if  name == row['name']:
                data = (row['name'], row['password'], row['is_admin'])
                break
            
    if data == None:
        print_message(LOGIN)
        print(f"Ми не знайшли ім'я {name} в системі :(\n")
        sleep(2)
    
    else:
        for massage in ('', 'attempt2', 'attempt 3'):
            print_message(LOGIN)
            if input(f'введіть пароль {massage}\n') == data[1]:
                return data

        print_message(LOGIN)
        print('ви використали три спроби :(')
        sleep(2)
    
    return None


def user_interface(name, pw):
    user = User(name)
    USER_INTERFACE = f'{name.upper()}, вітаємо в системі GOLD LAMP'
    
    while True:
        print_message(USER_INTERFACE)
        print('1. Баланс')
        print('2. Поповнити рахунок')
        print('3. Зняти готівку')
        print('4. Вихід')
        get_op = input()
        # 1
        if get_op == '1':

            print_message(USER_INTERFACE)
            print(f'____ Ваш баланс {user.get_balance()}')
            input('____ для виходу натисніть ENTER\n')

        # 2
        elif get_op == '2':
            have_problem = True
            for _ in range(3):
                print_message(USER_INTERFACE)
                money = input('___ введіть суму яку слід покласти на рахунок?\n')
                if user.isfloat(money):
                    money = float(money)
                    user.replenish_balance(money)
                    user.add_transactions('add_money', money)

                    print_message(USER_INTERFACE)
                    print(f'____ Ви поповнили рахунок на {money}')
                    input('____ для виходу натисніть ENTER\n')

                    have_problem = False
                    break
                else:
                    print_message(USER_INTERFACE)
                    print_warning('___ Error writes :(', 2)

            if have_problem:
                print_message(USER_INTERFACE)
                print_warning('___ Ви використали три спроби  :(', 2)
        # 3
        elif get_op == '3':

            have_problem = True
            for _ in range(3):
                print_message(USER_INTERFACE)
                money = input('___ Скільки ви хочете зняти?\n')
                if user.isfloat(money):
                    money = float(money)
                    now_money = user.get_balance()
                    if now_money < money:
                        print_message(USER_INTERFACE)
                        print_warning(f'___ Ви хочете зняти більше ніж у вас є. Вам доступно {now_money}', 2)
                        have_problem = False

                    else:
                        
                        get_money = user.get_money_bank(int(money))
                        
                        if get_money:

                            user.replenish_balance(-money)
                            user.add_transactions('withdraw_money', money)
                            print_message(USER_INTERFACE)
                            for i in range(7):
                                if get_money[i] != 0:
                                    print(f'{NOMINAL[i]} x {get_money[i]}')

                            print(f'___ Ви зняли {money}')
                            input('Для завершення операції натисніть ENTER')

                            have_problem = False
                        else:

                            have_problem = False

                            print('На даний момент в банкомата не має таких купюр :(', 2)
                            input('Для завершення операції натисніть ENTER')
                    break
                else:
                    print_message(USER_INTERFACE)
                    print_warning('___ Error writes :(', 2)

            if have_problem:
                print_message(USER_INTERFACE)
                print_warning('___ Ви використали три спроби  :(', 1)
        # 4
        elif get_op == '4':
            break
        else:
            print_warning('Невідома команда :(', 2)


def admin_interface(name, pw):
    admin = User(name, password=pw, is_admin=True)
    while True:

        print_message(ADMIN)
        print('0 - Переглянути вміст касети')
        print('1 - Поповнит банкомат')
        print('2 - Вихід')
        input_admin = input()

        if input_admin == '0':
            print_message(ADMIN)
            res = admin.get_info_money_db()

            if res:
                for k, v in res.items():
                    print(f'{k} -> {v}')
                input('Щоб повернутися назад - натисніть ENTER')
            else:
                print_warning('error', 2)

        elif input_admin == '1':
            print_message(ADMIN)
            money = []

            i = 0
            while i < 7:
                input_admin = input(f'Яка кількість кюпюр буде додана номіналом {NOMINAL[i]} x ')
                if input_admin.isdigit():
                    money.append(int(input_admin))
                    i += 1
                    continue
                print('Error not intager')

            admin.add_money_db(money)
            print_warning('Банкомат поповнено', 2)

        elif input_admin == '2':
            break

        else:
            print_warning('Невірна команда :(')


def create_user():
    name = None
    pw = None
    is_admin = None

    while True:
        print_message(CREATE_USER)
        print("Ви бажаєте створити:")
        print("0 - звичайного користувача")
        print("1 - адміністратора")
        tmp = input()
    
        if tmp == '0':
            is_admin = False
            break
        elif tmp == '1':
            is_admin = True
            break
        else:
            print_warning('Error writes :(')
    
    while True:
        print_message(CREATE_USER)
        name = input("Введіть ім'я нового користувача\n")
        
        if name.upper() == 'EXIT':
            return None

        if name == '':
            print_message(CREATE_USER)
            print_warning("Ім'я не може бути пустою строкою", 2)
            continue

        for ch in '/\:*?"<>|':
            if ch in name:
                print_message(CREATE_USER)
                print_warning('Ім\'я не посинно містити такі символи /\:*?"<>|', 2)
                continue
        break            
    
    while True:
        while True:
            print_message(CREATE_USER)
            pw = input("Введіть пароль для нового користувача\n")

            if pw.upper() == 'EXIT':
                return None

            if len(pw) < 4:
                print_message(CREATE_USER)
                print_warning('Мінімальна довжина паролю має бути більша за чотири символи', 2)
                continue
            
            break
                
        print_message(CREATE_USER)
        pw_repeat = input("Повторіть пароль\n")

        if pw_repeat.upper() == 'EXIT':
            return 0

        if pw_repeat == pw:
            
            User(name, new_user=True, password=pw, is_admin=is_admin)
            print_message(CREATE_USER)
            print_warning('Створено нового користувача', 2)

            for i in range(4, 0, -1):
                print_message(CREATE_USER)
                print(f'Ви повернетесь до головного меню через {i} с.')
                sleep(1)
            break
        else:
            print_message(CREATE_USER)
            print_warning('паролі не співпадають :(', 2)


def start():
    while True:
        print_message(HELLO)
        print('0 Увійти в систему')
        print("1 Створити нового користувача")

        user_input = input()
        if user_input == '0':
            data = login()
            if data:
                if data[2] == 'True':
                    admin_interface(data[0], data[1])
                else:
                    user_interface(data[0], data[1])
               
        elif user_input == '1':
            create_user()
                    

start()
