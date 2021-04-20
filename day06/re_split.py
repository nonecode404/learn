import re

one = "dasdasd"

pattern = re.compile('s')
result = pattern.split(one)
#print(result)

two = '<a class="title text-truncate" target="_blank" href="https://blog.csdn.net/weixin_44312186/article/details/89000922#comments_13254919" data-report-click="{&quot;mod&quot;:&quot;popu_542&quot;,&quot;spm&quot;:&quot;1001.2101.3001.4231&quot;,&quot;dest&quot;:&quot;https://blog.csdn.net/weixin_44312186/article/details/89000922#comments_13254919&quot;,&quot;ab&quot;:&quot;new&quot;}">关于opencv报错：未定义标识符"CV_WINDOW_AUTOSIZE"</a>'
pattern = re.compile('[\u4E00-\u9FA5]+')

result = pattern.findall(two)
print(result)