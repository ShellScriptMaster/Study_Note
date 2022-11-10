# 类的继承  子类继承父类  动物与人、狗、猪
class Animal:        # 此处Animal 作为父类供子类继承
    d_type = '动物'   # 父类的属性也可以供子类继承

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        print('父类的init方法')

    def eat(self):
        print('[%s] 在吃东西' % self.name)


class Person(Animal):       # 括号中指定了继承哪个父类，此处继承了Animal
    d_type = '人'            # 此处可以对父类的属性进行修改

    def __init__(self,  name, age, breed, hobby):
        # Animal.__init__(self, name, age, breed)           # 继承父类的init方法
        # super(Person, self).__init__(name, age, breed)    # 同上
        super().__init__(name, age, breed)                  # 同上，only apply at python3
        print('子类的方法')
        self.hobby = hobby

    def study(self):
        print('[%s] 在学习' % self.name)

    def eat(self):
        Animal.eat(self)        # 先执行父类的方法
        print('[%s] 用筷子吃东西' % self.name)        # 自己定义的方法


class Dog(Animal):           # 括号中指定了继承哪个父类，此处继承了Animal

    def __init__(self, name, age, breed, food):
        super(Dog, self).__init__(name, age, breed)
        self.food = food
        print('Dog 重新修改init方法，[%s]喜欢吃[%s]' % (self.name, self.food))

    def sniff(self):
        print('[%s]狗拥有很强的嗅觉' % self.name)


p = Person('Alex', 26, 'Human', '踢球')
p.eat()             # 子类修改了父类的方法
p.study()           # 使用了子类定义的方法
print(p.breed, p.d_type)    # 可以在子类中对父类的属性进行修改
d = Dog('旺财', 2, 'Dog', 'bone')
d.eat()             # 使用了Animal 父类的方法
d.sniff()           # 使用了子类定义的方法
print(d.breed, d.d_type)  # 继承了父类的属性



