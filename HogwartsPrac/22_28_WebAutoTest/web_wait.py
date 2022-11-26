import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_sleep():
    """
    如果直接执行，不添加任何等待，可能会报错
    """
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/")
    # 不加等待，可能会因为网速等原因产生报错
    # 报错：no such element: Unable to locate element
    # 原因：页面未加载完成，就去查找元素，此时这个元素还没有加载出来
    # ********强制等待的使用
    # 解决方案：在no such element: Unable to locate element报错之前添加强制等待，等待页面渲染完成
    # 如果没有报错，证明就是页面渲染速度导致的问题，如果添加了强制等待还报错，那么可能是别的问题，比如定位错误
    # time.sleep(3)
    # ********隐式等待的使用
    # 强制等待的问题：
    # 1.不确定页面的加载时间，可能会因为等待时间过长，而影响用例的执行效率
    # 2.不确定页面的加载时间，可能会因为等待时间过短，而导致代码依然会报错
    # 使用方法：
    # 1.在代码一开始运行的时候就添加隐式等待的配置，注意，隐式等待是全局生效，所以在所有的find_element动作之前就执行此代码
    # 2.注意：隐式等待只能解决元素查找的问题，不能解决元素交互的问题
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, "//*[text()='个人中心']")
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//*[text()='题库']")


def wait_show():
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study")
    # driver.implicitly_wait(5)
    # 问题：元素可以找到，但是点击效果却没有触发
    # 原因：隐式等待只能解决元素查找的问题，不能解决元素交互的问题
    # ********显示等待的使用
    # 第一个参数是driver，第二个参数是最长等待时间，util方法内需要结合expected_conditions或者自己封装的方法进行使用
    # expected_conditions的参数传入的都是一个元祖，即多一层小括号
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, "success_btn")))
    driver.find_element(By.ID, "success_btn").click()


if __name__ == '__main__':
    # wait_sleep()
    wait_show()
