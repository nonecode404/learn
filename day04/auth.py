import requests

url = "http://172.28.10.66/login.asp?RedirectURL=/index2014/index.asp"

#内网
auth = (user,pwd)

response = requests.get(url, auth=auth)

print(response.text)