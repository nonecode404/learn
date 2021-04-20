import requests

data = {"wd":"徐晗"}
url = "http://172.28.10.66/login.asp?RedirectURL==&push_type=1&userNameUCn=xh3033&password=vbZqYmg5"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
           "Referer": "http://172.28.10.66/login.asp"}
resp = requests.post(url,headers=headers)
resp.encoding="utf-8"
print(resp.text)