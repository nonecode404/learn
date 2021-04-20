import requests
import re

def sendRequest():

    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-09-06&leftTicketDTO.from_station=HZH&leftTicketDTO.to_station=ZZF&purpose_codes=ADULT'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
               'Cookie': '_uab_collina=159848930277257456750267; JSESSIONID=9AE1D1E94CDA0C8B35A60E65C08680E0; RAIL_EXPIRATION=1598787744725; RAIL_DEVICEID=lKnT4wKzelx-dKZqDYo0WRti-dFOUcPClAjb5biHMwrR8ZzAm3ITTSr_qBV77085sOFvtH3IWnvHC4PY5fTK-cq17CowOfo6aHqk3anCcdzn7PM6B19SRw_ypTU0PGNc3oVLWERCFwwV1C3pvV2D7SOLeVSu4uzP; _jc_save_fromStation=%u676D%u5DDE%2CHZH; _jc_save_toStation=%u90D1%u5DDE%2CZZF; _jc_save_wfdc_flag=dc; _jc_save_toDate=2020-08-28; route=c5c62a339e7744272a54643b3be5bf64; BIGipServerotn=116392458.38945.0000; _jc_save_fromDate=2020-08-28'}
    resp = requests.get(url,headers=headers)

    print(resp.text)
    return resp

def parseJson(resp, city):
    jsonData = resp.json()
    print(jsonData)
    dataL = jsonData['data']['result']

    lst = []
    for it in dataL:
        d = it.split("|")
        lst.append([d[3], city[d[6]],city[d[7]], d[31], d[30], d[13]])
    return lst
def getStaName():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9153'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
               'Cookie': '_uab_collina=159848930277257456750267; JSESSIONID=9AE1D1E94CDA0C8B35A60E65C08680E0; RAIL_EXPIRATION=1598787744725; RAIL_DEVICEID=lKnT4wKzelx-dKZqDYo0WRti-dFOUcPClAjb5biHMwrR8ZzAm3ITTSr_qBV77085sOFvtH3IWnvHC4PY5fTK-cq17CowOfo6aHqk3anCcdzn7PM6B19SRw_ypTU0PGNc3oVLWERCFwwV1C3pvV2D7SOLeVSu4uzP; _jc_save_fromStation=%u676D%u5DDE%2CHZH; _jc_save_toStation=%u90D1%u5DDE%2CZZF; _jc_save_wfdc_flag=dc; _jc_save_toDate=2020-08-28; route=c5c62a339e7744272a54643b3be5bf64; BIGipServerotn=116392458.38945.0000; _jc_save_fromDate=2020-08-28'}

    resp = requests.get(url, headers=headers)
    resp.encoding = 'UTF-8'
    stationNames = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', resp.text)
    staionData = dict(stationNames)
    staionDataTemp = {}
    for it in staionData:
        staionDataTemp[staionData[it]] = it
    return staionDataTemp


if __name__ == '__main__':
    lst = parseJson(sendRequest(), getStaName())
    for it in lst:
        if it[3] != '无' and it[3] != '':
            print(it)
