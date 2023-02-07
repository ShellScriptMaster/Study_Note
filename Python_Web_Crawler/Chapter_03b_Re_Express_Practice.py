##!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
# 取python出来
key = 'javapythongoc++cphpcssvue'
a = re.findall('python', key)[0]        # findall 取出来是一个列表
print(a)

# 取hello world
key = '<html><h1>hello world<h1></html>'
b = re.findall('<h1>(.*)<h1>', key)[0]
print(b)

# 取170
key = '战老师身高只有170'
c = re.findall('\d+', key)[0]
print(c)

# 提取http:// 和 https://
key = 'http://www.baidu.com and https://boob.com'
d = re.findall('https?://', key)
print(d)

# 提取hello
key = 'lalala<hTml>hello</HtMl>hahahaha'
e = re.findall('<[hH][Tt][Mm][Ll]>(.*)</[hH][Tt][Mm][Ll]>', key)[0]
print(e)

# 提取hit.
key = 'bobo@hit.edu.com'
f = re.findall('h.*?\.', key)[0]
print(f)

# 提取sas和saas
key = 'saas and sas and saaaas'
g = re.findall('sa{1,2}s', key)
print(g)

# 提取img的来源scr
web_data_1 = """
<div class="article">
<a href="detailRelic.html?parentID=b320ac1b-29c8-4c68-a11f-dcffe58a0ad1&amp;id=9f910332-2853-4aff-9f87-04741fe4b513&amp;articleID=7fbb7b5c-3e34-4fde-8b1d-37885aa64e3c" target="_blank" class="imgbg">
<img src="/Attached/2019/10/15/24ac4e1dc02e6f7229ef7e0bbcb061f1.jpg">
<div class="title-btns">
<div class="ico-3d"></div>
</div>
</a>
<div class="title">
<div class="title-main">“V”形符号饼形金1号</div>
</div>
</div>
"""
ex = '<div class="article">.*?<img src="(.*?)">.*?</div>'
h = re.findall(ex, web_data_1, re.S)    # re.S --> 单行匹配 ; re.M --> 多行匹配
print(h)

