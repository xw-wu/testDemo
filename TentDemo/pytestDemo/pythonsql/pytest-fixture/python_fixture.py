import pytest

@pytest.fixture()
def login():
    print("完成登录操作")

def test_search():
    print("搜索")

def test_car(login):
    print("购物车")

def test_order(login):
    print("下单")