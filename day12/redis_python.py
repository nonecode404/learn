import redis

#1.连接数据库
client = redis.StrictRedis(host="127.0.0.1", port=6379)

#2.设置key
key = "pyone"

#3. string 增加
result = client.set(key, "1")

#4. string 删除
result = client.delete(key)

#5. string 改
result = client.set(key, "2")

#6. string 查
result = client.get(key)
#查看所有键
result = client.keys()
print(result)