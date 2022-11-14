class MasterSchool(object):  # 发工资，统计员工人数，统计学生人数，新学生注册
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.branches = {}
        self.__staff_list = []
        self.__stu_list = []

    def staff_onboard(self, staff_obj):
        self.__staff_list.append(staff_obj.staff_name)

    def count_staff(self):
        pass

    def count_stu(self,):
        pass

    def get_staff_list(self):
        print(self.__staff_list)


class BranchSchool(MasterSchool):  # 发工资，统计员工人数，统计学生人数，新学生注册，所属上级校区
    def __init__(self, name, address, master_obj):
        super(BranchSchool, self).__init__(name, address)
        self.name = name
        self.address = address
        self.master_obj = master_obj
        self.master_obj.branches[name] = master_obj.name

    def echo_master(self):
        print('总校是[%s],此为[%s]分校, 地址是[%s]' % (self.master_obj.name, self.name, self.address))

    def pay_staff(self):
        print('[%s]课程[%s]校区发工资！' % (self.name, self.address))


class Course(object):
    def __init__(self, course_name, course_price):
        self.course_name = course_name
        self.course_price = course_price


class Class():
    def __init__(self, course_obj, school_obj, class_num):
        self.course_obj = course_obj
        self.class_num = class_num
        self.school_obj = school_obj

    def class_begin(self):
        print('class %s is beginning' % self.course_obj.course_name)

    def get_class_num(self):
        print('this class num is [%s]学校[%s]课程[%s]期' %(self.school_obj.name,self.course_obj.course_name, self.class_num))




class Students(object):
    def __init__(self, name, age, class_obj):
        self.name = name
        self.age = age
        self.class_obj = class_obj

    def drop_out(self, stu_obj):
        print('%s 申请退学，退款%s' % (stu_obj.name, self.class_obj.course_obj.course_price))

class Staff(object):
    def __init__(self, staff_name, age, salary, department, position, school_obj):
        self.staff_name = staff_name
        self.age = age
        self.salary = salary
        self.position = position
        self.department = department
        self.school_obj = school_obj
        school_obj.staff_onboard(self)  # 用的时候需要指定name，否则是将整个对象加入列表


class Teacher(Staff):

    def __init__(self, staff_name, age, salary, department, position, school_obj, class_obj):
        super(Teacher, self).__init__(staff_name, age, salary, department, position, school_obj)
        self.class_obj = class_obj

    def teaching(self):
        print('[%s]老师在[%s]班教[%s]课程' % (self.staff_name, self.class_obj.class_num, self.class_obj.course_obj.course_name))


# 初始化总校
master1 = MasterSchool('tedu', '广州')
# 初始化分校区
branch1 = BranchSchool('NSD', '天河客运站', master1)
branch2 = BranchSchool('JAVA', '天河北', master1)
branch3 = BranchSchool('Python', '小北', master1)
branch4 = BranchSchool('Golang', '梅花园', master1)
# 调用方法 pay_staff  --> testing
for i in [branch4, branch3, branch2, branch1]:
    i.echo_master()
    i.pay_staff()

# Staff 实例化
staff1 = Staff('A', 20, 2000, '后勤部', '扫地阿姨', branch1)
staff2 = Staff('B', 25, 3000, '就业部', '就业老师', branch2)
staff3 = Staff('C', 30, 15000, '后勤部', '扫地阿姨', branch3)
staff4 = Staff('D', 50, 3500, '后勤部', '煮饭阿姨', branch4)
staff5 = Staff('E', 33, 3300, '就业部', '就业老师', branch1)
staff6 = Staff('F', 47, 5000, '后勤部', '修电脑', branch1)
for i in [branch4, branch3, branch2, branch1]:
    i.get_staff_list()

# Course 实例化
course1 = Course('Linux', 12000)
course2 = Course('Nginx', 13000)
course3 = Course('HTTPD', 5000)
course4 = Course('Python OOP', 8000)
course5 = Course('Kubernetes', 90000)

# Class 实例化
class1 = Class(course1, branch1, 2107)
class2 = Class(course2, branch1, 2107)
class3 = Class(course3, branch1, 2108)
class4 = Class(course4, branch1, 2109)
class5 = Class(course5, branch1, 2211)
class6 = Class(course5, branch2, 2211)
class7 = Class(course5, branch3, 2211)

for i in [class5, class4, class3, class2, class1]:
    i.class_begin()
    i.get_class_num()

# Teacher 实例化
teacher1 = Teacher('T1', 13, 11000, '教培部', '项目经理', branch1, class1)
teacher2 = Teacher('T2', 23, 12000, '教培部', '项目经理', branch1, class2)
teacher3 = Teacher('T3', 33, 13000, '教培部', '项目经理', branch1, class3)
teacher4 = Teacher('T4', 43, 14000, '教培部', '项目经理', branch1, class4)
teacher5 = Teacher('T5', 53, 15000, '教培部', '项目经理', branch1, class5)
teacher6 = Teacher('T6', 63, 16000, '教培部', '项目经理', branch2, class6)
teacher7 = Teacher('T7', 73, 17000, '教培部', '项目经理', branch3, class7)
for i in [teacher7, teacher6, teacher5, teacher4, teacher3, teacher2, teacher1]:
    i.teaching()

# Students 实例化
stu1 = Students('stu1', 11, class1)
stu2 = Students('stu2', 22, class2)
stu3 = Students('stu3', 33, class3)
stu4 = Students('stu4', 44, class4)
stu5 = Students('stu5', 55, class5)
stu6 = Students('stu6', 66, class6)
stu7 = Students('stu7', 77, class7)
stu8 = Students('stu7', 77, class7)
for i in [stu8, stu7, stu6, stu5, stu4, stu3, stu2, stu1]:
    i.drop_out(i)