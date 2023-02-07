import re
import requests

page_start = int(input('你想从第几页开始爬取图片？'))
page_end = int(input('你想爬取到第几页？'))+1

page_range = range(page_start, page_end, 1)
for page_num in page_range:
    url = 'https://www.gdmuseum.com/cn/col49/list_%d?'%page_num
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    web_code = requests.get(url=url, headers=headers).text
    ex = '<li class="li">.*?<img src="(.*?)" alt=.*?</li>'
    images_list = re.findall(ex, web_code, re.S)
    for image_item in images_list:
        image_url = 'https://www.gdmuseum.com%s'%image_item
        image_name = image_item.split('/')[-1]
        image_response = requests.get(url=image_url, headers=headers).content
        with open('C:/Users/shell_master/Desktop/爬虫照片/%s'%image_name,'wb') as fp:
            fp.write(image_response)
            print(image_name, '爬取成功!!!!')

