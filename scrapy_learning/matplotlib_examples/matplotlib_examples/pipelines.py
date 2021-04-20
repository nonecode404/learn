# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from urllib.parse import urlparse
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
from os.path import basename, dirname, join

class myFilesPipeline(FilesPipeline):

    def file_path(self, request, response=None, info=None, *, item=None):
        """重写文件路径名方法"""
        path = urlparse(request.url).path
        print(dirname(path))
        return join(basename(dirname(path)), basename(path))

class MatplotlibExamplesPipeline:
    def process_item(self, item, spider):
        return item
