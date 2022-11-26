import time

from selenium.webdriver.support.wait import WebDriverWait

if __name__ == '__main__':
    driver = "aaa"


    def fake_condition(driver):
        print("当前的时间为", time.time())
        # util传入的参数为一个函数对象，不是函数的调用
        # WebDriverWait(driver,10,2).until(fake_condition())
    WebDriverWait(driver, 10, 2).until(fake_condition, "霍格沃兹测试开发")
