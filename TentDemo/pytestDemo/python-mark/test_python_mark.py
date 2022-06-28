'''
mark：标记测试用例
    场景：只执行符合要求的某一部分用例，可以吧一个文本、项目划分为多个模块，然后指定模块名称执行
    解决：在测试用例方法上加@python.mark。标签名
    执行：-m执行自动一标记的相关用例
        pytest -s test_mark_zi_09.py -m =wetest
        pytest -s test_mark_zi_09.py -m apptest
        pytest -s test_mark_zi_09.py -m “not ios”
'''
import sys
import pytest

'''
mark:跳过（skip）及预期失败（xfail）
    这是pytest的内置标签，可以处理一些特殊的测试用例，不能成功的测试用例
    skip-始终跳过改测试用例
    skipif-遇到特定情况跳过改测试用例
    xfail-遇到特定情况，产生一个“齐王失败”输出
'''
'''
skip 使用场景
    调试时不想运行这个用例
    标记无法在某些平台上运行的测试功能
    在某些版本中执行，其他版本中跳过
    比如：当前的外部资源不可用时跳过
        如果测试数据是从数据库中渠道的，
        链接数据库的功能如果返回结果为成功就跳过，因为执行页都报错
    解决1：添加装饰器
        @pytest.mark.skip
        @pytest.mark.skipif
    解决2：代码中添加跳过代码
        pytest.skip(reason)
'''
'''
Xfalil 使用场景
    与skip雷士，预期结果为fail，标记用例未fail
    用法：添加装饰器@pytest.mark.xfail
'''
import pytest

#
# def double(a):
#     return a * 2
#
#
# @pytest.mark.int
# def test_double_int():
#     print("test double int")
#     assert 2 == double(1)
#
#
# @pytest.mark.minus
# def test_double1_minus():
#     print("test double minus")
#     assert -2 == double(-1)
#
#
# @pytest.mark.float
# def test_double1_float():
#     print("test double float")
#     assert 0.2 == double(0.1)
#
#
# @pytest.mark.float
# def test_double2_minus():
#     print("test double minus")
#     assert -2 == double(-1)
#
#
# @pytest.mark.zero
# def test_double_0():
#     assert 10 == double(0)
#
#
# @pytest.mark.bignum
# def test_double_bignum():
#     assert 200 == double(100)
#
#
# @pytest.mark.str
# def test_double_str():
#     assert 'aa' == double('a')
#
#
# @pytest.mark.str
# def test_double_str1():
#     assert 'a$a$' == double('a$')

'''
skip 使用场景
    调试时不想运行这个用例
    标记无法在某些平台上运行的测试功能
    在某些版本中执行，其他版本中跳过
    比如：当前的外部资源不可用时跳过
        如果测试数据是从数据库中渠道的，
        链接数据库的功能如果返回结果为成功就跳过，因为执行页都报错
    解决1：添加装饰器
        @pytest.mark.skip
        @pytest.mark.skipif
    解决2：代码中添加跳过代码
        pytest.skip(reason)
'''
# @pytest.mark.skip
# def test_aaa():
#     print("代码未开发完")
#     assert True
#
# @pytest.mark.skip(reason="代码没有实现")
# def test_bbb():
#     assert False
#
# #代码中添加 跳过代码块 pytest.skip(reason="")
# def check_login():
#     return False
#
# def test_function():
#     print("start")
#     #如果未登录，则跳过后续步骤
#     if not check_login():
#         pytest.skip("unsupported configuration")
#     print("end")

#
# print(sys.platform)
#
# @pytest.mark.skipif(sys.platform=='darwin',reason=" does not run on mac")
# def test_case1():
#     assert  True
#
# @pytest.mark.skipif(sys.platform=='win',reason=" does not run on win")
# def test_case2():
#     assert  True

'''
Xfalil 使用场景
    与skip雷士，预期结果为fail，标记用例未fail
    用法：添加装饰器@pytest.mark.xfail
'''
@pytest.mark.xfail
def test_aaa():
    print("test_xfail 方法执行")
    assert  2==2

@pytest.mark.xfail
def test_bbb():
    print("---开始测试----")
    pytest.xfail(reason="该功能尚未完成")
    print("测试过程")
    assert  2==2

xfail=pytest.mark.xfail
@xfail(reaon="bg_http 110")
def test_hello4():
    assert 0
