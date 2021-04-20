import json

import scrapy

from ..items import SoImageItem


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['image.so.com']

    # 注意%s的用法
    BASE_URL = 'https://image.so.com/zjl?ch=art&sn=%s'
    start_index = 0

    start_urls = [BASE_URL % 0]

    # 限制下载最大数量
    MAX_DOWNLOAR_NUM = 1000


    def parse(self, response):
        """解析出url并下载，在继续循环解析"""
        #使用json解析response
        infos = json.loads(response.body.decode('utf-8'))
        images = SoImageItem()
        images['image_urls'] = [info['qhimg_url'] for info in infos['list']]
        yield images

        # 如count 字段大于0，并且下载数量不足MAX_DOWNLOAD_NUM，继续获取下
        self.start_index += infos['count']
        if infos['count'] > 0 and self.start_index < self.MAX_DOWNLOAR_NUM:
            yield scrapy.Request(self.BASE_URL % self.start_index)
