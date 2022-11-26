# 导入selenium 包
from selenium import webdriver

# 创建一个 Chromedriver 的实例。Chrome()会从环境变量中寻找浏览器驱动
# 一定要在Chrome后面添加括号，代表实例化这个类
driver = webdriver.Chrome()
# 打开网址
driver.get("https://www.baidu.com/")
# 关闭driver
driver.quit()