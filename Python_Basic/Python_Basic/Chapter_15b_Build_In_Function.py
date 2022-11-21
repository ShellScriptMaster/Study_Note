"""
    内置函数:
        迭代器:
            range   生成一个序列
            next    迭代器往前遍历一次
            iter    生成一个迭代器
        相关内置函数:
            zip     把多个可迭代内容进行合并成一个新的可迭代对象
        作用域相关:
            locals  以字典的形式返回当前位置的全部局部变量
            globals 以字典形式返回全部全局变量
        字符串类型代码的执行:
            eval        执行字符串类型的代码，并且返回最终结果
            exec        执行字符串类型的代码
            complie     将一个字符串编译为字节代码
"""

# zip  列表中相同index的都放一起
lst1 = ['Jimmy', 'alex', 'sean']
lst2 = [28, 29, 33]
lst3 = ['运维', '开发', 'PM']
# result = []
# for i in range(len(lst1)):
#     result.append((lst1[i], lst2[i], lst3[i]))
# print(result)
result = zip(lst1, lst2, lst3)
print(dir(result))
# for item in result:
#     print(item)
print(list(result))
print('*' * 30, 'locals & globals', '*' * 30)

# locals globals
a = 188
print(locals())     # 此时locals写在全局作用域范围内，显示全局作用域的内容
print(globals())
def func1():
    a = 336
    print(locals()) # 此时locals放在局部作用域范围内 显示的是局部作用域的内容

func1()