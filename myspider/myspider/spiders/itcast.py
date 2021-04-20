import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        li_list = response.xpath("//div[@class='tea_con']//li")
        for li in li_list:
            item = {}
            item["name"] = li.xpath(".//h3/text()").extract_first()
            item["professor"] = li.xpath(".//h4/text()").extract_first()
            yield item #减少内存占用