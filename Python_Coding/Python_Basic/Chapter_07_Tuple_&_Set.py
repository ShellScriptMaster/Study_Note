# A description of Tuple
"""
    py内置数据结构之一，是一个不可变序列
        不可以进行增删改
        字符串，元组
    可变序列：列表，字典

    多任务环境下同时操作对象时不需要加锁，因此程序中尽量使用不可变序列
    元组中存储的是对象的引用：
        如果元组中的对象本身不可变对象，则不能引用其他对象
        如果元组中的对象是可变对象，则可变对象的引用不允许改变，但数据可以改变  --> 即列表中所有的元素内存ID不能改变
            for example:
                a = (9,[2,3,4],10)      此时列表内0,1,2三个位的元素不能改变,可以改变列表的元素但是不能改变1号位的数据
"""
# 可变序列在于序列改变前后内存ID不变
lst = [10,20,45]
print(id(lst))
lst.append(79)
print(id(lst))

# 不可变序列在改变以后内存ID发生改变，即已经生成了一个新的变量
s = 'hello'
print(id(s))
s = s + 'world'
print(s,id(s))

# 元组对象的引用
a = (9,[2,3,4],10)
print(a,type(a))
print(a[0],type(a[0]))      # 数据类型是int
print(a[1],type(a[1]))      # 数据类型是list
print(a[2],type(a[2]))      # 数据类型是int
a[1].append(20)
a[1].insert(1,2**8)
print('new a_tuple is ',a)  # 不能改变元组的元素，但是可以改变1号位列表内的数据。元组1号位的内存ID不变，但是列表内的元素内存ID可以改变
########################################################################################################################

# Create a Tuple
tpl1 = ("python",'world',98)
print(tpl1,type(tpl1))

info = 'python','world',98,2**8     # 省略了小括号的元组
info3 = ('python')                  # 单个元素的元组定义需要在元素后加上 ',' 否则将视为元素本身的类型
print(type(info3),info3)
info3 = ('python',)
print(type(info3),info3)            # 单个元素的元组定义需要在元素后加上 ','
tpl2 = tuple(info)
print(tpl2,type(tpl2),type(info))
# 空列表字典元组
em_lst = []
em_lsg = list()
em_dict = {}
em_dict = dict()
em_tpl = ()
em_tpl = tuple()
print('empty list',em_lst,'\nempty dict',em_dict,'\nempty tuple',em_tpl)
########################################################################################################################

# Go through a Tuple
tpl = (1**1,2**2,3**3,4**4,6**6,'goodmorning','python')
print(tpl)
print(tpl[3])
print(tpl[4])
print(tpl[5])
for i in tpl:
    print(i)
########################################################################################################################

# A description of Set
"""
    属于py内置的数据结构
    与列表字典一样属于可变类型序列
    集合可以理解为没有Value的字典
"""
# Create a Set
set1 = {1**1,2**2,3**3,4**4,1**1,2**2,1**1,'goodmorning','python','create','a','set'}
print(set1,type(set1))      # 集合中元素不能重复，且无序的
set1 = set(range(-1,8))     # 根据可迭代序列创建集合
print(set1)
lst = list(range(0,30,4))
set1 = set(lst)             # 根据列表创建集合
print(set(lst))
tup1 = tuple(range(0,60,6)) # 根据元组创建集合
print(set(tup1))
str1 = 'python'             # 根据字符串创建集合
print(set(str1))
em_set = set()              # 定义一个空集合
print(em_set)

# Operation of Set: Add, Delete, Modify, Qurey, Determine
# Determine
set2 = {1,2,3,4,0,10,30,20,79,551,6511,65461,684,13,2}
print(set2)
print(1 in set2)
print(32 in set2)
print(100 not in set2 )
print(13 not in set2)
# Add
set2.add(80)
print(set2)
set2.update({200,400,300,500})          # 批量添加元素
print(set2)
set2.update(('hello','good'))
print(set2)
# Remove
set2.remove(400)        # 指定元素不存在会返回ERROR
print(set2)
set2.remove(300)
print(set2)
set2.discard(500)
print(set2)
set2.discard(3.14159)
print(set2)
set2.pop()              # 随意删除一个元素,不能指定参数
set2.pop()
print(set2)
set2.clear()            # 清空集合
print(set2)

