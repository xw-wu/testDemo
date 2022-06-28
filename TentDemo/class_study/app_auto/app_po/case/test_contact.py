from class_study.app_auto.app_po.base.wework_app import WeWorkApp


class TestContact:
    def setup_class(self):
        self.app = WeWorkApp()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.back()

    def teardown_class(self):
        self.app.stop()

    def test_addcontact(self):
        name="w1w4"
        phoneNum="13222365245"
        result= self.main.goto_addresslist().click_addmemeber().click_addbymenual().edit_member(name,phoneNum).get_result()
        assert "添加成功" == result

    def test_addcontact2(self):
        name = "w1w5"
        phoneNum = "13522216235"
        result = self.main.goto_addresslist().click_addmemeber().click_addbymenual().edit_member(name,phoneNum).get_result()
        assert "添加成功" == result