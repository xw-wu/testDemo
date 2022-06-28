'''
dict 字典
    1.无序：无序键值对集合
    2.动态：字典是动态的
语法：
    1.字典用{}包围
    2.每个键/值对之间用一个逗号分隔
    3.各个键与值之间用一个冒号分隔
'''
'''
字典使用：三种创建
    1.使用大括号填充键值对
    2.通过构造方法dict()
    3.使用字典推导式
'''
#字典创建：1.使用大括号创建
dc={'name':'lili','age':18}
print(type(dc),dc)
#2.使用字典构造方法
dc1=dict()
dc2=dict(name="fevegr",age=18)
print(type(dc2),dc2)
dc3=dict([("name","lifefe"),("age",18)])
print(type(dc3),dc3)
#s使用字典推导式
dc4={k : v for k,v in[("name","feged"),("agee",18)] }
print(type(dc4),dc4)

'''
字典使用：访问元素
    与字典页支持中括号记法[key]
    字典使用键来访问其关联的值
    访问时对应的key必须要存在
'''
#1.访问存在的key
dc={"name":"feg","age":18}
print(dc["name"])
print(dc["age"])
#2.访问不存在的key，会报keyerror错误
# print(dc["fe"])

'''
字典使用：操作元素dict[key]=value
    添加元素，键不存在
    修改元素：键已经存在
'''
#1.字典使用修改
dc={"name":"feg","age":18}
dc['age'] = 20
print(dc)
#2.字典使用新增
dc['hobby'] = 'magic'
print(dc)

'''
字典使用：嵌套字典
    嵌套字典，字典的值可以是字典对象
'''
dc={"name":"degeg","age":18,"course":{"magic":90,"pyton":80}}
#1.获取课程magic的值
print(dc['course']['magic'])
#2.把python分数改成100
dc['course']['python']=100
print(dc)

'''
字典方法:
    key():返回由字典键组成的一个新视图对象。
        参数：入参：无。返回。
    values():返回由字典键组成的一个新视图对象
         参数：入参：无。返回。
    items():返回由字典项（（键，值）对）组成的一个新视图对象
    get()：获取制定key关联的value值
        入参：key,字典的键，必传。
        返回：key存在，返回key关联value。key不存在，返回none。
    update()：使用来自dict的键/值对更新字典，覆盖原有的键和值
        入参：dc，字典对象，必传。返回None
    pop()：删除自定key的键值对，并返回对应的value值
        入参：key，必传
        返回值：key值存在，则其移除并返回value值。如果可以不存在引发keyerror
'''
#字典方法：keys（）
#字典方法：values（）
dc={"name":"feg","age":18}
keys=dc.keys()
value=dc.values()
print(type(keys),keys)
print(type(value),value)
#1.遍历查看所有的键
for key in keys:
    print(key)
#2.框试图对象转成字典
print(list(keys))


#字典方法items()
dc={"name":"feg","age":18}
items = dc.items()
print(type(items),items)
#1.遍历查看所有的键
for item in items:
    print(item)
#2.将试图对象转换成为字典
print(list(items))

#字典方法 get（）
dc={"name":"feg","age":18}
#访问存在key值
print(dc.get('name'))
#访问不存在key值
print(dc.get('2113'))

#字典方法update（）
dc={"name":"fewwge","age":18}
dc.update({"age":20,"hobby":"magic"})
print(dc)

#字典方法 pop()
dc={"name":"feg","age":18}
#存在直接返回value值
print(dc.pop("name"))
#不存在报可以error
# print(dc.pop("name1"))

'''
字典推导式：可以从任何以键值对作为元素的可迭代对象中构建出字典
    给定一个对象{’a‘:1,'b':2,'C':3},找到大于1的，value进行平方
'''

dc={'a':1,'b':2,'C':3}
d_old=dict()

#未使用推导式
for k , v in dc.items():
     if v > 1:
         d_old[k]=v ** 2
print(d_old)

d_new={k:v**2 for k,v in dc.items() if v>1}
print(d_new)