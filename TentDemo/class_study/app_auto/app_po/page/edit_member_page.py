from appium.webdriver.common.mobileby import MobileBy

from class_study.app_auto.app_po.base.wework_app import WeWorkApp


class EditMemberPage(WeWorkApp):
    def edit_member(self,name,phoneNum):
        #输入名字和电话号，点击保存

        # self.driver.find_element(MobileBy.XPATH,
        #                          '//*[contains(@text, "姓名")] /../*[@text="必填"]').send_keys(name)
        self.find_senf_keys(MobileBy.XPATH,
                                 '//*[contains(@text, "姓名")] /../*[@text="必填"]',
                            name)

        # self.driver.find_element(MobileBy.XPATH,
        #                          '//*[contains(@text, "手机")] /..//android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.EditText')\
        #                         .send_keys(phoneNum)
        self.find_senf_keys(MobileBy.XPATH,
                            '//*[contains(@text, "手机")] /..//android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.EditText',
                            phoneNum)
        self.find_click(MobileBy.XPATH, "//*[@text='保存']")

        from class_study.app_auto.app_po.page.add_memeber_page import AddMemeberPage
        return  AddMemeberPage(self.driver)