# Flow Control
# Structure of the Procedure  程序的组织结构
"""
 顺序结构，选择结构(if)，循环结构(while, for-in ) 三种基本结构 就可以构成任何 简单 或 复杂 的算法
 顺序结构 程序从上到下执行代码，中间没有任何跳转或判断，直到程序结束
"""
# Sequential Structure 顺序结构
# How to put an elephant into a refrigerator
print('-'*10, 'Begin','-'*10)
print('1. open the door of refrigerator ')
print('2. put the elephant into the refrigerator')
print('3. close the door')
print('-'*10, 'End','-'*10,'\n')
########################################################################################################################

# Bool_Value of the object  对象的布尔值
# Py中一切皆对象，所有对象均有一个bool值，使用bool()获取对象布尔值
# 以下对象均为False
print(bool(False))  # False
print(bool(0))      # 0
print(bool(0.0))    # 0的浮点数
print(bool(None))   # None
print(bool(''))     # 空字符串
print(bool(""))     # 空字符串
print(bool([]))     # 空列表
print(bool(list())) # 空列表
print(bool(()))     # 空元组
print(bool(tuple()))# 空元组
print(bool({}))     # 空字典
print(bool(dict())) # 空字典
print(bool(set()))  # 空集合
########################################################################################################################

# 选择结构 程序根据判断条件的布尔值选择行地执行部分代码
# Branch Structure  分支结构
# Single Branch Structure 单分支结构
# Check whether the Balance is enough
"""  ------------------ Coding ------------------ 
money = 1000
withdrawal = int(input('How much do you want to take?'))
if withdrawal <= money:
    money -= withdrawal
    print('you can take your money, the Balance is:',money)
     ------------------ Coding ------------------  """

# Double Branch Structure 双分支结构
# input a integer , and verify if the integer is odd or even?
"""  ------------------ Coding ------------------ 
integer = int(input('please input a interger'))
if integer % 2 == 1:
    print('odd number')
else:
    print('even number')
     ------------------ Coding ------------------  """

# Multiple Branch Structure 多分支结构
# input a Score, 90-100 A; 80-89 B; 70-79 C; 60-69 D; 0-59 E; Score>100 or Score<0 Invalid
"""  ------------------ Coding ------------------ 
score = int(input('please input your Score'))
if   score <= 100 and score >= 90:
    print('A')
elif score <= 89  and score >= 80:
    print('B')
elif score <= 79  and score >= 70:
    print('C')
elif score <= 69  and score >= 60:
    print('D')
elif score <= 59  and score >= 0:
    print('E')
else:
    print('Invalid score')
     ------------------ Coding ------------------  """

# Nested Structure  嵌套结构
# VIP >= 200 , 20% discount
# 200 >= VIP >= 100 , 10% discount
# 100 >= VIP >= 0, 0 discount
# non-VIP >= 200 , 5% discount
# non-VIP <= 200 , 0 discount
"""  ------------------ Coding ------------------ 
VIP = input('are you a VIP？')
if VIP in ['y','Y','N','n']:
    bill = float(input('how much do you cost?'))
    if VIP == 'y' or VIP == 'Y':
            if  bill >= 200:
                cost = bill * 0.8
                print(cost)
            elif bill <= 200 and bill >= 100:
                cost = bill * 0.9
                print(cost)
            elif 100 >= bill > 0:
                cost = bill
                print(cost)
            elif bill <=0:
                print('Invalid amount')
    elif VIP == 'n' or VIP == 'N':
            if bill >= 200:
                cost = bill * 0.95
                print(cost)
            elif 200 >= bill > 0:
                cost = bill
                print(bill)
            elif bill <= 0:
                print('Invalid amount')
else:
    print('please confirm you are a VIP or not')
     ------------------ Coding ------------------  """

# Conditional Expression  条件表达式
# input 2 integers and compare which one is bigger
"""  ------------------ normal Coding ------------------ 
num_a = int(input('please input the first number'))
num_b = int(input('please input the second number'))
if num_a > num_b:
    print(num_a,'is bigger than',num_b)
elif num_a < num_b:
    print(num_b,'is bigger than',num_a)
else:
    print(num_a ,'=', num_b)
     ------------------ normal Coding ------------------  """
num_a = int(input('please input the first number'))
num_b = int(input('please input the second number'))
print('Conditional Expression')
print(( str(num_a) +' is bigger than '+ str(num_b))  if num_a > num_b else (str(num_a) +' is less than '+ str(num_b)) )
# 条件判断为True 执行if 左侧代码，条件判断为False 执行else 右侧代码
########################################################################################################################

# Pass 空语句
# Pass 语句什么都不做，只是一个占位符，用在语法上需要语句的地方，搭建语法结构的时候使用它
# VIP >= 200 , 20% discount
# 200 >= VIP >= 100 , 10% discount
# 100 >= VIP >= 0, 0 discount
# non-VIP >= 200 , 5% discount
# non-VIP <= 200 , 0 discount
VIP = input('are you VIP?')
if VIP == 'y':
    pass
elif VIP == 'n':
    pass
else:
    pass

