'''
sys内置库
    sys概述
        是python自带的内置模块
        是与python解释器交互的桥梁
    sys使用
        常用属性

        常用方法
        导入sys模块
'''

#导入sys模块
import sys
#查看sys模块帮助文档
# help(sys)
# #查看sys模块的属性和方法
# print(dir(sys))

'''
sys模块常用属性
    #返回python解释器版本
    sys.version
    #返回操作系统平台名称
    sys.platform
    #返回外部向程序传递的参数
    sys.argv
    #返回已导入的模块信息
    sys.modules
    #返回导报的搜索路径列表
    sys.path
'''
#返回python解释器版本
print(sys.version)
#返回操作系统平台名称
print(sys.platform)
# #返回外部向程序传递的参数
print(sys.argv)
# #返回已导入的模块信息
print(sys.modules)
# #返回导报的搜索路径列表
print(sys.path)

'''
sys 常用方法
    sys.getdefaultencoding():获取编码方式
    sys.exit 运行时退出
'''
#获取系统当前编码
print(sys.getdefaultencoding())
#运行时退出
# sys.exit()


#返回python 解释器版本
#返回操作系统平台名称
#返回外部想程序传递的参数
#返回已导入的模块信息