#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    破解百度翻译  https://fanyi.baidu.com/?aldtype=16047#auto/zh
        1. 当输入英文单词的到百度翻译的文本框中,页面出现了局部刷新的情况
            页面局部刷新 --> 由 ajax 请求实现
            ajax 请求发送后能够实现页面局部刷新
        2. 通过F12 --> 网络 --> XHR 即可筛选出由ajax请求发出的数据包并且通过载荷查看kw:就是输入的参数, 最后的sug内包含完整的单词(主要看最后的一个sug包)
        3. 查看最后一个sug的请求url以及请求方法
        4. 响应头的content-type 显示是 application-json  --> 证明post请求发送出去后返回的是一个json character 可以通过 响应 查看具体的json内容
        5. 使用post请求发送,并且携带参数(需要翻译的单词作为参数)
            - 使用request模块发送一个post请求
            - 发送post过程中处理post请求所携带的参数
"""
import requests
import json

post_url = 'https://fanyi.baidu.com/sug'        # 指定url
word = input('input a word ')
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'     # UA 伪装
}
data = {
    'kw': word  # 'kw' 是 百度翻译定义的       指定post携带的参数
}

response = requests.post(url=post_url, data=data, headers=header)   # 发送请求并且获取返回数据
# response.test()  返回的是一个字符串
dic_obj = response.json()     # 此处返回的是一个obj  只有确定了响应数据是json类型才能使用json方法  通过网页F12的响应头中的Content-Type可以查看响应数据类型
print(dic_obj)
print(type(response.json()))
fp = open('./Element/Chapter_02c_Request_Translation.json', mode='w', encoding='utf-8')
json.dump(dic_obj, fp=fp, ensure_ascii=False)       # 返回的值包含中文因此不能使用ascii码进行编码
print('Over~ ')
