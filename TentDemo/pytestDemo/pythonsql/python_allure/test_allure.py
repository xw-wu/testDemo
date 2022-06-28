import allure

@allure.feature("搜索模块")
class TestSearch():
    @allure.title("搜索用例-搜索词为Android")
    def test_case1(self):
        print("case1")

    @allure.title("搜索用例-搜索词为IOS")
    def test_case2(self):
        print("case2")


@allure.feature("登录模块")
class TestLogin():
    @allure.story("登录成功")
    def test_login_sucess(self):
        with allure.step("步骤1：打开应用"):
            print("打开应用")
        with allure.step("步骤2：登录页面"):
            print("登录页面")
            #放文件
            allure.attach.file("D:/C文档/appranking.png",
                               name="截图",
                               attachment_type= allure.attachment_type.PNG,
                               extension=".jpg"
                               )
        with allure.step("步骤3：输入用户名和密码"):
            # assert  1==2
            # 放文本
            allure.attach("这是一段文本信息",name="文本展示")
            print("输入用户名和密码")
        with allure.step("步骤4：进入成功页面"):
            allure.attach('<div class="detail-content  ql-editor font14 line20 font-Regular" data-v-5d0065e1=""><p>测试测试测试测试测试测试测试测试测试测试测试测试测试</p></div>', name="文本展示")
            print("这是登录：测试用例，登录成功")

    @allure.story("登录失败")
    def test_login_fail(self):
        print("这是登录：测试用例，登录失败")

    @allure.story("登录成功")
    def test_login_sucess_b(self):
        print("用户名缺失")


