from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self,driver:WebDriver=None):
        self.driver =driver

    def find(self,by,locator):
        return self.driver.find_element(by,locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_click(self, by, locator):
        return self.find(by, locator).click()

    def find_senf_keys(self, by, locator,text):
        return self.find(by, locator).send_keys(text)

    def back(self,num=3):
        for i in range(num):
            self.driver.back()