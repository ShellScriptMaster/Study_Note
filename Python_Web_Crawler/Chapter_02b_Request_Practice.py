#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    反爬机制:
        UA伪装
            UA --> User-Agent (请求载体的身份标识)
            让爬虫对应请求载体身份标识伪装成某一款浏览器
        UA检测:
            门户网站的服务器回检测对应请求载体的身份标识, 如果检测到身份标识为某一款浏览器就证明该请求是正常访问
            但是如果检测到请求载体的身份标识不是某一款浏览器证明该请求为不正常请求(爬虫), 服务器有可能拒绝该请求
"""
# 爬取搜狗指定词条对应的搜索结果页面(简易的网页采集器)
import requests
url = 'https://www.sogou.com/web'   # 'https://www.sogou.com/web?query=kubernetes'

# 处理 url 携带的参数 --> 可以封装到字典中
keyword_searching = input('please input a keyword')
# 进行UA伪装
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36' # 抓包工具中获取
}

parm = {
    'query': keyword_searching
}
# 对指定url发起的请求对应的url是携带参数的，并且通过requests.get()在请求过程中处理了参数
response = requests.get(url=url, params=parm, headers=headers)
page_text = response.text
file_name = 'Chapter_02b_Request_'+keyword_searching+'.html'
with open(file_name, mode='w', encoding='utf-8') as result:
    result.write(page_text)
print(file_name, '保存成功')
