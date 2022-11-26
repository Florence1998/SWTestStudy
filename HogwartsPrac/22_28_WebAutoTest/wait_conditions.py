import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_until():
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study")
    # 确定返回值是否为WebElement对象要点到condition中的源码进行查看，千万不要生搬硬套
    # 不是所有的expected_conditions的返回值都是WebElement
    # 调用expected_conditions.element_to_be_clickable()方法的结果就是内函数_predicate(driver)的函数对象_predicate
    # 所以expected_conditions.element_to_be_clickable()的本质就是传递函数对象，即内函数的函数对象
    ele1 = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, '#success_btn')))
    ele2 = driver.find_element(By.CSS_SELECTOR, "#success_btn")
    print(ele1, ele2)
    # time.sleep(5)


if __name__ == '__main__':
    wait_until()
