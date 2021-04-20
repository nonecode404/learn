import requests

session = requests.Session()
params = {"currentloginusername":"3033","currentloginv":"05F7A1B3D7BEADD5C8040F88F9388A22"}
mySession = session.post("http://172.28.10.66/confirm.asp", params)
print(mySession.cookies.get_dict())

mySession = session.get("http://172.28.10.66/index2014/index.asp")
print(mySession.text)