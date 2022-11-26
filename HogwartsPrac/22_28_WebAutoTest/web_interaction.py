import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# 元素操作
def element_interaction():
    """
    元素的操作 点击/输入/清空
    :return:
    """
    # 1.实例化driver对象
    driver = webdriver.Chrome()
    # 2.打开一个网页
    driver.get("https://sogou.com/")
    # 3.定位到输入框进行输入操作
    driver.find_element(By.ID, "query").send_keys("霍格沃兹测试开发")
    # 强制等待2秒
    time.sleep(2)
    # 4.对输入框进行清空
    driver.find_element(By.ID, "query").clear()
    time.sleep(2)
    # 5.再次输入
    driver.find_element(By.ID, "query").send_keys("霍格沃兹测试开发2")
    # 强制等待2秒
    time.sleep(2)
    # 6.点击搜索
    driver.find_element(By.ID, "stb").click()
    time.sleep(2)


# 获取元素属性
def element_get_attr():
    # 1.实例化driver
    driver = webdriver.Chrome()
    # 2.打开网页
    driver.get("https://vip.ceshiren.com/#/ui_study")
    # 3.定位一个元素
    web_element = driver.find_element(By.ID, "locate_id")
    # 4.打印这个元素对象
    # 断点打在想看的对象的下一行
    # print(web_element)
    # 输出结果：<selenium.webdriver.remote.webelement.WebElement (session="0bd8c492a7e8e63a13879177d1b589ac", element="7cfd980e-1001-456e-a48c-7d522b197dbe")>
    # 5.获取元素的文本信息
    # 不是每个元素都含有文本信息的
    # print(web_element.text)
    # 输出结果:元素定位
    # 6.获取元素的属性信息，title="xxx"
    # res = web_element.get_attribute("name")  # 输出结果：locate
    # res = web_element.get_attribute("id")  # 输出结果：locate_id
    res = web_element.get_attribute("class")  # 输出结果：el-menu-item
    print(res)



if __name__ == "__main__":
    # 元素操作
    # element_interaction()
    element_get_attr()
