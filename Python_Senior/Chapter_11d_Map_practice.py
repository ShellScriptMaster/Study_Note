"""
模拟VS_FTP工作流程
    1. 连接服务器
    2. 登录账户
    3. 下载文件
    4. 上传文件
    5. 断开连接
"""


class VS_FTP(object):
    def __init__(self, server_name, username, passwd, file_name):
        self.server_name = server_name
        self.username = username
        self.passwd = passwd
        self.file_name = file_name

    def connect(self):
        print('connecting Server %s' % self.server_name)

    def login(self):
        print('login your account \n username %s;\n password %s' % (self.username,self.passwd ))

    def download(self):
        print('download file %s' % self.file_name)

    def upload(self):
        print('upload file %s' % self.file_name)

    def disconnect(self):
        print('disconnect')
        exit()


test1 = VS_FTP('192.168.4.8', 'root', '123', '/opt/firco/conf')
while 1:
    user_cmd = input('>>').strip()
    if hasattr(test1, user_cmd):
        execute = getattr(test1, user_cmd)
        execute()
    else:
        print('there is no such cmd')

