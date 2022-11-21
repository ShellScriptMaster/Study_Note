"""
    匿名函数 lambda
    表达式
        变量 = lambda 参数1,参数2,参数3... : return值
    作用:
        快速创建一个简单的函数
"""

def func():
    print(123456)
    return 999
ret = func()
print(ret)


def func1(a,b):
    return a + b


ret = func1(15,13)
print(ret)

fn = lambda a, b: a + b

print(fn(17, 19))
print(fn(19, 26))