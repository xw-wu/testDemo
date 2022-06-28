'''
list列表的定义
    1.列表是有序可变元素的集合
    2.动态：随时扩展和收缩
    3.异构，存在不同类型的对象
    4.可重复
5.语法，[]包围，逗号分隔
'''


'''
创建列表：两种
    1.通过构造函数创建
    2.中括号创建并填充元素
    3.列表推导式
'''
#创建：1.构造方法
li=list()
li1= list('liebiao')
#创建：2.列表填充
li2= [1,2,3]
li3=[4,5,'ceshi']
li4=[6,7,'few',[9,1,3]]
#创建：3.列表推导式
li5= [i for i in range(1,10) if i %2 == 0]

'''
列表使用：索引
    默认：正向索引，编号从0开始，从左向右
    支持：反向索引，编号从-1开始，从右向左
'''
li6=[1,2,3,4,5,6]
#索引：正向索引
print(li6[2])
#索引：反向索引
print(li6[-4])

'''
列表使用：切片[start:stop:step]
    start:开始索引，没有指定默认未0
    stop：指定结束索引，没有指定，取列表最大索引值；实际索引的个数
    step：步长值，指定每一步大小，没有指定，默认步长为
    三个值：均可选，非必填
    
'''
#切片基本用法
li7=['1','3','d','g','f','e']
#基础用法1
print(li7[0:5:2])
#省略step
print(li7[2:4])
#省略start和step
print(li7[:5])
#省略stop和step
print(li7[2:])
#省略start和st0p
print(li7[::2])
#逆序打印
print(li7[::-1])

'''
列表使用：运算符
    重复：使用*运算符何以重复生成列表元素
    合并：使用+运算符可以将两个列表合二为一
'''
#列表运算符：重复
li8=[1]*5
#列表运算符：合并
li1=[1,2,3]
li2=[99,100]
print(li1+li2)

'''
列表使用：成员检测
    in:检查对象是否再列表中
        返回Boolean：True/Fals
    not in:检查列表是否不包含某个元素
        返回Boolean：True/Fals
'''
li=[1,2,3]
#列表成员检测：in
print(1 in li)
print(100 in li)
#列表成员检测：not in
print(1 not in li)
print(100 not in li)

'''
列表方法
    append():将对象item添加到列表末尾
        参数：入参，对象item；返回值none
        特点：只能在列表末尾添加
    extend():将一个可迭代对象的所有元素，添加到列表末尾
        参数：入参，可迭代对象iterable；返回值none    
        特点：只能在列表末尾添加
    insert():将一个对象插入到指定的索引位置
        参数：入参，索引值 index，一个对象item；返回值none
        特点：原索引位置及后面的元素后移一位
    pop():弹出返回列表指定索引对应的元素
        参数：入参，索引值 index ，可不传；
        返回值：指定索引的元素；未指定索引返回末尾元素
        索引错误：索引值不正确，或列表为空，引发indexerror错误
    remove():移除列表中第一个等于item的元素
        参数：入参，指定元素item，返回值none
        特点：目标元素必须存在，否则会报valueError
    sort():sort(key=None,reverse=False0列表进行原地排序，只使用<来进行各项之间的比较
        参数：两个关键词参数；key，指定带有一个参数的函数，用于从每个列表元素中提取比较键。reverse，默认值未False表示升序，True表示降序。返回none
    revsrse():将列表中的元素顺序反转
        参数:无。返回值，none。反转只是针对索引值，元素之间不相互比较。
'''

#列表方法添加元素：append(item)
lili=[]
lili.append(1)
lili.append("howa")
lili.append({'mes':'hell0'})
print(lili)
print(len(lili))

#列表方法添加迭代对象所有元素：extend（iterable）
lili=[]
#添加迭代元素：字符串的所有字母
lili.extend('howagde')
#接受列表的所有元素
lili.extend([1,2,3])
#接受元组的所有元素
lili.extend((4,5,6))
#接受字典的所有key值
lili.extend({'a':1,'b':2})
print(lili)

#列表方法添加对象到指定索引：insert（index,item）
lili=[0,1,2]
print('插入前',lili)
lili.insert(0,"hgeegg")
print('插入后：',lili)
#列表方法添加对象到指定索引：insert（index,item）
letters=['f','e','h','a','d']

#列表方法：pop()找到指定元素：传入索引值
n1=letters.pop(3)
print(n1)
#列表方法找到指定元素：不传入索引值
print(letters.pop())


#列表方法：remove()移除指定元素
li=['f','e','h','a','d']
li.remove('h')
print(li)
li=[1,2,3]
li.remove(2)
print(li)

#列表方法：排序sort(key=None,reverse=False)
num=[1,4,2,6,3]
#不传参数，默认升序，数字从小到大排列
num.sort()
print(num)
#指定key=len,按元素长度排序
words=['putho','fefe','d','gr']
words.sort(key=len)
print(words)
#指定reverse=True，降序
num.sort(reverse=True)
print(num)

#列表方法：reverse(),反转顺序
nums=[8,1,3,2,77]
nums.reverse()
print(nums)

'''
列表嵌套
    定义：在列表中存放列表
    列表常用方法都适用于列表嵌套列表
'''
#嵌套列表
li21=[[1,2,3],['dfe','eeee','qwe']]
print(li21[1][2])
li21[1].append('bh')
print(li21)

'''
列表推导式
    列表推导式是指循环创建列表，相当于for循环创建列表的简化版
    语法：[x for x in li if x...]
'''

#实例：将1-10中所有偶数平方后组成新的列表
result=[]
for ele in range(1,11):
    if ele % 2==0:
        result.append(ele ** 2)
print(result)

result2 = [ele **2 for ele in range(1,11) if ele % 2==0]
print(result2)
