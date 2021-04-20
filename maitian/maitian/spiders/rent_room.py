import scrapy
from maitian.items import MaitianItem

class MaitinSpider(scrapy.Spider):
    name = "zufang"
    start_urls = ["http://bj.maitian.cn/esfall/PG1"]
    def parse(self, response):
        for zufang_item in response.xpath('//div[@class="list_title"]'):
            yield {
                'title': zufang_item.xpath('./h1/a/text()]').extract_first().strip(),
                'price': zufang_item.xpath('./div[class="the_price"]/ol/strong/span]').extract_first().strip(),
                'area': zufang_item.xpath('.p/span/text()]').extract_first().replarc('m²','').strip(),
                'district': zufang_item.xpath('./p//text()]').re(r'昌平|朝阳|东城|大兴|房山|丰台')[0]
            }

        next_page_url = response.xpath('//div[@id="paging"]/a[@class="down_page"]/@href').extract_first()

        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))