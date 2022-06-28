'''
    conftest.py 名字是固定的，不能改变
'''
import pytest
#定义了登录的fixture，金陵避免以test_开头
@pytest.fixture(scope="module",autouse=True)
def login():
    #setup操作
    print("完成登录操作")
    token="5456487897grewyrtsg"
    name='efrgerr'
    yield token,name #相当于return
    #teardown操作
    print("完成登出操作")

@pytest.fixture
def connectDB():
    print("链接数据库")