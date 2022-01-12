from datetime import datetime, date, timedelta
from time import sleep

from lib.person import User, Incasator
from lib.login import Login
from lib.сurrency import Currency

import lib.calculate as calc
from lib.database import execute_sql, create_db, get_info_money_db
from lib.print import print_message, print_warning 


from lib.print import print_warning, print_message
import lib.calculate as calc

from lib._config import ADMIN, HELLO, CREATE_USER, NOMINAL, EXIT, LOGIN


class Interface(object):
    def __init__(self) -> None:
        self.name = ''


    def login(self) -> tuple:
        print_message(LOGIN)
        self.name = input("Введіть ім'я користувача | username\n")

        data = Login.is_login(self.name)

        if data == None:
            print_message(LOGIN)
            print(f"Ми не знайшли ім'я {self.name} в системі :(\n")
            sleep(2)

        else:
            for massage in ('', 'спроба 2', 'спроба 3'):
                print_message(LOGIN)
                if input(f'введіть пароль {massage}\n') == data[1]:
                    return data

            print_message(LOGIN)
            print('ви використали три спроби :(')
            sleep(2)

        return None


    def user_interface(self):
        user = User(self.name)
        USER_INTERFACE = f'{self.name.upper()}, вітаємо в системі GOLD LAMP'
        
        while True:
            print_message(USER_INTERFACE)
            print('1. Баланс')
            print('2. Поповнити рахунок')
            print('3. Зняти готівку')
            print('4. Показати всі транзакції')
            print('5. Курс валют на сьогодні')
            print('6. Валютний архів')
            print('7. Конвертер валют')
            print('8. Вихід')
            get_op = input()
            # 1
            if get_op == '1':

                print_message(USER_INTERFACE)
                print(f'____ Ваш баланс {user.get_balance()}')
                input(EXIT)
            # 2
            elif get_op == '2':
                have_problem = True
                for _ in range(3):
                    print_message(USER_INTERFACE)
                    money = input('___ введіть суму яку слід покласти на рахунок?\n')
                    if calc.isfloat(money):
                        money = float(money)
                        user.replenish_balance(money)
                        user.add_transactions('add_money', money)

                        print_message(USER_INTERFACE)
                        print(f'____ Ви поповнили рахунок на {money}')
                        input(EXIT)

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
                    if calc.isfloat(money):
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

                                print('На даний момент в банкомата не має таких купюр :(')
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
                transactions = user.get_transactions()
                print_message(USER_INTERFACE)
                for op, m in transactions:
                    print(f'{op} ---> {m}')
                input(EXIT)            
            # 5
            elif get_op == '5':
                print_message(USER_INTERFACE)
                tmp = 14
                print(f'Курси валют у відділеннях')
                print()
                print(f"---     {'купівля'.ljust(tmp)}подаж")

                for d in Currency.get_rates():
                    print(f"{d['ccy']}     {d['buy'].ljust(tmp)}{d['sale']}")

                print()
                input(EXIT)
            # 6
            elif get_op == '6':
                            
                currency = None
                flag = True

                while True:
                    print_message(USER_INTERFACE)
                    print('USD - долар США')
                    print('EUR - євро')
                    print('RUB - російський рубль')
                    print('CHF - швейцарський франк')
                    print('GBP - британський фунт')
                    print('PLZ - польський злотий')
                    print('SEK - шведська крона')
                    print('CAD - канадський долар')
                    print()

                    currency = input('введіть валюту із запропонованих варіантів | Для виходу введіть EXIT\n').upper()

                    if currency == 'EXIT':
                        flag = False
                        break

                    if currency in ('USD', 'EUR', 'RUB', 'CHF', 'GBP', 'PLZ', 'SEK', 'CAD'):
                        break
                    else:
                        print_warning('Ви невірно ввели  назву валюту', 2)

                date_now = datetime.now() 
                date_user = None

                if flag:
                    while True:
                        try:
                            print_message(USER_INTERFACE)
                            user_input = input('Введіть початкову дату | Зразок: 2014 12 1\n')
                            year, month, day = list(map(int, user_input.split()))
                            date_user = date(year, month, day)
                            break
                        except Exception as r:
                            print_warning('Зверніть увагу на зразок: 2014 12 1', 2)


                    if date_user.toordinal() > date_now.toordinal():
                        print_warning('Нажаль ми не знаємо майбутнього :(', 2)

                    elif date_user.toordinal() < date(2014, 12, 1).toordinal():
                        print_warning('На той час не існувало таких технологій :(. Почніть з 2014 12 1', 2)
                    else:
                        year, month, day = date_user.year, date_user.month, date_user.day
                        r = Currency.get_rates_on_date(day, month, year)
                        
                        res = None
                        for d in r['exchangeRate']:
                            if d.get('currency') == currency:
                                res = d['saleRateNB']
                                break
                        
                        print(f"Currency: {currency}")
                        print()

                        print(f"Date: {str(date_user).replace('-', '.')}")
                        if res != None:
                            print(f'NBU:  {res}   ------')
                            print()
                        else:
                            res = 0

                        old_res = res
                        delta = timedelta(days=1)

                        for _ in range(date_now.toordinal() - date_user.toordinal()):
                        
                            date_user = date_user + delta

                            year, month, day = date_user.year, date_user.month, date_user.day
                            r = Currency.get_rates_on_date(day, month, year)
                            
                            res = None
                            for d in r['exchangeRate']:
                                if d.get('currency') == currency:
                                    res = d['saleRateNB']
                                    break
                            print(f"Date: {str(date_user).replace('-', '.')}")
                            
                            if res != None:
                                print(f'NBU:  {res}   {round(old_res - res, 4)}')
                            else:
                                res = 0

                            old_res = res
                            print()

                            sleep(.5)
                        
                        input(EXIT)
            # 7
            elif get_op == '7':
                flag = True
                currency = 'USD'

                while flag:
                    print_message(USER_INTERFACE)
                    print('USD - долар США')
                    print('EUR - євро')
                    print('RUB - російський рубль')
                    print('CHF - швейцарський франк')
                    print('GBP - британський фунт')
                    print('PLZ - польський злотий')
                    print('SEK - шведська крона')
                    print('CAD - канадський долар')
                    print()

                    currency = input('Яку валюту будете конвертувати | Для виходу введіть EXIT\n').upper()

                    if currency == 'EXIT':
                        flag = False
                        break

                    if currency in ('USD', 'EUR', 'RUB', 'CHF', 'GBP', 'PLZ', 'SEK', 'XAU', 'CAD'):
                        break
                    else:
                        print_warning('Ви невірно ввели  назву валюту', 2)

                money = 0.0
                try:
                    while flag:
                        print_message(USER_INTERFACE)
                        money = input(f'Скільки {currency} будете конвертувати | Для виходу введіть EXIT\n')

                        if money.upper() == 'EXIT':
                            flag = False
                            break
                        money = float(money)

                        if money < 0:
                            print_warning("Валюьа не повинна бути від'ємною", 2)
                        else:
                            break
                except Exception:
                    print_warning('Некоректне введення даних', 2)
                    flag = False

                new_currency = 'USE'

                while flag:
                    print_message(USER_INTERFACE)
                    print('USD - долар США')
                    print('EUR - євро')
                    print('RUB - російський рубль')
                    print('CHF - швейцарський франк')
                    print('GBP - британський фунт')
                    print('PLZ - польський злотий')
                    print('SEK - шведська крона')
                    print('CAD - канадський долар')
                    print()

                    new_currency = input('У яку валюту будете конвертувати | Для виходу введіть EXIT\n').upper()

                    if new_currency == 'EXIT':
                        flag = False
                        break

                    if new_currency in ('USD', 'EUR', 'RUB', 'CHF', 'GBP', 'PLZ', 'SEK', 'CAD'):
                        break
                    else:
                        print_warning('Ви невірно ввели  назву валюту', 2)

                if flag:
                    date_now = datetime.now() 
                    
                    year, month, day = date_now.year, date_now.month, date_now.day
                    r = Currency.get_rates_on_date(day - 1, month, year)
                    res = None
                    new_res = None
                    for d in r['exchangeRate']:
                        if d.get('currency') == currency:
                            res = d['saleRateNB']
                        elif d.get('currency') == new_currency:
                            new_res = d['saleRateNB']
                        # elif not (None in (res, new_res)):
                        #     break
                    
                    if currency == new_currency:
                        new_res = res

                    try:
                        print(f"{money} {currency} == {round(money * res / new_res, 4)} {new_currency}")
                    except Exception as e:
                        print(e)
                    input(EXIT)
            # 8
            elif get_op == '8':
                break
            else:
                print_warning('Невідома команда :(', 2)

    
    def admin_interface(self) -> None:
        admin = Incasator(self.name)
        while True:

            print_message(ADMIN)
            print('0 - Переглянути вміст касети')
            print('1 - Поповнит банкомат')
            print('2 - Вихід')
            input_admin = input()

            if input_admin == '0':
                print_message(ADMIN)
                res = get_info_money_db()

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


    @staticmethod
    def create_user() -> None:
        name = None
        pw = None
        is_admin = None

        while True:
            print_message(CREATE_USER)
            print("Ви бажаєте створити:")
            print("0 - звичайного користувача")
            print("1 - адміністратора")
            input_user = input()
        
            if input_user == '0':
                is_admin = False
                break
            elif input_user == '1':
                is_admin = True
                break
            elif input_user.upper() == 'EXIT':
                return None
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
            
            sql = "SELECT * FROM users WHERE name=='{}'".format(name)
            res = execute_sql(sql).fetchone()
            if res != None:
                print_message(CREATE_USER)
                print_warning("Це ім'я вже зайняте :(", 2)
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
                return None

            if pw_repeat == pw:
                
                Login.create_person(name, pw, is_admin)
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


    @staticmethod
    def start() -> None:

        create_db(restart=False)
        interface = Interface()
        
        while True:
            print_message(HELLO)
            print('0 Увійти в систему')
            print("1 Створити нового користувача")
            print("2 Вихід")

            user_input = input()
            if user_input == '0':
                data = interface.login()
                print(data)
                if data:
                    interface.name = data[0]
                    if data[2]:
                        interface.admin_interface()
                    else:
                        interface.user_interface()
                
            elif user_input == '1':
                interface.create_user()

            elif user_input == '2':
                break
