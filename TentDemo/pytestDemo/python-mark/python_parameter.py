'''
参数化
    参数化设计方法就是将模型中的定量信息变量化，使之成为任意调整的参数。对于变量华参数富裕不同数值，既可以得到不同大小和形状的零件模型
'''
'''
Mark:参数化测试函数使用
    单参数
    多参数
    用例重命名
    笛卡尔积
'''
'''
笛卡尔积 全量测试
    a=[1,2,3]
    b=[a,b,c]
组合形式
    （1,a）,(1,b),(1,c)
    （2,a）,(2,b),(2,c)
    （3,a）,(3,b),(3,c)
    
    当无法全量测试的时候，就需要等价类和边界值进行划分
'''
import pytest

#单参数
# search_list=['appium','selenium','pytest']
#
# @pytest.mark.parametrize('name',search_list)
# def test_search(name):
#     assert name in search_list

#多参数
#参数化的名字，要与方法中的参数名，一一对应
#如果传递多个参数，要放在列表中，列表中嵌套列表/元组
@pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+5",7),("7+5",12)],ids=["number1","number2","number3"])
def test_mark_more(test_input,expected):
    #eval 将字符串中表达式转化为实际的表达式
    assert eval(test_input) == expected

'''
参数化：笛卡尔积
'''
@pytest.mark.parametrize("wd",["appium","selenium","pytest"])
@pytest.mark.parametrize("code",["utf-8","gbk","gb2312"])
def test_dkej(wd,code):
    print(f"wd:{wd},code:{code}")

'''
参数化：用例重命名-添加ids参数
'''
@pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+5",7),("7+5",12)],ids=["add 3+5==8","add 2+5==7","add 7+5==12"])
def test_mark_more(test_input,expected):
    #eval 将字符串中表达式转化为实际的表达式
    assert eval(test_input) == expected