# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import requests

class WenkuBaiduPipeline:
    def process_item(self, item, spider):
        i=1
        for url in item['image_urls']:
            #response = requests.get(url)
            response = scrapy.Request(url)
            pageIndex_str = str(i)
            i = i+1
            with open("C:\\Users\\xh3033.ARCVIDEO\\PycharmProjects\\untitled\\scrapy_learning\\wenku_other\\wenku_other\\download_images\\%s.png"%pageIndex_str, "wb") as f:
                f.write(response.body)
                #f.write(response.content)
            f.close()

