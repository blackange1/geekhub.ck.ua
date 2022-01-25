import requests
from csv import DictWriter
from pathlib import Path


path_csvfile = Path(__file__).parent.parent.joinpath('csv')


class ErrorType(Exception):
    pass


class Stories(object):

    __head_file = {
        "askstories": ['by', 'descendants', 'id', 'kids', 'score', 'text', 'time', 'title', 'type'],
        "showstories": ['by', 'descendants', 'id', 'kids', 'score', 'text', 'time', 'title', 'type', 'url'],
        "newstories": ['by', 'descendants', 'id', 'kids', 'score', 'text', 'time', 'title', 'type', 'url'],
        "jobstories": ['by', 'id', 'score', 'text', 'time', 'title', 'type', 'url']
    }

    __link = "https://hacker-news.firebaseio.com/v0/"

    def __init__(self, type_stories="newstories"):
        if type_stories in Stories.__head_file:
            self.type_stories = type_stories
            self.name_csv_file = f"{type_stories}.csv"
            self.__head_csv_file = Stories.__head_file[type_stories]
            self.create_csv_file()
        else:
            raise ErrorType()

    def create_csv_file(self):
        with open(path_csvfile.joinpath(self.name_csv_file), 'w', newline='', encoding='utf-8') as file:
            writer = DictWriter(file, fieldnames=self.__head_csv_file)
            writer.writeheader()

    def write_data_csv(self, sub_link: str):
        link = f"{self.__link}item/{sub_link}.json"
        req = requests.get(link)
        print(link, 'status_code', req.status_code)
        req = req.json()
        with open(path_csvfile.joinpath(self.name_csv_file), 'a', newline='', encoding='utf-8') as file:
            writer = DictWriter(file, fieldnames=self.__head_csv_file)
            writer.writerow(req)

    def run_parsing(self):
        req = requests.get(f"{self.__link}{self.type_stories}.json").json()
        for sub_link in req:
            self.write_data_csv(sub_link)
        print("Stop parsing".upper())

    def __str__(self):
        return f"class Stories_{self.type_stories}"
