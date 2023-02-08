"""
使用 bs4 进行数据解析
    数据解析原理:
        - 标签定位
        - 提取标签、标签属性中存储的数据值
    bs4数据解析的原理:
        - 实例化一个BeautifulSoup对象, 并且将网页源码数据加载到该对象中
        - 通过调用BeautifulSoup对象中相关的属性或者方法进行标签定位和数据提取
    环境准备:
        - bs4
        - bs4解析器
            python标准库             Python内置标准库,执行速度适中,文档容错能力强
            ** lxml HTML            速度快,文档容错能力强
            lxml XML                速度快,唯一支持XML解析器
            html5lib                最好的容错性,以浏览器方式解析文档,生成Html5文档
    实例化BeautifulSoup
        - from bs4 import BeautifulSoup
          BeautifulSoup(被解析对象, '解析器')
        - 对象的实例化
            - 将本地的html文档中的数据加载到该对象中
            - 将互联网上获取的页面源码加载到该对象中
    BeautifulSoup提供的方法和属性
        - bs4_obj.tagName
        - bs4_obj.find(‘tag_Name', class_/id/attr='properties_name')
        - bs4_obj.find_all('tag_Name')
        - bs4_obj.select('某种选择器(id/class/标签...选择器)') 返回一个列表
            - 层级选择器:
                - bs4_obj.select('.某个标签的属性值 > 下一层级A > 下一层级B > 最底层标签C')[n]  选择了某个属性的标签 底下的标签A 底下的标签B 最底层标签C 的所有内容返回的一个列表的 第n号元素
                - bs4_obj.select('.某个标签的属性值 > 下一层级  最底层标签')[n]    空格表示多个层级, > 表示一个层级
            - 获取标签中的文本数据
                - bs4_obj.定位标签方法.get_text()     可以获取某个标签中所有的文本内容
                - bs4_obj.定位标签方法.text           可以获取某个标签中所有的文本内容
                - bs4_obj.定位标签方法.string         只能够获取该标签下直系的文本内容
                - bs4_obj.定位标签方法.gettext        只能够获取该标签下直系的文本内容
        - 获取标签中的属性值
                - bs4_obj.定位标签方法['属性名']

"""
from bs4 import BeautifulSoup
web_obj_local = open('./Chapter_03f_Data_Parsing_BS4_Test_Case.html', 'r', encoding='utf-8')
web_obj_bs4 = BeautifulSoup(web_obj_local, 'lxml')
print('%s bs4_obj.tag_Name %s' % ('*'*30, '*'*30))
# print(web_obj_bs4)
# BeautifulSoup 提供的方法和属性

# bs4_obj.tag_Name  返回的是html文件中第一次出现的tagName标签内容
print(web_obj_bs4.meta)
print(web_obj_bs4.div)
print('%s bs4_obj.find() %s' % ('*'*30, '*'*30))

# bs4_obj.find()  查找输入的标签的内容 返回第一个符合要求的标签内容
print(web_obj_bs4.find('meta'))
# bs4_obj.find('标签名', class_/id/attr='html中标签属性的名称')  定位标签功能
print(web_obj_bs4.find('div', class_='song'))
print('%s web_obj_bs4.find_all() %s' % ('*'*30, '*'*30))

# bs4_obj.findall('tag_Name')  返回符合要求的所有标签(列表)
print(web_obj_bs4.find_all('div'))
print('%s web_obj_bs4.select() %s' % ('*'*30, '*'*30))

# bs4_obj.select('selector')   选择器
print(web_obj_bs4.select('.tang > ul > li > a')[0])  # 层级选择器 选择了属性为tang的标签底下ul标签底下li标签底下a标签的所有内容 返回的一个列表的第0号元素
print(web_obj_bs4.select('.tang > ul  a')[0])     # 空格表示多个层级, > 表示一个层级
print('%s 获取标签中的文本数据 %s' % ('*'*30, '*'*30))
# 获取标签内的文本数据
print(web_obj_bs4.select('.tang a')[0].get_text())  # 获取标签内的文本数据  可以获取某个标签中所有的文本内容
print(web_obj_bs4.select('.tang a')[0].text)        # 获取标签内的文本数据  可以获取某个标签中所有的文本内容
print(web_obj_bs4.select('.tang a')[1].string)      # 获取标签内的文本数据  只能够获取该标签下直系的文本内容

print(web_obj_bs4.div.get_text())                   # 获取标签内的文本数据  可以获取某个标签中所有的文本内容
print(web_obj_bs4.div.text)                         # 获取标签内的文本数据  可以获取某个标签中所有的文本内容
print(web_obj_bs4.div.string)                       # 获取标签内的文本数据  只能够获取该标签下直系的文本内容
print(web_obj_bs4.div.gettext)                      # 获取标签内的文本数据  只能够获取该标签下直系的文本内容
print('%s 获取标签中的属性值 %s' % ('*'*30, '*'*30))

print(web_obj_bs4.meta['charset'])
print(web_obj_bs4.find('div')['class'])
print(web_obj_bs4.select('.tang a')[0]['title'])
