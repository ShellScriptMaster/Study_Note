# Bug 常见类型
"""
    SyntaxError
    索引越界
    方法不熟练
    思路不清晰问题         使用print 以及嵌套拆解来排错
    被动掉坑（除法运算）
"""
# 豆瓣电影TOP 250排行，使用列表存储了电影信息，要求输入名字在屏幕上显示xxx出演了哪部电影
lst = [{'rating':[9.7,50],'id':'1292052','type':['犯罪','激情'],'title':'肖申克的救赎','actors':['蒂姆·罗宾斯','摩根·弗里曼']},
        {'rating':[9.6,50],'id':'1291546','type':['剧情','爱情','同性'],'title':'霸王别姬','actors':['张国荣','张丰毅','巩俐','葛优']},
        {'rating':[9.6,50],'id':'1296141','type':['剧情','犯罪','悬疑'],'title':'控方证人','actors':['泰隆·鲍华','玛琳·黛德丽']},
       {'rating':[9.5,50],'id':'1292720','type':['剧情','爱情'],'title':'阿甘正传','actors':['汤姆·汉克斯','罗宾·怀特']}
       ]
"""
name = input('please input the actor name')
for item in lst:            --> item is a dictionary
    for movie in item:      --> movie is a key 
        actors = movie['actors']
        if name in actors:
            print(name + 'acts ' + movie)
"""
# name = input('please input the actor name')
# for item in lst:
#     ac_list = item['actors']
#     if name in ac_list:
#         print(item['title'] )

# 计算2个数的商   输入的数需要为int 或float， 且b不能为0
"""
    使用 try except异常处理机制
    try:
        xxx
    except xxx:
        xxx
    捕获异常的顺序按照先子类后父类的顺序，为了避免遗漏可能出现的异常，可以在最后增加BaseException
    try:
        可能出现异常的代码
    except Exception1:
        异常处理代码
    except Exception2:
        异常处理代码
    except BaseException:
        异常处理代码
"""
# a = int(input('please input the 1st number'))
# b = int( input('please input the 2nd number'))
# print(a/b)
# 使用异常处理机制，在异常出现的时候捕获然后内部消化，让程序继续运行  异常处理
# try except
try :
    a = int(input('please input the 1st number'))
    b = int(input('please input the 2nd number'))
    result = a/b
    print(result)

except ZeroDivisionError:
    print('2nd number should not be Zero 0!!!')
except ValueError:
    print('please input float or integer!')
except BaseException as e :
    print(e)
# try  ... except ... else...
# 如果try 块中没有出现异常则执行else块， 如果try 块出现异常，则执行except块
try :
    a = int(input('please input the 1st number'))
    b = int(input('please input the 2nd number'))
    result = a/b
except BaseException as e :
    print(e)
else:
    print(result)
# try .. except .. else .. fianlly
# 无论程序执行结果如何都会执行的代码块 --> finally
try :
    a = int(input('please input the 1st number'))
    b = int(input('please input the 2nd number'))
    result = a/b
except BaseException as e :
    print(e)
else:
    print(result)
finally:
    print('whatever happen exception or not, finally would be excute')
    print('end procedure, thanks for you using')

# 常见的exception 类型
"""
    ZeroDivisionError           被除数为0的异常
        print(10/0)
    IndexError                  序列中没有此index
        alst = [1,2,3,4]
        print(alst[4])
    KeyError                    映射中没有此key
        adict = {'name':'Tom','age':12}
        print(adict['gender'])
    NameError                   未声明变量
        print(not_claim_variety)
    SyntaxError                 语法错误
        int a = 20
    ValueError                  传入无效参数
        a = int('hello')
"""

# traceback 模块  打印异常信息

import  traceback
try:
    print('-'*30)               # ---有时候在前有时候在后
    print(1/0)
except:
    traceback.print_exc()       # 可以将异常输入到log日志·
