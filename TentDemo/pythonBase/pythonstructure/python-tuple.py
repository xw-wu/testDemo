'''
tuple 元组 定义
    1.有序不可变的对象集合
    2.异构：可以包含多种数据类型
语法：使用()包围，逗号分隔
'''

'''
元组创建：三种
    1.直接使用逗号
    2.小括号填充
    3.通过构造函数创建
注意;单个元组元素，逗号不能获取
'''
#元组创建一：直接使用逗号分隔
t1=1,3,4
print(type(t1))
#元组创建二：通过小括号填充
t2=(3,4,5)
print(t2)
t3=('s','f')
print(t3)
#元组创建三：通过构造函数tuple()创建
t4=tuple([1,3])
print(type(t4),t4)
#注意：单个元素元组，逗号不可获取
t5=1,
print(type(t5),t5)

'''
元组使用：索引[]
    正向索引，默认从0开始
    反向索引，默认从-1开始
'''
#元组索引：正向
t=tuple(range(1,6))
print(t[2])
print(t[-2])

'''
元组使用：切片[start:stop:step]
    start:开始索引，没有指定默认未0
    stop：指定结束索引，没有指定，取列表最大索引值；实际索引的个数
    step：步长值，指定每一步大小，没有指定，默认步长为
    三个值：均可选，非必填
'''
t6=tuple('gegrgyrhrt')
print(t6[0:3:1])
print(t6[::-2])

'''
元组常用方法：
    index(item):返回与目标元素首个元组相匹配的索引，
        特点：必须存在否则报错
    count(item):返回某个元素出现的次数
        入参：对象item。返回值次数
'''
#元组常用方法：index（item）
t7=('g','egrgyrhrt')
print(t7.index('g'))
t8=(1,3,4,5,5,4,3,1)
print(t8.index(3))

#元组常用方法：count（item）
t9=(1,3,4,5,5,4,3,1)
print(t8.count(3))

'''
元组解包：把一个可迭代对象李的元素，一并赋值到由对应变量组成的元组中
'''
#传统逐个赋值的方式
t=(1,2,3)
a=t[0]
b=t[1]
c=t[2]
print(a,b,c)

#使用元组解包
a,b,c=(1,2,3)
print(a,b,c)