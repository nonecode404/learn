import json

#1.字符串和dic list转换

#2.字符串----dict list
data = '[{"name":"张三","age":20},{"name":"李四","age":18}]'

list_data = json.loads(data)

list2 = [{"name":"张三","age":20},{"name":"李四","age":18}]
data_json = json.dumps(list2)

print(data)
print(type(list_data))
print(type(list2))
print(type(data_json))