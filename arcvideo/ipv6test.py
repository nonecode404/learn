import socket  # 导入 socket 模块

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 8989  # 设置端口号

print(host)

s.connect((host, port))

s.close()