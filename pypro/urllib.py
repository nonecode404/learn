from urllib import request

resp = reqeust.urlopen('https://www.baidu.com')
print(resp.read().decode())