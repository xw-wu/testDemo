'''
    python 模块与包
    package 包
    module 模块
        包含python定义和语句的文件
        .py文件
        作为脚本运行
    function 方法
'''

'''
模块导入
    import 模块名
    from <模块名> import <方法|变量|类>
    from <模块名> import*
    注意:
        同一个模块写多次，只被导入一次
        import应该放在代码的顶端
'''
'''
模块分类
    系统内置模块
    第三方的开源模块
    自定义模块
'''
'''
使用模块
    系统内置模块
        python 安装好之后自带的一些非常有用的模块（sys,os,time,json模块等）
    第三方开源模块
        是通过包管理工具pip完成的 “pip install 模块名”
    自定义模块
        自定义模块是自己写的模块，对某段逻辑或默写函数进行封装后宫其他函数调用
'''
#系统内置模块
# import sys
# print(sys.path)
# import  time



# time.sleep()

#第三方开源模块

'''
from与import的区别
    from 直接从某个模块中导入某个方法，直接调用方法
    import 直接导入摸个某块， 调用方法需用模块.方法进行调用
    一个模块中存在多种方法，可以用，后添加多个方法  from baidu import search，search1，hello
'''

'''
常用方法
    dir() 找出当前模块定义的对象
    dir（sys）找出参数模块定义的对象 
    
    搜索路径
        Python解释器对模块位置的搜索顺序是
            包含输入脚本的目录（如果未指定文件，则为当前目录）
            pythonpath（目录名称列表，语法与shell变量相同PATH）
            安装的默认路径
'''
'''
    使用模块的优点
        代码的可维护性
        提升编码效率
        函数名可重复（起名避免与系统重复）
'''



