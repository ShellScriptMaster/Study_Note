import requests
import urllib.parse
from lxml import etree
"""
    爬取贝壳上广州二手房房源信息
    步骤:
        1. 获取网址: https://gz.ke.com/ershoufang/pg1rs/           注意url转码问题 urllib.parse.quote(被转码内容)
        2. 请求获取网站源码
        3. 实例化etree
        4. xpath解析
        5. 持久化
        
"""
search_parm = urllib.parse.quote('白云')
headers = {
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
for i in range(1, 20):
    url = 'https://gz.ke.com/ershoufang/pg%drs%s/' % (i,search_parm)
    page_response = requests.get(url=url, headers=headers).text

    tree = etree.HTML(page_response)
    li_list = tree.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[4]/ul[1]//li')
    for li in li_list:
        if len(li) > 1:
            house_title = li.xpath('./div[1]/div[1]/a/@title')
            house_price = li.xpath('./div[1]/div[2]/div[5]/div[1]/span/text()')
            print(house_title, '\t\t', '总价', house_price, '万')
        else:
            pass





# house_intro = tree.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[4]/ul/li/div[1]/div[1]/a/@title')[0].strip()
# house_price = tree.xpath('//*[@id="beike"]/div[1]/div[@class="content "]/div[@class="leftContent"]/div[@data-component="list"]/ul/li/div[1]/div[2]/div[5]/div[1]/span/text()')[0].strip()
# print(house_intro, '\t\t', '总价', house_price, '万')
