import re
#纯数字正则

pattern = re.compile('^\d+$')
one = "132131"
result = pattern.match(one)
print(result.group())
