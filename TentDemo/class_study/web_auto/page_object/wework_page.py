'''

'''
import time

import yaml

from class_study.web_auto.page_object.base_page import BasePage


class WeworkPage(BasePage):
    #baseurl 是指每个页面的URL
    _BASE_URL = ""
    """
    是企业微信的公共业务的封装
    """
    def login(self):
        self.driver.get(self._BASE_URL)
        time.sleep(3)
        # cookie = yaml.safe_load(open(r"X:\test\TentDemo\class_study\web_auto\page_object\cookie.yaml"))
        cookie = yaml.safe_load(open(r"X:\test\TentDemo\web_demo\cookie_login\cookie.yaml"))
        # 3.植入cookie
        for c in cookie:
            self.driver.add_cookie(c)
        time.sleep(3)
        # 4.再次访问企业微信页面发现无需登录
        self.driver.get(self._BASE_URL)

    def back_start_page(self):
        self.driver.get(self._BASE_URL)