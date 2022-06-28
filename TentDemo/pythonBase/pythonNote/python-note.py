'''
类型提示功能
    用于提示代码参数等
    参考网址：https://docs.python.org/zh-cn/3/library/typing.html
    好处：
        1.增强代码可读性
        2.ide中代码提示
        3.静态代码检查
'''
#用法一：为参数与返回数据指定类型
# def greeting(name:str):
#     return 'hello ' +name.split(',')[1]
# print(greeting('python,java'))

#用法二：为类型取别名
Vevtor=list[float]
def scale(scalar:float,Vevtor:Vevtor)->Vevtor:
    return [scalar *num for num in Vevtor]
print(scale(1.1,[1.1,1.2,3.3]))
#警告表明输入的值得类型与设置的类型不一致
# print(scale('aaa',[1.1,1.2,3.3]))

'''
自定义类型
'''
class Studet:
    name:str
    age:int
def get_stu(name:str) ->Studet:
    return  Studet()
# get_stu()

'''
静态代码检查功能
    安装 mypy  ：pip install mypy
    控制台输入 mypy 文件路径/文件名
    添加类型提示，mypy依赖于类型提示
'''
from  typing import List
a:List[int]=[]
a=[1,2,'1']