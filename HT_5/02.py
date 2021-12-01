"""
2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
   - щось своє :)
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
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


# test 
print(validation('asdasdasdasd', 'asBa5wdawdw'))
validation('asdasdasdasd', 'asBawdawdw')
