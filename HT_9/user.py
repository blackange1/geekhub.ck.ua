import pathlib, json, os
from time import sleep 
import sqlite3 as sq


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


MAIN_PATH = pathlib.Path(__file__).parent.joinpath('db')

USERS_DB = MAIN_PATH.joinpath('users.db')
MONEY_DB = MAIN_PATH.joinpath('money.json')
BALANCE_PATH = MAIN_PATH.joinpath('balance')
TRANSACTIONS_PATH = MAIN_PATH.joinpath('transactions')


def execute_sql(sql):
    try:
        with sq.connect(USERS_DB) as con:
            cur = con.cursor()
            cur.execute(sql)
            return cur
    except Exception as error:
        print(f'error: {error}')
    

class User():

    def __init__(self, name, new_user=False, password=None, is_admin=False):
        self.name = name
        self.is_admin = is_admin
        
        if new_user:
            new_file = open(TRANSACTIONS_PATH.joinpath(f'{name}__transactions.data'), 'w')
            new_file.close()
            
            sql = "INSERT INTO users (name, password, is_admin, balance) VALUES('{}', '{}', '{}', '{}')".format(name, password, int(is_admin), 0)
            execute_sql(sql)


    @staticmethod
    def sum(a, b):
        return (int(a) * 100 + int(b) * 100) / 100

    @staticmethod
    def isfloat(s):
        return s.replace('.', '', 1).isdigit()

    def get_balance(self):
        sql = "SELECT balance FROM users WHERE name == '{}'".format(self.name)
        return float(execute_sql(sql).fetchone()[0])
        

    def replenish_balance(self, money):
        now_money = self.get_balance()
       
        sql = "UPDATE users SET balance = {} WHERE name == '{}'".format(self.sum(now_money, money) , self.name)
        execute_sql(sql)


    def add_transactions(self, op, money):
        try:
            with open(TRANSACTIONS_PATH.joinpath(f'{self.name}__transactions.data'), 'a') as file:
                to_json = {'operation': op, 'money': money}
                file.write(json.dumps(to_json))
                file.write('\n')
        except Exception as error:
            print(f'error: {error}')

    @staticmethod
    def get_info_money_db():
        try:
            with open(MONEY_DB) as file:
                return json.load(file)
        except Exception as error:
            print(f'error: {error}')

    def add_money_db(self, count_bills):
        money = self.get_info_money_db()
        
        i = 0
        for key in sorted(money, key=lambda x: int(x), reverse=True):
            money[key] += count_bills[i]
            i += 1

        with open(MONEY_DB, 'w') as file:
            file.write(json.dumps(money))


    @staticmethod
    def get_info_money_db():
        money = None
        
        try:
            with open(MONEY_DB) as file:
                money = json.load(file)
        except Exception as error:
            print(f'error: {error}')

        return money

    def get_money_bank(self, n):
        money = self.get_info_money_db()

        if money:
            res = None
            value = [money[key] for key in sorted(money, key=lambda x: int(x), reverse=True)]
            res = self.__get(n, value)
            if res:
                NOMINAL = (1000, 500, 200, 100, 50, 20, 10)
                index = 0
                for key in map(str, NOMINAL):
                    money[key] -= res[index]
                    index += 1
            else:
                return None
            if money:
                with open(MONEY_DB, 'w') as file:
                    file.write(json.dumps(money))
                    return res

    @staticmethod
    def __get(n, args):
        if len(args) != 7:
            return None
        
        n1000, n500, n200, n100, n50, n20, n10 = args

        for k1000 in range(min(n // 1000, n1000), -1, -1):
            for k500 in range(min(n // 500, n500), -1, -1):
                for k200 in range(min(n // 200, n200), -1, -1):
                    for k100 in range(min(n // 100, n100), -1, -1):
                        for k50 in range(min(n // 50, n50), -1, -1):
                            for k20 in range(min(n // 20, n20), -1, -1):
                                for k10 in range(min(n // 10, n10), -1, -1):
                                    if 1000 * k1000 + 500 * k500 + 200 * k200 + 100 * k100 + 50 * k50 + 20 * k20 + 10 * k10 == n:
                                        return (k1000, k500, k200, k100, k50, k20, k10)
