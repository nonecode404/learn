import requests

class RequestSpider(object):
    def __init__(self):
        url = "http://www.baidu.com"
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        }
        self.response = requests.get(url, headers=headers)

    def run(self):

        data = self.response.content

        #获取请求头
        request_headers = self.response.request.headers
        print(request_headers)
        #获取响应头
        response_headers = self.response.headers
        print(response_headers)
        #响应状态码
        code = self.response.status_code
        print(code)

        #请求的cookie
        # request_cookie = self.response.request.
        # print(request_cookie)

        #响应的cookie
        response_cookie = self.response.cookies
        print(response_cookie)

RequestSpider().run()