'''
用例运行
    运行某个/多个用例包
    运行某个/多个用例模块
    运行某个/多个用例类
    运行某个/多个用例方法
第一种运行方式：界面运行
    界面方式：选中包/用例/方法 右键运行
第二种运行方式：代码运行
    执行包下所有的用例：pytest/py。test[包名]
    执行单独一个pytest模块：pytest 文件名.py
    运行某个模块某个类：pytest 文件名.py::类名
    运行某个模块里面某个类里面的方法：pytest 文件名。pu::类名::方法名：
'''

class Testdemo:
    def test_demo(self):
        print("666666")
def test_dem02():
    print("22222")


'''
运行结果分析
    常用的：fail/error/pass
    特殊的记过：warning/deselect（后面会讲）
        warning：警告 不影响运行
        deselect 没有被选中
'''