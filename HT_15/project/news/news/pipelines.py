# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class NewsPipeline:
    # def __init__(self):
    #     self.com = sqlite3.connect('mtiles.db')
    #     self.cur = self.con.cursor()
    #     self.create_table()
    #
    # def create_table(self):
    #     self.cur.execute("""
    #         CREATE TABLE IF NOT EXISTS products(
    #             sku REAL PRIMARY KEY,
    #             name TEXT,
    #             price REAL,
    #         )
    #     """)

    def process_item(self, item, spider):
        # self.cur.execute("""
        #     INSERT OR IGNORE INTO products
        # """)
        print('9' * 30)
        print(item)
        print('0' * 30)
        return item
