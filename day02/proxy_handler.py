import urllib.request

def create_proxy_handler():
    url = "https://www.baidu.com/"

    proxy = {
        #"http":"http://113.121.43.128:9999"
        "http":"//113.121.43.128:9999"
    }
    #代理处理器
    proxy_headler = urllib.request.ProxyHandler(proxy)

    #创建自己opener
    opener = urllib.request.build_opener(proxy_headler)
    #用的代理ip发送请请求
    data = opener.open(url).read()
    print(data)

create_proxy_handler()
