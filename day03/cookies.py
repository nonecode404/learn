import urllib.request

url = "https://www.yaozh.com/member/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
    "Cookie": "acw_tc=2f624a5816002176729092359e0cdc3d9ce9a21b58da0c557cdd109b11e401; PHPSESSID=4j7da4tc15ir2r3iqvh4092q64; _ga=GA1.2.1584314457.1600217673; _gid=GA1.2.587577787.1600217673; _gat=1; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1600217673; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1600217746; yaozh_logintime=1600217754; yaozh_user=982459%09xh3033; yaozh_userId=982459; yaozh_jobstatus=kptta67UcJieW6zKnFSe2JyXnoaab5dpmp2HnKZxanJT1qeSoMZYoNdzbZtaqsuYkpSXhpyqn26fhtHCpquUrJrOnlNu1HCWlHNZkm5ik5a23B444F09831649e451172c0E2F5d061Zk5malFmgqJ%2BYn4OnoKKdU5ysa2SUcIeVb2eRamOanJeWlZSTWaCy216c120f398fe4dd90b8a781e12749e3; db_w_auth=816960%09xh3033; UtzD_f52b_saltkey=fOh9PxPo; UtzD_f52b_lastvisit=1600214156; UtzD_f52b_lastact=1600217756%09uc.php%09; UtzD_f52b_auth=aa85GMG%2FHp%2BnKFrj6AUqhXs9oDQnRbLurLxQ3oK%2BeyDTqDubByqu5EdMrBF6K7r8Ck0JvAYb%2BIjI3sf9A94niaOBs4E",
    "Host": "www.yaozh.com",
    "Referer": "https://www.yaozh.com/"
}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(url)
data = response.read().decode()
with open("cookies.html", "w", encoding="utf-8") as f:
    f.write(data)