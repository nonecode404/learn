import requests
import re
import string
import smtplib
from email.header import Header
from email.mime.text import MIMEText
import time

login_url = "http://172.28.10.66/confirm.asp"
record_url = "http://172.28.10.66/hrinfo/attendance/viewRecord.asp"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
}

#自动保存cokkie
session = requests.session()

# 代码登录

login_form_data = {
    "RedirectURL": "",
   " push_type": "1",
    "userNamec2U": "xh3033",
    "password": "vbZqYmg5"
}

login_response = session.post(login_url, data=login_form_data, headers=headers)
#2 登录成功后，session带着有效的cookie，再去访问
data = session.get(record_url, headers=headers).content.decode()

pattern = re.compile('<font class="exp">2020-(.*)</font>')
result = pattern.findall(data)
print(result)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(data)

time_list = result[0].split(" ")
print(time_list[1])
time_compare = time_list[1].split(":")
result_str = "获取失败"
if int(time_compare[0]) < 9 and int(time_compare[1]) <= 30:
    result_str = time_list[0] + " 打卡成功"
else:
    result_str = time_list[0] + " 打卡失败"


mail_host = "smtp.163.com"  # SMTP服务器
mail_user = "xuhan9191991@163.com"  # 用户名
mail_pass = "9191991"  # 授权密码，非登录密码

sender = 'xuhan9191991@163.com'    # 发件人邮箱(最好写全, 不然会失败)
receivers = ['1589420163@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

content = result[0]
title = result_str  # 邮件主题


def sendEmail():
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


if __name__ == '__main__':
    sendEmail()
    # receiver = '***'
    # send_email2(mail_host, mail_user, mail_pass, receiver, title, content)