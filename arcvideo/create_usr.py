import requests
import _thread
import time

def send_post(name_str, phone_str):
    create_url = "http://172.17.22.136:20080/v2/user"
    headers = {
        'Content-Type': "application/json",
        }
    payload = "{\r\n  \"address\": \"string\",\r\n  \"age\": 0,\r\n  \"areaCode\": \"string\",\r\n  \"city\": \"string\",\r\n  \"gender\": \"string\",\r\n  \"moderator\": 0,\r\n  \"name\": \"" \
              + name_str +"\",\r\n  \"password\": \"1\",\r\n  \"phone\": \""\
              + phone_str + "\",\r\n  \"province\": \"string\"\r\n}"
    response = requests.post(create_url, data=payload, headers=headers)
    print(response.content.decode(encoding="utf-8"))
    # data_dict = response.json()
    # return data_dict

def process_user():
    data_dict = send_post()
    create_success_num = 0
    if data_dict == None:
        pass
        # print(response.content.decode(encoding="utf-8"))
    elif data_dict["code"] == 0:
        create_success_num += 1
    elif data_dict["code"] != 0:
        pass
        # print(response.content.decode(encoding="utf-8"))

if __name__ == '__main__':
    count = 0
    while count < 100:
        count += 1
        count_add = "%05d" % count
        name_str = "test" + count_add
        phone_str = "150000" + count_add
        send_post(name_str, phone_str)