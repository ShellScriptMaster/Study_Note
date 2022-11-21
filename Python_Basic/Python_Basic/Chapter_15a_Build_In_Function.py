"""
    内置函数
        数据类型相关:
            bool
            int
            float
            complex     转换成复数的形式  实部+虚部  i ** 2 = -1
        进制转换:
            bin 二进制
            oct 八进制
            hex 八进制
        数学运算:
            abs         绝对值
            divmod      divmod(被除数,除数) --> 返回值是一个元组  (商,余数)
            round       round(浮点数,保留小数位)  四舍五入, 保留小数为空则自动四舍五入取整
            pow         pow(a,b)   表示 a ** b
            sum         求和
            min         在一个序列中取最小数
            max         在一个序列中取最大数
        数据结构:
            列表和元组:
                list        对序列中元素循环遍历生成列表
                tuple       对序列中元素循环遍历生成列表
            相关内置函数:
                reversed    返回反转的迭代器 --> 需要使用list()对其进行转换
                slice
                    切片器 slice(开始位置,结束位置,步长)
                    使用方法
                     f = slice(1,9,2)
                    print('123456789'[f])
        字符串:
            str         转换成字符串类型
            format      指定一个输出的格式 --> (源变量,指定格式)
            bytes       是字节组成的有序的不可变序列
            bytearry    是字节组成的有序的可变序列
            memoryview  内存展示
            ord         查看文字的编码位置
            chr         使用编码位查看对应的文字
            ascii       以ascii形式进行展示
            repr        repr
        数据集合:
            字典: dict
            集合:
                set
                frozenset   集合内元素不允许更改
        相关内置函数:
            len         输出长度
            sorted      整理迭代器 (迭代器, reversed=True/False)  顺序,倒序
            enumerate   以元组的形式返回可迭代对象中的每一个元素及其索引 --> 返回结果 --> (索引,元素)
            all         对可迭代对象里面的元素进行遍历[a,b,c], 相当于 输出 bool(a and b and c)
            any         对可迭代对象里面的元素进行遍历[a,b,c], 相当于 输出 bool(a or b or  c)
            zip
            fiter
            map
        输入输出:
            input
            print
        内存相关:
            hash        对一个特定的对象进行hash算法返回一个hash值, 对象必须可hash
            id          查看对象占用的内存地址
        文件操作:
            open
        模块相关:
            import
        帮助:
            help
        调用相关:
            callable
        查看内置属性:
            dir         查看对象可执行的方法
"""

# bool int float complex
a = '123'
print(bool(a))
print(int(a))
print(float(a))
print(complex(a))

# bin oct hex int
b = 23
print(bin(b))   # 二进制    0b10111
print(oct(b))   # 八进制    0o27
print(hex(b))   # 十六进制  0x17
print(int(0b10111))

# abs divmod round pow sum min max
c = 10
d = 3
e = [i for i in range(10)]
print(abs(-20))
print(divmod(c, d))
print(round(10.822, 2))
print(pow(c, d))
print(sum(e))
print(min(e))
print(max(e))

# reversed slice
print(list(reversed(e)))
f = slice(1, 10, 2)
print('123456789'[f])

# str format bytes bytearry memoryview ord chr ascii repr
g = 23
print(format(g, 'x')) # 二进制b,八进制o, 十六进制x
g = 10
print(format(g, '08b')) # 输出一个8位的二进制的数，高位补0
print(format(g, '08o')) # 输出一个8位的八进制的数，高位补0
print(ord('洪'))     # 中文的unicode码位
print(chr(27946))   #  使用码位输出文字
# for i in range(65536):
#     print(chr(i)+' ', end="")

# dict set frozenset
# len sorted enumerate all any zip fitermap
h = [98, 123, 54, 8, 415, 854, 521, 61, 45]
print(sorted(h))                    # 顺序
print(sorted(h, reverse=True))      # 倒序
print(all(h))
h.append('')        # 有空值 --> 0 --> False
print(all(h))       # 输出False
print(any(h))
h = []
print(any(h))
i = ['jimmy', 'alex', 'alan', 'joice', 'sean']
for index , item in enumerate(i, 0):        # enumerate(可迭代对象, start=0)
    print(index, item)

for a in range(len(i)):
    print(a, i[a])

# hash id
j = (1, 2, 3, 4, 5, 6)
print(hash(j))
print(id(j))

# help
# dir
k = '呵呵哒'
print(help(k))
print(dir(k))       # 查看对象可执行的方法




