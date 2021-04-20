import requests
import _thread
import time

def send_post():
    name_str = "test"
    phone_str = "15000000002"
    create_url = "https://www.baidu.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363"
    }

    response = requests.post(create_url,headers=headers)
    print(response.content.decode(encoding="utf-8"))


if __name__ == '__main__':
    count = 0
    while count < 100:
        count += 1
        send_post()
