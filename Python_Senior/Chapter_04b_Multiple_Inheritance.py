# 多继承(Only available on Python, C++. Not available on Java)
# 孙悟空既是神仙也是猴子，同时继承了2个类
class Base:
    def fight(self):
        print('Base 打架')


class ShenXianBase(Base):
    # def fight(self):
    #     print('神仙始祖打架')
    pass


class ShenXian(ShenXianBase):       # 继承ShenXianBase
    def fly(self):
        print('神仙都会飞')

    # def fight(self):
    #     print('神仙打架')


class MonkeyBase(Base):
    def fight(self):
        print('猴子始祖打架')


class Monkey(MonkeyBase):           # 继承MonkeyBase
    def eat_peach(self):
        print('猴子都喜欢吃桃')

    def fight(self):
        print('猴子打架')


class MonkeyKing(ShenXian, Monkey):  # 同时继承2个类，比较少用
    def play_golden_stick(self):
        print('孙悟空会用金箍棒')


sun = MonkeyKing()
sun.fly()
sun.eat_peach()
sun.play_golden_stick()
# 多继承可以使用多个方法

sun.fight() # 继承父类的方法有顺序，从左到右的顺序继承
"""
    因为继承顺序从左往右，所以继承的还是ShenXian的类方法, 由于在ShenXian类中对fight()方法重新定义为'神仙打架', 因此此处返回的结果依旧是'神仙打架'
    如果ShenXian中没有fight方法，则直接使用ShenXian的父类中定义的fight (深度优先)
    如果ShenXian & ShenXianBase 都没有fight方法，则直接继承Monkey的fight方法 (广度优先)
"""
# 类的2种写法: 经典类 & 新式类


class Classic:            # 经典类
    pass


class New(object):       # 新式类  所有的python类都是从object类演变出来，python3两种写法都当作新式类
    pass

# 多继承顺序
# python2.3 以前，经典类采用的是深度优先查找法，新式类采用的是广度优先
# python3   中，无论经典类还是新式类，都是按广度优先查找  (多继承C3算法)
class A:
    def test(self):
        print('from A')
    pass

class B1(A):
    def test(self):
        print('from B1')
    pass


class B2:
    def test(self):
        print('from B2')
    pass


class C1(A):
    def test(self):
        print('from C1')
    pass


class C2:
    def test(self):
        print('from C2')
    pass


class D(B1,B2):
    def test(self):
        print('from D')
    pass


class E(C1,C2):
    def test(self):
        print('from E')
    pass


class F(D, E):
    def test(self):
        print('from F')
    pass


a = F()
a.test()
# 继承顺序 F-->D-->E-->B1-->E-->C1-->A-->B2-->C2  可以使用命令 print(F.mro()) 进行查看

