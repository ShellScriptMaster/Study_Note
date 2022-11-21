# 闭包函数  Closure_Function
"""
闭包:  (内层函数对外层函数局部变量的使用，此时内层函数被称为闭包函数)
    可以使一个变量常驻余于内存中(可以做计数器效果)
    可以在全局使用局部变量并且避免变量被修改(保护变量)
"""
# 闭包函数结构


def func1():
    a = 10

    def inner():
        print(a)
        return a            # 需要确保a这个变量一致都能被访问，所以常驻内存中
    return inner


def func2():
    a = 10

    def inner():
        nonlocal a
        a += 1
        return a
    return inner


ret = func2()
ret()
ret()
ret()
print(ret())