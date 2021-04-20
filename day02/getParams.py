import urllib.request
import urllib.parse
import string

def getParams():
    url = "https://ww.baidu.com/s?"

    params = {
        "wd":"中文",
        "key":"zhang",
        "value":"sad"
    }

    paramsStr = urllib.parse.urlencode(params)
    print(paramsStr)
    finalUrl = url + paramsStr
    print(finalUrl)

    endUrl = urllib.parse.quote(finalUrl, safe=string.printable)
    print(urllib.parse.unquote(endUrl))
    response = urllib.request.urlopen(endUrl)
    data = response.read().decode()
    print(data)

getParams()