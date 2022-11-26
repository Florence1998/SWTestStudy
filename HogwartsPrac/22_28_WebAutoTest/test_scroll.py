import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestScroll(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_scroll_to_element(self):
        self.driver.get("https://ceshiren.com/")
        ele = self.driver.find_element(By.XPATH, "//*[text()='上海 - 极氪智能科技（SNC） - java测试开发']")
        ActionChains(self.driver).scroll_to_element(ele).perform()
        time.sleep(10)

    def test_scroll_by_amount(self):
        self.driver.get("https://ceshiren.com/")
        ActionChains(self.driver).scroll_by_amount(0, 3000).perform()  # 没有横向滚动，所以设为0，纵向滚动3000(10000可能就是滚到底)
        time.sleep(10)
