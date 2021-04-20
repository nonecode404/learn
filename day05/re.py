import requests
import re

# 贪婪模式从开头匹配到结尾

one = "masdsaddasdsadasnlsdfas112nn1"
two = "a\d"
pattern = re.compile(r"a\b")
# pattern = re.compile("m(.*?)n")

result = pattern.findall(two)

print(result)