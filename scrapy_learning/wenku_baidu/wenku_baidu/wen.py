import re

import requests
import json

from PIL import Image
import os

def combine2Pdf( folderPath, pdfFilePath ):
    files = os.listdir( folderPath )
    pngFiles = []
    sources = []
    for file in files:
        if 'png' in file:
            pngFiles.append( folderPath + file )
    pngFiles.sort()
    output = Image.open(pngFiles[0])
    pngFiles.pop(0)
    for file in pngFiles:
        pngFile = Image.open(file)
        if pngFile.mode == "RGBA":
            pngFile = pngFile.convert( "RGB" )
            sources.append(pngFile)
        pngFile = pngFile.convert("RGB")
        sources.append(pngFile)
    print(len(pngFiles))
    output.save(pdfFilePath, "PDF", resolution=100.0,save_all=True, append_images=sources)




headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363"
     ,
"Cookie": "BIDUPSID=6B19A068AE8275D1DF754FB8A4112D9B; PSTM=1594108529; BDUSS=lhQaEd1Q3p1ajJGZXlLOFY1MlJVc2ZHbXNUUGRzRmx6RW0wem11YWxmbFktVEZnSVFBQUFBJCQAAAAAAAAAAAEAAABshhGly8TKrs7luPZjYwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFhsCmBYbApga; BDUSS_BFESS=lhQaEd1Q3p1ajJGZXlLOFY1MlJVc2ZHbXNUUGRzRmx6RW0wem11YWxmbFktVEZnSVFBQUFBJCQAAAAAAAAAAAEAAABshhGly8TKrs7luPZjYwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFhsCmBYbApga; MCITY=-%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; __yjs_duid=1_338ed865fa5c0cae02a8579e81f8bbf61616978757359; BAIDUID=D2047E9F7F9C87A10F345AEF957ED876:FG=1; H_PS_PSSID=33817_33746_33272_31253_33781_33760_33675_33392_26350_33794; BDSFRCVID=nBKOJeC62rR8hqrejjjTt8A-UmaDrIQTH6aovajQ1CZj9TijNPHnEG0PDM8g0Kub5ymwogKKKgOTHICF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJPq_I_2JI83fP36qRjqbJjH-UnLqMkJ02OZ0l8KttoCjnFmjto8ypQ-5a7CelQLWbrJKfbmWIQHDp6H5PQF5R_hyJQWtpQOb2Q4KKJxfnLWeIJo5t5DybtrhUJiBMnMBan7alOIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbC_RjTLhD6oBepJf-K6L2CobWnT856rjDCvkLxRcy4LdjG5HQjv3-6r-BJc_QP-WEj6ahtQUKxFu3-Aq54RqKCQIolOu2DTxjJc80M7_QfbQ0-OuqP-jW5Ta_4TEbb7JOpvobUnxyMFdQRPH-Rv92DQMVU52QqcqEIQHQT3m5-5bbN3ut6T2-DA__IDXfCbP; BDSFRCVID_BFESS=nBKOJeC62rR8hqrejjjTt8A-UmaDrIQTH6aovajQ1CZj9TijNPHnEG0PDM8g0Kub5ymwogKKKgOTHICF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJPq_I_2JI83fP36qRjqbJjH-UnLqMkJ02OZ0l8KttoCjnFmjto8ypQ-5a7CelQLWbrJKfbmWIQHDp6H5PQF5R_hyJQWtpQOb2Q4KKJxfnLWeIJo5t5DybtrhUJiBMnMBan7alOIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbC_RjTLhD6oBepJf-K6L2CobWnT856rjDCvkLxRcy4LdjG5HQjv3-6r-BJc_QP-WEj6ahtQUKxFu3-Aq54RqKCQIolOu2DTxjJc80M7_QfbQ0-OuqP-jW5Ta_4TEbb7JOpvobUnxyMFdQRPH-Rv92DQMVU52QqcqEIQHQT3m5-5bbN3ut6T2-DA__IDXfCbP; BAIDUID_BFESS=D2047E9F7F9C87A10F345AEF957ED876:FG=1; delPer=0; PSINO=5; BA_HECTOR=21aga0a1248ha52hce1g6bdhb0r; ZD_ENTRY=baidu; ab_sr=1.0.0_ODMwMWMwNGY0ODgxMTY4M2EwYTExYmY2M2UzZmVhYzE5ZGYwZDQ2NTA3ZmM0NDVkNDcyNWQ2YTM3YzNhYTkyZWFlZWI0YWQ2MDg5NWEyNjA5MWEwY2EwNmZmOTk2MTdiODhhNDA1ZGRkOGZiM2QzMWM2YTA0NzI3M2JlNDBlOTc="}
start_urls = 'https://wenku.baidu.com/view/521180a9b5daa58da0116c175f0e7cd1842518e8.html'
#start_urls = 'https://wenku.baidu.com/view/f06f412805087632301212bb.html'
response = requests.get(start_urls, headers=headers)
response_str = response.text
with open("1.html", "w") as f:
    f.write(response.text)
#pattern = re.compile('"htmlUrls":(.*)')
#pattern = re.compile("WkInfo.htmlUrls = '(.*)'")
pattern = re.compile('var pageData = \{(.*)\}')
result = pattern.findall(response_str)
print(result)

result_str = result[0].replace("\\","").replace("x22","\"")
print(result_str)
# dict = json.loads(result_str)
# print(dict['png'])
# for sigle_dict in dict['png']:
#     image_url = sigle_dict['pageLoadUrl']
#     image_response = requests.get(image_url, headers=headers)
#     pageIndex_str = str(sigle_dict['pageIndex'])
#     with open("D:\\log\\images\\%s.png"%pageIndex_str, "wb") as f:
#         f.write(image_response.content)

#
# folder = "D:/log/images/"
# pdfFile = "D:/log/contract.pdf"
# combine2Pdf(folder, pdfFile)


