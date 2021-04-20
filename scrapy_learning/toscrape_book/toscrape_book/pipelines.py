# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter
from scrapy import Item
from scrapy.exceptions import DropItem


class BookPipeline:

    review_rating_map = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5,
    }

    def process_item(self, item, spider):
        rating = item['review_rating']
        if rating:
            item['review_rating'] = self.review_rating_map[rating]

        return item


class DuplicatesPipeline(object):
    def __init__(self):
        self.book_set = set()

    def process_item(self, item, spider):
        name = item['name']
        if name in self.book_set:
            raise DropItem("Duplicate book found: %s" % item)

        self.book_set.add(name)
        return item

class MongoDBPipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        cls.DB_URI = crawler.settings.get('MONGO_DB_URI',
                                          'mongodb://localhost:27017/')
        cls.DB_NAME = crawler.settings.get('MONGO_DB_NAME', 'scrapy_data')
        return cls()


    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.DB_URI)
        self.db  = self.client[self.DB_NAME]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        collection = self.db[spider.name]
        post = dict(item) if  isinstance(item, Item) else item
        collection.insert_one(post)
        return item