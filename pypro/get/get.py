import requests
import urllib.parse
'''
编码解码

word = {"wd":"徐晗"}
print(urllib.parse.urlencode(word))
print(urllib.parse.unquote(urllib.parse.urlencode(word)))
'''

url = 'http://www.baidu.com/s'
word = {"wd":"徐晗"}
word = urllib.parse.urlencode(word)#编码成字符串
newurl = url + "?" +word

resp = requests.get(newurl)
print(resp.text)