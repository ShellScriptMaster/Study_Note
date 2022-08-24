# 字符串驻留机制
"""
    字符串是py的基本数据类型，是一个不可变的字符序列
    字符串驻留机制
        仅保存一份相同且不可变字符串的方法，不同值被存放在字符串的驻留池中
        对相同字符串只保留一份拷贝，后续创建相同字符串的时候不会开辟新空间，而是将字符串的ID赋给新创建的变量
        需要值相同的字符串可以直接从字符串池里面拿来使用，避免频繁创建或销毁，节约内存
        字符串拼接的过程中建议使用str.join方法而非 + 连接
            join()方法计算出字符串长度然后拷贝
            只创建一次对象，效率高于 + 连接
"""
a = 'python'
b = "python"
c = """python"""
print(id(a),'\n',id(b),'\n',id(c))          # 所有的变量指向了同一个内存地址，不会另外开辟新的内存地址

"""
    驻留机制的几种情况（交互模式）
        字符串长度为0或1  (交互模式下，字符串长度为0或为1的时候才符合驻留机制)     
            符合驻留机制
                a = '%'
                b = '%'
                a is b  --> True   符合字符串长度小于或等于1
                a = ''
                b = ""
                a is b --> True
            不符合驻留机制
                a = 'abc%'         不符合标识符,且长度大于1
                b = 'abc%'         不符合标识符
                a == b --> True
                a is b --> False
        符合标识符的字符串 (数字字母下划线)
            符合驻留机制
                a = 'abc_'
                b = 'abc_'
                a == b --> True
                a is b --> True    符合标识符
        字符串只在编译时驻留而非运行时
                a = 'abc'
                b = 'ab' + 'c'
                c = ''.join(['ab','c'])
                a == b --> True
                a == c --> True
                a is b --> True     在运行前就已经将2个字符串连接起来了
                a is c --> False    需要执行join的方法则意味需要编译器处理，此时需要划分一个空间进行join的操作结果
        [-5,256]之间的整数
                a = -6
                b = -6
                a == b --> True 
                a is b --> False
    可以导入sys模块，使用sys的intern方法强制2个字符指向同一个对象
        import sys
        a = -6
        b = -6
        a is b --> False            
        a = sys.intern(b)
        a is b --> True
    Pycharm 对字符串进行了优化处理 --> 原本不驻留的变成了驻留            
"""
a = 'abc%'
b = 'abc%'
print(a is b )          # 原本不驻留的变成了驻留
########################################################################################################################

# 字符串常用操作
# 查询方法
"""
    index()     查找substr第一次出现的位置，如果查找substr不存在返回ValueError
    rindex()    查找substr最后一次出现的位置，如果查找substr不存在返回ValueError
    find()      查找substr第一次出现的位置，如果substr不存在返回-1
    rfind()     查找substr最后一次出现的位置，如果substr不存在返回-1
"""
a = 'hello,hello'
print(a.index('lo'))    # 返回第一次出现的位置
print(a.find('lo'))     # 返回第一次一次出现的位置
print(a.find('z'))      # 查找不存在的字符返回-1
print(a.rindex('lo'))   # 返回最后一次出现的位置
print(a.rfind('lo'))    # 返回最后一次出现的位置
print(a.rfind('z'))     # 查找不存在的字符返回-1
########################################################################################################################

# 字符串大小写转换
"""
    upper()         将字符串中所有的字符都转换成大写字母
    lower()         将字符串中所有的字符都转换成小写字母
    swapcase()      将字符串中大写的字母转换成小写，小写转换成大写
    capitalize()    将第一个字符转换成大写，将其余字符转换成小写
    title()         将每一个单词的第一个字符转换成大写，将每个单词的剩余字符转换成小写
"""
s = 'hello,python'
print('original is :',s,id(s))
a = s.upper()           # 转换成大写后会产生新的字符串对象
print(a,id(a))
b = a.lower()           # 转换成小写会产生新的字符串对象
print(b,id(b))
print(b == s)
print(b is s)           # 与原来小写的字符串不为同一对象

s1 = 'hello, Python'
print(s1.swapcase())        # 大写变小写，小写变大写
print(s1.capitalize())      # 将字符串的首字母大写
print(s1.title())           # 将字符串每个单词字母大写了
########################################################################################################################

# 字符串内容对齐的操作方法
"""
    center()            居中对齐，第一个参数指定宽度，第二个参数指定填充符(可选，默认是Space)，如果设置宽度小于实际宽度则返回原字符串
    ljust()             左对齐，第一个参数指定宽度，第二个参数指定填充符(可选，默认是Space)，如果设置宽度小于实际宽度则返回原字符串
    rjust()             右对齐，第一个参数指定宽度，第二个参数指定填充符(可选，默认是Space)，如果设置宽度小于实际宽度则返回原字符串
    zfill()             右对齐且左边以0填充，此方法只接收用于指定字符串宽度的参数，如果指定宽度小于等于字符串宽度则返回原字符串
"""
s = 'hello,Python'
print(s.center(20,'*'))         # 字符串长度为20，填充符为'*'
s1 = 'hello,Python.'
print(s1.center(20,'-'))
print(s.ljust(20,'-'))          # 左对齐，空位用'-'填充
print(s.rjust(20,'-'))          # 右对齐，空位用'-'填充
print(s.zfill(20))              # 相当于 print(s.rjust(20,'0'))
print(s.zfill(2))
print('-29'.zfill(8))           # 如果字符串是负数形式的字符串，则会在'-'后添0
print('--h'.zfill(8))            # 字符串最左有'-'时，会在首个'-'与字符串之间补0
########################################################################################################################

