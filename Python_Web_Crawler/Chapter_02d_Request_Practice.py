#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    爬取豆瓣电影分类排行榜中的电影详细数据 https://movie.douban.com/
    实现方式
        当滚轮拖动到底部时, 页面实现自动刷新(发生了一次ajax请求, 实现当前网页的部分刷新)
        打开F12查看网络 --> 请求URL --> 载荷(查看携带的参数) --> 查看响应头发现是json格式
"""
import json

import requests
# url = 'https://movie.douban.com/j/chart/top_list?type=22&interval_id=100%3A90&action=&start=20&limit=20' 携带了参数 可以将参数以字典形式传入, 此处省去参数
url = 'https://movie.douban.com/j/chart/top_list'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
limit = input('一次取出多少电影')
parm_dict = {
    'type': '22',
    'interval_id': '100:90',
    'action': '',
    'start': '0',       # 从第几部开始取
    'limit': limit       # 一次取出多少
}

response = requests.get(url=url, headers=headers, params=parm_dict)
json_obj = response.json()
fp = open('Chapter_02d_Request_DouBan_Movie.json', mode='w', encoding='utf-8')
json.dump(json_obj, fp=fp, ensure_ascii=False)
