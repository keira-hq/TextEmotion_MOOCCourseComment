# 获取结果
import urllib.request
import json

import requests

text = input("请输入课程评论：")
request_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/text_cls/mooc_comment"  # 自己的api地址
params = json.dumps({"text": text, "top_num": 5}).encode("utf-8")

access_token = '24.8424e320822c13784208f97760642914.2592000.1645084410.282335-25526000' # 上一部分中获取的密钥
request_url = request_url+'?access_token='+access_token
response=requests.post(url=request_url,data=params,headers={'content-type':'application/json'})
content = response.json()
# print(content)
if content:
    resu = content
    print(resu)
    for i in range(0,5):
        Comment_Score = resu['results'][i]['name']
        a = resu['results'][i]['score']
        a = ('%.5f' %a)
        print("该评论为"+Comment_Score+"分的概率为:" +a)  # 输出相应分类结果与置信度