# 字符串的分割操作方法
"""
    split()     
        从字符串的左边开始分割，默认分割字符是空格，返回值是一个列表
        可以通过sep参数指定分割符
        通过参数maxsplit可以指定字符串最大分割次数。如果经历了最大分割次数后剩余的substr会单独作为一部分
    rsplit() 
        从字符串右边开始分割，默认分割字符是空格，返回值是一个列表
        可以通过sep参数指定分割符
        通过参数maxsplit可以指定字符串最大分割次数。如果经历了最大分割次数后剩余的substr会单独作为一部分
"""
a = '2022/08/24 Jacky Windows hello,Python need to earn money'
print(a.split())                            # 以空格作为分割
print(a.split(sep='/'))                     # 以'/'作为分割符
print(a.split(sep=' ',maxsplit=4))          # 以空格作为分割符，并且只切分4次，得到了5个substr

alst = a.split(sep=' ',maxsplit=4)          # 最后得出一个列表
print(alst[1:3])

print(a.rsplit())
print(a.rsplit(sep='/'))
print(a.rsplit(sep=' ',maxsplit=4))         # 字符串从右往左进行分割
########################################################################################################################

# 判断字符串的操作
a.isalnum()
"""
    isidentifier()          判断指定字符串是不是合法标识符     字母数字下划线
    isspace()               判断指定字符串是否全部由空白字符组成(回车，换行，水平制表符，空格)
    isalpha()               判断指定的字符串是否全部由字母组成
    isdecimal()             判断指定字符串是否全部由十进制数字组成
    isnumeric()             判断指定字符串是否全部由数字组成
    isalnum()               判断指定字符串是否全部由字母或数字组成
"""
a = 'hello,python'
print('1',a.isidentifier())                     # false
print('2','hello'.isidentifier())               # True
print('3','晚上好'.isidentifier())               # True
print('4','晚上好_333abc'.isidentifier())        # True

print('5','\t'.isspace())                       # \t属于空白字符
print('6',''.isspace())                         # 空字符串不属于空白字符，因为没有字符
print('7','abc'.isalpha())                      # True
print('8','张三'.isalpha())                      # True,中文可以视为alpha字符
print('9','张三1'.isalpha())                     # 数字不属于alpha
print('9+1','Ⅰ'.isalpha())                      # Ⅰ属于数字

print('10','123'.isdecimal())                   # True
print('11','Ⅰ'.isdecimal())                     # 罗马数字属于数字
print('11+1','123456789A'.isdecimal())          # 不识别十六进制

print('12','1231231'.isnumeric())               # True
print('13','0101'.isnumeric())                  # True,视为十进制数
print('14','123四'.isnumeric())                  # True,中文数字也视为数字
print('15','Ⅰ'.isnumeric())                     # 罗马数字视为数字
print('16','A'.isnumeric())                      # 不识别十六进制

print('17','abc5641'.isalnum())                  # True
print('18','123四'.isalnum())                    # True,中文四视为数字
print('19','!123'.isalnum())                     # '!'不属于数字或字母
########################################################################################################################

# 字符串替换与合并
"""
    replace()           第一个参数指定被替换的字符，第二个参数指定参与替代的字符串，[第三个参数指定最大替换次数]，该方法不会影响最初的字符串
    join()              将列表或元组的字符串合并为一个字符串
"""
a1 = 'hello,python'
print(a1.replace('python','Shell'))
print(a1.replace('l','123'))                    # 不指定次数会将所有的符合参数一的地方全部替换为参数二
a2 = 'hello,python,python,python'
shell_2 = a2.replace('python','Shell',2)        # 只替换2次
print(shell_2)
print(id(a2),'\n',id(shell_2))                  # 内存ID不同

blst = ['Shell','Python','Java','Golang']
print(blst)
print('/'.join(blst))                           # 将列表内的元素分割开然后与'/'连接
print(''.join(blst))                            # 指定的字符串为空，因此单纯将列表内所有的元素连接起来

ctupl = ('Shell','Python','Java','Golang')
print(ctupl)
print('/'.join(ctupl))                          # 将元组内的每个元素分割开然后与'/'连接
print('*'.join('python'))                       # 将字符串内每个元素分割开然后与'*'连接
########################################################################################################################

