# Dictionary
# What is Dictionary?
"""
 是 PY 内置的数据结构之一，是一个可变序列（可以增删改查）。
 以键值对的形式存储数据，是一个无序的序列
 列表=[], 字典={Key:Value}
 所有元素以键值对形式存储，key不能重复，Value可以重复
 可以动态伸缩
 会浪费较大内存
 字典存储数据时，需要将key经过Hash计算后得出字典内元素存储位置 --> key需要为不可变序列 'str,float,int'

# The Principle of Dictionary
实现原理：
    根据key 查找Value所在的位置
"""
########################################################################################################################

# Create or Remove Dict
scores = {'Tom':100,'Jessica':80,'Monica':98,'Lucy':45 }  # Using '{}' to create a Dict
Jacky_info = dict(name='Jacky',age=20)                                 # Using dict() function to create a Dict  dict(key=Value,...)
emt_dict = {}
print(scores,type(scores))
print(Jacky_info)
print(emt_dict,type(emt_dict))
########################################################################################################################

# Query of Dict
print(scores['Tom'])
print(scores.get('Tom'))
# print(scores['hello'])          using [] for query from Dict, if element doesn't exsisting will return an Error
print(scores.get('Kristy'))    #  using get() to query from Dict , if element doesn't exsisting will return a None

print(scores.get('Tom'))
print(scores.get('Jessica'))
print(scores.get('Monica'))
print(scores.get('Lucy'))
print(scores.get('Hello',99))   # When the Value not exsisting, it will return 99  --> details in help(scores.get)
print(scores['Tom'])
print(scores['Jessica'])
print(scores['Monica'])
print(scores['Lucy'])
########################################################################################################################

# Operation on Dict: Add, Delete, Change, 判断
print('Tom' in scores)
print('Tom' not in scores)
print(45 in scores)
print(45 not in scores)
del scores['Tom']
print(scores)
print('Tom' not in scores)
scores.clear()          #  Clear a Dict
print(scores)           # get a empty Dict
# scores = {'Tom':100,'Jessica':80,'Monica':98,'Lucy':45 }
scores['Tom']=100               # add a key-Value element
scores['Jessica'] = 80          # add a key-Value element
scores['Monica']=75             # add a key-Value element
scores['Freshman']=60           # add a key-Value element
scores['Kristy']=85             # add a key-Value element
print(scores)
scores['Kristy'] = 120          # change value for a key
scores['Freshman'] = 0          # change value for a key
print(scores)

# 3 Method to acquire the view of Dict 获取字典视图的3种方法    字典视图： key, value, item
# To get all the key of Dict
new_scores = dict(Tony=55,Jessica=85,Meledy=90,Sam=88,Vicky=100,Yancy=120)
print(new_scores)
ns_keys = new_scores.keys()
print(type(ns_keys),ns_keys)
lskeys = list(ns_keys)                  # 将键的集合转换成列表
print(lskeys,type(lskeys))

# To get all the Value of Dict
new_scores = dict(Tony=55,Jessica=85,Meledy=90,Sam=88,Vicky=100,Yancy=120)
print(new_scores)
ns_values = new_scores.values()
print(ns_values,type(ns_values))
lsvalues = list(ns_values)              # 将值的集合转换成列表
print(lsvalues,type(lsvalues))

# To get all the item of Dict  (key-Value)
new_scores = dict(Tony=55,Jessica=85,Meledy=90,Sam=88,Vicky=100,Yancy=120)
ns_item = new_scores.items()                # Saving the item as tuple type (x,x)
print(ns_item,type(ns_item))
lsitem = list(ns_item)
print(lsitem,type(lsitem))              # 将键值对转换成元组，并且将所有元组排列到一个列表中

# Go through every item of Dict
new_scores = dict(Tony=55,Jessica=85,Meledy=90,Sam=88,Vicky=100,Yancy=120,Jacky=2**8,Kate=20*8)
print(new_scores)

# Go through all the Keys of the Dict
for i in new_scores:
    print(i)
print(type(i))
"""
Equals:
    for i in new_scores.key():
        print(i)
"""
# Go through all the Values of the Dict
for i in new_scores.values():
    print(i)
print(type(i))

for i in new_scores:
    print(new_scores[i])                # Get Values by Key Method 1
print(type(i))

for i in new_scores:
    print(new_scores.get(i))            # Get Values by Key Method 2
print(type(i))

# Go through all the items of the Dict,and print as a Tuple type
for i in new_scores.items():
    print(i)
print(type(i))
########################################################################################################################

# Dictionary Comprehension. (字典推导式)
info = {'name':'Terry','name':'Lucy'}           # key should be unique!
print(info)

info = {'name':'Tony','nickname':'Tony'}        # value can be repeated
print(info)

# info = {['hello','python']:'Study'}           List is a changable type, hence It can't be the key
# print(info)

items = ['Fruits','books','Others']
prices = [100,55,88]
# To get a Dict -->  { 'Fruits':100,'books':55,'Others':88 }   using built-in Function zip()
# zip() 用于可迭代的对象作为参数，将对象中对应的元素打包成一个元组，然后返回由这些元组组成的列表
good_list = zip(items,prices)
print(list(good_list))              # return a list

good_dict =  { items.upper():prices for items,prices in zip(items,prices)  }
print(good_dict)

items = ['book','Course','software','apple','laptop','pot']         # 6 arguments
prices = [20,300,60,8.6,3698]                                       # 5 arguments
good_dict = { items:prices for items ,prices in zip(items,prices) } # 木桶原理，以最少的参数作为字典元素的个数，因此最后只生成5个元素的字典
print(good_dict)
########################################################################################################################