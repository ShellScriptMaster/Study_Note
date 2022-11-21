"""
for 变量 in 可迭代：
    pass

iterable: 可迭代的东西
str, list, tuple, dict, set, open(), range()

可迭代的数据类型都会提供一个叫迭代器的东西，这个迭代器可以帮助我们把数据类型中的所有数据逐一拿到
获取迭代器的2种方案:
    1. iter()  内置函数可以直接拿到迭代器
    2. __iter__()  特殊方法
从迭代器中获取数据:
    1. next()  内置函数
    2. __next__() 特殊方法
for 里面一定是需要使用迭代器，所有不可迭代的东西不能用for循环
for 循环一定有__iter__, __next__出现

迭代器统一了所有不同数据类型的遍历工作  --> 不同数据类型有了相同的遍历方式
迭代器本身也是可迭代的内容
迭代器特性:
    1. 迭代器元素有顺序,只能向前获取数据,不能反复
    2. 特别节省内存  --> 用较少的内存遍历一个庞大的数据
    3. 惰性机制  --> 生成的迭代器只要不访问next就不会往前挪

"""

it = iter('你叫什么名字？')
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))   StopIteration 迭代已经停止了, 不能再从迭代器中拿数据了 需要重新获取迭代器

it = '呵呵哒'.__iter__()
print(it)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print('$'*30, '模拟 for 循环工作原理', '$'*30)

# 模拟 for 循环工作原理
s = '我是数据'
it = s.__iter__()
while 1:
    try:                        # 尝试运行内部代码
        data = it.__next__()
        print(data)
    except StopIteration:       # 如果出现 StopIteration 报错
        break                   # 停止


s = '你好我叫赛利亚'
it = s.__iter__()               # 迭代器本身也是可迭代的内容
for i in it:
    print(i)
