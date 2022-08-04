# function input()  to obtain user input content
"""
Usage
Variety_name = input('input your content')

name = input('please input your name')
age = int(input('please input your age'))
print('your name is',name,'and you are', age, 'years old')

a = int(input('please input a number'))
b = int(input('please input a number'))
print(type(a), type(b))
print('a + b =',a+b)
# To get the Sum of a and b

"""
########################################################################################################################

# Operator 运算符
# 运算符：算术运算符，赋值运算符，比较运算符，布尔运算符，位运算符
# 算术运算符：标准算术运算符，取余运算符，幂运算符
# basic Operation
print(1+1)      # 加法运算
print(1-1)      # 减法运算
print(9*9)      # 乘法运算
print(0.3333*0.02) # 浮点数  也会造成由于浮点数存储不精确的问题
print(1/2)      # 除法运算
print(11//2)    # 整除运算（取商弃余数）
print(21%2)     # 取余运算
print(2 ** 3)   # 幂运算

# advanced Operation
print(9 // 4)   # result should be 2
print(-9 // -4) # result should be 2
print(9 // -4)  # result is -3  (一正一负整除运算向下取整 -2.25向下取整得-3)
print(-9 // 4)  # result is -3  (一正一负整除运算向下取整 -2.25向下取整得-3)

print(9 % 4)   # result should be 1
print(-9 % -4) # result is -1 (一正一负整除需要公式： 余数=被除数-除数*商(向后取整)  -1 = -9 - (-4) * 2
print(-9 % 4)  # result is 3  (一正一负整除需要公式： 余数=被除数-除数*商(向后取整)  3 = -9 - 4 * (-3))
print(9 % -4)  # result is -3 (一正一负整除需要公式： 余数=被除数-除数*商(向后取整)  -3 = 9 - (-4) * (-3))
########################################################################################################################

# assignment  赋值运算符 =
# 执行顺序 右 --> 左
a = 10 + 20   # 10 + 20 = a --> invalid assignment
print(a)

# 支持链式赋值
a = b = c = 20
print(id(a),a,'\n',id(b),b,'\n',id(c),c,'\n')  #全部变量都指向同一个内存地址

# 支持参数赋值
a = 20
a += 30
print(a)  # 相当于 a = a + 30 , type(a) = Int
a -= 10
print(a)  # 相当于 a = a - 10 , type(a) = Int
a *= 2
print(a)  # 相当于 a = a * 2 , type(a) = Int
a /= 3
print(a)  # 相当于 a = a / 3 , type(a) = Float
a //= 2
print(a)  # 相当于 a = a // 2, type(a) = Float
print(type(a))
a %= 3
print(a,type(a))

# 支持系列解包赋值    需要中间变量的时候可以运用解包赋值
a,b,c = 20,30,40
print(a,b,c)
print(id(a),'\n',id(b),'\n',id(c),'\n')
a,b,c = 20,20,20
print(id(a),'\n',id(b),'\n',id(c),'\n')
a = 20
b = 20
c = 20
print(id(a),'\n',id(b),'\n',id(c),'\n')
# 交换2个变量的值
a,b = 10,20
print('before exchange',a,b)
# 交换
a,b = b,a
print('after exchange',a,b)
########################################################################################################################

# 比较运算符   运算结果是bool类型
# >,<,>=,<=,!=,==
a,b = 10,20
print(a > b)   # return False
print(a < b)   # return True
print(a <= b)  # return True
print(a >= b)  # return False
print(a == b)  # return False
print(a != b)  # return True
"""
一个 '=' 称为赋值运算符，'==' 称为比较运算符
一个变量由 标识，类型，值组成
'==' 比较的是两个变量的value
'is' 比较两个变量的标识
"""
a = 10
b = 10
print(a == b)
print(a is b)
print(id(a),'\n',id(b),'\n')  # a 与 b 标识相等
list1 = [11,22,33,44]
list2 = [11,22,33,44]
print(list1 == list2)
print(list1 is list2)
print(id(list1),'\n',id(list2))
print(a is not b)          # id_a is different from id_b
print(list1 is not list2)  # id_list1 is different from id_list2
########################################################################################################################

# 布尔运算符  对布尔值之间的运算 and, or , not , in , not in
a, b = 1, 2
# and
print(a == 1 and b == 2)  # True and True return True
print(a == 1 and b < 2)   # True and False return False
print(a != 1 and b == 2)  # False and True return False
print(a != 1 and b != 2)  # False and False return False
# or
print(a == 1 or b == 2)   # True or True return True
print(a == 1 or b != 2)   # True or False return True
print(a != 1 or b == 2)   # False or True return True
print(a != 1 or b != 2)   # False or False return False
# not  对bool 操作数进行取反
f1 = True
f2 = False
f3 = 1
f4 = 0
print(not f1)  # return False
print(not f2)  # return True
print(not f3)  # return False
print(not f4)  # return True
# in , not in
a = 'helloworld'
print('h' in a)                 # 判断a中是否包含'h'字母, return True
print('k' in a)                 # 判断a中是否包含'k'字母, return False
print('h' not in a)             # 判断a中是否不包含'h'字母, return False
print('k' not in a)             # 判断a中是否不包含'k'字母, return True
########################################################################################################################

# 位运算符  将数据转换成二进制进行计算
# 位与& 对应位数都是1，结果数位才是1，否则为0
"""
    位运算方法 &
    转换二进制 4 --> 0 1 0 0  不足位数的用0补上
    转换二进制 8 --> 1 0 0 0
    比较            0 0 0 0  对应数位均为1，数位才为1，否则为0  由于 0000 结果为0，因此输出也为0
    比较二进制每一位，对应位数都是1结果才为True/1
"""
print(4 & 8 )  # 结果为0
print(4 & 12)  # 结果为4
# 4  --> 0 1 0 0
# 12 --> 1 1 0 0
# result 0 1 0 0   --> 4

# 位或| 对应位数都是0，结果数位才为0，否则为1
"""
    位运算方法 |
    转换二进制 4 --> 0 1 0 0  不足位数的用0补上
    转换二进制 8 --> 1 0 0 0
    比较            1 1 0 0  对应数位均为0，数位才为0，否则为1  将 1100 转换成十进制数字，输出结果为12
    比较二进制每一位，对应位数都是0结果才为
"""
print(4 | 8)
print(4 | 12)
print(4 | 13)
# 4     --> 0 1 0 0
# 12    --> 1 1 0 0
# result--> 1 1 0 0  --> 12
# 13    --> 1 1 0 1
# result--> 1 1 0 1   --> 13

# 左移运算符 <<  高位溢出舍弃，低位补0    结果相当于乘2
# 4       -->     0 0 0 0 0 0 1 0 0
# 左移     -->   0 0 0 0 0 0 1 0 0
# 补零     -->   0 0 0 0 0 0 1 0 0 0   高位溢出，因此在低位补0  最后使用 1000 转换成十进制数字 为8
print(4 << 1)
# 再补一个  --> 0 0 0 0 0 0 1 0 0 0 0  相当于8乘2，结果为16
print(4 << 2)
# 右移运算符 >>  低位溢出舍弃，高位补0    结果相当于除以2
# 4       -->  0 0 0 0 0 0 1 0 0
# 右移     -->    0 0 0 0 0 0 1 0 (0)
# 补零     -->  0 0 0 0 0 0 0 1 0     低位溢出相当于舍弃溢出的位数，同时在高位补0 结果为2
print(4 >> 1)  # 相当于4/2 结果为2
print(4 >> 2)  # 相当于4/4 结果为1
print(4 >> 3)  # 此时已经将所以的位数右移  二进制中已经没有了1  结果则为0


# Priority of the Operators
# ** --> *,/,//,% --> +,- --> >>,<< --> & --> | --> >,<,>=,<=,==,!= --> and --> or --> =
# 先进行算术运算，再进行位运算，再进行比较运算，再进行布尔运算，再进行赋值，有括号先算括号


