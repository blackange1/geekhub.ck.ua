# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import XmlItemExporter
from pathlib import Path


class NewsPipeline:
    @staticmethod
    def open_spider(spider):
        with open(Path(__file__).parent.parent.joinpath('res').joinpath(spider.name_file), 'w', newline='', encoding='utf-8') as f:
            f.write('name;content;tags;link')
            f.write('\n')

    @staticmethod
    def process_item(item, spider):
        with open(Path(__file__).parent.parent.joinpath('res').joinpath(spider.name_file), 'a', newline='', encoding='utf-8') as f:
            name, content, tags, link = item['name'].replace(';', ''), item['content'].replace(';', ''), item['tags'], item['link']
            f.write(f'{name};{content};{tags};{link}\n')

        return item
