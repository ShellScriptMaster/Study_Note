# 装饰器实战
"""
员工信息管理系统
    登录验证后再进行操作
    增、删、改、查
    登录成功后需要保留登录成功状态
    登录次数最多3次，超过3次则程序自动退出
"""
login_status = False

def login_verify(target):
    def inner(*args, **kwargs):
        global login_status
        if login_status == False:
            a = 0
            while a < 3:
                username = input('input your username:')
                passwd = input('input your passwd:')
                if username == 'admin' and passwd == '123':
                    print('login successfully')
                    login_status = True
                    break
                else:
                    print('login failed')
                    a += 1
            else:
                print('登录次数太多，请稍后再试')
                exit()
        ret = target(*args, **kwargs)
        return ret
    return inner

@login_verify
def insert(name):
    print('添加员工信息', name)

@login_verify
def delete(name):
    print('删除员工信息', name)

@login_verify
def update(name):
    print('修改员工信息', name)

@login_verify
def select(name):
    print('查询员工信息', name)


insert('admin')
delete('admin')
update('admin')
select('admin')