# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class BookItem(scrapy.Item):
    name = Field()
    price = Field()
    authors = Field(serializer=lambda x: '|'.join(x))


class ForeignBookItem(BookItem):
    translator = Field()