# Your first code
print('hello world')
########################################################################################################################

#print a paragraph  using   """ your message  """
print("""
hello
world
,
I 
am
learning
python_coding
""")
########################################################################################################################

# print as a file
fp = open('D:/text.txt','a+')  # the drive should exsist.  use "file= ". if the file not exsist, then create one; if exsist , then append.
print('helloworld',file=fp)
fp.close()
########################################################################################################################

# Escape character
"""
Grammar  \character
example : \n \r \t \b
"""
print('hello\nworld')             # \n 回车符，将光标移到下一行开头，因此可以看到后面的'world'
print('hello\rworld')             # \r 回车符，并且将光标移到本行开头，因此看不到后面的'world'
print('hello\tworld')             # \t 水平制表符，相当于Tab键（使占满制表位）。在此处，'hell'占用了一个制表位，4个字符占一个制表位，下一个制表位为'o'和三个空格
print('helloo\tworld')            # \t 水平制表符，相当于Tab键（使占满制表位）。在此处，'hell'占用了一个制表位，4个字符占一个制表位，下一个制表位为'oo'和两个空格
print('hellooo\tworld')           # \t 水平制表符，相当于Tab键（使占满制表位）。在此处，'hell'占用了一个制表位，4个字符占一个制表位，下一个制表位为'ooo'和一个空格
print('helloooo\tworld')          # \t 水平制表符，相当于Tab键（使占满制表位）。在此处，'hell'占用了一个制表位，4个字符占一个制表位，下一个制表位为'oooo',再下一个制表位为四个空格
print('hello\bworld')             # \b 退格（backspace）。将光标移动到前一字符前，因此看不到最后的'o'
print('http:\\\\www.baidu.com')   # \\ 反斜线  能够输出单个'\'
print('I say:\'hello everyone\'') # \' 单引号
print('I say:\"hello everyone\"') # \" 双引号
print('good\
\tmorning')                       # \ 在行末使用表示一行未完，可以转到下一行继续

# Literal Character  'r' or 'R'   原字符，可使内容中的中转义字符失效。在字符串前加上r or R
print(r'hello\nworld')      # \n 失效
#   print(r'helloworld\')   使用原字符，字符串最后不能为\
########################################################################################################################

# binary system 0 1
# 8 bit = 1 byte , 1024 byte = 1 Kb , 1024 Mb = 1 Gb, 1024 Gb = 1 Tb
# UTF-8  1 bit for 1 letter, 3 bit for 1 Chinese character
# Unicode  2 bit for 1 letter or 1 Chinese charater
print(chr(0b0101010011001000))  # 0101010011001000代表了一个'哈'字，使用chr()函数输入一个二进制数字，可以得出一个字符
print(ord('哈'))                #  可以使用ord()函数查看汉字对应的十进制数字
########################################################################################################################

# Identifier and Reserved Character   标识符与保留字符
# 查看保留字符
import keyword
print(keyword.kwlist)  # 查看keyword字符
print('#'*30)
########################################################################################################################

# Variety 变量  包含了三部分：标识，类型，值
name = 'Jacky'      # define a Variety
print('name occupy the memory address',id(name))     # 查看变量的标识（所占内存的地址），使用id()函数查看
print(type(name))   # 查看变量的类型，使用type()函数查看
print(name)         # 查看变量的值
name = 'Jessica'    # redefine the Variety
print('name occupy the memory address',id(name))     # 内存空间改变，之前的内存空间变成内存垃圾
print(type(name))                                    # the type is the same as former
print(name)                                          # Value changed

# Variety type: int, long(only in py2), float, bool(boolean), complex, str
a = 98
print(type(a),a)
b = 2 ** 64
print(type(b),b)
a1 = -98
print(type(a1),a1)
b1 = 0
print(type(b1),b1)

c,c1, = 1.25, -1.25
print(type(c),c)
print(type(c1),c1)
print('1.1+2.1=',1.1+2.1,'\n')   # in this case will not occur the issue
print('1.1+1.3=',1.1+1.3)   # the answer should be 2.4, but it get wrong answer。由于浮点数存储不精确造成
from    decimal import Decimal
print('1.1+1.3=',Decimal('1.1') + Decimal('1.3'),'\n')  #using the decimal module to fix this issue

d,e = True, False  # True stand for 1 , False stand for 0
print(type(d),type(e),d,e)
print('d+1=',d+1,'\n','\be+1=',e+1, '\n')  # can use bool type to do some calculation

# complex type
i = 4 + 2j
k = 12 + 7j
print(i + k)
print(1j ** 2)
print(type(i),type(k),'\n')

# 0d stand for decimalism system
print('binary system',0b1111111)      # 0b treat the number as binary digits, and print out a decimalism number
print('octonary system', 0o176)       # 0o treat the number as octonary digits, and print out a decimalism number
# for hexadecimal, here are the base digits: 1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
print('hexadecimal system', 0x1EAF,'\n')   # 0x treat the number as hexadecimal digits, and print out a decimalism number

# String
f = 'hello, I am Jacky'
f1 = "hello, I am Jacky"
print(type(f),f)
print(type(f1),f1)   # " and ' will return a same output
f2 = """hello, \
I am Jacky
"""
print(type(f2),f2)  # use """ """ to get a multi-paragraph string to output
f3= '''hello, \
I am Jacky
'''
print(type(f3),f2)  # use ''' ''' to get a multi-paragraph string to output

# Data type Transfered
name = 'Jessica'
age = 20
print('I am '+ name + ' my age is '+ str(age))  # using str() to transfer 'int' ype into 'string'type
# change Data type to String -------------------------------------------------------
a = 10
b = 198.8
c = False
print(type(a), type(b), type(c))
print(str(a),str(b),str(c), type(str(a)),type(str(b)), type(str(c)))

# change Data type to integer -------------------------------------------------------
b = 198.8
b1 = '2000'
b2 = '21.25'
b3 = True
b4 = 'hello'
print(type(b),type(b1),type(b2),type(b3),type(b4))
print(int(b),type(int(b)))
print(int(b1),type(int(b1)))
# print(int(b2),type(int(b2)))    因为字符串为浮点数形式，因此无法转换成int格式
print(int(float(b2)),type(int(float(b2))))   # 可以使用float 将str 格式转换成浮点数类型后再对浮点数类型转换成整数格式
print(int(b3),type(int(b3)))
# print(int(b4), type(int(b4)))   字符串必须为整数格式的数字串， 否则报错

# change Data type to float -------------------------------------------------------
c = '129.98'
c1 = 75
c2 = False
c3 = '88'
c4 = 'hello'
print(type(c),type(c1),type(c2),type(c3))
print(float(c),type(float(c)))
print(float(c1),type(float(c1)))
print(float(c2), type(float(c2)))
print(float(c3),type(float(c3)))
# print(float(c4), type(float(c4)))   字符串中的数据如果是非数字串，无法转换成浮点数类型

########################################################################################################################
# 注释： 单行注释 # ; 多行注释： """ """ ; 中文编码声明注释 文件开头加上中文声明注释，用以指定源码文件的编码格式（py3后不需要指定）
