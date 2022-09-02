"""
    面向对象的三大特征：  --> 适用所有的编程语言
        封装: 提高程序的安全性 (Encapsulation)
            将数据(属性)和行为(方法)包装到类对象中。
            在方法内部对属性进行操作，在类对象的外部调用方法
            如此，不必关心方法内部的具体实现细节，从而隔离了复杂度
            python中没有专门修饰符用于属性的私有，如果该属性不希望在类对象外部被访问，前面使用2个'_'
        继承: 提高代码复用性 (Inheritance)
            如果一个类没有继承任何类，则默认继承object
            python支持多继承
            定义子类时，必须在其构造函数中调用父类的构造函数

            * 方法重写
                如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其方法体进行重新编写
                子类重写后的方法可以通过super(),xxx()调用父类中被重写的方法
            * object类
                object类是所有类的父类，因此所有类都有object类的属性和方法
                内置函数dir()可以查看指定对象所有属性
                object有一个_str_()方法，用于返回一个对于'对象的描述'，对应内置函数str()经常用于print()方法，帮助我们查看对象的信息，因此我们经常对_str_进行override
        多态: 提高程序的可扩展性和可维护性 (Polymorphism)
            即使不知道一个变量所引用的对象到底是什么类型，仍然可以通过这个变量调用方法，在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象的方法
    特殊方法和特殊属性
        特殊属性：
            _dict_  获得类对象或实例实例对象所绑定的所有属性和方法的字典
        特殊方法：
            _len_() 通过重写_len_()方法，使内置函数len()的参数可以是自定义类型
            _add_() 通过重写_add_()方法，可使用自定义对象具有'+'功能
            _new_() 用于创建对象
            _init_()对创建的对象进行初始化
"""
########################################################################################################################

# Encapsulation  封装
class Car:                      # 创建一个类对象
    def __init__(self,brand):
        self.brand = brand
    def Start(self):
        print('Start a Car')

car1 = Car('BMW X5')
car1.Start()                    # 在类外部使用类封装的方法
print(car1.brand)               # 在类外使用类封装的属性

print('--'*30)

class Student:                       # 创建一个类对象
    def __init__(self,name,age):     # 创建一个init方法,并且方法内有name和age属性
        self.__age = age             # 不希望age被外部使用，因此加了2个'_'
        self.name = name
    def get_age(self):
        print(self.name, self.__age )
    def set_age(self,age):
        if 0 <= age <= 120:
            self.__age = age
        else:
            self.__age = 18
stu1 = Student('Kristy',20)
stu2 = Student('Jesica',23)
stu1.get_age()                      # 在类的外部使用name 和 age
print(stu1.name)
# print(stu1.__age)                 # __的变量不能在类的外部被使用
# 如何使用__定义的类的内部属性
print(dir(stu1))                    # 使用dir查看类的内部属性与方法 --> 找到了   _Student__age
print(stu1._Student__age)           # 可以获取到__age属性了
########################################################################################################################

print('--'*30)
# Inheritance 继承
"""
class 子类(父类1，父类2)
    pass
"""
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def info(self):
        print('name:{0}, age:{1}'.format(self.name,self.age))
# 先定义父类 --> Person
class Student_A(Person):        # 继承Person 父类
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)      # 调用super类的init方法
        self.stu_no = stu_no

class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teacherofyear = teachofyear

stu3 = Student_A('Tim',23,3115003949)
stu3.info()                     # 从父类(Person)中继承了info方法

# object 类 <--继承-- Person 类  <--继承-- Student_A 类 & Teacher 类

stu4 = Student_A('Albert',12,3115003949)
tch1 = Teacher('Pual',31,8)
stu4.info()
tch1.info()

# 多继承
class A(object):
    pass
class B(object):
    pass
class C(A,B):           # C 有2个父类(A,B)
    pass

# 方法重写  子类需要输出自己独有的属性(stu_no,teachofyear)，父类方法(info)不支持的时候，需要对子类进行重写
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def info(self):
        print('name:{0}, age:{1}'.format(self.name,self.age))
