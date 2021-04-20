import requests

url = "https://www.12306.cn"

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        }

free_proxy = {
    "http":"163.204.94.243:9999"
}

response = requests.get(url, headers=headers, proxies=free_proxy, verify=True)

print(response)