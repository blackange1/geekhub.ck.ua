import requests


class Currency(object):
    link = 'https://api.privatbank.ua/p24api/'


    @classmethod
    def get_rates(cls):
        r = requests.get(f'{cls.link}pubinfo?json&exchange&coursid=5')
        return r.json()


    @classmethod
    def get_rates_on_date(cls, day: int, month: int, year: int):
        r = requests.get(f'{cls.link}/exchange_rates?json&date={day}.{month}.{year}').json()
        return r