# 先定义父类 --> Person
class Student_A(Person):        # 继承Person 父类
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)      # 先调用Person的init方法
        self.stu_no = stu_no            # 新增加stu_no属性
    def info(self):                    # Overrides method 方法覆写
        super().info()           # 使用super().info()调用父类的方法
        print('stu_no:{0}'.format(self.stu_no)) # info新增的方法，因此输出是两行，一行是原来的info，一行是此行的代码

class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)          # 先调用Person的init方法
        self.teacherofyear = teachofyear    # 新增加teachofyear属性
    def info(self):
        super().info()
        print('teachofyear:{0}'.format(self.teacherofyear))
stu5 = Student_A('Tim',22,3115003949)
stu5.info()
tch2 = Teacher('Paul',38,8)
tch2.info()
print('--'*30)

# object 类
class Student_B:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def __str__(self):      # 重写object父类的方法
        return 'my name is {0}, I am {1} years old'.format(self.name,self.age)

stu6 = Student_B('Vincent',29)
print(dir(stu6))            # 查看object的属性和方法
print(stu6.__str__())       # __str__ 未重写前，查看对象的内存地址  --> 重写后，此时不会输出对象内存地址
print(stu6)                 # 默认会调用__str__的方法
print(type(stu6))           # 类型是Student_B的类
########################################################################################################################

print('--'*30)
# 多态   即使不知道一个变量所引用的对象到底是什么类型，仍然可以通过这个变量调用方法，在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象的方法

class Animal(object):
    def eat(self):
        print('Animal will eat sth')
class Dog(Animal):
    def eat(self):
        print('Dog eat meat')
class Cat(Animal):
    def  eat(self):
        print('Cat eat fish')
class Human(object):
    def eat(self):
        print('People eat rice')
# 定义一个函数fun
def fun(sth):
    sth.eat()
# 开始调用函数fun
fun(Cat())          # --> Cat().eat()
fun(Dog())          # --> Dog().eat()
fun(Human())        # --> Human().eat()
fun(Animal())       # --> Animal().eat(）
print('--'*30)

"""
    静态语言与动态语言关于多态的区别
    静态语言实现多态三个必要条件
        继承
        方法重写(override)
        父类引用指向子类对象
    动态语言多态崇尚'鸭子类型':当一只鸟各种行为看起来像鸭子时，这只鸟就可以被称为鸭子。在此类型中不需要关心对象是什么类型，只关心对象行为
"""
########################################################################################################################

# 特殊方法和特殊属性
"""
        特殊属性：
            _dict_  获得类对象或实例实例对象所绑定的所有属性和方法的字典
        特殊方法：
            _len_() 通过重写_len_()方法，使内置函数len()的参数可以是自定义类型
            _add_() 通过重写_add_()方法，可使用自定义对象具有'+'功能
            _new_() 用于创建对象
            _init_()对创建的对象进行初始化
"""
print(dir(object))
class B :
    pass
class C:
    pass
class D(B,C):
    def __init__(self,name,age):
        self.name = name
        self.age  = age
class E(B):
    pass
# 特殊属性
x = D('Jack',20)       # x 是C类的一个实例对象
print(x.__dict__)      # 查看此实例对象绑定了哪些属性(name,age)
print(D.__dict__)      # 查看类对象的属性
print(C.__dict__)      # 查看类对象的属性
print('--'*30)
print(x.__class__)          # 输出对象所属的类
print(D.__bases__)          # 以元组形式输出所有的父类
print(D.__base__)           # 输出一个父类D(B,C)  --> 谁写前面就输出谁  --> 输出B
print(D.__mro__)            # 输出类的层次结构
print(B.__subclasses__())   # 输出此类下的所有子类
print('--'*30)

# 特殊方法
# __add__()方法
a = 20
b = 100
c = a + b       # 2个整数类型的对象相加
d = a.__add__(b)    # 底层原理
print(c)
print(d)

