import pytest


def double(a):
    return a * 2


@pytest.mark.int
def test_double_int():
    print("test double int")
    assert 2 == double(1)


@pytest.mark.minus
def test_double1_minus():
    print("test double minus")
    assert -2 == double(-1)


@pytest.mark.float
def test_double1_float():
    print("test double float")
    assert 0.2 == double(0.1)


@pytest.mark.float
def test_double2_minus():
    print("test double minus")
    assert -2 == double(-1)


@pytest.mark.zero
def test_double_0():
    assert 10 == double(0)


@pytest.mark.bignum
def test_double_bignum():
    assert 200 == double(100)


@pytest.mark.str
def test_double_str():
    assert 'aa' == double('a')


@pytest.mark.str
def test_double_str1():
    assert 'a$a$' == double('a$')
    assert 'a$a$' == double('a$')

# if __name__=='__main__':
#     # 运行当前目录下所有符合规则的用例，包括子目录（test_*.py 和*_test.py）
#     # pytest.main()
#     # 运行test_mark1.py::test_dke模块中的某一条用例
#     # pytest.main(['test_demo.py::test_double_str1', '-vs'])
#     # 运行某个标签
#     pytest.main(['test_demo.py', '-vs', '-m', 'str'])
