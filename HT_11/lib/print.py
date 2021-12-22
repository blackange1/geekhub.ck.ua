import os
from time import sleep 

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


def print_warning(text, second=2):
    print(text)
    sleep(second)