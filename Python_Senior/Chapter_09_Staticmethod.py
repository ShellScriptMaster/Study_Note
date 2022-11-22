"""
    静态方法 @Staticmethod:
        类方法通过@Staticmethod装饰器实现, 不能访问类变量,也不能访问实例变量
        @Staticmethod
        def func(self):

        静态方法隔断了它跟类和实例的任何关系


"""


class Student(object):
    role = 'Stu'

    def __init__(self, name):
        self.name = name

    @staticmethod
    def fly(self):
        print(self.name, 'is flying')
        print(Student.role)

    @staticmethod
    def walk():
        print('student is walking')


s = Student('Alex')
# s.fly()  此处因为静态方法装饰的缘故, 不能访问实例变量
s.fly(s)    # 需要手动传入self 实例
Student.walk()
s.walk()        # 可以进行调用, 但是如果有参数则需要手动传入
