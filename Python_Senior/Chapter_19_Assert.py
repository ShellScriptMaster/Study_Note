"""
    Assert 用于判断代码是否符合执行预期
        应用场景
            别人调用你的接口, 你的接口要求他调用时必须传递指定的关键参数, 等参数传入时可以使用assert 判断参数是否符合预期
"""
assert 1 + 1 == 2
assert type(int('2')) == int
# assert 1 + 1 == 3           # AssertionError报错  结果不符合执行预期


def my_interface(name, age, score):
    assert type(name) is str
    assert type(age) is int
    assert 0 <= age <= 100
    assert type(score) is float


my_interface('Jimmy', 20, 0.8)
my_interface('Jacky', 101, 99.9)
