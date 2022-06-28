from class_study.web_auto.page_object.base_page import BasePage
from class_study.web_auto.page_object.main_page import MainPage
from class_study.web_auto.page_object.content_page import ContentPage


class TestAddMember:
    def setup_class(self):
        #用例执行前的准备工作，对象初始化
        self.main = MainPage()
        self.main.login()
        # self.contact =ContentPage()
        # self.contact.login()
    def teardown_class(self):
        '''
        退出Driver 进程
        :return:
        '''
        self.main.driver.quit()
        # self.contact.driver.quit()

    def teardown(self):
        '''
        保证每一条用例开始的时候，执行状态是正确的
        恢复到用例的初始页面
        :return:
        '''
        self.main.back_start_page()
    # 数据清理的两种方式
    # 1. 在teardown/teardown_class 即为每条用例执行后，清理用例数据
    # 2. setup_class 的时候清理数据。保证自动化测试用例在执行过程中有一个干净的测试环境
    # 在UI自动化测试中，测试的前置后置动作，不一定要通过UI的方式完成
    # 建议大家使用稳定的方式去完成比如通过数据接口

    def test_add_member(self):
        name="张一4"
       # main=MainPage()
        #1.点击添加成员，跳转到添加成员页面
        #2.add member的操作
        #3.获取通讯录页面的成员列表
        #链式调用
        mem_list = self.main.\
            goto_add_member_page().\
            add_member(name,"436e414","16548225412").\
            get_member_list()
  # 字面差值表达式
        print(f"成员列表为:{mem_list}")
        #4.断言 实际结果也就是成员列表是否符合预期
        assert name in mem_list

    # def test_contact(self):
    #     print("11111111")
    def test_add_member_fail(self):
        '''
        当收集号码格式输入错误，有没哟错误提示
        :return:
        '''
        name = "张一2"
        res=self.main.goto_add_member_page().add_member_fail(name,"45336414","13548")
        assert "请填写正确的手机号码" in res