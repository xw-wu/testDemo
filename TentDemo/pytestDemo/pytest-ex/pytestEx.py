'''
常用的异常处理方法
try.except

pytest.raises
    可以捕获特定的异常
    获取捕获的异常的细节（异常类型，异常信息）
    发生异常，后面的代码将不会被执行
'''
import pytest


def test_raise():
    with pytest.raises(ValueError,match='must be 0 or None'):
        raise  ZeroDivisionError("除数为0")


def test_raise2():
    with pytest.raises((ZeroDivisionError,ValueError),match='除数为0'):
        raise ZeroDivisionError("除数为0")