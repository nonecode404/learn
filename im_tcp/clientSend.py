import socket
import json
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置端口号
port = 2233
host = "172.17.22.137"

# 连接服务，指定主机和端口
s.connect((host, port))

json_body = {"action": 1, "appId": "99907d430d774e04928a216c45cc9234", "customerId": "459", "orgId": "98765", "userId": "5_1", "extInfo": "test_1", "apiVersion": "2.0"}
stream = json.dumps(json_body)
packet = struct.pack('!I', len(stream)) + stream.encode()

s.send(packet)

# 接收小于 1024 字节的数据
msg = s.recv(1024)

s.close()

print (msg)