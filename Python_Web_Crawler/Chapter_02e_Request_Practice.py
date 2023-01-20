"""
    爬取肯德基餐厅查询中指定地点的餐厅数  http://www.kfc.com.cn/kfccda/storelist/index.aspx
"""
import requests
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
keyword_input = input('输入查询餐厅关键字')
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
parameters = {
    'cname': '',
    'pid': '',
    'keyword': keyword_input,
    'pageIndex': 1,
    'pageSize': '10'
}

response = requests.post(url=url, data=parameters, headers=header)
page_text = response.text
with open('Chapter_02e_Request_KFC.txt', mode='w', encoding='utf-8') as page_obj:
    page_obj.write(page_text)

print('爬取结束')

