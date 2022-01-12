from lib.database import execute_sql, get_info_money_db
import lib.calculate as calc


class Person(object):
    def __init__(self, name: str) -> None:
        self.name = name

        sql = "SELECT user_id FROM users WHERE name=='{}'".format(name)
        self.id_user = execute_sql(sql).fetchone()[0]

    def change_password(self):
        pass


class User(Person):
    def __init__(self, name) -> None:
        super().__init__(name)


    # operation with balance user
    def get_balance(self):
        sql = "SELECT balance FROM users WHERE name == '{}' LIMIT 1".format(self.name)
        return execute_sql(sql).fetchone()[0]


    def replenish_balance(self, money):
        now_money = self.get_balance()
       
        sql = "UPDATE users SET balance = {} WHERE name == '{}'".format(calc.sum(now_money, money) , self.name)
        execute_sql(sql)


    def get_money_bank(self, n):
        money = get_info_money_db()

        if money:
            res = None
            value = [money[key] for key in sorted(money, key=lambda x: int(x), reverse=True)]
            res = calc.number_of_bills(n, value)
            if res:
                NOMINAL = (1000, 500, 200, 100, 50, 20, 10)
                index = 0
                for key in map(str, NOMINAL):
                    money[key] -= res[index]
                    index += 1
            else:
                return None
            if money:
                for key, v in money.items():
                    sql = "UPDATE money SET count = {} WHERE nominal == '{}'".format(v, key)
                    execute_sql(sql)
                return res


    # operation with balance user
    def add_transactions(self, op, money):
        sql = "INSERT INTO transactions (user_id, operation, money) VALUES('{}', '{}', '{}')".format(self.id_user, op, money)
        execute_sql(sql)


    def get_transactions(self):
        sql = "SELECT operation, money FROM transactions WHERE user_id == '{}'".format(self.id_user)
        res = execute_sql(sql)
        return res.fetchall()


class Incasator(Person):
    def __init__(self, name) -> None:
        super().__init__(name)


    def add_money_db(self, count_bills):
        money = get_info_money_db()
        
        i = 0
        for key in sorted(money, key=lambda x: int(x), reverse=True):
            money[key] += count_bills[i]
            i += 1

        for key, v in money.items():
            sql = "UPDATE money SET count = {} WHERE nominal == '{}'".format(v, key)
            execute_sql(sql)
