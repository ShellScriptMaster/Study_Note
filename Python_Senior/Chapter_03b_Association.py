# 关联关系  二人情侣关系
"""

class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.gender = gender
        self.age = age
        self.partner = None  # 应该是一个对象，代表另一半

    def do_private_stuff(self):
        pass

二人关系需要进行双向绑定
p1 = Person('Alex', 26, 'Male')
p2 = Person('Jessica', 28, 'Female')
# 生成了2个人，但是2人关系需要被定义为情侣关系

p1.partner = p2  # 此处将p2当作p1 partner
p2.partner = p1  # 此处将p1当作p2 partner
print(p1.partner.name, p2.partner.name)   # 双向关联

p2.partner = None
p1.partner = None
print(p1.partner, p2.partner) # 解除关系也需要进行双向解除
"""


class Relationship:
    # 这个类主要用来保存2人之间的对象关系
    def __init__(self):
        self.couple = []

    def make_couple(self, obj1, obj2):
        self.couple = [obj1, obj2]
        print('[%s] 和 [%s] 确定了情侣关系' % (obj1.name, obj2.name))

    def get_my_partner(self, obj):
        # print('找', obj.name, '的对象', self.couple)
        for i in self.couple:
            if i != obj:  # 此处的i代表的是obj的对象
                return i
        else:
            print('你没有对象')

    def break_up(self):
        print('[%s]和[%s]结束情侣关系' % (self.couple[0].name, self.couple[1].name))
        self.couple.clear()


class Person:

    def __init__(self, name, age, gender, relation):
        self.name = name
        self.gender = gender
        self.age = age
        self.relation = relation  # 每个人实例里都存储[关系]对象

    def do_private_stuff(self):
        pass


relation_obj = Relationship()
p1 = Person('Alex', 26, 'Male', relation_obj)
p2 = Person('Jessica', 28, 'Female', relation_obj)

relation_obj.make_couple(p1, p2)   # 执行了make_couple 方法 可以查看二人的情侣关系
# 通过一个人能够得知另一半是谁
print(p1.relation.couple)
print(p1.relation.get_my_partner(p1).name)  # 此处 p1.relation代表的是relation_obj实例本身,并不是p1实例,所以需要将p1传入

p1.relation.break_up()
p2.relation.get_my_partner(p2)
