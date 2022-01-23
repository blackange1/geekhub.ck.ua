# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import XmlItemExporter
from pathlib import Path
import sqlite3


class NewsPipeline:
    path = Path(__file__).parent.parent.joinpath('db').joinpath('news.db')

    def __init__(self):
        self.conn = sqlite3.connect(NewsPipeline.path)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS news(
                id_new INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                tags TEXT,
                link TEXT NOT NULL,
                data TEXT NOT NULL
            );
        """)

    def insert_table(self, title, content, tags, link, data):
        if (link,) in self.conn.execute('SELECT link FROM news').fetchall():
            return None

        row = [title, content, tags, link, data]
        query = """
            INSERT INTO news (title, content, tags, link, data)
            VALUES(?, ?, ?, ?, ?)
        """
        self.conn.execute(query, row)
        self.conn.commit()

    def close_spider(self):
        self.conn.close()

    def process_item(self, item, spider):
        title = item['title']
        content = item['content']
        tags = item['tags']
        link = item['link']
        date = item['date']

        self.insert_table(title, content, tags, link, date)

        return item
