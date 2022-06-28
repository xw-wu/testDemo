'''
函数
    复用，实现单一或相关关联功能的代码段
    优点：提高模块性和重复利用率
    python内置函数：https://docs.python.org/zh-cn/3.8/library/functions.html
'''

'''
函数定义:自定义函数
    def:函数定义关键词
    function_name:函数名称
    ():参数列表放置的位置，可以为空
    parameter_list：可选，指定向函数中传递的参数
    comments：可选，为函数指定注释
    function_body:可选，指定函数体
示例    
def function_name([parameter_list]):
    [function_body]
'''
'''
定义函数的注意事项
    缩进：python 是通过严格的缩进来判断代码块儿
        函数体和注释相对于def关键词必须保持一定的缩进，一般都是4个空格
        pycharm自动格式话快捷键 ctrl+alt+L
    定义空函数：
        使用pass语句占位
        写函数注释comments
'''

def func_demo():
    #函数体
    print("这是一个函数")

def func_with_params(a,b,c):
    '''
    这是一个携带参数和注释的函数
    '''
    print(f"传入的参数为：a={a},b={b},c={c}")

#打印函数 comments的内容
# print(func_with_params.__doc__)
#
# help(func_with_params)

#定义空函数
def filter_char(s):
    '''
    功能：过滤敏感词
    '''
    # pass

'''
函数调用
    function_name:函数名称
    parameter_value：可选，指定各个参数的值
    function_name([parameter_value])
'''
#调用函数
func_demo()
func_with_params(1,3,4)

'''
参数传递
    形式参数：定义函数时，函数名称后面括号中的参数
    实际参数：调用函数时，函数名称后面括号中的参数
'''
#a,b,c为形式参数
def demo_func(a,b,c):
    print()

#1，2,3为实际参数
demo_func(1,3,4)

'''
    位置参数
        数量必须与定义时一致
        位置必须与定义时一致
'''
def demo_func(a,b,c):
    print(a,b,c)
 #a=1,b=2,c=3
demo_func(1,3,5)

'''
关键字参数
    使用形式参数的名字确定输入的参数值
    不需要与形式参数的位置完全一致
'''
def demo_func(a,b,c):
    print(a,b,c)
demo_func(a=1,b=22,c=3)

'''
为参数设置默认值
    定义函数时可以指定参数的默认值
    指定默认值的形式参数必须放在所有参数的最后，否则会产生语法错误
    param=default_value:可选，指定参数并且为该参数默认值为default_value:可选，指定参数并且为该参数设置默认值为default_value
    def function_name(...,[param=default_value]): 
        [function_body]
    默认值一定要使用不可变对象
'''
def person(name,age,nationality="中国"):
    print(f"姓名为{name}年龄是{age}国籍是{nationality}")

person("zhangsan ",20)


#错误示范，默认值为空列表
#默认值一定要用不可变对象，否则的话默认值可能会随着调用发生变化
def wrong_demo2(a,b,c=[]):
    c.append(a)
    c.append(b)
    print(a,b,c)
wrong_demo2(1,2)
wrong_demo2(3,4)

'''
函数返回值
    value:可选，指定要返回的值
    返回值多个值，是保存在元组中
    如果没有返回值，返回None
示例
    def function_name([parameter_list]):
        [''comments'']
        [function_body]
        return [value]
 '''

def sum(a,b):
    wreturn =a+b
    # return wreturn,a,b
r=sum(1,2)
print(r)