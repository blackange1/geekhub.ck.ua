"""
3. На основі попередньої функції створити наступний кусок кода:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
"""
from string import ascii_uppercase


def validation(name, password):
    set_password = set(password)
    if not(3 < len(name) < 50 and 3 < len(password)):
        raise Exception("You have a problem. 3 < name < 50 and 3 < password")
    if not(len(set_password & set('0123456789'))):
        raise Exception("You have a problem. Password not have number")
    if not(len(set_password & set(ascii_uppercase))):
        raise Exception("You have a problem. Password not have caps lock char")
    return True


data = [
   ('asdasdasdasd', 'asBa5wdawdw'),
   ('asdasdasdasd', 'asBawdawdw'),
   ('asdasdasdasd', 'asba5wdawdw'),
   ('asdasdasdasd', 'a'),
]


def print_status(name, password, error='OK'):
   print(f'Name: {name}')
   print(f'Password: {pw}')
   print(f'Status: {error})')
   print('-' * 5)


for name, pw in data:
   try:
      if validation(name, pw):
         print_status(name, pw)
   except Exception as error:
      print_status(name, pw, error)