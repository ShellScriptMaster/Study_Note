# 组合关系  人狗大战中加入武器

class Dog:

    def __init__(self, name, age, breed, attack_val, life_val):
        self.name = name
        self.age = age
        self.breed = breed
        self.attack_val = attack_val
        self.life_val = life_val

    def bite(self, person_obj):
        person_obj.life_val -= self.attack_val
        print('狗[%s]咬了人[%s],人掉血[%s],还剩血量[%s]' % (self.name, person_obj.name, self.attack_val, person_obj.life_val))


class Person:
    def __init__(self, name, age, gender, life_val):
        self.name = name
        self.age = age
        self.gender = gender
        # self.attack_val = attack_val   因为有武器库所以不需要单独定义人的攻击力了
        self.weapon = Weapon()    # 直接通过武器库定义人的攻击力, 此处直接对Weapon进行实例化
        self.life_val = life_val

    def beat(self, dog_obj): # 使用武器库以后，此方法已经不调用
        dog_obj.life_val -= self.attack_val
        print('人[%s]打了狗[%s],狗掉血[%s],还剩血量[%s]' %(self.name, dog_obj.name, self.attack_val, dog_obj.life_val))


class Weapon:  # 定义武器,单独不能运行，需要与人进行关联
    def dog_stick(self, obj):
        self.name = '打狗棒'
        self.attack_val = 40
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def knife(self, obj):
        self.name = '屠龙刀'
        self.attack_val = 80
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def gun(self, obj):
        self.name = 'AK47'
        self.attack_val = 100
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def print_log(self,obj):
        print('[%s] 被 [%s] 攻击了，掉血[%s]， 还剩血量[%s]' %(obj.name, self.name, self.attack_val, obj.life_val))


d = Dog('旺财', 2, '二哈', 20, 100)
p1 = Person('Alex', 23, 'Male', 100)
d.bite(p1)
p1.weapon.gun(d)  # 直接调用Weapon的gun
p1.weapon.knife(d)

