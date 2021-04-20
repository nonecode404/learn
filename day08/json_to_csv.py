import json
import csv

#1.读、创建文件
json_fp = open("text.json", "r")
csv_fp = open("csv.csv", "w")

#2.提出表头
data = json.load(json_fp)

sheet_title = data[0].keys()
sheet_data = []

for it in data:
    sheet_data.append(it.values())

writer = csv.writer(csv_fp)

writer.writerow(sheet_title)
writer.writerows(sheet_data)

json_fp.close()
csv_fp.close()