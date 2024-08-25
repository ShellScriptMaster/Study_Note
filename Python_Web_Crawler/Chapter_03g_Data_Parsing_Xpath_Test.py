"""
    Xpath解析:
        最常用并且最便捷高效
    Xpath解析原理:
        1. 实例化一个etree 对象, 并且将被解析页面源码数据加载到该对象中
        2. 调用etree对象中的xpath方法结合xpath表达式实现标签定位以及内容捕获
    Xpath 环境:
        lxml
    实例化etree对象:
        1. from lxml import etree
        2a. 将本地html文档中源码数据加载到etree对象中
            etree.parse('filePath')
        2b. 将互联网上获取的源码数据加载到该对象中
            etree.HTML('page_text')
        3. xpath('xpath表达式')
            /   : 表示从根节点开始定位
            //  : 表示多个层级,可以表示任意位置开始定位
            属性定位:
                //div[@class='song  '][tag@attrName='attrValue']
            索引定位:
                //[div@class='song']/p[3]   索引从1开始, 此处取p标签的第3个
            取文本:
                /text()                     获取标签中直系文本内容
                //text()                    获取标签中所有文本内容
            取属性:
                /@attrName                  获取属性的值
"""
from lxml import etree

tree = etree.parse('./Chapter_03f_Data_Parsing_BS4_Test_Case.html')
r1 = tree.xpath('/html')
r2 = tree.xpath('/html/head/meta')
r3 = tree.xpath('//meta')
r4 = tree.xpath('/html/head/meta/@charset')[0]
r5 = tree.xpath('//title/text()')
r6 = tree.xpath('//div')
r7 = tree.xpath('//div[@class="qingkong"]/p/text()')[0]
r8 = tree.xpath('//div[@class="song"]/p[3]/text()')[0]
r9 = tree.xpath('//div[@class="song"]/a[1]/text()')
r10 = tree.xpath('//div[@class="song"]/a[1]/@href')[0]
r11 = tree.xpath('//div[@class="song"]/a[1]/@title')[0]

var = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11]

for i in var:
    index = var.index(i) + 1
    print('r%d' % index, '=', i)








