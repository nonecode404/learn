import scrapy
import scrapy.settings.default_settings
from ..items import BookItem
from scrapy.linkextractors import LinkExtractor

class BookSpider(scrapy.Spider):
    name = "books"

    start_urls = ["http://books.toscrape.com/"]

    """
    def start_requests(self):
        yield scrapy.Request("http://books.toscrape.com/",callback=self.parse_book,headers={'User-Agent': 'Mozilla/5.0'},dont_filter=True)
   
    
    def parse_book(response):
        pass
    """

    def parse(self, response, **kwargs):
        for sel in response.css("article.product_pod"):
            book = BookItem()
            book["name"] = sel.xpath("./h3/a/@title").extract_first()
            book["price"] = sel.css("p.price_color::text").extract_first()
            yield book

            next_url = response.css("li.next a::attr(href)").extract_first()
            if next_url:
                next_url = response.urljoin(next_url)
                yield scrapy.Request(next_url, callback=self.parse)

            le = LinkExtractor(restrict_css='ul.pager li.next')
            links = le.extract_links(response)
            if links:
                next_url = links[0].url
                yield scrapy.Request(next_url, callback=self.parse)
