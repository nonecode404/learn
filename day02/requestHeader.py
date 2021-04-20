import urllib.request

def load_baidu():
    url = "https://www.baidu.com/"
    #创建请求对象
    request = urllib.request.Request(url)

    respose = urllib.request.urlopen(request)
    data = respose.read().decode()
    print(respose)
    #响应头
    #print(respose.headers)
    request_headers = request.headers
    print(request_headers)
    with open("02header.html", "w")as f:
        f.write(data)

load_baidu()