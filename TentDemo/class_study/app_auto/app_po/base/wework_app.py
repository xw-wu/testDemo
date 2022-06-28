from appium import webdriver

from class_study.app_auto.app_po.base.base_page import BasePage


class WeWorkApp(BasePage):

    def start(self):
        if self.driver == None:
            print("driver None")
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "True"
            # 与远程服务建立连接，返回一个session对象
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

            self.driver.implicitly_wait(5)
        else:
            # 启动 desire里面设置的appActivity
            print("driver!= None")
            self.driver.launch_app()
        return self

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        from class_study.app_auto.app_po.page.main_page import MainPage
        return MainPage(self.driver)
        # return MainPage(self.driver)