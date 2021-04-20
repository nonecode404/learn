from socket import *
from time import ctime

import re
import requests
import smtplib
from email.header import Header
from email.mime.text import MIMEText
import json
import datetime

def get_form():
    url = "http://172.28.10.66/login.asp"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363"
    }

    respone = requests.get(url, headers=headers)

    data = respone.content.decode()
    pattern = re.compile("var userCode = '(.*)'")
    result = pattern.findall(data)
    return result[0]

def get_record():
    login_url = "http://172.28.10.66/confirm.asp"
    record_url = "http://172.28.10.66/hrinfo/attendance/viewRecord.asp"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363"
    }

    #自动保存cokkie
    session = requests.session()
    # 代码登录
    str_form = get_form()#获取动态表单
    login_form_data = {
        "RedirectURL": "",
        "push_type": "1",
        "userName"+str_form: "xh3033",
        "password": "vbZqYmg5"
    }

    login_response = session.post(login_url, data=login_form_data, headers=headers)
    with open("confirm.html", "w", encoding="utf-8") as f:
        f.write(login_response.content.decode())
    #2 登录成功后，session带着有效的cookie，再去访问
    data = session.get(record_url, headers=headers).content.decode()
    pattern = re.compile('<font class="exp">(2020+.*)</font>')
    result = pattern.findall(data)
    print(result)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(data)
    return result

def time_handle(result):
    time_list = []
    for time in result:
        date_time = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        time_list.append(date_time)
    # today_record = time_list[0].split(" ")
    return "近两天打卡记录如下" + "\n" + result[0] + "\n" + result[1] + "\n" + result[2]  + "\n" + result[3]

    # time_compare = time_list[1].split(":")
    # result_str = "获取失败"
    # if (int(time_compare[0]) < 9 and int(time_compare[1]) <= 30) or (int(time_compare[0]) >= 17 and int(time_compare[1]) >= 30):
    #     result_str = time_list[0] + " 打卡成功"
    # else:
    #     result_str = time_list[0] + " 打卡失败"
    # return time_list[0] + " 打卡记录：" + "\n" + result[0] + "\n" + result[1]



def sendEmail(title, content):

    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print("send failed!")
        print(e)

def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):
    email_client = smtplib.SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())

    email_client.quit()

def get_access_token():
    """
    获取微信全局接口的凭证(默认有效期俩个小时)
    如果不每天请求次数过多, 通过设置缓存即可
    """
    result = requests.get(
        url="https://api.weixin.qq.com/cgi-bin/token",
        params={
            "grant_type": "client_credential",
            "appid": "wxb1a20486d2d6bbf5",
            "secret": "b4f84fbf2667cfa6b8069a8e945d2130",
            # "secret": "4d1918bc868f815713ef0e1e42f1ff28",
        }
    ).json()

    if result.get("access_token"):
        access_token = result.get('access_token')
    else:
        access_token = None
    return access_token

def get_openid():
    access_token = get_access_token()
    response = requests.get(
        url="https://api.weixin.qq.com/cgi-bin/user/get",
        params={
            'access_token': access_token,
            'next_openid': ""
        }
    )
    print(response.json())

def sendmsg(openid, msg):

    access_token = get_access_token()
    body = {
        "touser": openid,
        "msgtype": "text",
        "text": {
            "content": msg
        }
    }
    response = requests.post(
        url="https://api.weixin.qq.com/cgi-bin/message/custom/send",
        params={
            'access_token': access_token
        },
        data=bytes(json.dumps(body, ensure_ascii=False), encoding='utf-8')
    )
    # 这里可根据回执code进行判定是否发送成功(也可以根据code根据错误信息)
    result = response.json()
    print(result)


if __name__ == '__main__':



    #------邮箱发送-------
    # mail_host = "smtp.163.com"  # SMTP服务器
    # mail_user = "xuhan9191991@163.com"  # 用户名
    # mail_pass = "9191991"  # 授权密码，非登录密码
    # sender = 'xuhan9191991@163.com'  # 发件人邮箱(最好写全, 不然会失败)
    # receivers = ['1589420163@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    #
    # content = time_data[0]
    # title = result_str  # 邮件主题
    # sendEmail(title, content)
    # receiver = '***'
    # send_email2(mail_host, mail_user, mail_pass, receiver, title, content)

    host = ''
    port = 12345
    buffsize = 2048
    ADDR = (host,port)

    tctime = socket(AF_INET,SOCK_STREAM)
    tctime.bind(ADDR)
    tctime.listen(3)

    while True:
        print('Wait for connection ...')
        tctimeClient,addr = tctime.accept()
        print("Connection from :",addr)

        while True:
            data = tctimeClient.recv(buffsize).decode()
            if not data:
                break
            print(data)

            if data == "1":
                form_data = get_form()
                time_data = get_record()
                result_str = time_handle(time_data)
                sendmsg('oiCxq59xZe_klq_WkwHcfbbhIBB4', result_str)

            tctimeClient.send(('[%s] %s' % (ctime(),data)).encode())
        tctimeClient.close()
    tctimeClient.close()