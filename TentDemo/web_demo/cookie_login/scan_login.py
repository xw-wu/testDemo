import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCookieLogin:
    def setup_class(self):
        self.driver=webdriver.Chrome()

    def test_get_cookies(self):
        #1.访问企业微信主页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        #2.等待20，人工进行扫码操作
        time.sleep(20)
        #3.成功登录之后，再去获取cookies信息
        cookie=self.driver.get_cookies()
        print(cookie)
        # 将cookie存于一个可持久存储的地方，文件
        #打开文件的时候添加写入权限
        with open("cookie.yaml", "w") as f:
            #第一个参数是要写入的数据
            yaml.safe_dump(cookie,f)

    def test_add_cookie(self):
        # 1.访问企业微信主页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        #2.定义cookie从已经写入的文件中获取
        cookie = yaml.safe_load(open("cookie.yaml"))
        #3.植入cookie
        for c in cookie:
            self.driver.add_cookie(c)
        time.sleep(3)
        #4.再次访问企业微信页面发现无需登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

