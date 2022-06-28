import time

from selenium.webdriver.common.by import By

from class_study.web_auto.page_object.base_page import BasePage
from class_study.web_auto.page_object.wework_page import WeworkPage


class ContentPage(WeworkPage):
    _BASE_URL = "https://work.weixin.qq.com/wework_admin/frame#index"

    def add_member(self):

        pass

    def get_member_list(self):
        ele_list=self.driver.find_elements(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        member_list=ele_list
        # time.sleep(1000)
        # name_list = []
        # for web_ele in ele_list:
        #     name_list.append(web_ele.text)
        # 把元素列表转换为名称列表，使用列表推导式
        member_list=[ele.text for ele in ele_list]
        #返回最后一个成员列表
        return  member_list