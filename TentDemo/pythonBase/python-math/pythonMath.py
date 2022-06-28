'''
math 函数
    python提供的内置数学类函数库，包含了很多数学公式
    幂函数运算
    三角函数
    高等函数运算等
'''
'''
math 函数操作
    数字常数
    数论与表示函数
    幂对数函数
    三角对数函数
    高等特殊函数
'''
'''
数字常量
math.pi π 圆周率3.14
math.e  e  自然对数，值为2.7182818
math.inf    ∞   正无穷大，负无穷-math.inf
math.nan    NAN 非数字NAN（not a number）
'''

import math

# print(math.pi)
# print(math.e)
# print(math.inf)
# print(-math.inf)
# print(math.nan)

'''
数论与表示函数
cell(x):上取整
floor（x）：下取整
factorial（x）：阶乘
comb（n，x）
perm(n,k=none)
gcd(a,b)最大公约数
fsum（iteration）精确浮点数，比sum更精确
fabs（X）绝对值
prod（iteration，*，start=1）：计算输入的iteration中所有元素的积。积的默认start值为1
fmod（x，y）取余。fmod（）在使用浮点数时是首选，x%y在使用整数时是首选
copysign（x,y）基于X的绝对值和y的符号的浮点数
frexp（X）以（m,c）对的形式返回X的尾数和指数。m是一个浮点数，e是一个整数。正好是x==m*2**e
isclose（a,b,*,rel_tol=le-09,abs_tol=0.0）a,b是否接近
'''
print(math.ceil(4.3))
print(math.ceil(-4.3))

'''
幂函数与对等函数
    math.pow(x,y) 
    未完
'''