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
# Sorting for List element
# 列表推导式
