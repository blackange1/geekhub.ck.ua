import scrapy

from bs4 import BeautifulSoup
from datetime import datetime, date


def format_time(date_of_create):
    def form_num(n):
        if len(n) == 1:
            return '0' + n
        return n

    months = {
        'Січня': 1,
        'Лютого': 2,
        'Березня': 3,
        'Квітня': 4,
        'Травня': 5,
        'Червня': 6,
        'Липня': 7,
        'Серпня': 8,
        'Вересня': 9,
        'Жовтня': 10,
        'Листопада': 11,
        'Грудня': 12,
    }
    full_date = date_of_create.split(',')
    if len(full_date) == 2:
        date_calendar, time = full_date
        date_calendar = date_calendar.split()
        if len(date_calendar) == 3:
            day, month, year = date_calendar
            if month in months:
                month = str(months[month])
                return f'{year} {form_num(month)} {form_num(day)}, {time}'

    return '-- -- --'


def valid_date() -> tuple:
    example = '2022 01 07 or 2022 01 or 2022'

    def is_future(year: int, mont=1, day=1) -> bool:
        now = datetime.now().date()
        if date(year, mont, day) <= now:
            return False
        return True

    while True:
        try:
            s = input(f'Введіть дату через пробіл | Приклад: {example}\n')
            d = tuple(map(int, s.split()))
            if not is_future(*d):
                print(200)
                return tuple(map(str, d))
            print('Ви ввели дату яка ще не настала')
        except Exception as error:
            print(error, f'Приклад: {example}')


class NewsCrawlSpider(scrapy.Spider):
    name = 'news_crawl'
    url = 'https://www.vikka.ua/'

    _date = valid_date()
    start_urls = [url + '/'.join(map(str, _date)) + '/']
    name_file = f"{'_'.join(_date)}.csv"

    if start_urls:
        def parse(self, response, **kwargs):
            for link in response.css('a.more-link-style::attr(href)'):
                yield response.follow(link, callback=self.parse_new)

            next_link = response.css('a.next::attr(href)').get()
            if next_link:
                yield response.follow(next_link, callback=self.parse)

        @staticmethod
        def parse_new(response):
            tags = ['#' + tag.get().replace(' ', '_') for tag in response.css('a.post-tag::text')]

            html = response.css('div.entry-content').get()
            soup = BeautifulSoup(html, 'html.parser')
            content = soup.text.strip().replace('\n', ' ')

            date_of_create = response.css('div.single-postinfo-wrap span::text').get()
            date_of_create = format_time(date_of_create)

            yield {
                'title': response.css('h1.post-title::text').get(),
                'content': content,
                'tags': ', '.join(tags),
                'link': response.css('div.heateor_sss_sharing_container::attr(heateor-sss-data-href)').get(),
                'date': date_of_create,
            }

# run spider
# scrapy crawl news_crawl