# 集合的关系 A集合=B集合， A集合为B集合的子集， AB集合无交际, 交，并，补，差集
A = {10,520,30,40,50,60}
B = {520,50,30,40,60,10}
print(A==B)
print(A!=B)

A = {10,20,30,50,40,60}
B = set(range(10,120,10))
C = set(range(0,90,10))
D = set(range(200,300,50))
print(A,'\n',B,'\n',C)
print(A.issubset(B))            # 判断 A 是 B 的子集 A.issubset(B)
print(C.issubset(B))            # 判断 C 是 B 的子集 C.issubset(B)

print(B.issuperset(A))          # 判断 B 是 A 的超集 B.issuperset(A)
print(B.issuperset(C))          # 判断 B 是 C 的超集 B.issuperset(C)
print(not B.issuperset(C))      # 可以结合 not 使用

print(D.isdisjoint(C))          # 判断两集合是否无交集，无交集返回True,有交集返回False
print(C.isdisjoint(B))          # 判断两集合是否无交集，无交集返回True,有交集返回False

# 交集(intersection)
A = {10,20,30,40}
A1 = {20,30,40,50,60,70}
B = {1,2,3,4}
B1 = {1,2,3,4,5,6,7,8}
C = {'p','y','t','h','o','n'}
C1 = {'h','e','l','l','o'}
print(A.intersection(A1))           # 求两个集合的交集(intersection)
print(B.intersection(B1))           # 求两个集合的交集(intersection)
print(C.intersection(C1))           # 求两个集合的交集(intersection)
print(A & A1)                       # 求两个集合的交集(intersection)
print(B & B1)                       # 求两个集合的交集(intersection)
print(C & C1)                       # 求两个集合的交集(intersection)

# 并集(union)
print(A.union(B))                   # 求两个集合的并集(union)
print(A.union(C))                   # 求两个集合的并集(union)
print(A | C)                        # 求两个集合的并集(union)
print(B.union(C))                   # 求两个集合的并集(union)
print(B | C)                        # 求两个集合的并集(union)

# 差集(difference)
print(A.difference(A1))             # 求两个集合的差集(difference)  A - A1
print(A - A1)                       # 求两个集合的差集(difference)  A - A1
print(A1.difference(A))             # 求两个集合的差集(difference)  A1 - A
print(A1-A)                         # 求两个集合的差集(difference)  A1 - A
print(B.difference(B1))             # 求两个集合的差集(difference)  B - B1
print(B-B1)                         # 求两个集合的差集(difference)  B - B1
print(B1.difference(B))             # 求两个集合的差集(difference)  B1 - B
print(B1-B)                         # 求两个集合的差集(difference)  B1 - B
print(A.difference(C))              # 求两个集合的差集(difference)  A - C
print(A-C)                          # 求两个集合的差集(difference)  A - C
print('symmetric difference\n',)
# 补集(symmetric difference)      （并集减去交集）
print(A.union(A1) - A.intersection(A1)) # 并集减去交集
print(A.symmetric_difference(A1))       # 求两个集合的补集 CuA
print(B.union(B1) - B.intersection(B1)) # 并集减去交集
print(B.symmetric_difference(B1))       # 求两个集合的补集
print(C.union(C1) - C.intersection(C1)) # 并集减去交集
print(C.symmetric_difference(C1))       # 求两个集合的补集
########################################################################################################################

# 集合生成式/推导过程 与列表生成式相似
set1 = {i for i in range(0,20,2)}
print(set1)
set2 = {i * i for i in range(0,20,2)}
print(set2)




