import requests
import json
import time
import openpyxl

def getComm(productId, page):
    url = 'https://club.jd.com/comment/productPageComments.action?callback=' \
          'fetchJSON_comment98&productId={0}&score=0&sortType=5&page={1}&pageSize=10&isShadowSku=0&fold=1'.format(productId, page)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}

    resp = requests.get(url, headers=headers)

    s = resp.text.replace('fetchJSON_comment98(', '')
    s = s.replace(');', '')

    jsonData = json.loads(s)
    return jsonData

def getMaxPage(productId):
    dictData = getComm(productId, 0)
    return dictData['maxPage']

def getInfo(produtId):
    maxPage = 10
    lst = []
    for page in range(1, maxPage + 1): #左闭右开
        comments = getComm(productId, page)
        comm_list = comments['comments']
        for it in comm_list:
            content = it['content']
            color = it['productColor']
            size = it['productSize']
            lst.append([content, color, size])
        time.sleep(1)
    save(lst)

def save(lst) :
    wk = openpyxl.Workbook()
    sheet = wk.active
    for it in lst:
        sheet.append(it)

    wk.save('销售数据.xlsx')

if __name__ == '__main__':
    productId = '27069180004'
    print(getMaxPage(productId))
    getInfo(productId)

