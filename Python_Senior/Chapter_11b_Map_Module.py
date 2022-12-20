class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print('%s is walking' % self.name)


def speak(self):
    print('%s is speaking' % self.name)


def cook():
    print('cooking testing')


p1 = Person('Alex', 23)
p1_walk = getattr(p1, 'walk')
p1_name = getattr(p1, 'name')
print(p1_name)
p1_walk()

setattr(Person, 'speak', speak)

p2 = Person('Bob', 25)
p2_speak = getattr(p2, 'speak', None)
p2_speak()

# __name__ 和 __main__
print(__name__)
if __name__ == '__main__':          # 当且仅当此模块未被导入的时候, __name__ 才等于 __main__
    print('__name__ == __main__')
