import json

import scrapy
import re

from ..items import WenkuBaiduItem


class WenkuSpider(scrapy.Spider):
    name = 'wenku'
    allowed_domains = ['wenku.baidu.com']
    #start_urls = ['https://wenku.baidu.com/view/f4ad0f78ee06eff9aef807bf.html']

    def start_requests(self):
        yield scrapy.Request('https://wenku.baidu.com/view/f06f412805087632301212bb.html',
                             callback=self.parse,
                             headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'},
                                      dont_filter=True)

    def parse(self, response):
        #提取图片链接
        #pattern = re.compile("WkInfo.htmlUrls = '(.*)'")
        #pattern = re.compile('"htmlUrls":"\{\"ttf\":\[],\"json\":')
        pattern = re.compile('"htmlUrls":(.*)')
        url_str = pattern.findall(response.text)[0].replace("\\", "").replace("x22", "\"")
        url_json = json.loads(url_str)
        wenku = WenkuBaiduItem()
        url = []
        index = []
        for single in url_json['png']:
            url.append(single['pageLoadUrl'])
            index.append(single['pageIndex'])
        wenku['image_urls'] = url
        # wenku['index'] = index
        yield wenku



