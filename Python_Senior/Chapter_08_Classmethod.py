"""
    类方法 @classmethod:
        类方法通过@classmethod装饰器实现,类方法和普通方法的区别是类方法只能访问类变量，不能访问实例变量
        @classmethod
        def func(self)    -->   self 不接收实例对象本身，而是接收类本身

"""


class Dog(object):
    name = 'stupid dog'
    def __init__(self, name):
        self.name = name

    def eating1(self):
        print('狗[%s] is eating' % self.name)
        print('self-->', self)

    @classmethod
    def running(self):                  # self 不接收实例对象本身，而是接收类本身
        print('狗[%s] is running ' % self.name)
        # print('classmethod self-->', self)      # 同下面的classmethod 的cls, 为类对象

    @classmethod
    def playing(cls):       # 如果先书写@classmethod后书写def..., 则方法中的self自动换成cls --> class  访问的是类自身的变量
        print('狗[%s] is playing' % cls.name)
        # print('class --> ', cls)        # 同上面的classmethod 的self, 为类对象


d = Dog('Alex')
d.eating1()    # 此处可以访问实例变量 -->  alex
d.running()    # 此处不能访问实例变量alex了, 而是访问类自己的对象相当Dog.name 而不是d.name 并且类对象中如果没有name的时候会报错
print(d)
d.playing()

"""
应用场景:
    class student(object):
        s1 + 1
        s2 + 1 
        s3 + 1  
         
    s3.num --> 3 
    s2.num --> 3
        
        判断要不要num计数关键在于有没有生成新的实例
"""


class Student(object):
    __stu_num = 0                       # 不让程序可以通过外部对类变量进行修改 --> 更改为私有变量

    def  __init__(self, name):
        self.name = name
        # Student.__stu_num += 1           # 如果写在此处的话，每创建一个新的实例对象的时候stu_num + 1, 所以输出s1/s2/s3.stu_num 都显示 1
        # print('生成一个新学生', name, Student.__stu_num)
        self.add_stu(self)          # self 同 下面的obj

    @classmethod
    def add_stu(cls, obj):  # obj --> 代表 self
        if obj:
            cls.__stu_num += 1
            print('生成一个新学生', Student.__stu_num)


s1 = Student('Alex')
s2 = Student('Jeff')
s3 = Student('Wendy')
# Student.add_stu()     此处因为有if判断因此不生效 --> 避免作弊



