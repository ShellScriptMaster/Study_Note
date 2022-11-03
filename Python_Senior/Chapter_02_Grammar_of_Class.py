class Dog:
    d_type = "京巴"  # 属性，类属性，类变量   是公共属性，下面所有实例共享的属性。 相当于存在类里面的内存里
    d_sexual = "Male"

    def __init__(self, name, age):   # 初始化方法,构造方法,实例化时会自动进行一些初始化工作. 可以在初始化方法里面定义一些私有的属性
        print('hhhhh', name, age)
        #  如果想要把name age 2个值 真正存入到实例中，那就需要把2个值跟实例进行绑定. 将init 中的name, age 2个参数绑定到self本身
        self.name2 = name   # 绑定参数值到实例 (d2.name2 = name/d.name = name) 原先2个方法是独立的，此处打通了两个方法之间的关系，
        self.age2 = age

    def sayhi(self):    # 类中的函数叫 方法 , self 代表实例本身. 如果没有写self，那这个方法不知道是哪个实例在调用它，因此类下每个方法第一个参数都要是self, 是为了接受实例这个对象本身(self == this)
        print("hello , I am a Dog, my type is ",self.d_type,self.name2, self.age2)    # 由于在init方法中定义的参数与实例进行了绑定, 所以此处可以进行调用
    # 此处 类 已经写完，接下来需要进行实例化


d = Dog('Alex', 2)    # 生成了一个实例,有自己的内存空间   参数自动传到初始化函数中
d2 = Dog('Tommy', 3)  # 生成了一个实例,有自己的内存空间  参数自动传到初始化函数中

d.sayhi()   # 调用  实例.方法
d2.sayhi()  # d2.sayhi(d2)  自动把d2传参进去
print("d2 本身：", d2)

print(d.d_type, d.d_sexual)
print(id(d.d_type), id(d2.d_type))
print(id(d), id(d2))

d.color = "red"     # 可以在类外面给实例赋值 (相当于在init 中增加传参color)
print(d.color)

Dog.d_type = "哈士奇"       # 如果修改公共属性 d_type , 所有实例输出都会改变
print(d.d_type, d2.d_type)

################################################################################################################
# 属性引用
# 类属性, 类变量, 公共属性  所有实例共享
# 实例属性, 实例变量, 成员变量, 每个实例独享

# 类属性的引用与修改  针对类属性进行的修改会应用到类的所有实例中
Dog.d_type='金毛'
print(d.d_type)
print(Dog.d_type)
print(d2.d_type)
print('*'*30)


class People:
    Nationality = 'CN'

    def __init__(self, name, sexual, age):
        self.name = name
        self.age = age
        self.sexual = sexual
        print(self.name, self.sexual, self.age)


Person1 = People('Jimmy', 'Male', 23)
Person2 = People('Cindy', 'Female', 24)
print(Person2.Nationality, Person1.Nationality)

Person1.Nationality = 'USA'         # 可以修改Person1 单独的国籍，相当于self.Nationality = 'USA'
Person2.Nationality = 'UK'          # 可以修改Person2 单独的国籍，相当于self.Nationality = 'UK'
print('对象属性', Person2.Nationality, Person1.Nationality)
print('类属性', People.Nationality)           # 实例修改的属性属于自己的实例属性，不会对类属性产生影响

# 实例属性的引用与修改   实例属性不能通过类调用，只能通过实例进行调用
print('*'*30)
# print(Dog.name2)   --> Error
d.name2 = 'Jack'
d.color = 'Gold'
print(d.name2, d.color)



