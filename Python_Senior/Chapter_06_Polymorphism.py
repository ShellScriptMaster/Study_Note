# 类的特性 多态
"""
    有时候一个类会有多种表现形式，比如网站页面有个button按钮，这个button按钮的设计可以不一样（单选框、多选框、勾选按钮，提交按键），尽管形状不同
    但他们都有一个共同的调用方式就是 onClick()方法。只要在页面上点击就会触发这个方法，点击后有的会变成选中形态，有的会提交表单，有的会弹窗。
    这种多个对象共用一个接口，又表现的形态不一样的现象，称为多态（Polymorphism）
"""

# 多态代码演示


class Dog(object):
    def sound(self):
        print('汪汪汪')


class Cat(object):
    def sound(self):
        print('喵喵喵')


def make_sound(Animal_type):        # 一般使用抽象类来实现多态
    # 统一调用接口
    Animal_type.sound()    # 无论传进来什么动物都调用sound方法


dog1OBJ = Dog()
cat1OBJ = Cat()

make_sound(dog1OBJ)
make_sound(cat1OBJ)

# 一个文本编辑器支持多文档类型，用户打开文件前不清楚是什么文件类型，word/pdf. 如果为每个文件类型写一个类，每个类通过show()方法来调用打开对应的文档
# 为了确保每个类都必须实现show()方法，可以写一个抽象类


class Document(object):
    def __init__(self,filename):
        self.name = filename

    def show(self):         # 让子类重写这个方法，
        raise NotImplementedError("Subclass must implement abstract method")  # 手动进行报错  强制用户不能调用Document的show()方法


class PDF(Document):
    def show(self):
        return "Show pdf contents !!!"


class Word(Document):
    def show(self):
        return "Show Word contents !!!"


# docObj = Document('Document_obj.doc')
# print(docObj.show())         手动报错，让用户不能使用Document的show()方法

pdfObj = PDF('pdf_obj.pdf')
wordObj = Word('Word_obj.docx')

for i in [pdfObj, wordObj]:
    print(i.show())     # 不同对象调用的方法不同
