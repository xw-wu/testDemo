from appium.webdriver.common.mobileby import MobileBy

from class_study.app_auto.app_po.base.wework_app import WeWorkApp
from class_study.app_auto.app_po.page.add_memeber_page import AddMemeberPage


class AddressListPage(WeWorkApp):

    def click_addmemeber(self):
        #添加成员

        self.find_click(MobileBy.XPATH, "//*[@text='添加成员']")
        return AddMemeberPage(self.driver)