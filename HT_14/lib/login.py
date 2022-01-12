from lib.database import execute_sql


class Login(object):
    @staticmethod
    def is_login(name: str) -> tuple:
        # return None if data person not fined
        sql = "SELECT name, password, is_admin FROM users WHERE name == '{}'".format(name)
        return execute_sql(sql).fetchone()


    @staticmethod
    def create_person(name: str, password: str, is_admin: bool, balance=0) -> None:
        sql = "INSERT INTO users (name, password, is_admin, balance) VALUES('{}', '{}', '{}', '{}')".format(name, password, int(is_admin), balance)
        execute_sql(sql)

    