import urllib.request

def load_baidu():
    url = "https://www.baidu.com/"
    #创建请求对象
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=header)
    #动态的去添加head信息
    request.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36")
    #请求网络数据（系统没有请求头参数）
    respose = urllib.request.urlopen(request)
    data = respose.read().decode()
    print(respose)
    #响应头
    #print(respose.headers)
    request_headers = request.headers
    print(request_headers)
    #第二种打印头,首字母大写，其他小写
    request_headers1 = request.get_header("User-agent")
    print(request_headers1)
    with open("02header.html", "w", encoding="utf-8")as f:
        f.write(data)

    #获取完整的url
    final_url = request.get_full_url()
    print(final_url)

load_baidu()