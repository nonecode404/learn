import urllib.request

url = "https://www.baidu/dasdasda.cn"

try:
    response = urllib.request.urlopen(url)

except urllib.request.HTTPErrorProcessor as error:
    print(error.code)

except urllib.request.URLError as error:
    print(error)