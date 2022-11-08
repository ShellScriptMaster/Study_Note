# 依赖关系  主人遛狗


class Dog:
    def __init__(self, name, age, breed, master):
        self.name = name
        self.age = age
        self.breed = breed
        self.master = master
        self.sayhi()

    def sayhi(self):
        # 遛狗
        print("Hi, I'm %s, a %s dog, my master is %s" % (self.name, self.breed, self.master.name))  # 处此产生依赖关系，传入的参数self.master是一个实例对象，此处使用实例对象的name属性


class Person:
    def __init__(self, name, age, gender, dog):
        self.name = name
        self.age = age
        self.gender = gender
        self.dog = dog
        self.walk_dog(dog)

    def walk_dog(self, dog_obj):
        print('主人[%s]带狗[%s]去溜溜' % (self.name, dog_obj))


p1 = Person('Alex', 26, 'Male', '旺财')
d1 = Dog('旺财', 2, '二哈', p1)
