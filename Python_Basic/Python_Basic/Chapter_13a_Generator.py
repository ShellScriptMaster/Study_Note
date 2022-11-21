"""
生成器
    本质上是一个迭代器

    创建生成器的方式:
        1. 生成器函数  yield
            生成器函数执行的时候并不会执行函数,而是得到生成器
            yield作用:            只要函数中出现了yield,它就是一个生成器函数
                1. 可以返回数据
                2. 可以分段执行函数中的内容，通过__next__()执行到下一个yield的位置
                3. 可以节省内存
        2. 生成器表达式
            (数据 for循环 if判断)


"""


def func1():
    print(123456)
    return 999


ret = func1()
print('func1 return is ', ret)
print('*'*30, '生成器case', '*'*30)


def func2():
    print(123456)
    yield 999


ret = func2()
# print('func1 yield is ', ret)  # 并不会执行函数而是直接print出 生成器
print(ret.__next__())            # yield 也有返回的含义，只有当执行__next__()的时候才会返回yield部分
print('*'*30, 'yield', '*'*30)


def func3():
    print(123)
    yield 666
    print(456)
    yield 999
ret = func3()
print(ret.__next__())       # 执行第一个yield前的函数
print(ret.__next__())       # 执行第二个yield前的函数

print('*'*30, 'yield使用情况', '*'*30)
# 订购10000件衣服   --> 需要分批消化
# def order():
#     lst = []
#     for i in range(10000):
#         lst.append('衣服%s' % i)      # 消耗内存
#     return lst
#
# lst = order()
# print(lst)

def order():
    lst = []
    for i in range(10000):
        lst.append('衣服%s' % i)
        if len(lst) == 50:      # 分批每50件衣服出一次货
            yield lst
            # 下一次拿数据
            lst = []            # 下一次拿衣服应该重新开始装50件

gen = order()
print(gen)
print(gen.__next__())
print(gen.__next__())


