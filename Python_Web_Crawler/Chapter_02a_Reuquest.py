#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    网络请求模块
        urllib 模块
        Requests 模块  (最常用)
    Requests模块
        Python 原生的一款基于网络请求的模块, 简单便捷, 效率高
        作用:
            模拟浏览器发送请求
        如何使用:
            安装Requests模块
                File --> Setting --> Project --> + --> 搜索 'requests' --> 安装
            import 模块(request 模块编码流程)
                指定url
                发起请求  get/post
                获取相应数据
                数据持久化/保存数据
        实战案例:
            1. 爬取搜狗指定词条对应的搜索结果页面(简易的网页采集器)
            2. 破解百度翻译
            3. 爬取豆瓣电影分类排行榜中的电影详情数据 https://movie.douban.com/
            4. 爬取肯德基餐厅查询中指定地点的餐厅数  https://www.kfc.com.cn/kfccda/index.aspx
            5. 爬取国家药品监督管理总局中基于中华人民共和国化妆品生产许可证相关数据
"""
# 需求: 爬取搜狗首页的页面数据
import requests
import os
url = 'https://www.sogou.com/'
response = requests.get(url=url)
page_text = response.text
print(page_text)

if not os.path.exists('./Element'):
    os.mkdir('./Element')

with open('./Element/Chapter_02_Request_Sogou.html', mode='w', encoding='utf-8') as page:
    page.write(page_text)
print('爬取数据结束')

