from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 定义配置的实例对象option
from selenium.webdriver.common.by import By

option = Options()
# 修改实例属性 为 debug模式启动的 ip+端口
option.debugger_address = "localhost:9222"
# 实例化driver的时候，添加option的配置
driver = webdriver.Chrome(options=option)
# driver.get("https://work.weixin.qq.com/wework_admin/frame")
# 点击添加成员的操作
# driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_item").click()
# 想要调试的步骤：输入用户名为"hogwarts"
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("hogwarts")
driver.find_element(By.PARTIAL_LINK_TEXT)