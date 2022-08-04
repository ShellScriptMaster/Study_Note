#print as a file
print('hello world')
fp = open('D:/text.txt','a+')  # the drive should exsist.  use "file=fp". if the file not exsist, then create one; if exsist , then append.
print('helloworld',file=fp)
fp.close()

# To acquire python reserved keyword
import keyword
print(keyword.kwlist)

# """   """  --> commment
# data type in Python
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Number data type: int 2 ** 63, long, float, bool, complex   不可变数据
a = 2 ** 70   # there is no "long" type in Python3 , "long" type only apply in Python2
print(type(a),id(a))   # id() check the Variety occupy on which Memory
b = -10  # int
c = 20  # int
d = 0  # int
c = 1.25  # float
d = True  # bool
d = False  # bool
print(bool(1))
print(bool(0))
f = 1 + 2j  # complex
g = 2j + 2j  # complex
print(f,g,f + g)
total = a \
        + b \
        + c
print('total is ',total,a,b,c)
print(int(c))
print('*' * 30,'String','*' * 30)
a, b, c, d = 20 , 5.5 , True , 4+3j
print(type(a), type(b), type(c), type(d))
print(isinstance(a, int))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# String type     不可变数据
h = 'this is a line with enter \n'
i = r'this is a line without enter \n'  # r could transfer meaning
print(h)
print(i)
j = """
hello world 
hsbc 
python_coding
"""
k = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789'
print(k)
print(k[0:-1])
print(k[-1])
print(k[2:5])
print(k[0:8:2])


# List type

