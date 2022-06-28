'''
python 函数进阶与参数处理
'''
'''
可变参数：不定长参数
    传入函数中实际参数可以是任意多个
    常见形式
        *args
        **kwargs
'''
'''
*args
    接收任意多个实际参数，并将其放到一个元组中
    使用已经存在的列表或元组作为函数的可变参数，可以在列表的名称前加*
    定义中*手机所有参数整合成一个元组
    调用中*解包为参数传入函数
'''
#直接接收多个任意参数
#
def print_language(*args):
    print(args)
print_language("python","java","php","go")

#使用已存在的列表或元组
paramds=["python","java","php","go"]
#此处*相当于解包的操作，列表中的每一个元素都当做一个参数传入函数
print_language(*paramds)

'''
**kwargs
    接收任意多个类似关键字参数一样显示赋值的实际参数，并将其放到一个字典中
    使用已经存在字典作为函数可变参数，可以在字典的名称前加**
'''
def print_info(**kwargs):
    print(kwargs)

print_info(tom=18,jim=20,lily=12)
params={'tom':18,'jim':20,'Lily':12}
print_info(**params)