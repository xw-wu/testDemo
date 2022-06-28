import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException


class TestWorkbrench:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        #跳过uiautomator2 server 的安装
        caps["skipServerInstallation"] = "true"
        #跳过设备初始化
        caps["skipDeviceInitialzation"] = "true"
        #获取页面元素等待0秒后超时
        caps['settings[waitForIdleTimeout]'] = 0
        #报隐式等待的相关错误，用双引号写做"true"，不用引号可以写作True 可以用低版本包解决
        caps["noReset"] = "true"
        # 与远程服务建立连接，返回一个session对象
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def swipe_find(self,text,num=3):
        #滑动查找元素
        for i in range(num):
            try:
                elment = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                return  elment
            except:
                print("未找到")
                size = self.driver.get_window_size()
                width = size.get("width")
                height=size.get("height")
                start_x =width/2
                start_y =height*0.8
                end_x =start_x
                end_y =height*0.3
                self.driver.swipe(start_x,start_y,end_x,end_y,duration=2000)

            if 1==num-1:
                raise NoSuchElementException(f"找了{num}次，未找到")


    def test_daka(self):
        time.sleep(15)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        self.swipe_find("打卡").click()

        # self.driver.update_settings({'waitForIdleTimeout':0})
        time.sleep(2)
        print(time.time())
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        print(time.time())
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")