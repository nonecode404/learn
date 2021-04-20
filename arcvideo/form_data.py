import requests
import re

url = "http://172.28.10.66/login.asp"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363"
}

respone = requests.get(url, headers=headers)

data = respone.content.decode()
pattern = re.compile("var userCode = '(.*)'")
result = pattern.findall(data)
