import requests
import re
import _thread

url = 'https://www.qiushibaike.com/video/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}
resp = requests.get(url, headers = headers) #关键字参数

print(resp.request.headers)
info = re.findall(r'<source src="(.*)" type=\'video1/mp4\' />', resp.text)
print(info)
print(type(info))
lst = [] #用于存储拼接之后的url

for it in info:
    lst.append('https:' + it)

print(lst)

# def download(threadName) :
#     print(threadName + '启动')
#     with open('video1/' + str(count) + ".mp4", 'wb') as file:
#         file.write(resp.content)  # 写的是二进制数据
#
# count = 0
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