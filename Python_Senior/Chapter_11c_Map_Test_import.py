import Chapter_11b_Map_Module

# 此时__name__ == 模块名
# 用于查看模块中是否有某个属性/方法, 此时类作为一个属性整体进行引用
if hasattr(Chapter_11b_Map_Module, 'Person'):
    test_Person = getattr(Chapter_11b_Map_Module, 'Person')
    print(test_Person)

if hasattr(Chapter_11b_Map_Module, 'cook'):
    test_speak = getattr(Chapter_11b_Map_Module, 'cook')
    test_speak()

