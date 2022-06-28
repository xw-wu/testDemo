'''
fixture 的作用域
'''
'''
@pytest.fixture
def fixture_name():
    setup 操作
    yield 返回值
    teardown 操作
'''
import pytest
#定义了登录的fixture，金陵避免以test_开头
@pytest.fixture(scope="class")
def login():
    #setup操作
    print("完成登录操作")
    token="5456487897grewyrtsg"
    name='efrgerr'
    yield token,name #相当于return
    #teardown操作
    print("完成登出操作")

def test_search():
    #login 返回None
    print("搜索")

def test_car(login):
    print("购物车")

def test_order(login):
    token,userna=login
    print(f"token:{token},name={userna}")
    print("下单")

class TestDemo:
    def test_case1(self):
        print("case1")

    def test_case2(self):
        print("case2")
