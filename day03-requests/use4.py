import requests
import json

url = "https://api.github.com/usr"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        }
response = requests.get(url,headers=headers)
# data = response.content.decode()
# print(data)
#
# data_dict = json.loads(data)
# print(data_dict["message"])

#自动转换成dict或list
data =response.json()
print(type(data))