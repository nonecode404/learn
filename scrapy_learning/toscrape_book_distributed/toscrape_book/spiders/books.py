import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisSpider
from ..items import BookItem

"""
$ scp -r toscrape_book_distributed liushuo@116.29.35.201:～/scrapy_book
$ scp -r toscrape_book_distributed liushuo@123.59.45.155:～/scrapy_book
116.29.35.201:6379> lpush books:start_urls 'http://books.toscrape.com/'
(integer) 1
"""

class BooksSpider(RedisSpider.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    #start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        """书籍列表页面函数"""
        # 提取每本书的链接
        le = LinkExtractor(restrict_css='article.product_pod h3')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_book)

        #提取下一页的链接
        le = LinkExtractor(restrict_css='ul.pager li.next')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_book(self, response):
        """书籍页面解析函数"""
        book = BookItem()
        sel = response.css("div.product_main")
        book['name'] = sel.xpath("./h1/text()").extract_first()
        book['price'] = sel.xpath("./p[@class='price_color']/text()").extract_first()
        book['review_rating'] = sel.css("p.star-rating::attr(class)").re_first('star-rating ([A-Za-z]+)')

        sel = response.css("table.table-striped")
        book['upc'] = sel.xpath("//tr[1]/td/text()").extract_first()
        book['review_num'] = sel.xpath('(.//tr)[last()]/td/text()').extract_first()
        book['stock'] = sel.xpath('(.//tr)[last()-1]/td/text()').re_first('\((\d+) available\)')

        yield book
