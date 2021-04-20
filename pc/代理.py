import requests

data = {"wd":"徐晗"}
url = "http://www.baidu.com/s?"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"}
resp = requests.get(url,params=data,headers=headers)
print(resp.text)