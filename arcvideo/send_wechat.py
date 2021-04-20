# pip3 install requests
import requests
import json


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
            'next_openid' : ""
        }
    )
    print(response.json())


def sendmsg(openid,msg):


    access_token = get_access_token()
    print(access_token)
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
    print(response.headers)
    # 这里可根据回执code进行判定是否发送成功(也可以根据code根据错误信息)
    result = response.json()
    print(result)



if __name__ == '__main__':
    #get_openid()
    sendmsg('oiCxq59xZe_klq_WkwHcfbbhIBB4','test发送消息内容')