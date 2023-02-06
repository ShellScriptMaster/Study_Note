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


