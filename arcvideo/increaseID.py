import json
import requests
with open("./updateplaylist.json","r", encoding="utf-8") as f:
    updatalist_json = json.load(f)

print(updatalist_json)
ID = 1
for list in updatalist_json['updateplaylist']:
    list['ID'] = str(ID)
    list['PAUSE'] = 1

#    response = requests.get(url=list['URL'])
#    data = response.content
#    with open('./video1/' + str(ID), "wb") as f:
#        f.write(data)
    ID += 1
#    print("下载成功" + str(ID))
print(updatalist_json)


with open("./updateplaylist.json","w") as f:
    json.dump(updatalist_json, f, indent=4)
