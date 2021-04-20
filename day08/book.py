import requests
from lxml import etree
import json
from bs4 import BeautifulSoup

class BookSpider(object):
    def __init__(self):
        self.base_url = "http://book.zongheng.com/store/c0/c0/b0/u0/p{0}/v9/s9/t0/u0/i1/ALL.html"
        self.headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
                        }
        self.data_list = []

    #1.构建所有url
    def get_url_list(self):
        url_list = []
        for i in range(1,11):
            url = self.base_url.format(i)
            url_list.append(url)
        return url_list

    #2.发送请求
    def send_request(self, url):
        data = requests.get(url, headers=self.headers).content.decode()
        print(url)
        return data

    #3。解析数据
    def parse_xpath_data(self, data):
        parse_data = etree.HTML(data)
        #1. 解析出所有的书
        book_list = parse_data.xpath('//div[@class="bookbox fl"] | //div[@class="bookbox fr"]')
        #2. 每本书的信息
        for book in book_list:
            book_dict = {}
            #1.书名
            book_dict["book_name"] = book.xpath('.//div[@class="bookname"]/a/text()')
            #2. 图片
            book_dict["book_img_url"] = book.xpath('div[@class="bookimg"]/a/img/@src')
            #3. 作者
            book_dict["book_author"] = book.xpath('.//div[@class="bookilnk"]/a[1]/text()')
            #4. 简介
            book_dict["book_summary"] = book.xpath('.//div[@class="bookintro"]/text()')

            self.data_list.append(book_dict)

    def parse_bs4_data(self, data):

        bs4_data = BeautifulSoup(data, 'lxml')
        #1. 取出所有的书
        book_list = bs4_data.select('.bookbox')
        print(len(book_list))

        #2. 解析每本书的信息
        for book in book_list:
            book_dict = {}
            # 1.书名
            book_dict["book_name"] = book.select_one('.bookname').get_text()
            # 2. 图片
            book_dict["book_img_url"] = book.select_one('.bookimg img').get("src")
            # 3. 作者
            book_dict["book_author"] = book.select_one('.bookilnk a').get_text()
            # 4. 简介
            book_dict["book_summary"] = book.select_one('.bookintro').get_text()

            self.data_list.append(book_dict)


    #4.保存数据
    def save_data(self):
        json.dump(self.data_list, open("book.json", "w"))

    #5.统筹调用
    def start(self):
        url_list = self.get_url_list()
        for url in url_list:
            data = self.send_request(url)
            # self.parse_xpath_data(data)
            self.parse_bs4_data(data)
        self.save_data()

BookSpider().start()