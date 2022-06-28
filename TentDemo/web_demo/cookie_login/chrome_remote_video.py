from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

#需打开cmd --remote-debugging-port=9222
option = Options()
#定义配置的示例对象Option
option.debugger_address ="localhost:9222"
# 修改实例属性 为 debug 模式启动的Ip端口
driver = webdriver.Chrome(options=option)
# 实例化Driver的时候，添加Option 配置
driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()

driver.implicitly_wait(3)
# driver.find_element_by_id("username").send_keys("hogwarts")
driver.find_element(By.ID,"username").send_keys("hogwarts")
