# 装饰器
"""
内容回顾:
    1. 函数可以作为参数进行传递 funcA(func_a)
    2. 函数可以作为返回值进行返回  return funcA
    3. 函数名称可以当成变量一样进行赋值操作

装饰器:
    本质上是一个闭包函数  (外层函数返回内层函数)
    一般在登录验证、日志方面使用多
    通用装饰器写法:
        def wrapper(fn):     函数当作参数传入装饰器中
            def inner(*args, **kwargs):
                目标函数执行前执行的操作
                ret = fn(*args, **kwargs)        执行目标函数
                目标函数执行后执行的操作
                return ret                      接收target函数的返回值
            return  inner       # 把inner当作一个函数进行返回
        @wrapper
        def target():
            pass
        target() -->  inner()

    多个装饰器装饰一个目标函数执行顺序 wrapperA --> wrapperB --> target --> wrapperB --> wrapperA
"""
# 游戏开外挂


def manager(fn):
    def inner():
        print('启动外挂')
        fn()
        print('关闭外挂')
    return inner


@manager        # 启用装饰器的书写格式     --> play_dnf = manager(play_dnf)
def play_dnf():
    print('启动dnf')


@manager        # 启用装饰器的书写格式     --> play_lol = manager(play_lol)
def play_lol():
    print('启动lol')

#  装饰器原理
# play_dnf = manager(play_dnf)
# play_lol = manager(play_lol)
#


play_dnf()
print('*'*30)
play_lol()
print('*'*30, '被装饰函数的参数问题', '*'*30)

# 被装饰函数的参数问题


def manager(fn):
    def inner(*args, **kwargs):     # *和**代表接收所有参数并且打包成元组和字典
        print('启动外挂')
        fn(*args, **kwargs)         # *和**代表 把arg和kwarg打算成位置参数和关键字参数传递进去
        print('关闭外挂')
    return inner


@manager
def play_dnf(admin, passwd):
    print('我开始玩dnf了', admin, passwd)
    print('启动dnf')


@manager
def play_lol(admin, passwd, hero):
    print('我开始玩lol了', admin, passwd, hero)
    print('启动lol')


play_dnf('admin', 'passwd123')
print('*' * 30)
play_lol('admin', 'passwd123', '盖伦')
print('*' * 30, '装饰器返回值问题', '*' * 30)

# 装饰器返回值问题


def manager(fn):
    def inner(*args, **kwargs):
        print('启动外挂')
        ret = fn(*args, **kwargs)       # 用变量获取target函数的return值
        print('关闭外挂')
        return ret                      # 返回target函数执行的结果
    return inner                        # inner 通过ret的return接收了target函数的执行结果


@manager
def play_dnf(admin, passwd):
    print('我开始玩dnf了', admin, passwd)
    print('启动dnf')
    return '得到一把屠龙刀'


ret = play_dnf('admin', 'passwd123')
print(ret)

print('*' * 30, ' 一个函数被多个装饰器装饰 ', '*' * 30)
# 一个函数被多个装饰器装饰


def wrapperA(fn):
    def inner(*args, **kwargs):
        print('this is wrapper A IN')
        ret = fn(*args, **kwargs)
        print('this is wrapper A OUT')
        return ret
    return inner


def wrapperB(fn):               # fn --> target
    def inner(*args, **kwargs):
        print('this is wrapper B IN')
        ret = fn(*args, **kwargs)
        print('this is wrapper B OUT')
        return ret
    return inner

# 一个函数被2个装饰器进行装饰


@wrapperA                       # 被wrapperB装饰的target作为整体再被wrapperA装饰 target = wrapperA(wrapperB(target))
@wrapperB                       # target = wrapperB(target)  -->  target: wrapperB.inner 先被wrapperB装饰
def target():
    print('target function')


target()

