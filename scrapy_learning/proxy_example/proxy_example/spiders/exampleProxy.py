import json
import time

import scrapy


class ExampleproxySpider(scrapy.Spider):
    name = 'exampleProxy'
    allowed_domains = ['www.kuaidaili.com']

    def start_requests(self):
        for i in range(1,3):
            time.sleep(5)
            yield scrapy.Request('http://www.kuaidaili.com/free/inha/%s/'%i)

    def parse(self, response):
        for sel in  response.css("table.table tbody tr"):
            # 提取代理的IP、port、scheme(http or https)
            ip = sel.css('td:nth-child(1)::text').extract_first()
            port = sel.css('td:nth-child(2)::text').extract_first()
            scheme = sel.css('td:nth-child(4)::text').extract_first()
            # 使用爬取到的代理再次发送请求到http(s)://httpbin.org/ip，验证代理是否可用
            url = '%s://httpbin.org/ip' % scheme
            # list > table > tbody > tr:nth-child(1) > td:nth-child(1)
            proxy = '%s://%s:%s' % (scheme, ip, port)
            print(proxy)
            meta = {
                'proxy': proxy,
                'dont_retry': True,
                'download_timeout': 10,
                # 以下两个字段是传递给check_available 方法的信息，方便检测
                '_proxy_scheme': scheme,
                '_proxy_ip': ip,
            }
            yield scrapy.Request(url, callback=self.check_available,
                        meta=meta, dont_filter=True)

    def check_available(self, response):
        proxy_ip = response.meta['_proxy_ip']
        # 判断代理是否具有隐藏IP 功能
        print(json.loads(response.text))
        if proxy_ip == json.loads(response.text)['origin']:
            yield {
                'proxy_scheme': response.meta['_proxy_scheme'],
                'proxy': response.meta['proxy'],
            }
