# Function Create and calling
"""
    函数就是执行特定任务以完成特定功能的一段代码
    为什么需要函数
        复用代码
        隐藏实现细节
        提高可维护性
        提高可读性便于调试、
    函数创建
        def 函数名 ([参数])：
            函数体
            [return xxx]
"""
# 创建函数
def calc(a,b):          # 形参
    c = a + b
    return c
result = calc(10,20)    # 实参
print(result)
########################################################################################################################

# 函数的参数传递 (位置实参 & 关键字实参)
# 位置实参传递
def calc(a,b):
    c = a + b
    return c,a,b
result = calc(10,20)        # 默认是按照形参的顺序进行代入
print(result)
# 使用关键字进行实参传递
def calc(a,b):
    c = a + b
    return c,a,b
result = calc(b=20,a=60)    # 指定形参实际的值
print(result)

# 可变对象与不可变对象传参前后变化
def fun(arg1,arg2):
    print('arg1 = ',arg1)
    print('arg2 = ',arg2)
    arg1 = 100               # 对函数内的arg1进行改值，arg1 的Mem_id 发生改变
    arg2.append(10)          # 相当于对列表进行了追加，但是arg2的Mem_id不发生改变
    print('arg1 = ',arg1)
    print('arg2 = ',arg2)
    return True
n1 = 11
n2 = [22,33,44]
fun(n1,n2)                   # 这里是输出原来的Mem_id，输出原来的Mem_id后得到原来的int
print(n1,n2)                 # 这里是输出原来的Mem_id，输出原来的Mem_id后得到新的列表
# 函数内，不可变对象在函数内修改值后依旧返回不可变对象原来的值，因为不可变
# 函数内，可变对象在函数内修改值后返回修改后的值，因为可变
########################################################################################################################

# 函数返回值
def fun(num):
    odd=[]
    even=[]
    for i in num:
        if i % 2 :          # 如果i是奇数，与2的余数位1，bool为True
            odd.append(i)
        else:               # 如果i是偶数，与2的余数为0, bool为False
            even.append(i)
    return odd,even         # 如果函数不需要提供数据的话可以不写return
a =list(range(0,134,7))
print(fun(a))               # 函数返回值为多个的时候，返回一个元组； 如果函数返回值为一个值时，返回对应的类型

def fun2():
    return 'hello','world'  # 返回得到一个tuple
print(fun2())

def fun3():
    return  'hello'         # 返回得到一个str
print(fun3())

def fun4():
    return bool(0)
print(fun4())
########################################################################################################################

# 函数参数定义
# 函数定义默认值参数  函数定义时，可以给形参设置默认值，实参!=形参默认值，传递实参
def fun5(a,b=10,c=0):
    print(a,b,c)
    return 0
fun5(100,500)       # 默认b=10,但此时b=500,因此传递实参,c没有实参，所以默认输出0
fun5(100)           # 默认b=10，c=0,因此只需要更改a=100就ok
fun5(2,c=100)       # 默认b=10，c=0,此处指定更改了c的值，因此b按照默认值输出

# 个数可变的位置参数
"""
    定义函数的时候可能无法事先确定传递的位置参数的个数，使用可变的位置参数
    使用*定义个数可变的位置形参
    结果返回为一个元组
"""
def fun6(*agr):             # 使用*agr时，agr被当作是个元组
    print(agr)
    print(agr[0])
fun6(10)
fun6(10,20,30,4,0.9)

# 个数可变的关键字参数
"""
    定义函数的时候可能无法事先确定传递的关键字实参的个数，可以使用可变关键字形参
    使用**定义个数可变的关键字形参
    结果为一个字典 
"""
def fun7(**agr):                # 使用**agr 作为关键字参数的形参，最终返回的**agr是一个字典
    print(agr)
fun7(a=10)
fun7(a=10,b=20,c=30,agrs=99)
print()

def fun8(a,b,c):
    print('a = ',a)
    print('b = ',b)
    print('c = ',c)
fun8(10,20,30)
alst = [1,2,3]
fun8(*alst)                     # 函数调用时，将列表每个元素都按照位置进行传入

def fun9(a=100,b=300,c=500):
    print('a = ',a)
    print('b = ',b)
    print('c = ',c)
fun9()
a = {'a':30,'c':9,'b':20}
fun9(**a)                       # 函数调用时，将字典中每个键值对转换成关键字实参

def fun10(a,b=10):
    pass

def fun11(*args):
    return args

def fun12(**args):
    pass

def fun13(a,b,c,d):
    print('a = ',a)
    print('b = ',b)
    print('c = ',c)
    print('d = ',d)

print(fun11(20,30,415,3.14,15926))
fun13(10,20,30,40)
fun13(a=10,c=9.0,d=3.14,b=2)
fun13(10,20,c=20,d=40)
"""
    对于 fun13, c,d只能采用关键字实参传递
"""
def fun13(a,b,*,c,d):           # *后面的参数只能使用关键字参数传参
    print('a = ',a)
    print('b = ',b)
    print('c = ',c)
    print('d = ',d)
fun13(13,20,c=10,d=0)           # c,d只能够使用关键字传参  --> 只能写c=?,d=?

def fun14(a,b,*,c,d,**args):
    print('a = ',a)
    print('b = ',b)
    print('c = ',c)
    print('d = ',d)

def fun15(*args,**args1):           # 数量可变位置参数 与 数量可变的形参
    pass

def fun16(a,b=10,*args,**args1):    # 固定位置参数，默认值参数，数量可变位置参数 与 数量可变的形参
    pass
########################################################################################################################

# 变量作用域
"""
    程序代码能访问该变量的区域
    根据变量有效范围可分为：
        局部变量(离开函数就失效)
        全局变量(可以作用在函数外)
"""
def fun17(a,b):
    c = a + b       # c只作用在函数内，函数外不能使用未定义的c
    print(c)

f = 10              # 全局变量
g = 11              # 全局变量
def fun18(f,g):
    print(f,g)
fun18(f,g)
print(f,g)

def fun19():
    global age                  # 使用global 声明可以使变量变成全局变量
    age = 20
    print('age = ',age)
fun19()
print('out of function age = ', age)
########################################################################################################################

# 递归函数
"""
    如果一个函数的函数体调用了该函数本身，称为递归函数
    递归组成部分
        递归调用与递归终止条件
    递归调用过程
        每递归调用一次函数，都会在栈内存分配一个栈帧
        每执行完一次函数，都会释放相应的空间
    递归特点
        占用内存多，效率低
        思路与代码简单
"""
# 使用递归计算阶乘
def fac(n):
    if n == 1:
        return 1
    else:
        result =  n * fac(n-1)
    return result

print(fac(6))
"""
    n=6, --> else result = 6 * fac(6-1)
       fac(6-1) = fac(5) = 5 * fac(5-1)
       
    n=5, --> else result = 5 * fac(5-1)
       fac(5-1) = fac(4) = 4 * fac(4-1)
       
    n=4, --> else result = 4 * fac(4-1)
       fac(4-1) = fac(3) = 3 * fac(3-1)
       
    n=3, --> else result = 3 * fac(3-1)
       fac(3-1) = fac(2) = 2 * fac(2-1)
       
    n=2, --> else result = 2 * fac(2-1)
       fac(2-1) = fac(1) = 1
       
    6 * 5 * 4 * 3 * 2 * 1
"""

# 斐波那契数列            1 1 2 3 5 8 后一项为前两项之和
def f_b(n):
    if n == 1:
        return 1
    elif n == 2 :
        return 1
    else:
        result = f_b(n-1) + f_b(n-2)
        return result
print(f_b(10))