# 字符串的比较
"""
    运算符：> >= < <= == !=
    比较规则：
        首先比较字符串第一个字符，如果相同则依次比较后续的字符直至两个字符串的字符不相等，后续字符则不会再进行比较  
    比较原理：
        2个字符以上进行比较时，比较的是ordinal value(原始值)，调用内置函数ord()可以得到指定字符的ordinal value。 
        与内置函数ord()对应的是内置函数chr()，调用chr()函数指定ordinal value可以得到其对应的字符
"""
a1 = 'apple'
a2 = 'app'
print(a1 > a2)      # 首先对比相同位置的字符，由于到了'l'的字符后，a2已经没有字符，因此a1 > a2
a3 = 'banana'
print(a1 > a3)
print(ord('a'), ord('b'))           # a 与 b 的原始值 分别为 97和98，97>98 ， 输出结果为False
print(a3 > a1)                      # 98 > 97 返回结果为True
print(chr(97),chr(98))              # 可以通过ordinal value 求得原字符
print(ord('卡'))                     # 可以通过ordinal value 求得原字符
print(chr(21345))                      # 可以通过ordinal value 求得原字符

#  == 与 is 区别           == 比较的是value, is比较的是Mem_id
a = b = 'python'            # 纯字母，符合驻留机制
c = 'python'                # 纯字母，符合驻留机制
print(a == b)
print(b == c)
print(a is c)
for i in [a,b,c]:           # 查看abc 的Mem_id
    print(id(i))
########################################################################################################################

# 字符串的切片操作 (与列表切片相同操作，str与列表相比,为不可变序列,不具有增删改操作)  str[Start:End:Step]
a = 'hello,Python'
b = 'hello,Python'
c = a[:5]
d = a[6:]
e = c + '!' + d
print(id(a),id(b))          # pycharm 优化驻留机制
print(a[:5])
print(a[6:])
print(a[:5] + '!'+ a[6:])
print(e)
print(a[1:5:1])
print(a[::2])
print(a[::-1])
print(a[-6::1])
########################################################################################################################

# 格式化字符串
"""
    使用%作为占位符
        %s --> 字符串
        %i / %d --> 整数
        %f --> 浮点数
"""
name = 'Jessica'
age  = 21
job = 'Operator'
print('My name is %s, and I am %i years old, my job is %s'%(name,age,job))                      # 前面接多少个占位符，后面%()里面就应该由多少个参数
print('My name is {0}, and I am {1} years old,and my Ture name is {0}'.format(name,age))        # {0} {1}映射.format后面的参数位置
print('My name is {0}, and I am {1} years old,and my Ture name is {0}'.format(age,name))        # {0} {1}映射.format后面的参数位置
print(f'My name is {name}, and I am {age} years old, my job is {job}')                          # 直接使用{变量名}使用变量

print('%10d' % 102)         # 可以指定宽度，在 %与 s/i/d/f 之间添加指定宽度来指定
print('%.3f'% 3.1415926)    # 指定宽度并指定保留多少位小数 '%宽度.保留位数f'
print('%10.3f' % 3.1415926) # 指定宽度并指定保留多少位小数 '%宽度.保留位数f'
print('helloworld')
print('{0:.3}'.format(3.1415926))       # 只有一个占位符的时候{}可以不写数字  {占位符顺序:宽度.一共有几位数}  输出结果 3.14
print('{0:.3f}'.format(3.1415926))      # 指定了是浮点数后，可以使用数字指定保留几位小数 {占位符顺序:宽度.一共几位小数f}  输出结果 3.142
print('{0:10.3f}'.format(3.1415926))    # 指定了是浮点数后，可以使用数字指定保留几位小数 {占位符顺序:宽度.一共几位小数f}  输出结果 5个空格+3.142
########################################################################################################################
# 字符串的编码转换
"""
    str 在内存中以Unicoed表示 --> 编码 --> byte字节传输 --> 解码 --> 另外一台计算机显示
    编码: 将字符串转换为二进制数据(bytes)
    解码: 将bytes类型的字符串转换成字符串类型
"""
s = '豫章故郡，洪都新府'
print(s.encode(encoding='GBK'))         # GBK 编码格式中一个中文占2个字节 按照\xxx\格式进行计数，对于 s 而言共18个bytes
print(s.encode(encoding='UTF-8'))       # 对于UTF-8 编码格式中，一个中文占3个字节，对于s而言，共27个 bytes
s_coulst =str( s.encode(encoding='UTF-8')).split(sep='\\')
n = 0
for i in s_coulst:
    n += 1
print(n-1)

s_uncode = "b'\\xe8\\xb1\\xab\\xe7\\xab\\xa0\\xe6\\x95\\x85\\xe9\\x83\\xa1\\xef\\xbc\\x8c\\xe6\\xb4\\xaa\\xe9\\x83\\xbd\\xe6\\x96\\xb0\\xe5\\xba\\x9c'"
print(s_uncode)

byte = s.encode(encoding='GBK')         # 使用GBK进行编码
print(byte,'\t encoding with GBK')
print(byte.decode(encoding='GBK'))      # 使用GBK进行解码
byte = s.encode(encoding='UTF-8')       # 使用UTF-8进行编码
print(byte,'\t encoding with UTF-8')
print(byte.decode(encoding='UTF-8'))    # 使用UTF-8进行解码



