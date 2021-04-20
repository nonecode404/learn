import requests

params = {
    "wd":"美女a",
}

url = "https://www.baidu.com/s?"

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        }

response = requests.get(url, headers=headers,params=params)
data = response.content.decode()

with open("baidu.html", "w", encoding='utf-8') as f:
    f.write(data)

# 发送post 和添加参数