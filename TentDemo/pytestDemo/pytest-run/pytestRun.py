'''
命令行参数-使用缓存状态
    --lf(--last-failed)只重新运行故障
    --ff(--failed-first)先运行故障再运行其余的测试
'''
import pytest

'''
python 代码执行pytest
    使用main函数
    使用python -m pytest 调用pytest(jenkins持续集成用到)[直接输入命令行运行]
'''
'''
python 代码执行pytest -main 函数

if __name__'__main__':
    #运行当前目录下所有符合规则的用例，包括子目录（test_*.py 和*_test.py）
    pytest.main()
    #运行test_mark1.py::test_dke模块中的某一条用例
    pytest.main(['test_mark1.py::test_dke','-vs'])
    #运行某个标签
    pytest.main(['test1.py','-vs','-m','dkej'])
运行方式

python test_*.py
'''
