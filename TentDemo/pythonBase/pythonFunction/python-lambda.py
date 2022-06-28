'''
python 匿名函数 lambda
    定义：没有名字的函数
    使用场景：
        需要函数，不想命名这个函数
        通常只使用一次的函数
        可以指定短小的回调函数
    语法：
        result:调用lambda表达式
        [arg1[,arg2,,,,argn]]:可选，指定要传递的参数列表
        expression：必选，指定一个实现具体功能的表达式
    实例：
        result=lambda[arg1[,arg2,,,,argn]]:expression
'''

import math
def c_ar(r):
    resu=math.pi*r*r
    return resu

r=10
print(c_ar(r))

res2=lambda r:math.pi*r*r
print(res2(r))
rr=5
re3=lambda rr:rr*5
print(re3(rr))

#对获取到的信息进行排序
#书籍信息
book_info=[
    ("python零基础入门",22.5),
    ("java零基础入门",20),
    ("软件测试零基础入门",25)
]
#指定规则进行排序
#lambda x:(x[1]) 返回了列表中每个元组的第二个元素

book_info.sort(key=lambda x:(x[1]))
print(book_info)