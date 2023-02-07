##!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
# 爬取广东省博物馆的文物照片
url = 'http://www.gdmuseum.com/col49/list'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
# 对整张页面进行爬取
response = requests.get(url, headers)
web_code = response.text

with open('./广东省博物馆.html', 'w', encoding='utf-8') as fp:
    fp.write(web_code)
# 使用聚焦爬虫将页面所有的图片进行解析/提取
# 找到图片所属的标签,使用正则找到所有img对应的src并存入列表中
ex = '<li class="li">.*?<img src="(.*?)" alt=.*?</li>'
images = re.findall(ex, web_code, re.S)

# 生成图片连接
for i in images:
    ex = '/upload/cn/image/.*/(\d+.jpg)'
    image_name = re.findall(ex, i)[0]
    img_url = 'http://www.gdmuseum.com'+i
    img_response = requests.get(img_url, headers).content
    with open('C:/Users/shell_master/Desktop/爬虫照片/%s'% image_name, 'wb') as fp:
        fp.write(img_response)
        print(image_name, '保存成功')





