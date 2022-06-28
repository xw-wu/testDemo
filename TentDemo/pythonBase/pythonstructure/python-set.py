'''
set 集合定义
    1.无序唯一：无序的唯一对象集合
    2.动态：可随时添加或伤处元素
    3.异构：包含不同类型的数据
语法：大括号{}包围，逗号分隔
'''
'''
集合使用：三种创建
    1.使用大括号{}填充元素
    2.使用构造方法set()
    3.通过集合推导式
注意：不要单独使用{}集合来创建空集合，{}创建空集合是字典类型
'''
#集合创建一：使用{}创建填充元素
st1={1,2,3}
st2={'a','b','c'}
#集合创建二：使用构造方法创建
st3=set()
st4=set('grhhtyjyf')
li=[1,2,3,4]
st5=set(li)
#集合创建三：使用集合推导式
st6={x for x in li}
st7={}
print(type(st7))

'''
集合使用：成员检测
    in 判断元素是否存在集合中存在
    not in 判断元素是否在集合中不存在
'''
#集合：成员检测 in
st8={1,2,3,4,5,6,7,8}
#in
print(2 in  st8)
#集合：成员检测 not in
st8={1,2,3,4,5,6,7,8}
#in
print(99 not in st8)

'''
集合方法
    ddd(item):将单个对象添加到集合中
        参数：入参，对象item。返回值None。
    update(iterable):批量添加可迭代对象中的所有元素
        参数：可迭代对象iterable。返回，none。
    remove(item):从集合中移除制定元素item
        参数：入参，指定元素值。返回值，None。如果item不存在与集合中则会引发KeyError
    discard(item):从集合中移除制定对象item
        参数：入参，指定对象值。返回None，元素item不存在没有影响，不会抛出KeyError错误
    pop():随机从集合中移除并返回一个元素。
        参数：入参，无，被移除的元祖。如果集合为空会引发KeyError
    clear():清空集合，移除所哟元素
        入参：无，返回：none
'''
#集合方法add（）：添加对象
st={1,2,3}
st.add(99)
st.add('gegregr')

#集合方法update（）：添加对象
li=[1,2,3]
tup=(2,3,4)
st={'a','b','c'}
#批量添加列表中的元素
st1=set()
st1.update(li)
st1.update(tup)
st1.update(st)
print(st1)

#集合方法;remove()
st={1,2,3,4,5}
st.remove(2)#2为实在的对象

#集合方法 discard（）
st={1,2,3,4,5}
st.discard(3)
st.discard(1024)
print(st)

#集合方法pop()
st={1,2,3,4,5}
ite=st.pop()
print(ite,st)

#集合方法clear（）
#1.清空集合
st={1,2,3,4,5}
st.clear()
''
'''
集合运算
    交集运算：intersection(),操作符& 属于A且属于B
    并集运算:union(),操作符| 属于A或属于B
    差集运算:differnt()，操作符 -属于A不属于B
'''
#交集运算：intersection(), 操作符 &
set1={1,3,2}
set2={2,4,3}
print(set1.intersection(set2))
print(set1 & set2)
#并集运算:union(),操作符|
print(set1.union(set2))
print(set1 | set2)

#差集运算:differnt()，操作符 -
print(set1.difference(set2))
print(set1 - set2)

'''
集合推导式
    类似列表推导式，同样支持集合推导式
语法：{x forx in ..if}
'''
st={x for x in 'hfiegrgreg'if x in 'hedsfefgregrt'}
print(st)