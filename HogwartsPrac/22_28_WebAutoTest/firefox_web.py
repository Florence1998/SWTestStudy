# 导入selenium 包
from selenium import webdriver

# 创建一个 Geckodriver 的实例。Firefox()会从环境变量中寻找浏览器驱动
driver = webdriver.Firefox()
# 打开网址
driver.get("https://www.baidu.com/")
# 关闭driver
driver.quit()
