from lib.print import print_message, print_warning
import requests
from random import randint


EXIT = 'Для виходу натисніть ENTER\n'
ERROR = 'невірний ввід даних'
link = 'https://jsonplaceholder.typicode.com'
r = requests.get(f'{link}/users')

# get_users
users = {}
max_len_name = 0

for d in r.json():
    users[d['id']] = {'name': d['name'], 'username': d['username']}
    tmp = len(d['name'])

    if max_len_name < tmp:
        max_len_name = tmp
print()

id_user = None
while True:
    print_message(f'id      {"name".ljust(max_len_name)} | username', char='/')
    for i in users:
        print(f"{i}\t{users[i]['name'].ljust(max_len_name)} | {users[i]['username']}")
    print()

    input_user = input("Введіть ID користувача | для виходу введіть 0\n")
    
    if input_user == '0':
        break

    if input_user.isdigit() and int(input_user) in users.keys():
        id_user = int(input_user)
        while True:
            user_info = f"{id_user}      {users[id_user]['name'].ljust(max_len_name)} | {users[id_user]['username']}"
            print_message(user_info)
            print("1. Повна інформація про користувача")
            print("2. Пости:")
            print("3. ТУДУшка:")
            print("4. рандомний URL картинки:")
            print("0. Вихід:")
            input_user = input()

            if input_user == '0':
                break

            if input_user == '1':
                print_message(user_info)
                
                r = requests.get(f'{link}/users/{id_user}').json()
                print(f"email: {r['email']}")
                print("адреса")
                print(f"--- вулиця: {r['address']['street']}")
                print(f"--- suite: {r['address']['suite']}")
                print(f"--- код: {r['address']['zipcode']}")
                print("--- геолокація:")
                print(f"------ lat: {r['address']['geo']['lat']}")
                print(f"------ lat: {r['address']['geo']['lng']}")
                
                print(f"телефон: {r['phone']}")
                print(f"сайт: {r['website']}")
                print("компанія")
                print(f"--- назва: {r['company']['name']}")
                print(f"--- catchPhrase: {r['company']['catchPhrase']}")
                print(f"--- bs: {r['company']['bs']}")
                input(EXIT)
    
            elif input_user == '2':
                user_posts = {}
                r = requests.get(f'{link}/posts?userId={id_user}').json()
                for d in r:
                    user_posts[d['id']] = {'title': d['title'], 'body': d['body']}
                while True:
                    print_message(user_info + ' - Пости')

                    print('id\ttitle')
                    for i in user_posts:
                        print(f"{i}\t{user_posts[i]['title']}")

                    input_user = input("Введіть Id посту | для виходу 0\n")

                    if input_user == '0':
                        break

                    if input_user.isdigit() and int(input_user) in user_posts.keys():
                        id_post = int(input_user)
                        print_message(user_info + ' - пост id = ' + str(id_post))
                        print('--- Заголовок')
                        print(user_posts[id_post]['title'])
                        print()

                        print('--- Текстовка')
                        print(user_posts[id_post]['body'])
                        print()

                        r = requests.get(f'{link}/posts/{id_post}/comments').json()
                        count = 0
                        id_comments = []
                        for d in r:
                            id_comments.append(d['id'])
                            count += 1

                        print(f'--- Кількість коментарів = {count}\n')
                        print('--- Id коментарів =', ', '.join(map(str, id_comments)))
                        print()

                        input(EXIT)
                    
                    else:
                        print_warning(ERROR)

            elif input_user == '3':
                while True:
                    print_message(user_info + ' TODO')
                    print('0. вихід')
                    print('1. список невиконаних задач')
                    print('2. список виконаних задач')

                    input_user = input()
                    
                    r = requests.get(f'{link}/todos?userId={id_user}').json()
                    todo = {'completed': [], 'not_completed': []}
                    for d in r:
                        if d['completed']:
                            todo['completed'].append({'id': d['id'], 'title': d['title']})
                        else:
                            todo['not_completed'].append({'id': d['id'], 'title': d['title']})
                    
                    if input_user == '0':
                        break
                    elif input_user == '1':
                        print_message(user_info + ' TODO completed')

                        for d in todo['completed']:
                            print(f"{d['id']}\t{d['title']}")
                        
                        input(EXIT)
                    elif input_user == '2':
                        print_message(user_info + ' TODO not completed')

                        for d in todo['not_completed']:
                            print(f"{d['id']}\t{d['title']}")
                        
                        input(EXIT)
                    else:
                        print_warning(ERROR)

            elif input_user == '4':
                print_message('URL рандомної картинки')
                r = requests.get(f'{link}/photos').json()
                d = r[randint(0, len(r) - 1)]
                print()
                print(d['url'])
                print()
                input(EXIT)
    else:
        print_warning(ERROR)

