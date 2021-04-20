import requests
from lxml import etree

class BtcSpider(object):
    def __init__(self):
        self.base_url = "https://news.baidu.com/"
        self.headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363"
    }

    #1.发请求
    def get_response(self, url):
        response = requests.get(url, headers=self.headers)
        data = response.content
        return data

    #2.解析数据
    def parse_data(self, data):
        #使用xpath
        #1.转类型
        x_data = etree.HTML(data)

        #2.路径解析
        title_list = x_data.xpath("//a[@target=\"_blank\"]/text()")
        url_list = x_data.xpath("//a[@target=\"_blank\"]/@href")
        list = x_data.xpath('// *[ @ id = \"pane-news\"]/div//a/text() | // *[ @ id = \"pane-news\"]/ul//a/text()')
        print(list)
        data_list = []
        # for index, title in enumerate(title_list):
        #     news_dict = {}
        #     print(index)
        #     print(title)
        #     print(len(title))
        #     news_dict['name'] = title
        #
        #     if len(title) <= 3:
        #
        #         news_dict['url'] = url_list[index]
        #
        #     data_list.append(news_dict)


    #3.保存数据
    def save_data(self, data):
        with open("Newnews.html", "wb")as f:
            f.write(data)
    #4.启动
    def run(self):
        url = self.base_url
        data = self.get_response(url)
        self.parse_data(data)
        self.save_data(data)

BtcSpider().run()
