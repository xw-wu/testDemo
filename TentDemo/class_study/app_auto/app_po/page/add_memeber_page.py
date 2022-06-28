from appium.webdriver.common.mobileby import MobileBy

from class_study.app_auto.app_po.base.wework_app import WeWorkApp


class AddMemeberPage(WeWorkApp):
    def click_addbymenual(self):
        #click 添加成员

        self.find_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        from class_study.app_auto.app_po.page.edit_member_page import EditMemberPage
        return EditMemberPage(self.driver)

    def get_result(self):
        #get toast text
        element_toast = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']")

        result = element_toast.get_attribute("text")
        print(result)
        return result