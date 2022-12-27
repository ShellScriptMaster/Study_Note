"""
    普通双下划线方法：
        def __len__(self): 可以返回对象的某个属性的长度
        def __hash__(self): 返回hash值
        def __eq__(self,other):   判断一个类实例化出来的两个对象是否完全相同(内存地址是否完全相同)
            通过比较 self 和 other 两个实例对象的属性返回 True or False
        def __getitem__(self, item):    通过item属性查找实例对象item属性对应的值
            return self.__dict__[item]
        def __setitem__(self, key, value):  通过 self[key]=value 为实例对象添加属性及值
            self.__dict__[key] = value
        def __delitem__(self, key):         通过 del self['key'] 为实例对象删除属性
            self.__dict__.pop(key)
        def __delattr__(self, item):        通过 def self.item 为实例对象删除属性
            self.__dict__.pop(item)
"""


class Person1(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __len__(self):
        print('Call len')
        return len(self.name)

    def __hash__(self):
        print('Call hash')
        return hash(self.name)

    def __eq__(self, other):
        if type(self) == type(other) and other.name == self.name and other.age == self.age:
            return True
        else:
            return 0

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        print('call __delitem__')
        self.__dict__.pop(key)      # 删除元素

    def __delattr__(self, item):
        print('call __delattr__')
        self.__dict__.pop(item)


test = Person1('Jacky', 23)
print(test.__len__())
print(test.__hash__())
print(hash(test))

test_eqa = Person1('Cat', 22)
test_eqb = Person1('Cat', 22)
print(test_eqa == test_eqb)         # 如果class中没有__eq__()方法的话，此处会报False, 这是因为两者的内存地址别不相同因此判断为不同实例对象
print(id(test_eqa))
print(id(test_eqb))
# print(test_eqa.__eq__(test_eqb))    # 使用实例 test_eqa 和 实例 test_eqb进行比较, 此时 self=test_eqa ; other=test_eqb
print(test_eqa == test_eqb)

test_item = Person1('Sherry', 21)
test_item['gender'] = 'Female'
test_item['job'] = 'IT'
test_item['location'] = 'GZ'
print(test_item['name'])
del test_item['gender']     # 触发__delitem__
# print(test_item['gender'])       从字典删除此元素，因此key_error
test_item['name'] = 'Jessica'
print(test_item['name'])
del test_item.job           # 触发__delattr__
print(test_item.__dict__)




