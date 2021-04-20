import re

# .不匹配换行
one = '''
    mdafadfadfan
    132115661123N
'''

pattern = re.compile('m(.*)n', re.S | re.I)
result = pattern.findall(one)

print(result)