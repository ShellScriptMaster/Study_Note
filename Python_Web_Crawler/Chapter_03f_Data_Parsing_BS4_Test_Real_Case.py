from bs4 import BeautifulSoup
import requests
# 爬取三国演义小说中所有的章节标题和章节内容
url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

page_response = requests.get(url=url, headers=headers)
page_response.encoding = 'utf-8'
page_text = page_response.text
page_bs4_obj = BeautifulSoup(page_text, 'lxml')
# print(page_bs4_obj.find_all(class_='book-mulu'))
book_info = page_bs4_obj.select('.book-mulu > ul > li')
print(book_info)
#
# new_url = 'https://www.shicimingju.com/' + book_info[0].a['href']
# each_chapter_response = requests.get(url=new_url, headers=headers)
# print(new_url)
# each_chapter_response.encoding = 'utf-8'
# each_chapter_webcode = each_chapter_response.text
# each_page_bs4_obj = BeautifulSoup(each_chapter_webcode, 'lxml')
# print(each_page_bs4_obj)
# print(each_page_bs4_obj.find_all(id='main_left')[0].text)

for li in book_info:
    title = li.a.text
    location = li.a['href']
    new_url = 'https://www.shicimingju.com/' + location
    each_chapter_response = requests.get(url=new_url, headers=headers)
    each_chapter_response.encoding = 'utf-8'
    each_chapter_webcode = each_chapter_response.text
    each_page_bs4_obj = BeautifulSoup(each_chapter_webcode, 'lxml')
    # details = each_page_bs4_obj.find_all(id='main_left')
    # for content in details:
    #     with open('C:/Users/shell_master/Desktop/爬虫照片/%s.txt' % title, 'w', encoding='utf-8') as fp:
    #         fp.write(content.text)

    content = each_page_bs4_obj.find(class_='chapter_content')
    with open('C:/Users/shell_master/Desktop/爬虫照片/%s.txt' % title, 'w', encoding='utf-8') as fp:
        content.encoding = 'utf-8'
        details = content.text
        remove = str(details).split('/')[0]             # 删除【NBSP】空格
        del_sapce = str(remove).replace(u'\xa0', '')    # 删除【NBSP】空格
        fp.write(del_sapce)
    print('%s 爬取下载成功!!!!' % title)







