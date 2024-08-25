import requests
import re
import threading


header ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}


def page_list_get():
    page_list = []
    home_url = "https://www.gdmuseum.com/cn/col49/list?"
    page = requests.get(home_url, header).text
    page_max_regex = '<div class=\'Pages\'>.*?(\\d*)</a></em>'
    page_num = re.findall(page_max_regex, page, re.S)
    for num in range(1, int(page_num[0]) + 1):
        url = "https://www.gdmuseum.com/cn/col49/list_%d"
        page_list.append(format(url % num))
    return page_list


img_list=[]
def img_get(page):
    website = requests.get(page, header).text
    img_regex = '<li class="li">.*?<img src="(.*?)" alt=".*?</li>'
    img_info = re.findall(img_regex, website, re.S)
    for i in img_info:
        img_req_url = "https://www.gdmuseum.com" + i
        img_list.append(img_req_url)
    return img_list


def img_download(img):
    ex = "/image/.*?/(\\d*\\..*)"
    img_name = re.findall(ex,img,re.S)
    with open('./Element/%s'%img_name[0],mode='wb') as fp:
        fp.write(requests.get(img,header).content)



threads = []
for i in page_list_get():
    threads.append(
        threading.Thread(target=img_get,args=(i,))
        )
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


threads = []
for i in img_list:
    threads.append(
        threading.Thread(target=img_download,args=(i,))
    )
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()





