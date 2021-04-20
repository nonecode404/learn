import re

# 范围运算

one = "23113212312312312312312"

pattern = re.compile("[5-9]")

result = pattern.findall(one)
print(result)