import scrapy
from scrapy.linkextractors import LinkExtractor

from ..items import MatplotlibExamplesItem
import scrapy.pipelines.files

class ExamplesSpider(scrapy.Spider):
    name = 'examples'
    allowed_domains = ['matplotlib.org']
    start_urls = ['https://matplotlib.org/2.0.2/examples/index.html']

    def parse(self, response):
        le = LinkExtractor(restrict_css='div.toctree-wrapper.compound li.toctree-l2')
        print(len(le.extract_links(response)))
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_example)

    def parse_example(self, response):
        href = response.xpath("//a[@class='reference external']/@href").extract_first()
        url = response.urljoin(href)
        example = MatplotlibExamplesItem()
        example['file_urls'] = [url]

        yield example

