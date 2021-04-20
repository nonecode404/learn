import requests
import re
import _thread

def page():
    url = 'https://youku.com-youku.net/20180517/2484_c98d1fee/1000k/hls/index.m3u8'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}
    resp = requests.get(url, headers = headers) #关键字参数
    print(resp.text)
    info = re.findall(r"a href=\"(.*)\" class=\"btn btn-default btn-sm\"", resp.text)
    print(info)
    # intfo = re.findall(r'a href="(.*)" class="btn btn-default btn-sm"', info)
    # print(intfo)
    return info

if __name__ == '__main__':
    page()

# with open('video1', 'wb') as file:
#     file.write(resp.content)  # 写的是二进制数据