"""
    def __call__():   call 方法
        凡是可调用对象(类, 方法)都可以通过__call__()方法来调用该对象
        如果类中定义了__call__()方法, 则该类生成的实例对象也可以进行调用. 调用实例对象时, 执行__call__()下的方法

"""


def call_test():
    print('Function call_test is called')


print(callable(call_test))  # 函数是可以被调用的对象
call_test()                 # 调用
call_test.__call__()        # 同样可以使用__call__()方法对函数进行调用


class Call_test(object):
    def __init__(self, name):
        self.name = name
        print('__init__')


a = Call_test('Jessica')
print('a是否可以被调用: ', callable(a))            # 没有定义__call__ 方法的时候实例对象不能被调用


def __call__(self, *args, **kwargs):
    print('call : __call__ ')
    print('obj_name = %s __call__' % self.name)


setattr(Call_test, '__call__', __call__)        # 给Call_test()类添加一个__call__()方法
print(hasattr(Call_test, '__call__'))           # 确认Call_test()类存在__call__()方法

b = Call_test('Kristy')                         # 重新实例化
print('b是否可以被调用: ', callable(b))            # 在类中定义了__call__方法后实例对象可以被调用
b()                                             # 实例作为被调用对象进行调用时自动执行__call__方法定义的内容





