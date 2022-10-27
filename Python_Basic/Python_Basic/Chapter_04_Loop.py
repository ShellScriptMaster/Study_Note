# Loop Structure 循环结构
# range() function range()函数  三种方法,占用的内存空间都一致
# range(stop) 创建一个（0，stop）之间的整数序列，步长为1
a = range(12)
print(a,type(a))   #返回的类型是range，默认从0开始，一共12个数
print(list(a))  # 将迭代对象转换成列表用于查看range返回的所有元素

# range(start, stop) 创建一个（start，stop）之间的整数序列，步长为1
a = range(1,12)
print(a,type(a))
print(list(a))

# range(start, stop, step) 创建一个（start，stop）之间的整数序列，步长为step
a = range(1,14,2)
print(a,type(a))
print(list(a))

# 可以使用 in ,not in 判断一个Int 是否包含在序列中
print(10 in a )   #  1,3,5,7,9,11,13   10 not in this range, return False
print(3 in a)     #  1,3,5,7,9,11,13   3  in this range, return True
print(10 not in a )  #  1,3,5,7,9,11,13   10 not in this range, return True
print(3 not in a )   #  1,3,5,7,9,11,13   3 in this range, return False

print(range(1,20,1))    # [1,19]   无论多少元素占用内存一致，存储内容为(start,stop,step)
print(range(1,101,1))   # [1,100]  无论多少元素占用内存一致，存储内容为(start,stop,step)
########################################################################################################################

# while
"""
while expression:
    do
"""
a = 1
if a < 10:
    print(a)
    a += 1
# comparison with if
a = 1
while a < 10:
    print(a)
    a += 1
# Sum 0 to 10
count = 0
total = 0
while count < 11:
    total += count
    count += 1
print(total)
"""
a  a<5  sum  sum+=a
0  0<5  True  0+0
1  1<5  True  0+1
2  2<5  True  1+2
3  3<5  True  1+2+3
4  4<5  True  1+2+3+4
5  5<5  False 1+2+3+4  end
"""
# Calculate all even number from 1 to 100
count = 0
total_even = 0
while count < 101: # 加到100
    total_even += count
    count += 2
print(total_even)
# another Method
count = 1
total_even = 0
while count < 100:  # 加到99
    if count % 2 == 0:
#   if not bool(count % 2):    # count % 2 为0 即为False， 为1 即为 True
        total_even += count
    count += 1
print(total_even)
########################################################################################################################

# for-in  for循环
# 可迭代对象 range(), str, list, tuple,dict
for i in 'Python':
    print(i)  # 将字符串的内容遍历一遍同时分别输出
for i in range(10):
    print(i)  # print 0123456789
# 如果循环中不需要使用到自定义变量，可以将自定义变量写为"_"
for _ in range(5):
    print('hello world')  # print 'hello world' for 5 times

# print sum of even number from  0 to 100
total = 0               # need to change total to 0
for i in range(0,101):
    if not bool(i % 2):
        total += i
print(total)

# 计算100 到 999 之间的水仙花数
"""
水仙花数，举例：
        153 = 3*3*3+5*5*5+1*1*1
"""
# Developed By myself
for i in range(100,1000):       # 遍历 100 到 1000的数  793
    num = 0                     # 从循环开始先使和为0
    for a in str(i):            # 将数字转换成文本格式，然后遍历 个十百 位的数字
        num += int(a) ** 3      # 对 个十百 位提取出的数字进行求立方后求和
    if num == i:                #  如果和等于现在取出的数字，则打印出来
        print(num)
# Studying Case  先取出所有数字的 个十百 位数字
for item in range(100,1000):
    ge = item % 10
    shi = item // 10 % 10
    bai = item // 100
    if  ge ** 3 + shi ** 3 + bai ** 3 == item:
        print(item)
########################################################################################################################

# break , continue, else
# 输入密码，最多录入3次，如果正确结束程序  while & for
"""  ------------------ normal Coding ------------------ 
#   using "while"
times = 0
PASSWD = '123'
while times < 3:
    password = input('please input your passwd')
    if password == PASSWD:
        break
    else:
        times += 1
#   using "for-in"

times = 0
PASSWD = '123'
for _ in range(0,3):
    password = input('please input your passwd')
    if password == PASSWD:
        break

     ------------------ normal Coding ------------------  """

# continue 用于结束当前循环，进入下一次循环，通常与分支结构中的if 一起使用
# 输出0-50所有5的倍数,使用continue
# Developed by myself
for i in range(0,51):
    if i % 5 == 0 :
        print(i)
# Studying Case 2
for item in range(0,51):
    if item % 5 != 0:
        continue
    print(item)

# else 与 while 或 for 进行搭配  循环执行完了以后就会执行else
# input password   for-in case
"""  ------------------ normal Coding ------------------ 
for item in range(3):
    passwd = input('please input your passwd')
    if passwd == '123':
        print('correct')
        break
    else:
        print('incorrect')
else:                                             # 执行完了for 以后执行else内容
    print('you have input passwd for 3 times')
     ------------------ normal Coding ------------------  """
# input passwd   while case
"""  ------------------ normal Coding ------------------ 
item = 0
while item < 3 :
    passwd = input('please input your passwd')
    if passwd == '123':
        print('correct')
        break
    else:
        print('incorrect')
    item += 1
else:
    print('you have input passwd for 3 times' )
     ------------------ normal Coding ------------------  """
########################################################################################################################

# Nested loop  嵌套循环
# 循环结构中又嵌套了另外完整的循环结构，其中内层循环作为外层循环的循环体执行
# 输出一个三行四列的矩形
for i in range(3):
    for j in range(4):
        print('*',end='\t')
    print()                 # 一行的4个*已经输出完， 需要打印空白，实现换行
# 九九乘法表
# 输出一个 9 * 9 直角三角形
for i in range(1,10):               # 输出行
    for j in range(1,i+1):          # 第i行最多有i列
        print('*' ,end='')          # 第几行就输出几个*，不换行输出
    print()                         # 换行

# 将乘法表代入到三角形中
for i in range(1,10):                       # 输出行
    for j in range(1,i+1):                  # 第i行最多有i列
        print( j,'*',i,'=',i*j ,end='\t')   # 从第1行 第1列进行乘法运算，j代表第几列
    print()                                 # 换行

# 二重循环中的break 和 continue
# break 退出当前循环，不影响外部循环的执行； continue 继续执行当前循环，对外层循环没影响   --> 控制本层的循环
for i in range(5):
    for j in range(1,11):
        if  j % 2 == 0:
            #break
            continue
        print(j,end='\t')
    print()
for i in range(5):
    for j in range(1,11):
        if  j % 2 == 0:
            break
        print(j,end='\t')
    print()



