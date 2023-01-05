"""
    重点双下划线方法：
        def __str__(self):      使实例对象输出特定的返回值( 终端中使用print(obj) 返回obj.__str__() )
        def __repr__(self):     使实例对象输出特定的返回值( 终端中优先返回 obj.__repr__() )
        def __del__(self):      删除实例对象释放内存, 不使用del进行手动删除的话,程序最后也会自动执行 del方法
"""


class Str_test(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        return 'from __str__ %s' % self.name

    def __repr__(self):
        return 'from __repr__ %s' % self.gender

    def __del__(self):
        print('删除对象 %s, 释放内存 ' % self.name)


p1 = Str_test('Jessica', 'female')
p2 = Str_test('Kristy', 'female')
del p2          # 直接使用del方法对p2实例对象进行删除
print(p1)       # 如果没有__str__ 或 __repr__ 的话，输出结果为 <__main__.Str_test object at 0x0000029152097C70>  此处优先输出 p1.__str__()
print(p1.__str__())
# del p1
print(p1.__repr__())
del p1

