"""
 Because I set this folder as a GIT Repository. Before the code git add . The file name will be red.
 # 列表可以存储许多元素（不同数据类型也可以存储），程序可以方便对这些数据进行整体操作 相当于其他的语言中的数组
 列表索引
-7 -6 -5 -4 -3 -2 -1    --> 索引方式一
 a  b  c  d  e  f  g
 0  1  2  3  4  5  6    --> 索引方式二
"""
a = 10
print(id(a),type(a),a)
b = 20
c = 30.252
d = 'hello world'
e = [a,b,c,d]
print(id(e),'\n',type(e),'\n',e)
print(id(b))
print(id(c))
print(id(d))
# 列表内不同元素有自己的ID，列表作为PY中的一个对象，因此也会有自己的ID
########################################################################################################################

# List Create and Delete
# using [] to define a List
lst = ['hello world',98]
print(lst)
# using list() function to define a list
lst = list(['hello world','using','list() function','to define a list'])
R1 = range(1,30)
lst2 = list(R1)
print(lst2)
print(lst)
print(lst[0],'\n',lst[-3])
"""
    列表元素按顺序排序，每个索引映射一个数据，列表可以存储重复数据，列表可以任意数据类型混存，可以根据需要动态分配和回收内存
"""
l1 = list(['hello world',3.14159,3115003949,[45239114,'yesterday88.'],range(1,30)])
print(l1[0],'\n',l1[1],'\n',l1[2],'\n',l1[-1])
########################################################################################################################

# List query
lst = ['hello',123,3.14159,'goodmorning','hello']
print(lst.index('hello'))    # 如果列表中有相同元素，只返回列表中第一个相同元素的索引
# print(lst.index(('python')))  列表中没有被查找元素，py会报错
print(lst.index('hello',1,5))  # 在列表中可以指定 起始位 终止位 查找对应元素的索引
print(lst[2])       # 逆向索引  获取索引为2的元素
print(lst[-2])      # 逆向索引  获取索引为-2的元素
# print(lst[10])        索引不在列表范围内，程序会报错

# 获取列表中多个元素  (List Slice)
lst = [10,20,30,40,50,60,70,80,90]
# when step > 0
print(lst[1:6])     # default step is 1
print(lst[1:6:])    # default step is 1
print(lst[:6:])     # default start is 0 , default step is 1
print(lst[::1])     # default start is 0 , default end(include) is last element
print(lst[1:6:1])   # start = 1 , end = 6 (exclude) , step = 1
print(lst[1:7:2])   # start = 1 , end = 7 (exclude) , step = 2
print('List Slice ID is ',id(lst[1:7:2]),)
print('Origin List Id is ',id(lst))
# When step < 0
print('Origin list is ',lst)
print(lst[::-1])    # 排列顺序调转
print(lst[7::-1])   # Start = 7 (include), default end = 0 , step = -1
print(lst[6:0:-2])   # Start = 6 (include),  end = 0 (exclude) , step = -6

# check whether a element in a list or not
print('p' in 'python')      # for string type --> True
print('k' not in 'python')  # for string type --> True
lst = [10,20,'python','hello']
print(10 in lst)    # True
print(20 in lst)    # True
print(3 in lst)     # False
print(3 not in lst) # True

for i in lst:       # print every element in the list
    print(i)
########################################################################################################################
# Add, Delete, Change For List Element

# 向列表末尾增加元素
"""
append() 在列表末尾添加一个元素
extend() 在列表末尾至少添加一个元素
insert() 在列表指定位置添加一个元素
切片      在列表指定位置替换/添加至少一个元素 
"""
lst = [10,20,30]
print(id(lst))
lst.append(100)
print(lst,id(lst))          # 查看是否新增列表对象   ---> 还是原来的变量,内存ID地址未改变
lst2 = ['hello world',2,102]
# 向列表末尾一次性添加多个元素
# lst.append(lst2)            # 将列表作为整体元素添加到列表末尾 append
lst.extend(lst2)
print(lst)                    # 向列表中一次性添加多个元素(将列表元素拆开放入列表 )
a = range(1,20)
lst.extend(a)
print(lst)
# 向列表插入元素
lst = [0,10,20,30,40,50,60,70,80,90,100]
lst.insert(1,90)        # 在1号位添加90这个元素
print(lst)
lst.insert(-1,100)      # 支持2种顺序插入元素
lst1 = [0,10,20,30,40,50,60,70,80,90,100]
print(lst1)
lst3 = [True,False,'hello']
# 切片添加
lst1[1:4] = lst3
print(lst1)              # 1号位到3号位的元素将被lst3的元素替代
lst1 = [0,10,20,30,40,50,60,70,80,90,100]
lst1[1:1] = lst3         # 可以设置在2号位开始添加多个元素
print(lst1)

