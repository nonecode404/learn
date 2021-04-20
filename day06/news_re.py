import requests
import re

url = "http://news.baidu.com/"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
}

data = requests.get(url, headers=headers).content.decode()

#每个新闻的标题和url
#<a href="http://www.xinhuanet.com/politics/leaders/2020-09/19/c_1126513115.htm" target="_blank" class="a3" mon="ct=1&amp;a=1&amp;c=top&amp;pn=0">什么样的企业，让总书记牵挂在心</a>

pattern = re.compile('<a (.*?)</a>', re.S)
result = pattern.findall(data)
print(result)
with open("news.html", "w", encoding="utf-8")as f:
    f.write(data)