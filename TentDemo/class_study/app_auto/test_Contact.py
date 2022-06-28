import time

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class TestContact:

    def setup(self):
        caps= {}
        caps["platformName"]="Android"
        caps["deviceName"]= "hogwarts"
        caps["appPackage"]="com.tencent.wework"
        caps["appActivity"]=".launch.LaunchSplashActivity"
        caps["noReset"]= "True"
        #与远程服务建立连接，返回一个session对象
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)

        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_add_contact(self):
        '''
        前提条件
            1.提前注册企业微信管理员账号
            2.手机端安装企业微信
            3.企业微信app处于登录状态
        通讯录添加成员用例步骤
            1.打开【企业微信】应用
            2.进入【通讯】页面
            3.点击【手动输入添加】
            4.输入【姓名】【手机号】并点击
        :return:
        # '''


        name = "lili2"
        phoneNum="13241254511"
        time.sleep(15)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[contains(@text, "姓名")] /../*[@text="必填"]').send_keys(name)
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[contains(@text, "手机")] /..//android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.EditText')\
                                .send_keys(phoneNum)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()

        '''  与 实战代码一致，自己运行暂时无法找到这个元素 '''
        element_toast = self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']")
        result = element_toast.get_attribute("text")
        assert "添加成功" == result


        #

        #辅助查看页面布局的方式
        # while True:
        #     current_xml = self.driver.page_source
        #     if "添加成功" in current_xml:
        #         print(current_xml)
        #         break
    #
    def wait_for_test(self,text):
        try:
            WebDriverWait(self.driver,10). \
                until(lambda x:x.find_element(MobileBy.XPATH,f"//*[@text='{text}']"))
            # self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
            # time.sleep(3)
            return True
        except:
           return False

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

    def test_del_contact(self):
        serchkey = "lili"
        time.sleep(15)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        #找到后面的所有兄弟节点，如果找到有多个从1开始数
        self.driver.find_element(MobileBy.XPATH, "//*[@text='软件测试模拟企业']/../../../following-sibling::*/*[1]").click()
        #输入搜索词，等待X秒，判断是否有结果；情况一:[五搜索结果]直接设为xfail，情况2，有搜索结果
        self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys(serchkey)
        # if "无搜索结果" in self.driver.page_source:
        #     pytest.xfail(reason=f"无搜索结果：{serchkey}") // 该元素在页面存在却没显示
        # time.sleep(3)
        exists = self.wait_for_test("联系人")
        if not exists:
            pytest.xfail(reason=f"无搜索结果：{serchkey}")

        #第二种情况：有结果，删除操作 beforenum
        befornum = len(self.driver.find_elements(MobileBy.XPATH, "//*[@text='联系人']/../following-sibling::*"))

        self.driver.find_elements(MobileBy.XPATH,"//*[@text='联系人']/../following-sibling::*")[0].click()
        #点击个人信息页的右上角的三个点
        time.sleep(2)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='个人信息']/../../../../following-sibling::*[1]").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='编辑成员']").click()
        self.swipe_find("删除成员").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='确定']").click()
        time.sleep(2)
        #判断搜索结果种的【联系人个数】 afternum
        afternum = len(self.driver.find_elements(MobileBy.XPATH, "//*[@text='联系人']/../following-sibling::*"))

        #删除之后，再拿一次联系人的个数 beforenum-afternum ==1
        assert befornum-afternum ==1