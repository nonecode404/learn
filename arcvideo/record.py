import re
import requests
import smtplib
from email.mime.text import MIMEText
import json
import datetime
#from lxml import etree
import collections


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
        "password": "vbZqYmg4"
    }

    login_response = session.post(login_url, data=login_form_data, headers=headers)
    # with open("confirm.html", "w", encoding="utf-8") as f:
    #     f.write(login_response.content.decode())
    #2 登录成功后，session带着有效的cookie，再去访问
    data = session.get(record_url, headers=headers).content.decode()
    # x_data = etree.HTML(data)
    # result = x_data.xpath('//td[@bgcolor="#FFFFFF"]/font[@class="exp"]/text()')
    pattern = re.compile('<font class="exp">(2+.*)</font>')
    result = pattern.findall(data)

    result_dict = collections.defaultdict(list)
    for it in result:
        result_list = it.split(' ')
        if  result_list[0] not in result_dict:
            result_dict[result_list[0]].append(result_list[1])
        else:
            result_dict[result_list[0]].append(result_list[1])
    # pattern = re.compile('<font class="exp">(2021+.*)</font>')
    # result = pattern.findall(data)
    print(result_dict)

    # with open("index.html", "w", encoding="utf-8") as f:
    #     f.write(data)
    return result_dict


def time_handle(result_dict):
    result_new_dict = {}

    today = datetime.date.today().strftime("%Y-%m-%d")
    for date in result_dict.keys():
        new_date = datetime.datetime.strptime(date, '%Y-%m-%d').strftime("%Y-%m-%d")
        result_new_dict[new_date] = result_dict[date]

    for record_day in result_new_dict.keys():
        if today not in result_new_dict.keys():
            today = (datetime.date.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
        else:
            break

    print(result_new_dict)
    result_str = ""
    for i in range(0, len(result_new_dict[today])) :
        result_str = result_str + "\n" + result_new_dict[today][i]
    return "最近一天打卡记录如下：\n" + today + result_str + "\n 发送于 " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def sendEmail(title, content):

    mail_host = "smtp.163.com"  # SMTP服务器
    mail_user = "xuhan15083135786@163.com"  # 用户名
    mail_pass = "xuhan...."  # 授权密码，非登录密码
    sender = 'xuhan15083135786@163.com'  # 发件人邮箱(最好写全, 不然会失败)
    receivers = ['xuhan9191991@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

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
    return result


if __name__ == '__main__':

    form_data = get_form()
    time_data = get_record()
    result_str = time_handle(time_data)
    print(result_str)
    result_send_wechat = sendmsg('oiCxq59xZe_klq_WkwHcfbbhIBB4', result_str)
    # ------邮箱发送-------
    if result_send_wechat['errcode'] != 0:
        content = result_str
        title = result_str  # 邮件主题
        sendEmail(title, content)