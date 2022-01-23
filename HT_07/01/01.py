import csv, pathlib, json, os
from time import sleep 


MAIN_PATH = pathlib.Path(__file__).parent.joinpath('db')
USERS_DB = MAIN_PATH.joinpath('users.data')
BALANCE_PATH = MAIN_PATH.joinpath('balance')
TRANSACTIONS_PATH = MAIN_PATH.joinpath('transactions')


class NameNotValid(Exception):
    def __str__(self):
        return 'User.name have /\:*?"<>|'


class User():

    def __init__(self, name, new_user=False, password=None):
        
        self.name = name
        
        if new_user:
            new_file = open(BALANCE_PATH.joinpath(f'{name}__balance.data'), 'w')
            new_file.write('0.0')
            new_file.close()

            new_file = open(TRANSACTIONS_PATH.joinpath(f'{name}__transactions.data'), 'w')
            new_file.close()
            
            new_file = open(USERS_DB, 'a')
            new_file.write(f'{name},{password}\n')
            new_file.close()

    @staticmethod
    def sum(a, b):
        return (int(a) * 100 + int(b) * 100) / 100

    @staticmethod
    def isfloat(s):
        return s.replace('.', '', 1).isdigit()

    def get_balance(self):
        try:
            with open(BALANCE_PATH.joinpath(f'{self.name}__balance.data')) as file:
                return float(file.read())
        except Exception as error:
            print(f'error: {error}')

    def replenish_balance(self, money):
        now_money = self.get_balance()
        print(now_money)
        with open(BALANCE_PATH.joinpath(f'{self.name}__balance.data'), 'w') as file:
            file.write(str(self.sum(now_money, money)))


    def add_transactions(self, op, money):
        try:
            with open(TRANSACTIONS_PATH.joinpath(f'{self.name}__transactions.data'), 'a') as file:
                to_json = {'operation': op, 'money': money}
                file.write(json.dumps(to_json))
                file.write('\n')
        except Exception as error:
            print(f'error: {error}')


HELLO = 'You are greeted by the best in the world GOOLD LAMP'
CREATE_USER = 'Creating new user GOLD LAMP | for get main menu write EXIT'
LOGIN = 'authorization in the system GOLD LAMP'


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def print_message(text, char='='):
    clear_console()
    print(char * len(text))
    print(text)
    print(char * len(text))


def print_warning(text, second=1):
    print(text)
    sleep(second)


def login():
    print_message(LOGIN)
    name = input("write username\n")

    data = None
    with open(USERS_DB) as file:
        reader = csv.DictReader(file)

        for row in reader:
            if  name == row['name']:
                data = (row['name'], row['password'])
                break
            
    if data == None:
        print_message(LOGIN)
        print(f"We didn't find username: {name} in sistem :(\n")
        sleep(2)
    
    else:
        for massage in ('', 'attempt2', 'attempt 3'):
            print_message(LOGIN)
            if input(f'write password {massage}\n') == data[1]:
                return data

        print_message(LOGIN)
        print('you used three attempts :(')
        sleep(2)
    
    return None


def user_interface(name, pw):
    user = User(name)
    USER_INTERFACE = f'{name.upper()}, welcome to the system GOLD LAMP'
    
    while True:
        print_message(USER_INTERFACE)
        print('1. view balance')
        print('2. add money my balance')
        print('3. get money')
        print('4. exit')
        get_op = input()
        # 1
        if get_op == '1':

            print_message(USER_INTERFACE)
            print(f'____ yoyr balance {user.get_balance()}')
            input('____ to exit, press ENTER\n')

        # 2
        elif get_op == '2':
            have_problem = True
            for _ in range(3):
                print_message(USER_INTERFACE)
                money = input('___ how much cash you want to withdraw?\n')
                if user.isfloat(money):
                    money = float(money)
                    user.replenish_balance(money)
                    user.add_transactions('add_money', money)

                    print_message(USER_INTERFACE)
                    print(f'____ You have replenished your balance {money}')
                    input('____ to exit, press ENTER ENTER\n')

                    have_problem = False
                    break
                else:
                    print_message(USER_INTERFACE)
                    print_warning('___ Error writes :(', 2)

            if have_problem:
                print_message(USER_INTERFACE)
                print_warning('___ You used three attempts  :(', 2)
        # 3
        elif get_op == '3':

            have_problem = True
            for _ in range(3):
                print_message(USER_INTERFACE)
                money = input('___ How much money do you want to withdraw?\n')
                if user.isfloat(money):
                    money = float(money)
                    now_money = user.get_balance()
                    if now_money < money:
                        print_message(USER_INTERFACE)
                        print_warning(f'___ You do not have enough funds. your balance {now_money}', 2)
                    else:
                        user.replenish_balance(-money)
                        user.add_transactions('withdraw_money', money)
                        print_message(USER_INTERFACE)
                        print_warning(f'___ You received {money}', 2)

                        have_problem = False
                        break
                else:
                    print_message(USER_INTERFACE)
                    print_warning('___ Error writes :(', 2)

            if have_problem:
                print_message(USER_INTERFACE)
                print_warning('___ You used three attempts  :(', 1)
        # 4
        elif get_op == '4':
            break
        else:
            print_warning('Unknown command :(', 2)


def create_user():
    name = None
    pw = None
    while True:
        print_message(CREATE_USER)
        name = input("write name new user\n")
        
        if name.upper() == 'EXIT':
            return None

        if name == '':
            print_message(CREATE_USER)
            print_warning('name cannot be empty', 2)
            continue

        for ch in '/\:*?"<>|':
            if ch in name:
                print_message(CREATE_USER)
                print_warning('name should not contain /\:*?"<>|', 2)
                continue
        break            
    
    while True:
        while True:
            print_message(CREATE_USER)
            pw = input("write password of new user\n")

            if pw.upper() == 'EXIT':
                return None

            if len(pw) < 4:
                print_message(CREATE_USER)
                print_warning('lenth password cannot be < 4', 2)
                continue
            
            break
                
        print_message(CREATE_USER)
        pw_repeat = input("repeat password\n")

        if pw_repeat.upper() == 'EXIT':
            return 0

        if pw_repeat == pw:
            
            User(name, new_user=True, password=pw)
            print_message(CREATE_USER)
            print_warning('created a new user', 2)

            for i in range(4, 0, -1):
                print_message(CREATE_USER)
                print(f'you will go to the main menu via {i} second.')
                sleep(1)
            break
        else:
            print_message(CREATE_USER)
            print_warning('passwords do not match :(', 2)


def start():
    while True:
        print_message(HELLO)
        print('0 log in')
        print("1 create new user")
        user_input = input()
        if user_input == '0':
            data = login()
            if data:
                user_interface(*data)
                
        elif user_input == '1':
            create_user()
                    

start()
