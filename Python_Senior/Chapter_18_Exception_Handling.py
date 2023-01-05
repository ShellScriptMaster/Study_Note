"""
    异常处理
        把可能发生的异常, 提前在代码里捕捉
            try:
                执行代码
            except [错误代码/Exception] [as] [变量]:
                出错后执行的代码
            else:
                try代码不出错执行else
            finally:
                try代码无论是否出错都执行finally

        常见异常类型
            AttributeError 试图访问一个对象没有的属性
            IOError 输入/输出异常  通常是无法打开文件
            FileNotFoundError   打开一个不存在的文件
            ImportError 无法引入模块/包   路径问题或名称错误
            IndentationError  语法错误   代码缩进问题
            IndexError  索引错误  下标索引超出序列边界  a=[1,2,3] print(a[5])
            KeyError  试图访问字典内不存在的key
            KeyboardInterrupt  按下Ctrl+c 强行终止程序
            NameError    使用一个未赋予对象的变量
            SyntaxError  代码语法错误
            TypeError    传入对象类型与要求的不符合
            UnboundLocalError   试图访问一个还未被设置的局部变量, 基本上是由于有一个同名的全局变量导致在访问全局变量
            ValueError    传入一个调用者不期望的值 即使值的类型是正确的
        触发错误
            raise 异常代码(NameError)
        自定义异常
"""

while True:
    num1 = input('num1 = ')
    num2 = input('num2 = ')
    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 + num2
        num1.age                        # AttributeError num1没有age属性
        print(result)
        print(name)                     # NameError
    except ValueError as V_e:             # 遇到ValueError才会执行except后面的内容
        print('输入的值必须为数字')
        print(V_e)        # 打印错误信息
        break
    except NameError as N_e:                # 遇到NameError才会执行except后面的内容
        print('存在未定义的变量')
        print(N_e)
    except AttributeError as A_e:
        print(A_e)
    except Exception as e:  # 遇到有Exception都会执行except后面的内容
        print('pls check your code ')


while True:
    num3 = input('num3 = ')
    num4 = input('num4 = ')
    try:
        num3 = int(num3)
        num4 = int(num4)
    except Exception as e :
        print(e)
    else:
        print('没有异常执行这里')
        print('else 可以用来做代码检测')
    finally:
        print('无论是否发生异常都会执行finally')
        break

print('*'*30, '自定义异常', '*'*30)


class MyException(BaseException):           # 所有的异常都是继承BaseException而来
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message                 # 异常信息

try:
    raise MyException('自定义异常')

except MyException as i:
    print(i)


class VpnError(BaseException):
    def __init__(self, vpn):
        self.vpn = vpn

    def __str__(self):
        if self.vpn.lower() == 'down':
            return 'vpn is down'
        else:
            return 'up'


class FireWallError(BaseException):
    def __init__(self, fire_wall):
        self.fire_wall = fire_wall

    def __str__(self):
        if self.fire_wall.lower() == 'up':
            return 'fire_wall is up'
        else:
            return 'down'


vpn_down = VpnError('down')
fire_up = FireWallError('up')

try:
    raise vpn_down

except VpnError as vpn_e:
    print(vpn_e)

try:
    raise fire_up

except FireWallError as firewall_e:
    print(firewall_e)



