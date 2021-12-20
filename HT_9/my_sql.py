import pathlib
import sqlite3 as sq


USERS_DB = pathlib.Path(__file__).parent.joinpath('db').joinpath('users.db')
NOMINAL = (1000, 500, 200, 100, 50, 20, 10)


def execute_sql(sql):
    try:
        with sq.connect(USERS_DB) as con:
            cur = con.cursor()
            cur.execute(sql)
            return cur
    except Exception as error:
        print(f'error: {error}')
    

def create_db(restart=False): 
    with sq.connect(USERS_DB) as con:
        cur = con.cursor() #Cursor

        if restart:
            cur.execute("DROP TABLE IF EXISTS users") # delete
            cur.execute("DROP TABLE IF EXISTS transactions") # delete
            cur.execute("DROP TABLE IF EXISTS money") # delete
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                password TEXT NOT NULL,
                is_admin INTEGER NOT NULL DEFAULT 0,
                balance REAL
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                transactions_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                operation TEXT NOT NULL,
                money REAL
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS money (
                money_id INTEGER PRIMARY KEY AUTOINCREMENT,
                nominal TEXT NOT NULL,
                count INTEGER
            )
        """)

        if len(cur.execute("SELECT nominal, count FROM money").fetchall()) == 0:
            for n in NOMINAL:
                cur.execute("INSERT INTO money (nominal, count) VALUES('{}', 0)".format(n))
