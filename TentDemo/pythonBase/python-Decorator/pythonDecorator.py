'''
闭包函数
    函数引用
        函数可以被引用
        函数可以被赋值给一个变量
'''
# 定义函数
# def ho():
#     print("seewgeg")
# #函数对象赋值给变量
# ha=ho
# ha()
'''
    闭包函数的概念
        闭包的内部函数中，对外部作用域的变量进行引用
        闭包无法修改外部函数的局部变量
        闭包可以保存当前的运行环境
'''
# def output_student(grade):
#     def inner(name,gander):
#         print(f"学生姓名{name},学生性别{gander},学生年级是{grade}")
#     return inner
# student=output_student(1)
# student("张三","男")
# student("王二","男")

'''
装饰器
函数在开始执行与结束执行的时候分别答应提示信息
'''

# 不适用装饰器
# def hogwarts():
#     print("霍格沃兹测试学社")
#
# def hogwarts2():
#     print("霍格沃兹测试学社2")
#
# #第二部优化把中间的执行函数，使用参数话代理
# def func_tips(fun):
#     print("函数开始执行")
#     #不再是写死的任何一个函数，二十任意外部的函数对象
#     fun()
#     print("函数结束执行")
#
# #需要传入一个函数对象
# func_tips(hogwarts)

'''使用装饰器'''


# 定义两个函数，一个内函数，一个外函数
# 第五步，在装饰器执行过程中会自动传入一个参数
# def timer(func):
#     def inner():
#         # 第二步，在内函数添加装饰器的逻辑
#         print("函数开始执行")
#         func()  # 第六步添加被装饰函数的执行步骤
#         print("函数结束执行")
#     # 第三步，装饰器的使用
#     return inner
#
#
# # 装饰器的使用
# @timer
# def hogwarts():
#     print("霍格沃兹测试学社")
#
# # def hogwarts2():
# #     print("霍格沃兹测试学社2")
#
# hogwarts()

'''
装饰器带参
'''

def timer(func):
    #如果被装饰函数有参数，那么需要在内函数加形参以及在函数参数调用的时候添加参数信息
    #如果写死一个参数，但是无法确定被装饰函数的vans胡数量，这种方法就不行，会报错
    #解决方法：把两个地方的参数全部换成不定长参数
    def inner(*args,**kwargs):
        print("函数开始执行")
        func(*args,**kwargs)
        print("函数结束执行")
    return inner



@timer
def hogwarts(name,age):
    print("霍格沃兹测试学社",name,age)

def hogwarts2(name):
    print("霍格沃兹测试学社",name)

hogwarts("kefe",1111)
hogwarts2("zhangsan")