# 从列表删除元素 remove() , poo(), 切片, clear(), del()
"""
remvoe() 
    一次删除一个元素
    重复元素只删除第一个
    元素不存在返回ValueError
pop()
    删除一个指定索引位置上的元素
    指定索引不存在返回IndexError
    不指定索引，默认删除列表中最后一个元素
切片
    一次至少删除一个元素
clear()
    清空列表
del
    删除列表
"""
# remove()
lst1 = [10,20,30,40,50,60,30]
lst1.remove(30)
print(lst1)     # 剔除一个元素，重复元素只剔除第一个
# lst1.remove(100) 不存在的元素不能移除
# pop()
print('lst1 is ',lst1)
lst1.pop(1)
print(lst1)
# lst1.pop(10)  # 指定索引不存在返回IndexError
lst1.pop()      # 不指定位置默认删除最后一个
print(lst1)
# 切片 删除至少一个元素，产生新的一个列表对象
lst = [10,20,30,40,50,60,30]
print(id(lst),lst)
newlst = lst[1:4]
print(id(newlst),newlst)            # 产生新的列表对象
lst[1:4]=[]
print(id(lst),lst)                      # 不产生新的列表对象
# clear() 清除列表元素
lst.clear()
print(lst)                         # 变成空列表
# del  删除列表
del lst
# print(lst)    删除列表，lst变成未被定义了

# 修改列表元素
"""
指定索引元素赋予一个新值
指定切片赋予一个新值
"""
Clst = list(range(10,50,10))  # 等同于 Clst = [10,20,30,40]
print(id(Clst),Clst)
# 一次修改一个值
Clst[2] = 100       # 将2号位的值改为100
print(id(Clst),Clst)  # 未生成新的列表对象
for i in Clst:
    print(id(i))      # 查看列表中每个元素的内存地址ID
# 修改列表中多个元素
print(Clst)
Clst[1:3] = [2,3,4,5,6,7]
print(Clst)
########################################################################################################################

# Sorting for List element
"""
常见方式：
    调用sort()方法
        列表中元素默认从小到大进行排列
        可以指定reverse=True 进行降序排序
    调用内置函数sorted()
        指定reverse=True， 进行降序排序
        产生新的列表对象
"""
# sort() 列表对象方法
Slst = [20,30,40,85,99,82,58,34,21,37]
print('Before Sorting',Slst,id(Slst))
Slst.sort()
print('After Sorting',Slst,id(Slst))
Slst.sort(reverse=True)     # 进行降序排序
print('After Sorting',Slst,id(Slst))

# sorted() 函数
Slst = [20,30,40,85,99,82,58,34,21,37]
print('Before Sorting',Slst,id(Slst))
newSlst = sorted(Slst)
print('sorted After Sorting',newSlst,id(newSlst))
newSlst = sorted(Slst,reverse=True)
print('sorted After Sorting',newSlst,id(newSlst))
########################################################################################################################

# 列表推导式 --> 生成列表的公式
"""
语法格式：
    [i for i in range(1,10)]
"""
mylst = [ i for i in range(1,10)]
print(mylst)

lst4 = []
for i in mylst:
    new = i*2
    lst4.append(new)
print(lst4)

mylst = [ i * i for i in range(1,10)]
print(mylst)

# 要求列表中元素为2，4，6，8，10
# 方法1
lst5 = [ i * 2  for i in range(1,6)]
print(lst5)
# 方法2
lst5 = []
for i in range(1,6):
    ele = i * 2
    lst5.append(ele)
print(lst5)