# Python 类的封装(避免在类的外部修改类的私有属性)
class Person1(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.life_val = 100         # 类的私有变量


p1 = Person1('Tom', 23)
p1.life_val -= 20   # 此处随意修改了Person类的life_val 是不合理的, 因此需要对类的私有属性设置权限，外部不能随意修改
print('Person1 生命值还有',p1.life_val)


class Person2(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__life_val = 100  # 加上2个__ 可以将变量变成私有属性, 外部无法访问

    def get_life_val(self):
        print('get  [%s]生命值还有' % self.name, self.__life_val)
        return self.__life_val

    def attack(self):
        self.__life_val -= 20
        print('attack [%s]生命值还有' % self.name, self.__life_val)
        return self.__life_val

    def __talking(self):            # 对类的方法进行封装
        print('人类可以对话')

    def perform_talking(self):
        self.__talking()
        print('调用__talking方法')


p2 = Person2('P2',26)
# print(p2.__life_val)   此处无法print 出p2.__life_val, 因为__life_val被封装起来了，需要使用类内部的方法对其进行访问或者修改
p2.get_life_val()       # 使用类的内部方式对封装的私有属性进行访问
p2.attack()             # 此处对私有属性进行修改，掉血20
# p2.__talking()        方法被封装了，因此不能从外部进行访问，需要在类的内部使用方法进行调用
p2.perform_talking()

# 强制访问封装的属性与方法
p3 = Person2('P3', 28)
p3.get_life_val()
p3._Person2__talking()          # 强制调用类封装的方法 "变量._类&方法"
print(p3._Person2__life_val)    # 强制调用类封装的属性 "变量._类&属性"
p3.Person2__life_val = 20       # 强制修改类封装的属性
print('p3 life_val = ',p3.Person2__life_val)

p3.__gender = 'Male'            # 实例生成以后再创建私有属性并不具有私有性，是可以直接访问的
print(p3.__gender)
