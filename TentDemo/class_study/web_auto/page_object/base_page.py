import time

import yaml
from selenium import webdriver


#1.为什么会出现重复打开页面，重复实例化driver的问题
#答案：其他页面子类继承与basepage，一旦子类实例化，那么就会执行父类的构造函数
#子类实例化几次，那么父类的构造函数u就要执行几次，就会打开几次浏览器
#解决方法：那么如果无法解决构造函数要执行多次的问题，那么就考虑在父类的构造函数里面
#添加判断，避免driver的重复实例化。定义一个base_drIver的形参
#base——driver代表，如果没有类在实例化的时候接收参数，那么久实例化driver
#如果有接收到参数，那么久残敌driver，保证driver 一直存在
class BasePage:
    '''
    封装与业务无关的代码
    是某些业务的底层
    '''
    def __init__(self,base_driver = None):
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(3)
            # 打开 index 页面

        else:
            self.driver = base_driver

    def find(self,by,locator=None):
        '''
        有可能传入的是一个元祖（a,b）
        有可能是传入两个参数
        :param by:
        :param locator:
        :return:
        '''
        print(f"元素定位方式{by}，元素的定位表达式未{locator}")
        if locator is None:
            #如果传入元祖，那么给元祖做解包，分别传入到函数中
            return self.driver.find_element(*by)
        else:
            self.driver.find_element(by,locator)
        return self.driver.find_element(by,locator)