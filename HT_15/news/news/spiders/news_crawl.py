import scrapy

from bs4 import BeautifulSoup
from datetime import datetime, date


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
            tags = ['#' + tag.get() for tag in response.css('a.post-tag::text')]

            html = response.css('div.entry-content').get()
            soup = BeautifulSoup(html, 'html.parser')
            content = soup.text.strip().replace('\n', ' ')

            yield {
                'name': response.css('h1.post-title::text').get(),
                'content': content,
                'tags': ', '.join(tags),
                'link': response.css('div.heateor_sss_sharing_container::attr(heateor-sss-data-href)').get(),
            }

# run spider
# scrapy crawl news_crawl
