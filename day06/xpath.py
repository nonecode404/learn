import requests
from lxml import etree

url = "http://news.baidu.com/"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
}

data = requests.get(url, headers=headers).content.decode()

#每个新闻的标题和url
#<a href="http://www.xinhuanet.com/politics/leaders/2020-09/19/c_1126513115.htm" target="_blank" class="a3" mon="ct=1&amp;a=1&amp;c=top&amp;pn=0">什么样的企业，让总书记牵挂在心</a>

xpath_data = etree.HTML(data)
result = xpath_data.xpath('/html/head/title/text()')
result = xpath_data.xpath('//a/text()')
result = xpath_data.xpath('//a[@mon="ct=1&a=1&c=top&pn=0"]/text()')
result = xpath_data.xpath('//a[@mon="ct=1&a=1&c=top&pn=0"]/@href')
result = xpath_data.xpath('//li/a/text()')

print(result)
