# 两大编程思想
"""
    面向过程
    面向对象
"""
# 类和对象的创建
"""
    class
        是多个类似事物组成的群体的统称，能够帮助我们快速理解和判断事物的性质
        不同数据类型属于不同的类，可以使用内置函数 type() 查看数据类型
        class class_name:    类名可以由一个或多个单词组成，每个单词的首字母大写，其余小写
            执行语句
    object
        10,20,30 都是int类下包含的相似的不同个例，这些个例称为对象或实例
        python 一切皆对象, class 也是对象
"""
########################################################################################################################

# 类的创建 以及 类组成
class Jessica:
    pass
print(type(Jessica))
print(id(Jessica))
print(Jessica)
print('--'*30)
"""
    class 组成
        类属性
            类中的方法外的变量称为类属性，被该类的对象所共享
        实例方法
        静态方法
            使用@staticmethod修饰的方法，使用类名直接访问的方法
        类方法
            使用@classmethod修饰的方法，使用类名直接访问的方法
"""
class Student:
    native_place = 'JiLin'              # 写在类里面的变量称为类属性

    def __init__(self,name,age):        # 初始化方法，()里面可以继续写对象名
        self.name=name                  # name --> 局部变量, self.name实例属性，此处进行了赋值操作,将局部变量的值赋给了实体属性
        self.age=age                    # age  --> 局部变量, self.age 实例属性，此处进行了赋值操作,将局部变量的值赋给了实体属性

    def eat(self):                      # 实例方法。 在类以外定义的称为函数，类内定义的称为函数
        print('Eating Hot Pot.')

    @staticmethod                       # 使用staticmethod 修饰的为静态方法
    def static_method():
        print('Using staticmethod, hence this is 静态方法')

    @classmethod                       # 使用classmethod 修饰的为类方法
    def class_method(cls):
        print('Using classmethod, hence this is 类方法')


def eat():                             # 在类外创建的为函数Function
    print('Function Eating. Out of class')
########################################################################################################################

# 创建类对象  --> 类的实例化   有了实例，就可以调用类中的内容
# 实例名 = 类名()                 # 实例对象的类指针指向了类对象
Stu = Student('Jessica',20)     # 相当于调用了Student 类中的 init 方法, 由于init方法中有2个参数则需要填上
print(Stu)                      # 相当于输出对象的内存地址(十六进制)
print(id(Stu))                  # 此处将Mem_id 转换为十六进制可得  输出对象的值
print(type(Stu))

print('--'*30)

# 查看类对象的信息
print(id(Student))
print(type(Student))
print(Student)

print('--'*30)
########################################################################################################################

# 使用Student类的方法
stu1 = Student('Jessica',23)
stu1.eat()                     # 调用了类的方法 对象名.方法名()
print(stu1.name)
print(stu1.age)
stu1.static_method()
stu1.class_method()

print('--'*30)

Student.eat(stu1)              # 调用类方法 与 stu1.eat()功能一致  类名.方法名(类的对象)

print('--'*30)

# 调用类属性 --> 类里面的变量
print(stu1.native_place)
print(Student.native_place)
stu2 = Student('Tom',33)
stu3 = Student('Kristy',25)
print(stu2.native_place)
print(stu3.native_place)
print('--'*30)
Student.native_place = 'TianJin'
print(stu2.native_place)
print(stu3.native_place)

print('--'*30)
# 类方法使用方式
Student.class_method()
# 静态方法使用方式
Student.static_method()

########################################################################################################################
print('--'*30)
# 动态绑定属性和方法   py是一门动态语言，创建对象后可以动态地绑定属性和方法
class YourInfo:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def eat(self):
        print(self.name + ' is Eating')
stu4 = YourInfo('Jessica',20)
stu5 = YourInfo('Kristy',23)
print(stu4.name,stu4.age)
print(stu5.name,stu5.age)
stu4.eat()
stu5.eat()
print('--'*30)
# 一个YourInfo类可以创建N个YourInfo实例对象，每个实体对象的属性值不同
# 需求: 需要为且仅为stu5增加一项属性 gender = 'girl'，此时需要动态绑定属性和方法

# 动态绑定属性
stu5.gender = 'girl'
print(stu5.name, stu5.age , stu5.gender)
# print(stu4.name, stu4.age , stu4.gender)  -->  AttributeError: 'YourInfo' object has no attribute 'gender'
# 仅为stu5绑定一个属性，没有为stu4绑定属性

# 动态绑定方法
# 正常情况下 stu4 stu5均可以调用 YourInfo 类的 eat方法
stu4.eat()
stu5.eat()

# 先定义一个类外的方法
def show():
    print('Show function! ------>  define out of YourInfo Class')

stu4.show = show()
stu4.show               # 单独为stu4定义的一个方法，
# stu5不能使用show()方法  AttributeError: 'YourInfo' object has no attribute 'gender'


