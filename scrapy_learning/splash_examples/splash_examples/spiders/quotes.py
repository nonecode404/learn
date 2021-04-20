import scrapy
from scrapy_splash import SplashRequest
from scrapy.linkextractors import LinkExtractor

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    #allowed_domains = ['quotes.toscrape.com']
    #start_urls = ['http://quotes.toscrape.com/js/']
    allowed_domains = ['wenku.baidu.com']
    start_urls = ['https://wenku.baidu.com/view/521180a9b5daa58da0116c175f0e7cd1842518e8.html']


    def start_requests(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363"
        }
        for url in self.start_urls:
            yield SplashRequest(url, args={'images':0,'timeout': 3}, headers=headers)

    def parse(self, response):
        print(response.text)
        # for sel in response.css("div.quote"):
        #     quote = sel.xpath("./span[@class='text']/text()").extract_first()
        #     author = sel.xpath("./span/small[@class='author']/text()").extract_first()
        #     yield {"quote":quote, "author":author}

        # le = LinkExtractor(restrict_xpaths='//nav//li[@class="next"]/a')
        # for link in le.extract_links(response):
        #     print(link.url)
        #     yield SplashRequest(link.url, args={'images': 0, 'timeout': 3})

        # href = response.css('li.next > a::attr(href)').extract_first()
        # if href:
        #     url = response.urljoin(href)
        #     yield SplashRequest(url, args={'images': 0, 'timeout': 3})
