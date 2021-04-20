import urllib.request

def proxy_user():

    proxy = [
        {"http":"1.196.177.113:9999"},
        {"http":"171.12.115.166:9999"},
        {"http":"1.197.204.158"},
        {"http":"110.243.15.173:9999"}
    ]

    for proxy in proxy:
        print(proxy)
        #用ip创建处理器
        proxy_handler = urllib.request.ProxyHandler(proxy)
        #创建opener
        opener = urllib.request.build_opener(proxy_handler)

        try:
            opener.open("https://www.baidu.com/", timeout=1)
            print("hah")
        except Exception as e:
            print(e)

proxy_user()