"""
    反射
        通过字符串映射调用实例的属性/方法，并且进行一系列增删改查操作
        python面向对象中的反射: 通过字符串的形式操作(增删改查)对象相关的属性:
            hasattr(obj, '属性/方法名')  --> 判断对象是否有这个名字的属性或方法
            getattr(obj, '属性/方法名', [default])  --> 通过属性/方法名返回obj的属性值，如果属性不存在，则返回[default]值, 没有定义[default]则抛出异常
            setattr(obj, '属性/方法名', value)  --> 操作对象的属性/方法, 有则覆盖，没有则创建
            delattr(obj, '属性/方法名')  --> 通过实例来删除属性/方法


"""


class Person(object):
    Obj_name = 'Person_name'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print('%s 使用了walk方法' % self.name)

    def eat(self):
        print('Eating')


p = Person('Amanda', 23)
if_name = hasattr(p, 'name')                # True
if_age = hasattr(p, 'age')                  # True
if_walk = hasattr(p, 'walk')                # True
if_gender = hasattr(p, 'gender')            # False
if_P_name = hasattr(Person, 'name')         # False
if_Obj_name = hasattr(Person, 'Obj_name')   # True
if_P_walk = hasattr(Person, 'walk')         # True

p1 = Person('Bob', 32)
get_walk = getattr(p1, 'walk')  # 结果相当于 p1.walk()
get_name = getattr(p1, 'name')  # 结果相当于 p1.name
# get_gender = getattr(p1, 'gender')  由于p1不存在gender为名的属性或方法，因此报错
get_gender = getattr(p1, 'gender', None)
print(get_gender)
get_walk()

p2 = Person('Jack', 35)
setattr(p2, 'name', 'Pony')
setattr(p2, 'gender', 'Male')
p2_name = getattr(p2, 'name')
p2_gender = getattr(p2, 'gender', None)
print(p2_name, p2_gender)

delattr(p2, 'gender')
delattr(p2, 'name')
p2_name = getattr(p2, 'name', None)
p2_gender = getattr(p2, 'gender', None)
print(p2_gender, p2_name)

p2_walk = getattr(p2, 'eat')
p2_walk()

# 使用setattr 绑定类方法
# 先在类外定义一个方法
def shopping(self):
    print(self.name, ' is shopping')

# 将方法与类进行绑定
setattr(Person, 'Shopping', shopping)
# 类实例化
p3 = Person('Pony', 33)
p3_shop = getattr(p3, 'Shopping')
# 引用方法
p3_shop()

