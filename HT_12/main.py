import requests
from bs4 import BeautifulSoup
from pathlib import Path
import sqlite3 as sq
from lib.print import print_message, print_warning

def parsing():
    print_message('парсинг почато')
    link = 'http://quotes.toscrape.com'

    # clear
    with open(Path(__file__).parent.joinpath('csv').joinpath('authors.csv'), 'w', encoding='utf-8') as file:
        file.write(';'.join([ "text", "author", "link", "born_date", "born_location", "description"]))
        file.write('\n')

    with sq.connect(Path(__file__).parent.joinpath('db').joinpath('author.db')) as con:
        cur = con.cursor() #Cursor

        cur.execute("DROP TABLE IF EXISTS authors") # delete
        cur.execute("""
            CREATE TABLE IF NOT EXISTS authors (
                author_id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                author TEXT NOT NULL,
                link TEXT NOT NULL,
                born_date TEXT,
                born_location TEXT,
                description TEXT
            )
        """)

    i = 1
    while True:
        html_doc = requests.get(f'{link}/page/{i}/')
        
        print(f"\npage № {i}")
        i += 1

        soup = BeautifulSoup(html_doc.text, 'html.parser')

        quote = soup.find_all('div', class_='quote')
        if not quote:
            print('не існує (:')
            input('натисніть ENTER для виходу в меню')
            break
        for index in range(len(quote)):
            data = {}

            text = quote[index].span.text
            author = quote[index].find_all('span')[1].small.text
            sub_link = quote[index].find_all('span')[1].a.get('href')

            about_autor = BeautifulSoup(requests.get(link + sub_link).text, 'html.parser').find("div", class_="author-details")

            born_date = about_autor.find(class_="author-born-date").text
            born_location = about_autor.find(class_="author-born-location").text
            description = about_autor.find(class_="author-description").text.replace('\n', '')

            data.update({
                "text": text,
                "author": author,
                "link": link + sub_link,
                "born_date": born_date,
                "born_location": born_location,
                "description": description
            })

            with open(Path(__file__).parent.joinpath('csv').joinpath('authors.csv'), 'a', encoding='utf-8') as file:
                file.write(';'.join([text.replace(';', ':'), author, link + sub_link, born_date, born_location, description]))
                file.write('\n')

            try:
                with sq.connect(Path(__file__).parent.joinpath('db').joinpath('author.db')) as con:
                    cur = con.cursor()

                    cur.execute("""
                        INSERT INTO authors (text, author, link, born_date, born_location, description)
                        VALUES(?, ?, ?, ?, ?, ?)
                    """, tuple(data.values()))
            except Exception as error:
                print(f'error: {error}')

            info = f"{data['author']}: {data['text']}"
            print(info)
            print('#' * len(info))


def show_db():
    print_message('для економії місця ми не виводитемемо description')
    with sq.connect(Path(__file__).parent.joinpath('db').joinpath('author.db')) as con:
        cur = con.cursor() #Cursor

        for data in cur.execute("SELECT * FROM authors").fetchall():
            print(*data[:-2], sep=' |\t')
    input('натисніть ENTER для виходу в меню')


def start():
    while True:
        print_message("парсінг даних")
        print('0 - вихід')
        print('1 - переглянути вміст бази даних')
        print('2 - переглянути вміст csv')
        print('3 - почати парсинг')
        input_user = input()

        if input_user == '0':
            break
        elif input_user == '1':
            show_db()
        elif input_user == '2':
            print_warning("даний файл знаходиться в папці csv. Перегляньте за допомогою відповідного редактора")
        elif input_user == '3':
            while True:
                print_message('попередження')
                print('данні в author.db та author.csv будуть перезаписані')
                print('0 - вихід')
                print('1 - продовжити')
                input_user = input()

                if input_user == '0':
                    break
                elif input_user == '1':
                    parsing()
                    break
                else:
                    print_warning('невірние введення :(')

        else:
            print_warning('невірние введення :(')


start()