class Student_C:
    def __init__(self,name,):
        self.name = name
    def __add__(self, other):           # 在Student类中支持了add方法
        return self.name+other.name
stu7 = Student_C('Jacky')
stu8 = Student_C('Jessica')
s = stu7 + stu8           # 不能单纯相加 在Student类中支持了add方法，因此可以进行相加操作
print(s)
s = stu7.__add__(stu8)    # 调用了 Student_C 类中的add方法
print(s)
print('--'*30)

# __len__()方法
lst1 = [11,22,33,44]
print(len(lst1))            # 内置函数len计算列表长度
print(lst1.__len__())
class Student_C:            # 原Student_C 没有__len__()方法，因此需要进行添加
    def __init__(self,name,):
        self.name = name
    def __len__(self):
        return len(self.name)
stu7 = Student_C('Jessica')
print(stu7.__len__())
length = stu7.__len__()
print(length)
print('--'*30)

# __new__() 方法  --> 创建对象
class Person_A:

    def __new__(cls, *args, **kwargs):              # 创建对象
        print('__new__ is called and excuted, cls_id is {0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('Create a Object id is {0}'.format(id(obj)))
        return obj
    def __init__(self,name,age):                    # 为创建的对象进行初始化赋值
        print('__init__ is called and excuted, self_id is {0}'.format(id(self)))
        self.name = name
        self.age  = age
print('object class id is {0}'.format(id(object)))
print('Person_A class id is {0}'.format(id(Person_A)))   # 与__new__.cls_id一致

# 创建Person_A 实例对象
per1 = Person_A('Jacky',23)
per1
"""
    per1 --> 直接跑 __new__ 和 __init__ 方法, 然后再输出 per1这个实例的id
    __new__
        print(__new__.cls_id)  --> A  与Person_A类的id一致
        创建一个obj，obj是继承 object_class的 __new__方法
            此时obj_id 为B
    __init__
        print(__init__.self_id)  --> B
    per1 实例id
        print(per1_id) --> B
"""
print('per1 id is {0}'.format(id(per1)))   # 先执行per1内部的函数，然后执行print(per1.id)
print('--'*30)
########################################################################################################################

# 类的浅拷贝与深拷贝
"""
    变量的赋值操作
        形成多个变量，实际上还是指向同一个对象
    浅拷贝
        py拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝。因此源对象与拷贝对象会引用同一个子对象
    深拷贝
        使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同
"""
# 变量的赋值操作
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu = cpu
        self.disk = disk
# 变量的赋值
cpu1 = CPU()
cpu2 = cpu1             # cpu1 与 cpu2 两个变量都指向了同一个对象  CPU()
print(cpu1)
print(cpu2)
print('--'*30)

# 类的浅拷贝
disk1 = Disk()
computer1 = Computer(cpu1,disk1)
import  copy
computer2 = copy.copy(computer1)                # 拷贝了computer1以后，computer1 与 computer2 为2个对象
print(computer1,computer1.cpu,computer1.disk)   # computer1.cpu 与 computer2.cpu都指向了Cpu()        共用一个子对象
print(computer2,computer2.cpu,computer2.disk)   # computer1.disk 与 computer2.disk 都指向了Disk()    共用一个子对象
print('--'*30)


# 类的深拷贝
import copy
cpu1 = CPU()
cpu2 = cpu1
disk1 = Disk()
disk2 = disk1

computer1 = Computer(cpu1,disk1)
computer2 = copy.deepcopy(computer1)            # 源对象computer1 与拷贝对象computer2为2个对象
print(computer1,computer1.cpu,computer1.disk)   # computer1.cpu 与 computer2.cpu 地址不同，computer1 和 computer2 的子对象不同
print(computer2,computer2.cpu,computer2.disk)   # computer1.disk 与 computer2.disk 地址不同，computer1 和 computer2 的子对象不同








