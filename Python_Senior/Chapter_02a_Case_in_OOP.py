# 人狗大战使用OOP进行编写

class Dog:  # 先创建狗的类

    def __init__(self, name, breed, attack_val, life_val):  # 狗的属性
        self.name = name
        self.breed = breed
        self.attack_val = attack_val
        self.life_val = life_val

    def bite(self, person_o):                               # 狗咬人
        person_o.life_val -= self.attack_val
        print("[%s]狗[%s] 咬了人[%s] 一口，人掉血[%s], 还剩血量[%s]" % (self.breed, self.name, person_o.name, self.attack_val, person_o.life_val))


class Person:   # 创建人的类

    def __init__(self, sexual, name, life_val, attack_val):  # 人的属性
        self.sexual = sexual
        self.name = name
        self.life_val = life_val
        self.attack_val = attack_val

    def Beat(self, dog_o):                                   # 人打狗
        dog_o.life_val -= self.attack_val
        print('[%s]人 [%s] 打了狗[%s]，狗掉血[%s]，还剩血量[%s]' % (self.sexual, self.name, dog_o.name, self.attack_val, dog_o.life_val))


d1 = Dog('alex', '金毛', 10, 100)             # 使用狗的类创建狗的实例
d2 = Dog('dog2', '哈士奇', 30, 80)             # 使用狗的类创建狗的实例

p1 = Person('Male', 'Person1', 100, 20)

# 对象交互
d1.bite(p1)     # 狗咬人
p1.Beat(d1)     # 人打狗
p1.Beat(d2)     # 人打狗
