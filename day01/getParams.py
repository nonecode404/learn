import urllib.request
import urllib.parse
import string

def get_methon_params():
    url = "http://www.baidu.com/s?wd="
    name = "美女"
    finalUrl = url + name
    print(finalUrl)
    #汉字转义
    encodeUrl = urllib.parse.quote(finalUrl, safe=string.printable)

    respose = urllib.request.urlopen(encodeUrl)
    print(respose)
    #python支持ASCII 0-127
    data = respose.read().decode()
    print(data)
    with open("02encode.html", "w", encoding="utf-8") as f:
        f.write(data)
get_methon_params()