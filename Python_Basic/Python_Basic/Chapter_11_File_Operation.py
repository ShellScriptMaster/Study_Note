import string
import os
"""
    文件操作        open('路径', mode='读/写', encoding='utf-8')
        路径： 绝对路径、相对路径
        mode:
            r --> read 
                执行完了需要使用close()操作
            w --> write
                文件不存在情况下自动创建一个文件
                每次open操作都会清空文件内容
                执行完了需要使用close()操作
            a --> append
                执行完了需要使用close()操作
            with --> 上下文
                执行完了需要使用close()操作
            rb --> read bytes
                读取非文本文件
            修改
                
                

        encoding:
            打开文本文件需要给一个'utf-8'/ 'GDK'

"""
# 全部读取文件
pyvenv_cfg = open('../pyvenv.cfg', mode='r', encoding='utf-8')
print(pyvenv_cfg.read())
print('#'* 90, '\n')

# 逐行读取文件
pyvenv_cfg = open('../pyvenv.cfg', mode='r', encoding='utf-8')
print(pyvenv_cfg.readline())
print(pyvenv_cfg.readline())
# print输出的时候有一个换行动作,文件中每一行末尾也有一个换行,于是在这里显示了2个换行,可以使用strip()方法删除print()的换行符
print(pyvenv_cfg.readline().strip())
print(pyvenv_cfg.readline().strip())
print(pyvenv_cfg.readline().strip())
print('#'* 90, '\n')

# 多行读取
pyvenv_cfg = open('../pyvenv.cfg', mode='r', encoding='utf-8')
f = pyvenv_cfg.readlines()  # 此处将每一行作为一个元素(包含\n换行符)存入一个列表当中
print('f = ', f)
print('#'* 90, '\n')

# 最重要的文本读取方式

for line in f:
    print(line.strip())

# 文件写操作  Chapter_11_Testing
# 将26英文字母大小写和10个阿拉伯数字逐行存储文件Chapter_11_Testing.txt中
# 生成数字字母表
char = string.ascii_letters + str(string.digits)
char_list = []
for i in char:
    char_list.append(i)
print(char_list)
# open文件，mode=w
write_sample = open('./Chapter_11_Testing.txt', mode='w', encoding='utf-8')
for items in char_list:
    write_sample.write(items)    # open_obj.write('写入的内容')
    write_sample.write('\n')

write_sample.close()

# 文件追加写入
append_sample = open('./Chapter_11_Testing.txt', mode='a', encoding='utf-8')
append_sample.write('testing for append \n')
append_sample.close()
print('#'* 90, '\n')


# 文件with
with open('./Chapter_11_Testing.txt', mode='r', encoding='utf-8') as sample:
    print(sample.readlines())           # 对文件的操作需要在with的缩进下进行
print('#'* 90, '\n')

# sample.read() 此时无法在with外执行.read的操作，因为文件未被打开

# 文件复制操作(非文本文件)  读取被复制文件，然后将被复制文件内的每一行重新写入到一个新文件中
with open('OOP_Basic/Junior_Chapter_11_Object_Oriented.png', mode='rb' ) as init_obj , \
    open('OOP_Basic/Junior_Chapter_11_Object_Oriented.jpeg', mode='wb') as copy_obj:
    for items in init_obj:
        copy_obj.write(items)

# 对文件的修改操作
"""
    读取源文件内容，并且以写入模式打开一个副本文件
    针对每一行的数据进行判断，是否需要修改
    不需要修改的直接存入副本文件中
    需要修改的使用replace()方法进行修改并且存入副本文件中
    使用os模块的remove()方法将源文件删除
    使用os模块的rename()方法对副本文件进行重命名
    
"""
# 生成一个源文件
with open('Chapter_11_Testing.txt', mode='w', encoding='utf-8') as sample:
    for i in ['Alex', 'Tom', 'Jessica', 'Kristy', 'Sean', 'Kevin', 'John_aa', 'Paul_jj', 'Sam_jj']:
        sample.write(i)
        sample.write('\n')
# 生成副本文件
with open('Chapter_11_Testing.txt', mode='r', encoding='utf-8') as source_obj, \
    open('Chapter_11_Testing.txt_bak', mode='w', encoding='utf-8') as bak_obj:
    for line in source_obj:
        if '_' in line:
            line_list = line.split(sep='_')
            bak_obj.write(line_list[0])
            bak_obj.write('\n')
        else:
            bak_obj.write(line)
os.remove('Chapter_11_Testing.txt')
os.rename('Chapter_11_Testing.txt_bak', 'Chapter_11_Testing.txt')




