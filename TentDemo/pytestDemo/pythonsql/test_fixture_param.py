import  pytest

@pytest.fixture(params=[["selenium",123],["appium",12345]])
def login(request):
    print(f"用户名:{request.param}")
    return request.param

def test_demo1(login):
    print(f"demo1 case:数据为{login}")