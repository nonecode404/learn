import urllib.request

def load_data():
    url = "http://www.baidu.com/"
    response = urllib.request.urlopen(url)
    print(response)
    data = response.read()
    print(data)
    #换成字符串
    str_data = data.decode("utf-8")
    print(str_data)
    #将数据写入文件
    with open("baiud.html","w",encoding="utf-8")as f:
        f.write(str_data)
    #将字符串转为bytes
    #爬取类型：str，bytes，写入 decode("utf-8),读取

load_data()