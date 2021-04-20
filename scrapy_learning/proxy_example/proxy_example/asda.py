import requests

url = 'http://icanhazip.com'
proxy = {'http':'14.20.235.232:808'}

resp = requests.get(url,proxies=proxy).text

print(resp)