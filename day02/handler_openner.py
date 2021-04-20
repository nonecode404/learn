import urllib.request

def handler_opener():

    #urllib.request.urlopen()
    #系统没有添加代理的方法
    url = "https://www.baidu.com/"

    #创建自己的处理器
    handler = urllib.request.HTTPHandler()
    #创建自己的oppender
    opener = urllib.request.build_opener(handler)
    #用自己创建的opener调用open方法请求数据
    response = opener.open(url)
    data = response.read()
    print(response)
    print(data)

handler_opener()