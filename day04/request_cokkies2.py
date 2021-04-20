import requests

member_url = "https://www.yaozh.com/member/"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363"
}

#自动保存cokkie
session = requests.session()

# 代码登录
login_url = "https://www.yaozh.com/login/"
login_form_data = {
    'username': 'xh3033',
    'pwd': 'xh3033',
    'formhash': '2BBF2A207D',
    'backurl': 'https%3A%2F%2Fwww.yaozh.com%2F',
}

login_response = session.post(login_url, data=login_form_data, headers=headers)
print(login_response.content.decode())
print(session.cookies)

#2 登录成功后，session带着有效的cookie，再去访问
data = session.get(member_url, headers=headers).content.decode()

with open("cokkie2.html", "w", encoding="utf-8") as f:
    f.write(data)
