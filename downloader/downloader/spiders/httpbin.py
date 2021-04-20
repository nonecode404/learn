import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.com']
    start_urls = ['http://httpbin.com/get']

    def parse(self, response):
        print(response.text)
        print(response.status)
