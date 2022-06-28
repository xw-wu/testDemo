'''
数据驱动就是数据的改变从而驱动自动化测试的执行，最终引起吃测试结果的改变。
简单来说，就是参数化的应用。
数据量小的测试用例可以使用代码的参数化来实现数据驱动，数据量大的情况下建议大家使用一种结构化文件（yaml。json）来对数据进行存储，然后在测试用例中读取这些数据。
'''
import pytest
import yaml

'''
应用场景
    app、web、接口自动化测试
        测试步骤的数据驱动
        测试数据的数据驱动
        配置的数据驱动
'''
class TestDemo:
    @pytest.mark.parametrize("enu",yaml.safe_load(open("./enu.yml")))
    def test_demo(self,enu):
        if "test" in enu:
            print("这是测试环境")
            print(enu)
            print("测试环境ip是：",enu["test"])
        elif "dev" in enu:
            print("这是开发环境")
            print("开发环境ip是：", enu["test"])