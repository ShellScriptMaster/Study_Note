"""
    isinstance(obj, cls)
        检查obj是否是类cls的对象
    issubclass(sub, super)
        检查sub是否是super类的派生类/ super 是否是sub的父类

"""


class Person(object):
    name = 'Jessica'
    pass


a = Person()
print(isinstance(a, Person))


class A(object):
    pass


class B(A):
    pass


print(issubclass(B, A))
print(issubclass(B, Person))