import scrapy
from scrapy import FormRequest


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['quotes.toscrape.com']
    # start_urls = ['http://quotes.toscrape.com/login']
    login_url = 'http://quotes.toscrape.com/login'

    # def parse(self, response):
    #     sel = response.xpath('//div//div[@class="row"]')
    #     username = sel.xpath('//input[@type="username"]/@name').extract_first()
    #     password = sel.xpath('//input[@type="password"]/@name').extract_first()
    #
    #     yield dict(zip(username, password))

    def start_requests(self):
        yield scrapy.Request(self.login_url, callback=self.login)

    def login(self, response):

        form_data = {
            'username': 'xh3033',
            'pwd': 'xh3033'
        }
        yield scrapy.FormRequest.from_response(response, formdata=form_data, callback=self.parse_login)

    def parse_login(self, response):
        if 'Quotes to Scrape' in response.text:
            print("Success!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            yield from super().start_requests()  # Python 3语法

        else:
            print("Failed!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
