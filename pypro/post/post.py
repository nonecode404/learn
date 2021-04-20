import requests

data = "first=true&p=1&kd=python"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}
url = 'https://www.lagou.com/jobs/positionAjax.json'
resp = requests.get(url, headers=headers)
print(resp.text)