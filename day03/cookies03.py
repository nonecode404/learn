import urllib.request
import urllib.parse
from http import cookiejar
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
login_url = "https://rtcdemo.arcvideo.com:9443/login"

login_form_data = {
    "j_username":"admin",
    "j_password":"888888",
    # "formhash":"718595F213",
    # "backurl":"https%2F%2Fwww.yaozh.com"
}

cook_jar = cookiejar.CookieJar()
cook_handler = urllib.request.HTTPCookieProcessor(cook_jar)

opener = urllib.request.build_opener(cook_handler)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
}

login_str = urllib.parse.urlencode(login_form_data).encode("utf-8")
print(login_str)
login_request = urllib.request.Request(login_url, headers=headers, data=login_str)
opener.open(login_request)

center_url = "https://rtcdemo.arcvideo.com:9443/statistics/index"
center_request = urllib.request.Request(center_url, headers=headers)
response = urllib.request.urlopen(center_request)
data =  response.read().decode()

with open("03cookies.html", "w", encoding="utf-8") as f:
    f.write(data)