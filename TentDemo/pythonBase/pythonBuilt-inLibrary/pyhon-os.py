'''
python-os内置库
    OS：Operatng System
    OS模块的常用功能
    跨平台的差异
'''
'''
OS使用
    导入OS模块
    查看OS模块使用文档
        help（OS）
        dir（OS）
'''
import os
# help(os)
# print(dir(os))

'''
os常用方法
    系统相关
        os.name:获取系统名称
        os.envion:获取系统环境变量信息
        os.getenv('path'):获取制定名称的环境变量信息
        OS.syStem（）执行系统命令
    操作目录
        os.getcwd():获取当前目录
        os.chdir()切换目录
        os.listdir()列出当前目录内容
        os.mkdir(）创建空目录
        os.makedirs()递归创建多级目录
        os.rmdir()删除空目录
        os.rename()重命名目录
        os.remove()删除文件
    操作路径
        os.path.abspath()返回绝对路径
        os.path.basename()返回文件名
        os.path.dirname()返回文件路径
        os.path.split()分割路径
        os.path.join()拼接路径
        os.path.exists()判断路径是否存在
        os.path.isdir()判断是否是目录
        os.path.isfile()判断是否是文件
        os.path.getsize()获取文件大小
'''

# #获取系统名称 nt代表window，posix代表linux
# print(os.name)
# #获取系统环境变量信息
# print(os.environ)
# #获取制定名称的环境变量信息
# print(os.getenv('PATH'))
# #执行系统命令
# print(os.system('pwd'))

# #获取当前所在目录
# print(os.getcwd())
# #切换目录
# print(os.chdir('..'))
# #列出当前目录下的所有文件
# print(os.listdir())
# #创建空目录
# os.mkdir('new')
# #地柜床架多及空目录
# os.makedirs('a/b/c')
# #删除空目录
# os.rmdir('new')
# #重命名目录
# os.rename('a','a1')
# #删除文件
# os.remove('demo.txt')

#返回绝对路径
print(os.path.abspath('./os_demo.py'))

# 返回文件名
print(os.path.basename('X:\\test\TentDemo\pythonBase\pythonBuilt-inLibrary\os_demo.py'))

# 返回文件路径
print(os.path.dirname('X:\\test\TentDemo\pythonBase\pythonBuilt-inLibrary\os_demo.py'))

# 分割路径
print(os.path.split('X:\\test\TentDemo\pythonBase\pythonBuilt-inLibrary\os_demo.py'))

# 拼接路径
os.path.join("X:\\test\TentDemo\pythonBase\pythonBuilt-inLibrary", "os_demo.py")

# 判断路径是否存在
print(os.path.exists('X:\\test\TentDemo\pythonBase\pythonBuilt-inLibrary'))

# 判断是否是目录
print(os.path.isdir('\\test\TentDemo\pythonBase\pythonBuilt-inLibrary'))
#
# # 判断是否是文件
print(os.path.isfile('X:\\test\TentDemo\pythonBase\pythonBuilt-inLibrary\os_demo.py'))
#
# # 获取文件大小
print(os.path.getsize('X:\\test\TentDemo\pythonBase\pythonBuilt-inLibrary\os_demo.py'))

