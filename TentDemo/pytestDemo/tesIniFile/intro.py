'''
pytest-ini
定义：
    pytest.int 是pytest的配置文件
    可以修改pytest的默认行为
    不能使用任何中文符合，包括汉字、空格、引号、冒号等
适用场景：
    修改用例的命名规则
    配置日志格式，笔袋吗配置更方便
    添加标签，防止运行过程报警错误
    指定执行目录
    排除搜索目录
改变运行规则
    执行check_开头和test_开头的所有文件，后面一定要加*
        python_files = check_* test_*
    执行所有的以test和check开头的类
        python_classes = Test* Check*
    执行所有以test_和check_开头的方法
        python-Functions=test_* check_*
添加默认参数
    addopts = -v -s --allureddir =./results
指定/忽略执行目录
    设置执行的路径
    testpaths=bilbili baidu
    忽略某些文件夹/目录
    borecursedirs=result logs datas test_demo*
日志
    配置参考链接：https://ceshiren.com/t/topic/13105
'''
