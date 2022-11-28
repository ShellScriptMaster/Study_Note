"""
    属性方法 --> property
        作用:
            把一个方法变成一个静态的属性(变量)

        case 查机票:
            实现逻辑:
                1. 连接各机场航班系统的API
                2. 查询信息
                3. 对返回的信息进行处理解析，然后显示给用户
            用户段:(从用户端看是一个属性，但是实际操作上应该是一个方法)
                获取飞机的状态、价格
                flight.status = 到达
"""


class Flight(object):
    def __init__(self, name):
        self.flight_name = name

    def checking_status(self):
        print('连接航空公司的API ... ... ')
        print('检查航班[%s]的状态 ' % self.flight_name)
        return 1               # 1 --> arrive ; 2 --> departure ; 3 --> cancel

    @property
    def flight_status(self):
        status = self.checking_status()     # 返回的是1
        if status == 1:
            print('航班到达')
        elif status == 2:
            print('航班起飞')
        elif status == 3:
            print('航班取消')
        else:
            print('状态码错误，请重新查询')

    @flight_status.setter
    def flight_status(self, status):
        print('修改航班状态为%s' % status)
        self.status = status

    @flight_status.deleter
    def flight_status(self):
        print('del .... ')


flight1 = Flight('CA980')
flight1.flight_status       # 实际上相当于执行 @property 修饰下的方法
# flight1.flight_status = 3  --> 不能直接对property属性进行直接赋值，需要使用setter的方法来修改属性
# 手动 更改property 属性          # 添加@flight_status.setter修饰器
flight1.flight_status = 3           # 实际上执行 @flight_status.setter修饰下的方法
# 删除flight_status 属性方法      # 添加@flight_status.deleter修饰器
del flight1.flight_status           # 实际执行的 @flight_status.deleter修饰下的方法

