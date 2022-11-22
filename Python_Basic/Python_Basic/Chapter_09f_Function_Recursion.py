"""
    递归:
        函数自己调用自己
        如果没有任何拦截的话会成为一个死循环
        超过函数最大调用深度               # maximum recursion depth exceeded while calling a Python object
            python 默认最大递归深度位1000       一般不会递归到1000，如果出现递归超1000多数情况下是代码不合理
"""
import sys
print(sys.getrecursionlimit())      # python 默认最大递归深度位1000

# 递归函数   --> 自己调用自己
# def func():
#     print(123)
#     func()              # 每次执行此语句会产生新的内存地址, 不加限制内存会爆
#
# func()
