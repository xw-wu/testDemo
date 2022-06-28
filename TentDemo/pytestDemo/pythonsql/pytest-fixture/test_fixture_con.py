
def test_search():
    #login 返回None
    print("搜索")

def test_car(login):
    print("购物车")

def test_order(login):
    token,userna=login
    print(f"token:{token},name={userna}")
    print("下单")

def test_get_product(login,connectDB):
    print("验证获取单品信息")
class TestDemo:
    def test_case1(self):
        print("case1")

    def test_case2(self):
        print("case2")
