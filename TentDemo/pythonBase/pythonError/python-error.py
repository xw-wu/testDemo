'''
错误
    语法错误：语法不正确，不符合代码标准
    逻辑错误：语法正确，逻辑异常
    系统错误:系统错误，内存泄漏等
'''
#语法错误
# if 0>1
#     print("0>1")
#逻辑错误:语法没有任何错误，逻辑错误
# if 0<1:
#     print("0=1")

'''
异常
    程序执行过程中出现的未知错误
    语法和逻辑都是正常的
    程序业务逻辑不完善引起的程序漏洞（bg_http）
'''


'''
常见的异常的类型
    异常类型：参考网址：https://docs.python.org/3/library/exceptions.html#bltin-exceptions
    常见类型：
        除零类型
        名称异常
        索引异常
        键异常
        值异常
        属性异常
'''
#除零异常
# def div(a,b):
#     return a/b
#
# print(div(1, 0))


#名称异常
# num=name/2

#索引异常
# list=[1,2]
# print(list[3])

#键异常
# dic={'name':'tom'}
# print(dic['age'])

#值异常
# num='deg'
# print(int(num))

#属性异常

'''
异常/错误处理流程
    监测到错误--》引发异常--》捕获异常操作
    如果是拼写、配置等引起的错误，根据出错信息排查错误出现的位置进行解决
    如果是程序设计不完善引起的漏洞，根据漏洞情况进行设计处理漏洞的逻辑
异常的捕获与异常处理
  执行方式一
    try：
        执行代码
    except：
        发生异常时执行的代码
    finally：
        最后执行的代码
        
  执行方式二
    try：
        执行代码
    except：
        发生异常时执行的代码
    else：
        没有异常时执行的代码
'''
# def div(a,b):
#     return a/b
# try:
#     print(div(1, 0))
# except ZeroDivisionError as e:
#     print(f"异常:{e}")
# else:
#     print('没有异常的时候执行')
# finally:#最终都会执行，无论有异常还是没有异常的情况
#     pass

'''
使用raise抛出异常
    使用raise触发异常
    raise--->exception
'''
def set_age(num):
    if num <=0 or num>200:
        raise  ValueError(f"值错误{num}")
    else:
        print(f"设置的年龄为：{num}")
print(set_age(-1))

'''
自定义异常
    class MyError（Exception）
        def __init__(self,value):
            self.value=value
        
        def __str__(self):
            return repr(self.value)

'''