import scrapy

from bs4 import BeautifulSoup
from datetime import datetime, date


def valid_date(url) -> tuple:
    while True:
        try:
            s = input('Введіть дату через пробіл | Приклад: 2022 01 07\n')
            year, mont, day = map(int, s.split())
            d = date(year, mont, day)
            now = datetime.now().date()

            if d <= now:
                return [url + '/'.join(map(str, (year, mont, day))) + '/']
            print('Ви ввели дату яка ще не настала')
        except Exception as error:
            print(error, 'Приклад: 2022 01 07')

# scrapy crawl news_crawl
class NewsCrawlSpider(scrapy.Spider):
    name = 'news_crawl'
    url = 'https://www.vikka.ua/'
    start_urls = valid_date(url)
    print(start_urls)

    if start_urls:
        def parse(self, response, **kwargs):
            for link in response.css('a.more-link-style::attr(href)'):
                yield response.follow(link, callback=self.parse_new)

        @staticmethod
        def parse_new(response):
            tags = ['#' + tag.get() for tag in response.css('a.post-tag::text')]

            html = response.css('div.entry-content').get()
            soup = BeautifulSoup(html, 'html.parser')
            content = soup.text.strip().replace('\n', '')

            yield {
                'name': response.css('h1.post-title::text').get(),
                'content': content,
                'tags': ', '.join(tags),
            }

