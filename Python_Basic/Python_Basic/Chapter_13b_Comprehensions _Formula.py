"""
    list, dict, set 推导式:
        作用:
            简化代码
        语法:
            list : [数据 for循环 if判断 ]
            set: {数据 for循环 if判断 }
            dict: {key:value for循环 if 判断}
            生成器表达式： (数据 for循环 if判断)
            没有元组表达式
"""
lst = []
for i in range(50):
    lst.append(i)

lst1 = [i for i in range(50)]
print(lst1)
lst2 = [i for i in range(1, 50, 2)]
print(lst2)
lst2 = [i for i in range(0, 50) if i % 2 == 1]
print(lst2)
set1 = {'衣服%s' % i for i in range(50)}
print(set1)
lst_name = ['alex', 'tony', 'jimmy', 'apple']
set2 = {i.upper() for i in lst_name}
print(set2)
lst_name = ['alex', 'tony', 'jimmy', 'apple']
dict1 = {i: lst_name[i] for i in range(len(lst_name))}
print(dict1)

gen = (i ** 2 for i in range(10))        # 生成器推导式
print(gen)
for i in gen:
    print(i)

# gen = (i ** 2 for i in range(10))
gen_lst = list(gen)                     # list()方法有for循环 --> 有__next__()  因为gen已经在for循环遍历完，于是gen_lst 是一个空列表
print(gen_lst)
