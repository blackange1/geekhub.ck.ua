import requests

from django.db import models


class Askstories(models.Model):
    by = \
        models.CharField(max_length=30)
    descendants = \
        models.IntegerField()
    id_askstories = \
        models.IntegerField()
    kids = \
        models.TextField()
    score = \
        models.IntegerField()
    text = \
        models.TextField()
    time = \
        models.IntegerField()
    title = \
        models.CharField(max_length=80)
    type = \
        models.CharField(max_length=80)

    def __str__(self):
        return self.title


class Showstories(models.Model):
    by = \
        models.CharField(max_length=30)
    descendants = \
        models.IntegerField()
    id_showstories = \
        models.IntegerField()
    kids = \
        models.TextField()
    score = \
        models.IntegerField()
    text = \
        models.TextField()
    time = \
        models.IntegerField()
    title = \
        models.CharField(max_length=80)
    type = \
        models.CharField(max_length=80)
    url = \
        models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Newstories(models.Model):
    by = \
        models.CharField(max_length=30)
    descendants = \
        models.IntegerField()
    id_newstories = \
        models.IntegerField()
    kids = \
        models.TextField()
    score = \
        models.IntegerField()
    text = \
        models.TextField()
    time = \
        models.IntegerField()
    title = \
        models.CharField(max_length=80)
    type = \
        models.CharField(max_length=80)
    url = \
        models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Jobstories(models.Model):
    by = \
        models.CharField(max_length=30)
    id_jobstories = \
        models.IntegerField()
    score = \
        models.IntegerField()
    text = \
        models.TextField()
    time = \
        models.IntegerField()
    title = \
        models.CharField(max_length=80)
    type = \
        models.CharField(max_length=80)
    url = \
        models.CharField(max_length=150)

    def __str__(self):
        return self.title


class ErrorType(Exception):
    pass


class Parser(object):

    stories = {
        'askstories': Askstories,
        'showstories': Showstories,
        'newstories': Newstories,
        'jobstories': Jobstories,
    }

    __link = "https://hacker-news.firebaseio.com/v0/"

    def __init__(self, type_stories="newstories"):
        if type_stories in Parser.stories.keys():
            self.type_stories = type_stories
            self.__id = tuple(
                Parser.stories.get(type_stories).objects.all().values_list(
                    f'id_{type_stories}',
                    flat=True
                )
            )
        else:
            raise ErrorType()

    def write_db(self, sub_link: str) -> None:
        if sub_link in self.__id:
            print('Такий запис уже існує в database')
        else:
            link = f"{self.__link}item/{sub_link}.json"
            req = requests.get(link)
            print(link, 'status_code', req.status_code)
            if req.status_code == 200:
                req = req.json()
                if self.type_stories == 'newstories':
                    history = Newstories(
                        by=req.get('by', ''),
                        descendants=req.get('descendants', 0),
                        id_newstories=req.get('id', 0),
                        kids=req.get('kids', ''),
                        score=req.get('score', 0),
                        text=req.get('text', ''),
                        time=req.get('time', 0),
                        title=req.get('title', ''),
                        type=req.get('type', ''),
                        url=req.get('url', ''),
                    )
                    history.save()
                elif self.type_stories == 'askstories':
                    history = Askstories(
                        by=req.get('by', ''),
                        descendants=req.get('descendants', 0),
                        id_askstories=req.get('id', 0),
                        kids=req.get('kids', ''),
                        score=req.get('score', 0),
                        text=req.get('text', ''),
                        time=req.get('time', 0),
                        title=req.get('title', ''),
                        type=req.get('type', ''),
                    )
                    history.save()
                elif self.type_stories == 'showstories':
                    history = Showstories(
                        by=req.get('by', ''),
                        descendants=req.get('descendants', 0),
                        id_showstories=req.get('id', 0),
                        kids=req.get('kids', ''),
                        score=req.get('score', 0),
                        text=req.get('text', ''),
                        time=req.get('time', 0),
                        title=req.get('title', ''),
                        type=req.get('type', ''),
                        url=req.get('url', ''),
                    )
                    history.save()
                elif self.type_stories == 'jobstories':
                    history = Jobstories(
                        by=req.get('by', ''),
                        id_jobstories=req.get('id', 0),
                        score=req.get('score', 0),
                        text=req.get('text', ''),
                        time=req.get('time', 0),
                        title=req.get('title', ''),
                        type=req.get('type', ''),
                        url=req.get('url', ''),
                    )
                    history.save()
                print('додано в database')

    def run_parsing(self):
        req = requests.get(f"{self.__link}{self.type_stories}.json").json()
        for sub_link in req:
            self.write_db(sub_link)
        print("Stop parsing".upper())

    def __str__(self):
        return f"class Parser_{self.type_stories}"
