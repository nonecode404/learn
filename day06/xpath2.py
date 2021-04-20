from lxml import etree
html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<ul>
    <li>1
        <a herf="">子</a>
    </li>
    <li>2
        <a herf="">子</a>
    </li>
    <li>3
        <a herf="">子</a>
    </li>
    <li>4
        <a herf="">子</a>
    </li>
    <li>5
        <a herf="">子</a>
    </li>
</ul>  
</body>
</html>
'''

x_data = etree.HTML(html)

result = x_data.xpath("//li[4]//text()")
result = x_data.xpath("//a/text()")
print(result)