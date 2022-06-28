from class_study.web_auto.page_object.content_page import ContentPage
from selenium.webdriver.common.by import By
from class_study.web_auto.page_object.base_page import BasePage

from class_study.web_auto.page_object.wework_page import WeworkPage


class AddMemberPage(WeworkPage):
    INPUT_USERNAME = (By.ID,"username")

    def add_member(self,username,accid,phone):
        #Driver 实例化了多次，
        #解决方案让driver只实例化一次
        # sleep(30)
        # self.driver.find_element(By.ID,"username").send_keys("王二1326")

        # self.driver.find_element(By.ID,"memberAdd_acctid").send_keys("931126")
        # # self.driver.find_element(By.ID, "memberAdd_biz_mail").send_keys("wanger")
        # self.driver.find_element(By.ID, "memberAdd_phone").send_keys("13413375153")
        # self.driver.find_element(By.CSS_SELECTOR,".js_btn_save").click()

        self.find(self.INPUT_USERNAME).send_keys(username)
        self.find(By.ID,"memberAdd_acctid").send_keys(accid)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        self.find(By.CSS_SELECTOR,".js_btn_save").click()


        return ContentPage(self.driver)

    def add_member_fail(self, username, accid, phone):

        self.find(self.INPUT_USERNAME).send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(accid)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        eles=self.driver.find_elements(By.CSS_SELECTOR,".ww_inputWithTips_tips")
        error_list =[ele.text for ele in eles]
        return error_list
        # return ContentPage(self.driver)