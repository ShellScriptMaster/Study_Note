"""
    使用type()创建一个类
"""


class Person(object):
    def __init__(self, name):
        self.name = name


a = Person('Jessica')
print(type(a))
print(type(Person))         # 类是一个type 类型

# 使用type()创建一个类
dog_set = type('Dog', (object,), {'animal': 'dog', 'food': 'meat'})
b = dog_set()
print(b.animal, b.food)

# 使用type()创建一个类, 并且插入__init__方法


def __init__(self, name):
    print(' call __init__')
    self.name = name


def eat(self):
    print('[%s] is eating ' % self.name)


cat_set = type('Cat', (object,), {'animal': 'cat', 'food': 'fish', '__init__':__init__, 'eat':eat})
c = cat_set('Kristy')
c.eat()
print(c.animal, c.food)
