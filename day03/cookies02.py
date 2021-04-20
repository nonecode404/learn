import urllib.request
import urllib.parse
from http import cookiejar

login_url = "https://www.yaozh.com/login"

login_form_data = {
    "username":"xh3033",
    "pwd":"xh3033",
    "formhash":"718595F213",
    "backurl":"https%2F%2Fwww.yaozh.com"
}

cook_jar = cookiejar.CookieJar()
cook_handler = urllib.request.HTTPCookieProcessor(cook_jar)

opener = urllib.request.build_opener(cook_handler)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
}

login_str = urllib.parse.urlencode(login_form_data).encode("utf-8")

login_request = urllib.request.Request(login_url, headers=headers, data=login_str)
opener.open(login_request)

center_url = "https://www.yaozh.com/member/"
center_request = urllib.request.Request(center_url, headers=headers)
response = urllib.request.urlopen(center_request)
data =  response.read().decode()

with open("02cookies.html", "w", encoding="utf-8") as f:
    f.write(data)