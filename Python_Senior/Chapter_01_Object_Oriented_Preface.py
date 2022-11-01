# 人狗大战
"""
    Dog Properties:
        name
        d_tpye
        attack_val
        Color
"""
# 使用字典生成一条狗以及定义属性

dog = {
    "name":"A",
    "d_type":"JingBa",
    "attack_val":30
}
def Bite(Person_obj):
    Person_obj.life_val -= 30
#############################################################################################################################

# 此时狗不只有A,还应该有很多狗，并且狗的属性都只有 name,d_type, 只是字典的值不同，此处用函数可以减少重复代码量
# 通过函数定义一个狗的模板

def dog(name,d_type):
    data = {
        "name": name,
        "d_type": d_type,
        "life_val": 100
    }
    return data

d1 = dog("A",'Jingba')
d2 = dog("B",'Zangao')
print(d1,d2)

#############################################################################################################################
# 可以根据不同狗的d_type 自动赋值attack_val

attack_val = {
    "Jingba":30,
    "Zangao":80
}

def dog(name,d_type):
    data = {
        "name":name,
        "Type":d_type,
        "life_val": 100
    }

    if d_type in attack_val:
        data["attack_val"] = attack_val[d_type]
    else:
        data["attack_val"] = 15  # 默认攻击力
    return data
d1 = dog("A",'Jingba')
d2 = dog("B",'Zangao')
print(d1,d2)

#############################################################################################################################
# 生成人的属性
def Person(name,age):
    data = {
        "name":name,
        "age":age,
        "life_val":100
    }
    if age > 18 :
        data["attack_val"] = 50
    else:
        data["attack_val"] = 30
    return data
d1 = dog("A",'Jingba')
d2 = dog("B",'Zangao')

p1 = Person("Jacky",20)
print(d1,d2)
print(p1)

#############################################################################################################################
# 狗咬人动作
def dog_bite(dog_obj,person_obj):
    person_obj["life_val"] -= dog_obj ["attack_val"]   # 执行咬人
    print("狗[%s]咬了人[%s]一口, 人掉血[%i],还有血量[%i] "%(dog_obj['name'],person_obj['name'],dog_obj['attack_val'],person_obj['life_val']))

dog_bite(d1,p1)

# 人打狗动作
def person_beat(person_obj,dog_obj):
    dog_obj["life_val"] -= person_obj["attack_val"]
    print("人[%s]打了狗[%s]一下，狗掉血[%i],还有血量[%i] " %(person_obj['name'],dog_obj['name'],person_obj['attack_val'],dog_obj['life_val'] ))

person_beat(p1,d1)


