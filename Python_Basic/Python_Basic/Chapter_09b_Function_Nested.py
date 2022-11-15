# 函数嵌套  Nested
# 函数内嵌套函数
def func1():
    b = 20
    def func_1_nested():
        print(b)
    func_1_nested()     # 在func1内调用func_1_nested


func1()
print('#' * 60, '嵌套函数执行顺序', '#' * 60)

# 嵌套函数执行顺序


def func_1():
    print(123)                     # step 1
    def func_2():
        print(456)                 # step 3
        def func_3():
            print(789)             # step 5
        print(1)                   # step 4
        func_3()                   # call func3
        print(2)                   # step 6
    print(3)                       # step 2
    func_2()                       # call func2
    print(4)                       # step 7


func_1()
print('*' * 60, '函数内部变量调用方法', '*' * 60)

# 函数内部变量/函数/参数调用方法


def func4():
    b = 20
    return b


b1 = func4()
print(b1)
print('*' * 60, '返回值为函数', '*' * 60)


def func5():
    def inner():
        print(123)
    return inner    # 执行func5会返回inner函数, 把函数当作变量进行返回


b1 = func5()
b1()               # 直接调用inner()  b1 = inner  --> b1() = inner()
print(b1)           # 此处显示b1是一个函数，是func5内部的inner函数
"""
def func5():
    def inner():
        print(123)
    return inner()    返回函数执行结果
b1 = func5()
b1                    此处不能加(),直接会执行inner函数   b1 = inner()
"""
print('*' * 60, '设计模式-->代理模式', '*' * 60)


def func6(a):
    print(a)
    a()                 # 把本身函数的参数作为函数进行执行


def target():
    print('我是target')


func6(target)       # 把函数当作参数传入函数中

print('*' * 60, 'global & nonlocal', '*' * 60)

num = 10


def func7():
    num = 30            # 此处只是创建了一个局部变量


func7()
print(num)              # 输出依旧是全局变量的num = 10


def func8():
    global num          # 使用关键字global将全局变量引入到函数中
    num = 90            # 重新对全局变量进行定义


func8()
print(num)


def func9():
    num9 = 10

    def func10():
        nonlocal num9       # 此时可以对上层函数的变量进行修改(可以返回上面多层函数), python2.7没有nonlocal这个关键字
        num9 = 90
    func10()
    print(num9)


func9()

