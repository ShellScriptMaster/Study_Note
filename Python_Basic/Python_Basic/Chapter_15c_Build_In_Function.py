"""
    内置函数:
        相关内置函数:
            sorted      整理迭代器 (迭代器, key=排序函数, reversed=True/False)  顺序,倒序
            filter      筛选 filter(函数,可迭代对象)  将可迭代对象所有元素传入函数中，通过函数的False & True选择哪些元素被筛选下来, 最后返回一个生成器，需要使用list进行包装
            map         分发/映射, map(函数,可迭代对象)  将可迭代对象所有元素传入函数中, 通过函数进行处理最终返回一个生成器

"""
# sorted
lst1 = [161, 231, 5451, 64, 158, 1, 4981, 81, 8138613, 61, 41, 63]
a_lst = sorted(lst1)
b_lst = sorted(lst1, reverse=True)
c_lst = sorted(lst1, reverse=False)
print(a_lst)
print(b_lst)
print(c_lst)
lst2 = ['卡卡罗特', '漩涡鸣人', '比克', '皮卡丘', '杰尼龟', '小岛龟仙人', '宠物小精灵和平镇的小智']


def func1(item):        # item对应的就是列表中的每一项数据
    return len(item)


func2 = lambda it: len(it)

d1 = sorted(lst2, key=func1)
d2 = sorted(lst2, key=func2)
print(d1)
print(d2)
d3 = sorted(lst2, key=lambda n: len(n))     # lambda 使用场景
print(d3)

# sorted 案例练习
lst3 = [
    {"id": 1, 'name': '周润发', 'age': '18', 'salary': '58000'},
    {"id": 2, 'name': '周星驰', 'age': '23', 'salary': '59000'},
    {"id": 3, 'name': '周大幅', 'age': '24', 'salary': '63000'},
    {"id": 4, 'name': '周大兴', 'age': '25', 'salary': '66000'},
    {"id": 5, 'name': '周六七', 'age': '28', 'salary': '55000'},
    {"id": 6, 'name': '周扒皮', 'age': '29', 'salary': '78000'},
    {"id": 7, 'name': '周伯通', 'age': '33', 'salary': '12000'}
]
# 根据lst3的age进行排序
# def func3(item):
#     for i in item:
#         print(i['age'])
#
# func3(lst3)
age_lst3 = sorted(lst3, key=lambda n: n['age'], reverse=True)
print(age_lst3)

# 根据salary进行排序
salary_lst3 = sorted(lst3, key=lambda n: n['salary'], reverse=True)
print(salary_lst3)

# filter
lst4 = ['张无忌', '张三丰', '张翠山', '殷素素', '灭绝师太', '周芷若', '赵敏']
f = filter( lambda item: item.startswith('张'), lst4)
print(list(f))

g = filter(lambda item: not item.startswith('张'), lst4)
print(list(g))

h = filter(lambda item: len(item) < 3, lst4)
print(list(h))

# map
lst5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
square_lst5 = [i ** 2 for i in lst5]
print(square_lst5)
square_lst5 = map(lambda item: item ** 2, lst5)
print(list(square_lst5))
