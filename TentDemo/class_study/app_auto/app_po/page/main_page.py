import time

from appium.webdriver.common.mobileby import MobileBy

from class_study.app_auto.app_po.base.wework_app import WeWorkApp
from class_study.app_auto.app_po.page.addresslist_page import AddressListPage


class MainPage(WeWorkApp):
    _addresslist_element = (MobileBy.XPATH, "//*[@text='通讯录']")
    def goto_addresslist(self):
        #click 通讯录
        time.sleep(5)
        self.find_click(*self._addresslist_element)
        return AddressListPage(self.driver)