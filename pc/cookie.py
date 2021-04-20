import requests
import time

mycookie = {"bdsid":"zhaidu"}
resp = requests.get("http://httpbin.org/cookies", cookies = mycookie)
time.sleep(3)
print(resp.cookies)
print(resp.text)