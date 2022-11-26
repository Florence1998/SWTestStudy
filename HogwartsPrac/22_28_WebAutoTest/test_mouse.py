import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestMouse(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_double_click(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study/frame")
        ele = self.driver.find_element(By.ID, "primary_btn")
        ActionChains(self.driver).double_click(ele).perform()
        time.sleep(3)

    def test_drag_and_drop(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study/action_chains")
        # 获取起始位置的元素
        start_ele = self.driver.find_element(By.ID, "item1")
        # 获取目标元素的为止
        target_ele = self.driver.find_element(By.ID, "item3")
        # 实现拖拽操作
        ActionChains(self.driver).drag_and_drop(start_ele, target_ele).perform()
        time.sleep(3)

    def test_move_to_element(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study/action_chains2")
        ele = self.driver.find_element(By.CSS_SELECTOR, ".title")
        ActionChains(self.driver).move_to_element(ele).perform()
        self.driver.find_element(By.XPATH, "//*[contains(text(),'管理班')]").click()
        time.sleep(3)

