"""
    def __new__(self)
        作用:
            类的实例化过程中, 首先调用__new__ 方法在系统中申请一个内存地址,然后用__init__初始化这个内存空间(往里面填数据),最终这个内存空间以及内部数据组成了一个实例对象
            实例对象:
                空间 --> 由 __new__ 方法申请
                数据 --> 由 __init__ 完成
        用法:
            如果没有定义__new__方法的时候会自动调用父类(object)中定义的__new_方法
            自己定义了__new__方法,一定要调用父类(object)的__new__返回一个实例对象 --> 此处一般用python封装好的__new__方法申请内存空间并且返回
            __new__初始化时可以自己定义类属性以及实例属性, 后续__init__对这些属性进行修改后会对其进行覆盖   class Test_new(object)
            当__new__返回本类的实例对象时会自动调用本类的__init__,但如果__new__返回的不是本类实例对象时,就不调用本类__init__  class Test_self(object)


"""
print('自己定义了__new__方法,一定要调用父类(object)的__new__返回一个实例对象')


class First_new(object):
    def __init__(self,name):
        self.name = name
        print('call __init__')

    def __new__(cls, *args, **kwargs):
        print('call __new__')
        return object.__new__(cls)


test1 = First_new('Jessica')
print(test1.name)
print('-+'*30)


class New(object):
    def __new__(cls, *args, **kwargs):
        return '__new__方法'


t = New()
print(t)                # 实例对象是由__new__ 返回
print('__new__初始化时可以自己定义类属性以及实例属性, 后续__init__对这些属性进行修改后会对其进行覆盖   class Test_new(object)')


class Test_new(object):
    def __new__(cls, *args, **kwargs):
        print('__new__')
        cls.name = '类对象'      # cls 等同于Test_new, 此处为类对象增加一个类属性name
        instance_obj = object.__new__(cls)  # 使用object类的__new__方法返回一个实例对象  instance_obj t调用__init__之前的状态
        instance_obj.obj_name = '实例对象'
        return instance_obj

    def __init__(self, name):
        print('__init__')
        self.name = name      # 覆盖__new__中新建的name属性


t = Test_new('Jessica')
print(t)                    # 先调用__new__ 后调用 __init__
print(Test_new.name)        # 此处返回 cls.name = '类对象'
print(t.__dict__)           # 出现{'obj_name': '实例对象', 'name': 'Jessica'}  实例属性有2个, 一个是instance_obj.obj_name = '实例对象' 另一个是  self.name = name
print(t.__class__.name)     # 查看t的类的name属性
print(t.name, t.obj_name)
print('__new__返回本类的实例对象时会自动调用本类的__init__,但如果__new__返回的不是本类实例对象时,就不调用本类__init__  class Test_self(object)')


class Test_self(object):
    def __new__(cls, *args, **kwargs):
        print('call __new__')
        return super().__new__(cls)

    def __init__(self):
        print('call __init__')


self_obj1 = Test_self()  # 先调用__new__ 后调用__init__
print('-'*30, 'Test_other', '-'*30)


class Foo(object):
    name = 'Foo'

    def __new__(cls, *args, **kwargs):
        print('call Foo.__new__')
        return super().__new__(cls)         # 返回一个实例化对象

    def __init__(self):
        print('call Foo.__init__')
        self.name = 'Foo'                   # 以Foo()形式返回其他类的实例对象时,会调用其他类的__init__  相当于先对Foo()进行一次实例化赋值返回给self_obj2


class Test_other(object):
    def __new__(cls, *args, **kwargs):
        print('call __new__')
        # return object.__new__(Foo)     # 返回的是由Foo 创建的实例
        return Foo()

    def __init__(self):                 # __init__ 方法失效
        print('call __init__')
        self.name = 'Jessica'


self_obj2 = Test_other()   # 由于__new__ return了Foo(), 此处相当于 self_obj2 = Foo()

print(self_obj2)
print(self_obj2.name is Foo.name)               # 此处 self_obj2.name == Foo.name
print('-'*30, '单例设计模式', '-'*30)


class Windows(object):
    # 确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例，这个类称为单例类，单例模式是一种对象创建型模式
    task = []
    instance = None

    def __init__(self, name):
        self.name = name

    def print_task(self, job_name):
        self.task.append(job_name)
        print('应用 [%s] 添加打印任务 [%s] 到打印机, 总任务数 [%s]' % (self.name, job_name, len(self.task)))

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            obj = object.__new__(cls)
            print('obj', obj)
            cls.instance = obj
        return cls.instance
        # 第一次执行的时候生成实例对象 obj = object.__new__(cls) 并且存到cls.instance里, 后续都没有新的实例对象产生
        # 因此每次调用__init__相当于修改了 self.name 三次  所以最后print的 self.name 显示都是 p3.name 的值


p1 = Windows('Word')
p2 = Windows('PDF')
p3 = Windows('Excel')
p1.print_task('Word file')
p2.print_task('PDF file')
p3.print_task('Excel file')
print(p1, p2, p3)
print(p1.name, p2.name, p3.name)
