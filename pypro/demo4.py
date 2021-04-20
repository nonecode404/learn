import requests
import re
import _thread
import json

url = 'http://pl.tcc-interiors.com/hls/888b4161fa18768e487fe28545d28e991698c1c8'
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Host': 'pl.tcc-interiors.com',
'Referer': 'http://1090ys1.com/play/4103~0~0.html',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}
resp = requests.get(url, headers = headers) #关键字参数
print(resp)
json_dict_2 = json.dumps(headers, indent=2, sort_keys=True, ensure_ascii=False)
print(json_dict_2)

# count = 1
# with open('video1/' + str(count) + ".mp4", 'wb') as file:
#     file.write(resp.content)  # 写的是二进制数据


# for it in lst :
#     #发请求
#     resp = requests.get(it, headers = headers)
#     count += 1
#     try:
#         _thread.start_new_thread(download, ('线程1',))
#         _thread.start_new_thread(download, ('线程2',))
#         _thread.start_new_thread(download, ('线程3',))
#         _thread.start_new_thread(download, ('线程4',))
#     except:
#         print('Error: 无法启动')
#     print('--')


print('下载结束')