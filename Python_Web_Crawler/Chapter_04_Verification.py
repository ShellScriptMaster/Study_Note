"""
    验证码识别
        图片验证    https://www.cqccms.com.cn/cqc/Captcha.jpg
            使用模块 ddddocr
                导入模块  import ddddocr
                实例化对象  ocr = ddddocr.DdddOcr()
                读取图片内容
                    with open('图片地址',mode='rb') as pic:
                        img = pic.read()
                将使用ocr 对象的classification方法 并且将图片内容作为参数传入 返回结果为识别出的验证码
                    result = ocr.classification(img)
                    print(result)
        滑块验证
        点选验证码
"""

import ddddocr
import requests

url = 'https://www.cqccms.com.cn/cqc/Captcha.jpg?rnd=0.1793780114466892'
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

response = requests.get(url,headers=headers).content
with open("./Element/Captcha.jpg",mode='wb') as fb:
    fb.write(response)

pic = open("./Element/Captcha.jpg",mode='rb')
img = pic.read()
ocr = ddddocr.DdddOcr()
result = ocr.classification(img)
