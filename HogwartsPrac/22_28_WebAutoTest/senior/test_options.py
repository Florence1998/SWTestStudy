import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_options():
    # 在实例化driver对象之前，需要先定义好配置信息
    options = webdriver.ChromeOptions()
    # 在浏览器启动之前，就配置完成，窗口最大化的配置
    options.add_argument("start-maximized")
    # 指定浏览器分辨率
    options.add_argument('window-size=1920x3000')  # （我这执行看着没啥变化）
    # 无头模式：浏览器不会显示的启动在机器上
    options.add_argument('--headless')
    # 实例化一个driver对象，注意：配置对象options要通过chrome_options参数添加
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://ceshiren.com/")
    # 获取登录按钮中的文本信息
    login_text = driver.find_element(By.CSS_SELECTOR, "#ember41").text
    print(login_text)
    time.sleep(3)
