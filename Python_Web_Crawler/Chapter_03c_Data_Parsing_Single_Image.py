##!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests

url = 'https://imgcdn.yicai.com/uppics/slides/2023/02/5fda3f8b987b3d26d549aeee4bab619e.jpg'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
# 图片数据使用content      text, json
img_data = requests.get(url=url, headers=headers).content
with open('./Element/Single_Img_Test.jpg', 'wb') as fp:
    fp.write(img_data)
    

