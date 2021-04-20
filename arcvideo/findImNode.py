import requests
import time
import datetime
from requests.exceptions import ConnectionError

#im_url = 'http://172.17.230.193/_sys/s'
im_url_list = []
im_url_list.append('http://172.17.22.136:8083/_sys/s')
im_url_list.append('http://172.17.22.137:8083/_sys/s')
im_url_list.append('http://172.17.230.193/_sys/s')

#im_url = 'http://172.17.22.136:8083/_sys/s'

while True:
    response = None
    for im_url in im_url_list:
        try:
            response = requests.get(im_url)

            if response.status_code == 200:
                print('success')
                break
        except ConnectionError:
            print('---' + im_url + '---' + '不可用')


    json_data = response.json()

    groups_data = json_data['result']['groups']

    curr_time = datetime.datetime.now()
    time_str = datetime.datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S')
    print('--------------' + time_str + '----------------')
    for gd in groups_data:
        if gd['userId'] == 'iwqwaramaw':
            print(gd['userId'] + '----' + gd['tcpIp'])

        if gd['userId'] == 'nzrneynaia':
            print(gd['userId'] + '----' + gd['tcpIp'])

        if gd['userId']                == 'jewjforivy':
            print(gd['userId'] + '----' + gd['tcpIp'])
    print()
    time.sleep(3)
