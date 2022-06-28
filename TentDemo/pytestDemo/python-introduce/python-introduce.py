'''
pytest
    可以支持简单的单元测试和复杂的功能测试
    可以结合requests实现接口测试；结合selenium。appium是心啊自动化功能测试
    使用putest 结合allure继承到jenkins中可以实现持续继承
    pytest支持315以上的插件
'''
'''
优点
    丰富的第三方插件
        报告
        多线程
        顺序控制
    简单灵活
    兼容unittest
    定制话插件开发
'''
'''
python 格式要求
    文件名 test_开头或者_test结尾
    类名  Test开头
    方法/函数名  test_开头：类内的叫做方法  类外的函数
注意：测试类中不可以添加__init__构造函数
    示例：谷歌方法
'''
'''
pycharm 中设置默认执行器为pytest
    tool--》python intergrated
    default test runner 为pytest
'''

class Testdemo:
    def test_demo(self):
        print("666666")
def test_dem02():
    print("22222")