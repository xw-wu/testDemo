import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

from class_study.web_auto.page_object.add_member_page import AddMemberPage
from class_study.web_auto.page_object.base_page import BasePage
from class_study.web_auto.page_object.content_page import ContentPage
from class_study.web_auto.page_object.wework_page import WeworkPage


class MainPage(WeworkPage):
    _BASE_URL = "https://work.weixin.qq.com/wework_admin/frame#index"
    #跳转通讯录页面的功能
    def goto_contact_page(self):
       return ContentPage()

    #跳转添加成员页面的功能
    def goto_add_member_page(self):
        # 实例化

        #点击添加成员按钮
        self.driver.find_element(By.CSS_SELECTOR,".ww_indexImg_AddMember").click()


        return AddMemberPage(self.driver)